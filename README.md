# 🚗 Autonomous Vehicle Object Detection System (YOLOv8)

![Python](https://img.shields.io/badge/Python-3.11-blue) 
![Framework](https://img.shields.io/badge/Framework-Ultralytics_YOLOv8-red) 
![Domain](https://img.shields.io/badge/Domain-Computer_Vision-green) 
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

A computer vision-based object detection system designed for autonomous driving scenarios. This project uses **Ultralytics YOLOv8** to detect and classify road entities such as cars, pedestrians, cyclists, and trucks in real-time.

---

## Table of Contents
- [System Overview](#-system-overview)
- [Key Features](#-key-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Workflow](#-workflow)
- [Installation & Setup](#-installation--setup)
- [How to Run](#-how-to-run)
- [Results](#-results)
- [Project Roadmap](#-project-roadmap)

---

## System Overview

This project simulates a core perception module of an autonomous vehicle. It processes image/video data and detects objects using a trained YOLOv8 model.

### Core Components

1. **Dataset Processing Module**
   - Converts raw annotations (KITTI format) into YOLO format

2. **Training Module**
   - Trains YOLOv8 model using custom dataset

3. **Detection Module**
   - Performs real-time object detection using webcam/video

4. **Visualization Module**
   - Displays bounding boxes, class labels, and confidence scores

---

## 📊 Project Data Flow

```mermaid
graph LR
    A[Raw Dataset] --> B[Label Conversion]
    B --> C[Dataset Split]
    C --> D[YOLOv8 Training]
    D --> E[Trained Model]
    E --> F[Input Video/Webcam]
    F --> G[Object Detection]
    G --> H[Bounding Boxes and Labels]
  ```
## 🚀 Key Features

- 🚗 Real-time object detection (cars, pedestrians, cyclists, trucks)  
- 📦 KITTI → YOLO annotation conversion  
- 📂 Automated dataset splitting (train/validation)  
- 🧠 Custom YOLOv8 model training  
- 🎯 Detection with confidence scores  
- 📊 Visualization using OpenCV and Matplotlib  

---

## 🛠️ Tech Stack

| Component | Technology |
|----------|-----------|
| Programming Language | Python |
| Object Detection | Ultralytics YOLOv8 |
| Image Processing | OpenCV |
| Visualization | Matplotlib |
| Data Handling | NumPy |

---

## 📁 Project Structure

```text
autonomous_vehicle_Identifying_objects_using_yolo/
│
├── dataset/
│   ├── images/
│   │   ├── train/
│   │   ├── val/
│   ├── labels/
│   │   ├── train/
│   │   ├── val/
│
├── convert_kitti_to_yolo.py
├── split_dataset.py
├── train_model.py
├── detect_object.py
├── data.yaml
├── yolov8n.pt
├── runs/
├── README.md

```
##  Workflow
1. Data Preprocessing
Convert raw KITTI annotations into YOLO format
Normalize bounding box coordinates
Dataset Preparation
Split dataset into training and validation sets
Model Training
Train YOLOv8 model using custom dataset
Inference
Run real-time object detection on video/webcam

## Installations and Setup
# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install ultralytics opencv-python matplotlib numpy
## How to Run
## Step 1 — Convert Labels
python convert_kitti_to_yolo.py
## Step 2 — Split Dataset
python split_dataset.py
## Step 3 — Train Model
python train_model.py
## Step 4 — Run Detection
python detect_object.py

## Results
    Successfully detects:
        Cars 🚗
        Pedestrians 🚶
        Cyclists 🚴
    Trucks 🚛
        Output includes:
        Bounding boxes
        Class labels
        Confidence scores
## Project Roadmap
- [x] Dataset preprocessing and annotation conversion
- [x] YOLOv8 model training
- [x] Real-time object detection
- [x] Visualization of predictions
- [x] Improve accuracy with larger dataset
- [x] Add object tracking (DeepSORT)
- [x] Integrate lane detection
- [x] Deploy on edge devices (Raspberry Pi)

## Learning Outcomes

-- Hands-on experience with object detection pipelines
-- Understanding YOLO architecture and training process
-- Data preprocessing and annotation handling
-- Debugging and improving model performance
-- Real-world application of computer vision in autonomous systems

## 🙌 Acknowledgment

    This project was developed as part of my learning journey in Computer Vision, AI, and Autonomous Systems.
