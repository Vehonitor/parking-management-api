from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from src.db.session import get_db
from src.db.models.user import User
from src.core.security import verify_password, create_access_token
from src.repositories.user_repo import UserRepo
from src.utils.logger import logger
import razorpay

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepo(db)
        self.razorpay_client = razorpay.Client(auth=("RAZORPAY_KEY_ID", "RAZORPAY_KEY_SECRET"))

    def signup(self, email: str, password: str):
        if self.user_repo.get_user_by_email(email):
            raise HTTPException(status_code=400, detail="Email already registered")
        
        user = User(email=email)
        user.set_password(password)
        self.user_repo.create_user(user)
        logger.info(f"User created: {email}")
        return {"message": "User created successfully"}

    def login(self, email: str, password: str):
        user = self.user_repo.get_user_by_email(email)
        if not user or not verify_password(password, user.password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        
        access_token = create_access_token(data={"sub": user.email})
        logger.info(f"User logged in: {email}")
        return {"access_token": access_token, "token_type": "bearer"}

    def create_payment(self, amount: float, currency: str = "INR"):
        payment = self.razorpay_client.order.create({"amount": amount * 100, "currency": currency, "payment_capture": 1})
        logger.info(f"Payment created: {payment['id']}")
        return payment

def get_auth_service(db: Session = Depends(get_db)):
    return AuthService(db)