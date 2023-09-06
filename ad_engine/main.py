def get_ad_img(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image
    """

    path = "ads/" + recommended_interest + ".jpg"

    with open(path, "rb") as f:
        return f.read()
