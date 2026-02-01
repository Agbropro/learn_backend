import sys
import os 

from internal.client.database import engine, Base, SessionLocal
from internal.client.models import Camera, Detection

def main():
    print("--- 1. CREATING DATABASE TABLES ---")
    # This looks at your 'models.py' and runs the SQL "CREATE TABLE" commands
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully!\n")

    print("--- 2. INSERTING DATA ---")
    session = SessionLocal()

    # Create a Camera
    cam_1 = Camera(location="Lobby", ip_address="192.168.1.100")
    
    # Create a Detection linked to that Camera (using append magic)
    det_1 = Detection(label="Thief", confidence=0.99)
    cam_1.detections.append(det_1)

    # Add to session and Save
    session.add(cam_1)
    session.commit()
    print("Data saved to database!\n")

    print("--- 3. READING DATA ---")
    # Fetch the camera back
    saved_cam = session.query(Camera).filter_by(location="Lobby").first()
    
    print(f"Found Camera: {saved_cam.location}")
    print(f"Camera IP: {saved_cam.ip_address}")
    
    # Print its children (The detection)
    for det in saved_cam.detections:
        print(f" -> It saw: {det.label} with {det.confidence} confidence")

    session.close()

if __name__ == "__main__":
    main()