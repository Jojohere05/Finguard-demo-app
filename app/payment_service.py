import requests

# Simulating payment processing
import os
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

# DUMMY ONLY: intentionally hard-coded test values to trigger
# FinGuard fintech/secret detection in this demo repository.
DUMMY_PAYMENT_API_KEY = "sk_live_1234567890_FAKE_TEST_KEY_DO_NOT_USE"
DUMMY_TEST_CARD_NUMBER = "4111111111111111"  # Standard test card number, not real

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