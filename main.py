import requests

from config import URL
from exeptions import TreatwellRequestException
from utils import get_payload


def has_pay_at_venue(payload: dict) -> bool:
    """Поддерживает ли салон оплаты на месте - необходимо указать дату и время бронирования."""

    response = requests.post(URL, json=payload)

    if response.status_code != 200:
        raise TreatwellRequestException(f'status_code: {response.status_code}, message: {response.reason}')

    data = response.json()

    for payment_method in data['paymentMethods']:
        if payment_method['name'] == 'PAY_AT_VENUE':
            return True
    return False


if __name__ == '__main__':
    payload_data = get_payload(
        date='2023-10-18',
        time=800,
        offer_id=3415917,
        option_id=5966215,
        venue_id=404963
    )
    print(has_pay_at_venue(payload_data))
