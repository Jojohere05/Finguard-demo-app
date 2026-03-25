import jwt

def generate_token(user_id):
    secret = "my_jwt_secret_key"
    return jwt.encode({"user": user_id}, secret, algorithm="HS256")