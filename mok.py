import requests

def get_cat_image(breed_id, headers):
    """
    Получает данные о котике с API.

    Args:
        breed_id (str): Идентификатор породы
        headers (dict): Заголовки запроса

    Returns:
        dict: Данные о котике или None при ошибке
    """
    url = f"https://api.thecatapi.com/v1/images/search?breed_ids={breed_id}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None
