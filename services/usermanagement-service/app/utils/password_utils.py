from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    print("jsgdhdsvfhdns",pwd_context.hash(password))
    return pwd_context.hash(password)