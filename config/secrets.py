# Internal secrets (BAD PRACTICE)
import os

JWT_SECRET = os.getenv("JWT_SECRET")
RAZORPAY_KEY = os.getenv("RAZORPAY_KEY")