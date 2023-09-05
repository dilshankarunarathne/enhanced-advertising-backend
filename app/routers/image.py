import cv2
import numpy as np
from fastapi import APIRouter, UploadFile, File, Depends

from app.security.authorize import get_current_user, credentials_exception, oauth2_scheme
from classifier import main

"""
    routers for image evaluation
"""

router = APIRouter(
    prefix="/api/image",
    tags=["image"],
    responses={404: {"description": "Not found"}},
)


@router.post("/evaluate")
async def evaluate_image(
        image: UploadFile = File(...),
        token: str = Depends(oauth2_scheme)
):
    if image.content_type != "image/jpeg":
        return "Only jpeg images are supported"

    if get_current_user(token) is None:
        raise credentials_exception

    contents = await image.read()
    nparray = np.fromstring(contents, np.uint8)
    img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)

    age, gender = main.predict_age_and_gender(img)

    return age, gender
