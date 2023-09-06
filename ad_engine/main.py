def get_ad_img(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image
    """

    path = "ad_engine/ads/", recommended_interest, ".jpg"

    with open(path.__str__(), "rb") as f:
        return f.read()
