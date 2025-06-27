"""Here is how the API calls to tools will be defined."""

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "Provide weather forecast for a given location.",
        "parameters": {
            "type": "object",
            "properties": {
                "latitude": {
                    "type": "number",
                    "description": "Latitude of the location.",
                },
                "longitude": {
                    "type": "number",
                    "description": "Longitude of the location.",
                },
            },
            "additionalProperties": False,
            "required": ["latitude", "longitude"],
            "strict": True,
        },
    }
]
