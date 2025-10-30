from fastapi import APIRouter, FastAPI


API_PREFIX = "/openai-summary"

app = FastAPI(
    title="Appointment Summary API",
    description="API to summarize appointments using OpenAI and Twilio",
    version="1.0.0",
    docs_url=f"{API_PREFIX}/docs",       # Swagger UI
    redoc_url=f"{API_PREFIX}/redoc",     # ReDoc UI
    openapi_url=f"{API_PREFIX}/openapi.json"
)

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome", "stage": "preprod"}

@router.get("/health")
async def health():
    return {"status": "ok"}

app.include_router(router, prefix=API_PREFIX)
