from pydantic import BaseModel
from datetime import datetime

class UploadedFileResponse(BaseModel):
    id: int
    student_id: int
    filename: str
    stored_name: str
    file_path: str
    content_type: str
    category: str
    uploaded_at:datetime

    model_config = {
        "from_attributes": True
    }







