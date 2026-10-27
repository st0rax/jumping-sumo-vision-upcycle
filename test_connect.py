import cv2
from pyparrot.AirSim import JumpingSumo as Sumo
from pyparrot.DroneVision import DroneVision

def test_connection():
    s = Sumo()
    success, conn = s.connect(nic=pyparrot.WiFiNic("192.168.1.100"))
    print("Verbindung:", success)
    if success:
        vision = DroneVision(s, is_bebop=False)
        vision.connect_vision()
        for _ in range(5):
            vision.save_pil_image(image_name="test_" + str(_))
        vision.disconnect_vision()
        s.disconnect()

if __name__ == "__main__":
    test_connection()
