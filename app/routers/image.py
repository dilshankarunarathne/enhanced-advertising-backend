import cv2
import numpy as np
from fastapi import APIRouter, UploadFile, File, Depends

from app.security.authorize import get_current_user, credentials_exception, oauth2_scheme
import classifier.main as classifier
from iengine.recommender import predict_interest

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

    age, gender = classifier.predict_age_and_gender(img)

    recommended_interest = predict_interest(age, gender)

    # TODO: return ad based on recommended_interest
    ad =

    return age, gender, recommended_interest
