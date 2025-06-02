from fastapi import APIRouter, Depends, UploadFile, status
from fastapi.responses import JSONResponse
from helper.config import get_settings, Settings
from controllers import DataController
from model import ResponseSignal
import aiofiles
import logging
logger = logging.getLogger('uvicorn.error')

data_router = APIRouter(
    prefix="/api/v1/data",
    tags=["api_v1", "data"]
)
@data_router.post("/upload/{project_id}")
async def upload_data(project_id: str, file: UploadFile,
                    app_settings: Settings = Depends(get_settings)):

    if not project_id.strip():
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseSignal.INVALID_PROJECT_ID.value}
        )
        
    if not file.filename:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": ResponseSignal.FILE_DOESNOT_EXIST.value}
        )
    
    data_controller = DataController()
    is_valid, msg = data_controller.validate_uploaded_file(file)
    if not is_valid:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"message": msg, "project_id": project_id, "file_name": file.filename}
        )
    
    file_path = data_controller.generate_unique_file_name(file.filename, project_id)
    
    try:
        async with aiofiles.open(file_path, 'wb') as out_file:
            while True:
                content = await file.read(app_settings.FILE_DEFAULT_CHUNK_SIZE)
                if not content:
                    break
                await out_file.write(content)
    except Exception as e:
        logger.error(f"Failed to upload file {file.filename} for project {project_id}: {e}")
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={"message": ResponseSignal.FILE_UPLOAD_FAILED.value}
        )
        
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": ResponseSignal.FILE_UPLOAD_SUCCESS.value,
        }
    )