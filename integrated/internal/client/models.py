from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Camera(Base):
    __tablename__ = "cameras"

    id = Column(Integer, primary_key=True, index=True)
    location = Column(String)
    ip_address = Column(String,unique=True)

    detections = relationship("Detection", back_populates="camera")

    def __repr__(self):
        return f"<Camera(location='{self.location}')>"

class Detection(Base): 
    __tablename__ = "detections"

    id = Column(Integer, primary_key=True, index=True)
    label = Column(String)
    confidence = Column(Float)
    camera_id = Column(Integer, ForeignKey("cameras.id"))
    # The Relationship (Child side)
    # This lets us say: my_detection.camera
    camera = relationship("Camera", back_populates="detections")

    def __repr__(self):
        return f"<Detection(label='{self.label}', conf={self.confidence})>"