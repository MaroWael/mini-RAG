from enum import Enum
class ResponseSignal(Enum):
    
    FILE_VALIDATE_SUCCESS = "file_validate_successfully"
    FILE_SIZE_EXCEEDED = "file_size_exceeded"
    FILE_TYPE_NOT_SUPPORTED = "file_type_not_supported"
    FILE_UPLOAD_SUCCESS = "file_upload_success"
    FILE_UPLOADED_FAILED = "file_upload_failed"
    FILE_DOESNOT_EXIST = "file_does_not_exist"
    
    INVALID_PROJECT_ID = "invalid_project_id"