def get_payload(date: str, time: int, offer_id: int, option_id: int, venue_id: int) -> dict:
    """Формирует данные запроса"""

    payload = {
        "date": date,  # "2023-10-18",
        "time": time,  # 800,
        "items": [
            {
                "offerId": offer_id,  # 3415917,
                "options": [
                    {
                        "optionId": option_id  # 5966215
                    }
                ],
                "fulfillmentType": "APPOINTMENT"
            }
        ],
        "venueId": venue_id  # 404963
    }
    return payload


def formatted_header(header_str) -> dict:
    """Приводит строку в dict"""

    data = header_str.split('\n')
    result = {}
    for value in range(0, len(data), 2):
        key = value - 1
        if data[key] and data[value]:
            key = data[key].replace(':', '')
            result[key] = data[value]
    return result
