from typing import Optional
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from repositories.user_repo import UserRepository
from src.api.v1.schemas.user import UserCreate, UserLogin, Token
from src.core.security import verify_password, create_access_token
from src.db.models.user import User
from src.utils.logger import logger


class AuthService:
    """Service for authentication and authorization."""
    
    def __init__(self, db: Session):
        self.db = db
        self.user_repo = UserRepository(db)
    
    def register_user(self, user_data: UserCreate) -> User:
        """
        Register a new user.
        
        Args:
            user_data: User registration data
            
        Returns:
            Created user
            
        Raises:
            HTTPException: If email or username already exists
        """
        # Check if email already exists
        existing_user = self.user_repo.get_by_email(user_data.email)
        if existing_user:
            logger.warning(f"Registration attempt with existing email: {user_data.email}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        # Check if username already exists
        existing_user = self.user_repo.get_by_username(user_data.username)
        if existing_user:
            logger.warning(f"Registration attempt with existing username: {user_data.username}")
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )
        
        # Create new user
        user = self.user_repo.create(user_data)
        logger.info(f"New user registered: {user.username} ({user.email})")
        return user
    
    def login(self, login_data: UserLogin) -> Token:
        """
        Authenticate user and generate access token.
        
        Args:
            login_data: Login credentials
            
        Returns:
            Access token
            
        Raises:
            HTTPException: If credentials are invalid
        """
        # Get user by username
        user = self.user_repo.get_by_username(login_data.username)
        if not user:
            logger.warning(f"Login attempt with non-existent username: {login_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        
        # Verify password
        if not verify_password(login_data.password, user.hashed_password):
            logger.warning(f"Failed login attempt for user: {login_data.username}")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password"
            )
        
        # Check if user is active
        if not user.is_active:
            logger.warning(f"Login attempt by inactive user: {login_data.username}")
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive"
            )
        
        # Update last login
        self.user_repo.update_last_login(user.id)
        
        # Create access token
        access_token = create_access_token(
            data={"sub": user.id, "username": user.username, "role": user.role.value}
        )
        
        logger.info(f"User logged in: {user.username}")
        return Token(access_token=access_token)
    
    def get_current_user(self, token_payload: dict) -> User:
        """
        Get current user from token payload.
        
        Args:
            token_payload: Decoded JWT token payload
            
        Returns:
            Current user
            
        Raises:
            HTTPException: If user not found or inactive
        """
        user_id = token_payload.get("sub")
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        
        if not user.is_active:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="User account is inactive"
            )
        
        return user