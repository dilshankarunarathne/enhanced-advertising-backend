import cv2
import numpy as np

age_net = cv2.dnn.readNetFromCaffe("age_deploy.prototxt", "age_net.caffemodel")
gender_net = cv2.dnn.readNetFromCaffe("gender_deploy.prototxt", "gender_net.caffemodel")

age_ranges = ["(0-2)", "(4-6)", "(8-12)", "(15-20)", "(25-32)", "(38-43)", "(48-53)", "(60-100)"]
gender_labels = ["Male", "Female"]


def predict_age_and_gender(image):

    blob = cv2.dnn.blobFromImage(
        image,
        1.0,
        (227, 227),
        (78.4263377603, 87.7689143744, 114.895847746),
        swapRB=False
    )

    age_net.setInput(blob)
    age_pred = age_net.forward()
    age = age_ranges[np.argmax(age_preds)]

    gender_net.setInput(blob)
    gender_preds = gender_net.forward()
    gender = gender_labels[np.argmax(gender_preds)]

    return age, gender
