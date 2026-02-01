import requests
import time
import random

SERVER_URL = "http://localhost:8000"

def register_camera():

    print("----- REGISTERING CAMERA -----")

    payload = {
        "location": "Diddy Playhouse",
        "ip_address": "192.168.1.151"
    }
    try:
        response = requests.post(f"{SERVER_URL}/cameras", json=payload)
        
        if response.status_code == 200:
            camera_data = response.json()
            print(f"Camera registered successfully! ID: {camera_data['id']}")
            return camera_data['id']
        else:
            print("Camera already registered (IP exists).")
             
    except Exception as e:
        print(f"Error: {e}")
        return None


def start_surveilance(camera_id):
    print("\n----- STARTING SURVEILLANCE -----")
    
    classes = ["Prisoner", "Guard", "Pria Solo", "Tump","Nothing"]

    #looping
    while True: 
        detected_object = random.choice(classes)
        confidence = round(random.uniform(0.7, 0.99),2)

        if detected_object == "Nothing":
            print("Scanning... Nothing detected.")
            time.sleep(1)
            continue
        
        #prepare report
        report = {
            "label": detected_object,
            "confidence": confidence,
            "camera_id": camera_id
        }

        #send detection to server
        try: 
            print(f"-> Detecting {detected_object}... Sending to Server.")
            response = requests.post(f"{SERVER_URL}/detections/",json=report)
            if response.status_code == 200:
                print(f"   [Server]: Received! Log ID: {response.json()['id']}")
            else:
                print(f"   [Server]: Error {response.status_code}")
        except Exception as e:
            print(f"   [Error]: Connection lost! {e}")
        
        time.sleep(2)

if __name__ == "__main__":
    my_id = register_camera()
    if my_id:
        try:
            start_surveilance(my_id)
        except KeyboardInterrupt:
            print("\n----- SHUTTING DOWN CAMERA -----")
        