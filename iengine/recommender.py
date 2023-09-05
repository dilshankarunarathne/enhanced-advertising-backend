from iengine.ad_recommender_package import recommend_topic


def predict_interest(age_group: str, gender_string: str) -> str:
    gender = None
    age = None

    # parse gender
    if gender_string == 'Male':
        gender = 'M'
    elif gender_string == 'Female':
        gender = 'F'
    else:
        raise ValueError

    recommend_topic(age, gender)

