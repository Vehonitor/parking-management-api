
# ============================================================================
# STEP 7: Create src/utils/twilio_client.py
# ============================================================================
import os
from twilio.rest import Client
from src.core.config import settings
from typing import Optional
import logging
TWILIO_ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
logger = logging.getLogger(__name__)

class TwilioClient:
    def __init__(self):
        self.client = Client(
            TWILIO_ACCOUNT_SID,
           TWILIO_AUTH_TOKEN
        )
        self.from_number = TWILIO_FROM_NUMBER
    
    def send_sms(self, to_number: str, message: str) -> dict:
        """Send SMS using Twilio"""
        try:
            # Format phone number (ensure it has country code)
            if not to_number.startswith('+'):
                to_number = f"+91{to_number}"  # Default to India, change as needed
            
            message = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )
            
            logger.info(f"SMS sent to {to_number}, SID: {message.sid}")
            return {
                "success": True,
                "sid": message.sid,
                "status": message.status
            }
        except Exception as e:
            logger.error(f"Failed to send SMS to {to_number}: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }
    
    def send_otp(self, to_number: str, otp_code: str) -> dict:
        """Send OTP via SMS"""
        message = f"Your {settings.APP_NAME} verification code is: {otp_code}. Valid for {settings.OTP_EXPIRY_MINUTES} minutes."
        return self.send_sms(to_number, message)

