
# YOLOv8 Object Detection – Image & Video

A Computer Vision project demonstrating **object detection using YOLOv8n, Ultralytics YOLO, Python, OpenCV, and NumPy**.

This project covers two practical use cases:

- **Image Object Detection** using a teacher-student discussion image
- **Video Object Detection** using a short elephant video

---

## 🚀 Project Overview

The main goal of this project is to understand how a pretrained **YOLOv8n object detection model** can identify objects from images and videos.

The project demonstrates the complete workflow:

**Input Image/Video → YOLOv8n Inference → Detection Results → Bounding Boxes → Class & Confidence Display**

---

## 🔹 1. Image Object Detection

For image prediction, I used a **teacher-student discussion image** as the input.

The pretrained YOLOv8n model processes the image and detects objects based on the classes supported by the pretrained model.

### Concepts Used

- Python
- Ultralytics YOLO
- YOLOv8n
- Image Object Detection
- Confidence Threshold
- Bounding Boxes
- NumPy

### Basic Implementation

```python
from ultralytics import YOLO

# Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt", "v8")

# Perform object detection
detection_output = model.predict(
    source="input/teacher_student.jpg",
    conf=0.25,
    save=True
)

# Display prediction results
print(detection_output)

The model generates detection results containing information about the objects identified in the image.

🔹 2. Video Object Detection

For video prediction, I used a short elephant video.

The video is processed frame-by-frame using OpenCV.

For each frame:

Capture the video frame
Send the frame to YOLOv8n
Detect objects
Extract class ID
Extract confidence score
Extract bounding-box coordinates
Draw bounding boxes using OpenCV
Display the detected object information
Concepts Used
OpenCV
YOLOv8n
Video Processing
Frame-by-Frame Processing
Object Detection
Bounding Boxes
Confidence Scores
Class IDs
🔹 Video Detection Workflow
Elephant Video
      ↓
OpenCV Video Capture
      ↓
Read Individual Frame
      ↓
YOLOv8n Object Detection
      ↓
Extract Detection Results
      ↓
Class ID + Confidence + Coordinates
      ↓
Draw Bounding Box
      ↓
Display Frame
🔹 Detection Information

The video detection implementation extracts important information from each detected object.

Class ID
clsID = box.cls.numpy()[0]

The class ID represents the detected object class.

Confidence Score
conf = box.conf.numpy()[0]

The confidence value represents how confident the model is about the detection.

Bounding Box Coordinates
bb = box.xyxy.numpy()[0]

The xyxy values represent:

x1 → left
y1 → top
x2 → right
y2 → bottom

These coordinates are used to draw the bounding box around the detected object.

🔹 Bounding Box Visualization

OpenCV is used to draw the detection box:

cv2.rectangle(
    frame,
    (int(bb[0]), int(bb[1])),
    (int(bb[2]), int(bb[3])),
    detection_colors[int(clsID)],
    3
)

The detected class name and confidence information are also displayed on the frame.

🛠️ Technologies Used
Python
YOLOv8n
Ultralytics
OpenCV
NumPy
Computer Vision
📦 Installation

Clone the repository:

git clone https://github.com/PavanTorlapatiCodes/YOUR-REPOSITORY.git

Move into the project directory:

cd YOUR-REPOSITORY

Install the required Python packages:

pip install -r requirements.txt
📁 Project Structure
YOLOv8-Object-Detection/
│
├── yolov8n.py
├── yolov8noencv.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── weights/
│   └── yolov8n.pt
│
├── input/
│   ├── teacher_student.jpg
│   └── elephant.mp4
│
└── output/
▶️ How to Run
Image Detection

Run:

python yolov8n.py

The model will process the input image and generate the detection results.

Video Detection

Run:

python yolov8noencv.py

The video will be processed frame-by-frame.

Press:

Q

to stop the video detection window.

🎯 Confidence Threshold

The image detection implementation uses:

conf=0.25

The video detection implementation uses:

conf=0.45

The confidence threshold controls which detections are considered sufficiently confident to be displayed.

📚 Learning Outcomes

Through this project, I gained practical experience with:

Understanding YOLO object detection
Loading a pretrained YOLOv8n model
Performing image inference
Performing video inference
Processing video frames using OpenCV
Extracting class IDs
Extracting confidence scores
Extracting bounding-box coordinates
Drawing bounding boxes using OpenCV
Understanding YOLO prediction outputs
Combining deep-learning inference with OpenCV
🔮 Future Improvements

Some possible improvements for this project are:

Webcam-based real-time object detection
Object counting
Object tracking
FPS monitoring
Saving annotated videos
Saving detection results
Building a simple user interface
Training YOLO on a custom dataset
Developing domain-specific object detection applications
⚠️ Important Note

This project uses a pretrained YOLOv8n model for object detection.

It demonstrates model inference and computer vision processing. It is not presented as a custom-trained YOLO model.

👨‍💻 Author

Pavan Kumar Torlapati

GitHub:
https://github.com/PavanTorlapatiCodes

LinkedIn:
https://www.linkedin.com/in/pavan-torlapati-7543732ba

⭐ Project Focus

Computer Vision | Object Detection | YOLOv8 | OpenCV | Python | Deep Learning


**Small recommendation:** GitHub lo paste chesetappudu `YOUR-REPOSITORY` ni mee actual repository name tho replace chey
