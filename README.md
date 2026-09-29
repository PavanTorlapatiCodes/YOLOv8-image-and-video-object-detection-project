YOLOv8 Object Detection – Image & Video
A computer vision project demonstrating real-time object detection using YOLOv8n, Ultralytics YOLO, and OpenCV.

The project covers two practical use cases:

Image Object Detection: Detects objects in an image using a pretrained YOLOv8n model.
Video Object Detection: Processes a video frame-by-frame and draws bounding boxes, class labels, and confidence values around detected objects.
Project Highlights
YOLOv8n pretrained object detection
Image-based object detection
Frame-by-frame video detection
OpenCV video capture and display
Bounding-box visualization
Class ID and confidence extraction
NumPy conversion of YOLO prediction results
Configurable confidence thresholds
Custom class-label file support
Technologies Used
Python
Ultralytics YOLO
YOLOv8n
OpenCV
NumPy
How It Works
1. Image Detection
The image detection script loads a pretrained YOLOv8n model and runs prediction on an input image.

The model is loaded with:

from ultralytics import YOLO

model = YOLO("yolov8n.pt", "v8")
Prediction is performed with a confidence threshold:

detection_output = model.predict(
    source="path/to/image.jpg",
    conf=0.25,
    save=True
)
The prediction result contains the detected objects and their detection information.

2. Video Detection
The video script uses OpenCV to read the video frame-by-frame.

For every frame:

A frame is captured from the video.
YOLOv8n performs object detection.
Detection boxes are extracted.
Class IDs and confidence values are obtained.
Bounding boxes are drawn using OpenCV.
The detected class name and confidence are displayed.
The processed frame is shown in a window.
The video loop continues until the video ends or the user presses Q.

Example Demonstrations
Image Prediction
For the image demonstration, a teacher-student discussion image is used as the input. YOLOv8n identifies objects that belong to its pretrained COCO classes and displays the detection results.

Video Prediction
For the video demonstration, a short elephant video is processed frame-by-frame. The model detects objects in the video and displays bounding boxes and confidence information.

Note: The exact objects detected depend on the classes supported by the pretrained YOLOv8n model and the confidence threshold.

Important Implementation Details
Confidence Threshold
The image script uses:

conf=0.25
The video script uses:

conf=0.45
A higher threshold generally filters out more low-confidence detections.

Bounding Boxes
OpenCV is used to draw the detected object's bounding box from the YOLO xyxy coordinates.

Detection Information
The video implementation extracts:

box.cls → detected class ID
box.conf → confidence score
box.xyxy → bounding-box coordinates
Installation
Clone the repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
Create a virtual environment if required:

python -m venv venv
Activate it on Windows:

venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Required Model
The project uses the pretrained:

yolov8n.pt
Keep the model file in the project directory or update the model path in the Python scripts.

For the video script, if you use:

YOLO("weights/yolov8n.pt", "v8")
place the model at:

weights/yolov8n.pt
Input Files
Recommended project structure:

YOLOv8-Object-Detection/
│
├── yolov8n.py
├── yolov8noencv.py
├── yolov8n.pt
├── weights/
│   └── yolov8n.pt
├── elephant.txt
├── input/
│   ├── teacher_student.jpg
│   └── elephant.mp4
├── output/
├── requirements.txt
├── .gitignore
└── README.md
Update the input paths in the Python files before running them.

Running the Project
Image detection:

python yolov8n.py
Video detection:

python yolov8noencv.py
Press:

Q
to stop the video window.

Learning Outcomes
Through this project, I practiced:

Applying a pretrained computer vision model
Understanding YOLO object detection output
Working with image and video inputs
Processing video frames using OpenCV
Extracting class IDs, confidence scores, and coordinates
Visualizing detections with bounding boxes
Connecting deep-learning inference with OpenCV
Future Improvements
Add webcam/live-camera detection
Build a cleaner user interface
Save annotated image/video outputs
Add object counting
Add FPS monitoring
Improve confidence-score formatting
Add tracking using a suitable YOLO tracking workflow
Use a custom-trained dataset for domain-specific objects
Disclaimer
This project demonstrates inference using a pretrained YOLOv8n model. It is not presented as a custom-trained YOLO model unless a separate training dataset and training process are added.

Author
Pavan Kumar Torlapati

GitHub: https://github.com/PavanTorlapatiCodes

LinkedIn: https://www.linkedin.com/in/pavan-torlapati-7543732ba
