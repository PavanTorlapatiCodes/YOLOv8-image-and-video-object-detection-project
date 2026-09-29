from ultralytics import YOLO
import numpy

# load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt", "v8")  

# predict on an image"C:\Users\T pavan kumar\Downloads\download (5).jpg"
detection_output = model.predict(source=r"C:\Users\T pavan kumar\Downloads\students.jpg", conf=0.25, save=True) 

# Display tensor array
print(detection_output)
# Display numpy array
# print(detection_output[0].numpy())