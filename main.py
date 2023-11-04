import requests

def make_payment(amount, currency, payee_address):
    """Make an Interledger payment.

    Args:
        amount: The amount to pay.
        currency: The currency to pay in.
        payee_address: The Interledger address of the payee.

    Returns:
        A tuple containing the payment status and the payment ID.
    """

    payload = {
        "amount": amount,
        "currency": currency,
        "payee_address": payee_address,
    }

    response = requests.post("https://example.com/api/payments", json=payload)

    if response.status_code == 200:
        payment_status = "success"
        payment_id = response.json()["payment_id"]
    else:
        payment_status = "failed"
        payment_id = None

    return payment_status, payment_id

# Example usage:

amount = 10
currency = "USD"
payee_address = "ilp://example.com/payee"

payment_status, payment_id = make_payment(amount, currency, payee_address)

if payment_status == "success":
    print("Payment successful!")
else:
    print("Payment failed.")
