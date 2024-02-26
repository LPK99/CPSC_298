from typing import Any
from pydantic import BaseModel, EmailStr, SecretStr, validator
import bcrypt

class SecureString(SecretStr):
    @validator("get_secret_value", pre=True, allow_reuse=True)
    def validate_secure_string(cls, value):
        # Add password length, character requirements, etc. validation here
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        return value

class HashedPassword(BaseModel):
    algorithm: str
    value: str

class LoginCredentials(BaseModel):
    username: EmailStr
    password: SecureString

def secure_hash_password(password: SecureString) -> HashedPassword:
    # Use a secure hashing algorithm like bcrypt
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.get_secret_value().encode("utf-8"), salt)
    return HashedPassword(algorithm="bcrypt", value=hashed_password.decode("utf-8"))

def login(credentials: LoginCredentials) -> bool:
    hashed_password: HashedPassword = secure_hash_password(credentials.password)
    # ... (code with explicit type checks for security-sensitive operations)
    return True  # Replace with actual logic for login validation

# Example usage:
credentials_data = {"username": "user@example.com", "password": "secure_password"}
credentials = LoginCredentials(**credentials_data)

if login(credentials):
    print("Login successful")
else:
    print("Login failed")
