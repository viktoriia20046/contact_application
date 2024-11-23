from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from decouple import config  # Для роботи з .env

# Конфігурація з .env
SECRET_KEY = config("SECRET_KEY", default="your_default_secret_key")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Ініціалізація схеми OAuth2
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Контекст хешування паролів
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Хешування пароля
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

# Перевірка пароля
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Створення токена доступу
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Декодування токена
def decode_access_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Invalid token or expired token")