from fastapi import FastAPI
import logging
import sys

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Create a StreamHandler to log to stdout
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
logger.addHandler(handler)

def log_request(request):
    logger.info(f"Request: {request.method} {request.url}")

def log_response(response):
    logger.info(f"Response: {response.status_code}")

def log_exception(exception):
    logger.error(f"Exception: {exception}")