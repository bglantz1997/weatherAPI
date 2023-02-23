from fastapi import HTTPException


class Conflict(Exception):
    pass


class NotFound(Exception):
    pass


def raise_not_found_user(user_id: int):
    raise HTTPException(status_code=404, detail=f"could not find user {user_id}")


def raise_not_found_favorites_for_user(user_id: int):
    raise HTTPException(status_code=404, detail=f"could not find favorites data for {user_id}")


def raise_not_found_city(city_name: str):
    raise HTTPException(status_code=404, detail=f"could not find weather data for {city_name}")


def raise_conflict_favorite(city_name: str, user_id: int):
    raise HTTPException(status_code=409, detail=f"{city_name} has already been added as favorite by user {user_id}")
