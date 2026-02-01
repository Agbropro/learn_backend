from pydantic import BaseModel 

class CameraCreate(BaseModel):
    location:   str
    ip_address: str

class CameraResponse(CameraCreate):
    id:         int

    class Config: 
        # This tells Pydantic: "It's okay to read data from a SQLAlchemy class"
        from_attributes = True

class DetectionCreate(BaseModel):
    label:      str
    confidence: float
    camera_id:  int

class DetectionResponse(DetectionCreate):
    id:         int
    
    class Config: 
        from_attributes = True