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

    # parse age
    if age_group == '(0-2)':
        age = 2
    elif age_group == '(4-6)':
        age = 6
    elif age_group == '(8-12)':
        age = 12
    elif age_group == '(15-20)':
        age = 19
    elif age_group == '(25-32)':
        age = 27
    elif age_group == '(38-43)':

    return recommend_topic(age, gender)

