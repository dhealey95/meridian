from fastapi import APIRouter

from app.api.v1.endpoints import health

router = APIRouter(prefix="/v1")

router.include_router(health.router)
# Add new endpoint routers here:
# router.include_router(users.router, prefix="/users")
