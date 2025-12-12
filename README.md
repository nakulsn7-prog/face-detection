# Face Detection using OpenCV

This project performs real-time face detection using OpenCV's Haarcascade classifier. It can detect faces using a webcam or from a video file.

---

## 📌 Features
- Real-time face detection using webcam
- Detect faces in images or video files
- Uses Haarcascade classifier
- Fast and lightweight
- Easy to run

---

## 📁 Project Structure
Face-Detection-Project/
│
├── assets/
│    ├── haarcascade_frontalface_default.xml
│    ├── sample1.jpg
│    ├── sample2.jpg
│
├── results/
│    ├── README.md
│
├── src/
│    ├── face_detection.py
├── requirements.txt
│
└── README.md


---

## 🛠️ Requirements

Install dependencies:

pip install opencv-python
pip install numpy


Make sure the Haarcascade file is inside the `cascades/` folder.

---

## ▶️ How to Run

### 1️⃣ Run with Webcam


python src/face_detection.py


### 2️⃣ Run with a Video File
Edit this line in the code:



cam = cv2.VideoCapture(0)


Change it to:



cam = cv2.VideoCapture("samples/video.mp4")


---

## 📷 Output
The program draws rectangles around detected faces in real-time.

---

## 🧩 Code Summary

1. Load Haarcascade XML  
2. Read frames from webcam  
3. Convert to grayscale  
4. Detect faces  
5. Draw bounding boxes  
6. Display output window  
7. Press **q** to quit  

---

## 🏁 Exit
Press:



q


to stop the program.

---

## 👤 Author
Nakul S. N
