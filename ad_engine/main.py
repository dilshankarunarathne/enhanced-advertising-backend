def get_ad_img(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image
    """

    # path = "raw_ads/" + recommended_interest + ".jpg"

    path = "ad_engine/raw_ads/gaming.jpg"

    with open(path, "rb") as f:
        return f.read()
