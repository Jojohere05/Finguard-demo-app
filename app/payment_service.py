import requests

# Simulating payment processing
import os
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

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