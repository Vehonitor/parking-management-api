# ============================================================================
# src/utils/twilio_client.py
# ============================================================================
from twilio.rest import Client
from src.core.config import settings
from typing import Dict
import logging

logger = logging.getLogger(__name__)


class TwilioClient:
    """Wrapper for sending SMS/OTP via Twilio."""

    def __init__(self):
        # ✅ All values come from serverless.yml environment
        self.client = Client(
            settings.TWILIO_ACCOUNT_SID,
            settings.TWILIO_AUTH_TOKEN
        )
        self.from_number = settings.TWILIO_FROM_NUMBER

    def send_sms(self, to_number: str, message: str) -> Dict:
        """Send SMS using Twilio API."""
        try:
            # Format phone number — ensure it includes country code
            if not to_number.startswith('+'):
                to_number = f"+91{to_number}"  # Default to India — adjust for your region

            msg = self.client.messages.create(
                body=message,
                from_=self.from_number,
                to=to_number
            )

            logger.info(f"✅ SMS sent to {to_number}, SID: {msg.sid}")
            return {
                "success": True,
                "sid": msg.sid,
                "status": msg.status
            }

        except Exception as e:
            logger.error(f"❌ Failed to send SMS to {to_number}: {str(e)}")
            return {
                "success": False,
                "error": str(e)
            }

    def send_otp(self, to_number: str, otp_code: str) -> Dict:
        """Send an OTP via SMS."""
        message = (
            f"Your {settings.APP_NAME} verification code is: {otp_code}. "
            f"Valid for {settings.OTP_EXPIRY_MINUTES} minutes."
        )
        return self.send_sms(to_number, message)
