"""This is where the weather tools will be defined."""

from typing import Dict, Union

import requests


def get_weather(latitude: float, longitude: float) -> Union[str, float]:
    """
    Get current temperature for provided coordinates in celsius.

    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.

    Returns:
        str: Current temperature in celsius.
    """
    response = requests.get(
        f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}",
        timeout=60,
    )

    if response.status_code != 200:
        raise requests.exceptions.HTTPError(
            f"Error fetching weather data: {response.status_code} - {response.text}"
        )

    forecast: Dict[str, float | str] = response.json()

    return forecast["current"]
