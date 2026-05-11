from fastapi import APIRouter
from app.api.endpoints import (
    tiktok_web,
    douyin_web,
    bilibili_web,
    hybrid_parsing, download,
)

router = APIRouter()

# TikTok routers
router.include_router(tiktok_web.router, prefix="/tiktok/web", tags=["TikTok-Web-API"])

# Douyin routers
router.include_router(douyin_web.router, prefix="/douyin/web", tags=["Douyin-Web-API"])

# Bilibili routers
router.include_router(bilibili_web.router, prefix="/bilibili/web", tags=["Bilibili-Web-API"])

# Hybrid routers
router.include_router(hybrid_parsing.router, prefix="/hybrid", tags=["Hybrid-API"])

# Download routers
router.include_router(download.router, tags=["Download"])
