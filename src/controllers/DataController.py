from .BaseController import BaseController
from fastapi import UploadFile
from model import ResponseSignal
from .ProjectController import ProjectController
import re
import os

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024 
    
    def validate_uploaded_file(self, file: UploadFile) -> tuple[bool, str]:
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value

        if file.size is None:
            content = file.file.read()
            file_size = len(content)
            file.file.seek(0)
        else:
            file_size = file.size

        if file_size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseSignal.FILE_VALIDATE_SUCCESS.value
    
    def generate_unique_filepath(self, orig_file_name: str, project_id: str) -> str:
        random_key = self.generate_random_string()
        project_path = ProjectController().get_project_path(project_id)
        cleaned_file_name = self.get_clean_file_name(orig_file_name)
        new_file_path = os.path.join(project_path, f"{random_key}_{cleaned_file_name}")

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(project_path, f"{random_key}_{cleaned_file_name}")
        
        return new_file_path, f"{random_key}_{cleaned_file_name}"

    def get_clean_file_name(self, orig_file_name: str) -> str:
        cleaned_file_name = re.sub(r'[^\w\.-]', '', orig_file_name.strip())
        cleaned_file_name = cleaned_file_name.replace(" ", "_")
        return cleaned_file_name
