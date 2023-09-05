def predict_interest(age_group: str, gender_string: str) -> str:
    gender = None
    age = None

    # parse gender
    if gender_string == 'Male':
        gender = 'M'

