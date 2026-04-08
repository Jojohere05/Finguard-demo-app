import requests

# Simulating payment processing
import os
STRIPE_API_KEY = os.getenv("STRIPE_API_KEY")

# DUMMY ONLY: intentionally hard-coded test values to trigger
# FinGuard fintech/secret detection in this demo repository.
HARDCODED_STRIPE_SECRET_KEY = "sk_live_FAKE_DEMO_SECRET_KEY_DO_NOT_USE"
TEST_CARD_PAN = "4111111111111111"  # Test card number, not real
TEST_CARD_CVV = "123"               # Test CVV, not real

def process_payment(amount, user_id):
    url = "https://api.stripe.com/v1/payment_intents"
    headers = {
        # Intentionally using a hard-coded key here to simulate a
        # PCI-DSS style violation for FinGuard demos.
        "Authorization": f"Bearer {HARDCODED_STRIPE_SECRET_KEY}"
    }

    data = {
        "amount": amount,
        "currency": "inr"
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()