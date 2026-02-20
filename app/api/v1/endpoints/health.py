from fastapi import APIRouter
from sqlalchemy import text

from app.api.deps import DBSession
from app.core.config import get_settings
from app.schemas.common import HealthResponse

router = APIRouter(tags=["health"])
settings = get_settings()


@router.get("/health", response_model=HealthResponse, summary="Health check")
async def health_check(db: DBSession) -> HealthResponse:
    await db.execute(text("SELECT 1"))
    return HealthResponse(
        status="ok",
        version="0.1.0",
        environment=settings.APP_ENV,
    )


@router.get("/health/liveness", summary="Liveness probe (no DB)")
async def liveness() -> dict[str, str]:
    return {"status": "ok"}
