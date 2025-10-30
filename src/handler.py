# from mangum import Mangum
# from src.main import app
# from src.utils.logger import logger

# # Create Lambda handler
# handler = Mangum(app, lifespan="off")

# # Log handler initialization
# logger.info("Lambda handler initialized")

import os
import json
import logging
from datetime import datetime, timezone

from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from mangum import Mangum

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment variables
STAGE = os.getenv("STAGE", "dev")
S3_BUCKET = os.getenv("S3_BUCKET", "aws-transcribe-twilio")

# Helper for consistent responses
def http_response(status_code: int, content):
    if isinstance(content, dict):
        payload = content
    else:
        payload = {"message": content}
    return JSONResponse(status_code=status_code, content=payload)

# FastAPI app
app = FastAPI(title="Appointment Summary API")
router = APIRouter()

@router.get("/")
async def root():
    logger.info("Root endpoint called")
    return {"message": "Welcome to Appointment Summary API", "stage": STAGE}

@router.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(router)

# Lambda handler
handler = Mangum(app, api_gateway_base_path="/openai-summary")