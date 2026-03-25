import jwt

def generate_token(user_id):
    import os
    secret = os.getenv("JWT_SECRET")
    return jwt.encode({"user": user_id}, secret, algorithm="HS256")