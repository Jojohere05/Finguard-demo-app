import requests

# Simulating payment processing
STRIPE_API_KEY = "sk_test_123456789"

def process_payment(amount, user_id):
    url = "https://api.stripe.com/v1/payment_intents"
    headers = {
        "Authorization": f"Bearer {STRIPE_API_KEY}"
    }

    data = {
        "amount": amount,
        "currency": "inr"
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()