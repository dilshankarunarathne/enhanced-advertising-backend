def get_ad_img(recommended_interest):
    """
    :param recommended_interest: string
    :return: advertisement image
    """

    with open(f"ad_engine/ads/{recommended_interest}.jpg", "rb") as f:
        return f.read()
    return
