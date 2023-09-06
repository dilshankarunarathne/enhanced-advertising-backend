def get_ad_img_data(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image
    """

    path = "ad_engine/raw_ads/" + recommended_interest + ".jpg"

    with open(path, "rb") as f:
        return f.read()


