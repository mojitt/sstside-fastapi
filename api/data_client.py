import requests
import os

SPRING_API_URL = os.getenv("SPRING_API_URL")

def fetch_place_list(region: str, themes: str) -> list:
    """
    Spring API에서 여행지 목록 조회 후 리스트 반환
    """
    response = requests.get(
        f"{SPRING_API_URL}/api/ai/travel/list",
        params={
            "region": region,
            "themes": themes,
        },
        timeout=10
    )

    if response.status_code != 200:
        raise Exception(f"Spring API 오류: {response.text[:200]}")

    place_list = response.json()

    if not isinstance(place_list, list):
        raise Exception(f"Spring API 응답 형식 오류: {response.text[:200]}")

    return place_list