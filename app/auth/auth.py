from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Form, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.models.user_model import UserInDB
from app.auth.services.user_service import user_exists, get_next_avail_id, add_new_user
from app.security.authorize import authenticate_user, oauth2_scheme
from app.security.hashing import get_password_hash, create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES, blacklist_token

"""
    routers for authentication
"""

router = APIRouter(
    prefix="/api/auth",
    tags=["auth"],
    responses={404: {"description": "Not found"}},
)


@router.post("/register")
async def register_user(
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        is_adviser: bool = Form(...),
):
    if user_exists(username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )
    hashed_password = get_password_hash(password)
    user = UserInDB(
        id=get_next_avail_id(),
        username=username,
        email=email,
        hashed_password=hashed_password,
        is_adviser=is_adviser,
    )
    add_new_user(user)
    return user


@router.post("/login")
async def login_for_access_token(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires.seconds
        # Unresolved attribute reference 'username' for class 'bool'
    )

    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    blacklist_token(token)
    return {"message": "Successfully logged out"}
