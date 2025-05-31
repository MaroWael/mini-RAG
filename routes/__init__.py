from fastapi import APIRouter
import os

base_router = APIRouter(
    prefix='/api/v1',
    tags=['api_v1']
)

@base_router.get('/')
async def read_root():
    app_name = os.getenv('APP_NAME')
    app_version = os.getenv('APP_VERSION')
    return {
        'name': app_name,
        'version': app_version
    }