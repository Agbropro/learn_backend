from fastapi import APIRouter, Depends,HTTPException
from sqlalchemy.orm import Session
from ..client.database import SessionLocal
from ..client.models import Camera, Detection
from ..schemas import CameraCreate, CameraResponse, DetectionCreate, DetectionResponse
from typing import Optional

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#ENDPOINT -> POST : Accept JSON (CameraCreate)
#RESPONSE -> JSON (CameraResponse)

@router.post("/cameras",response_model = CameraResponse)
def create_camera(camera_data:CameraCreate, db: Session = Depends(get_db)):
    new_camera = Camera(
        location=   camera_data.location,
        ip_address= camera_data.ip_address
    )

    db.add(new_camera)
    db.commit()

    db.refresh(new_camera)
    
    return new_camera

@router.post("/detections",response_model = DetectionResponse)
def create_detection(detection_data:DetectionCreate, db: Session = Depends(get_db)):

    camera = db.query(Camera).filter(Camera.id == detection_data.camera_id).first()
    if not camera:
        raise HTTPException(status_code=404, detail="Camera ID not found")

    new_detection = Detection(
        label= detection_data.label,
        confidence = detection_data.confidence,
        camera_id = detection_data.camera_id
    )

    db.add(new_detection)
    db.commit()
    db.refresh(new_detection)
    return new_detection

@router.get("/cameras", response_model = list[CameraResponse])
def read_cameras(skip:int = 0, limit:int = 100, db:Session = Depends(get_db)):
    # SQL: SELECT * FROM cameras LIMIT 100 OFFSET 0;
    cameras = db.query(Camera).offset(skip).limit(limit).all()
    return cameras

@router.get("/detections", response_model = list[DetectionResponse])
def read_detections(
    skip:int = 0,
    limit:int = 100,
    camera_id : Optional[int] = None,
    db:Session = Depends(get_db)
):
    #SELECT * FROM DETECTION
    query = db.query(Detection)

    #filter if asked for specific cam
    if camera_id:
        query = query.filter(Detection.camera_id == camera_id)
    detections = query.offset(skip).limit(limit).all()
    return detections
    

