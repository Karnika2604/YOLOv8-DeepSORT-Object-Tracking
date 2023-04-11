# YOLOv8-DeepSORT-Object-Tracking


#Features

#YOLOv8 Object Detection with DeepSORT Tracking(ID + Trails)

# Steps to run Code
# Clone the repository

git clone https://github.com/noorkhokhar99/YOLOv8-Object-Detection-with-DeepSORT-Tracking.git

#Goto cloned folder
%cd YOLOv8-Object-Detection-with-DeepSORT-Tracking

#Install the ultralytics package
pip install ultralytics==8.0.0

#Setting the Directory.
%cd yolo/v8/detect

#Copy deep_sort_pytorch folder and place the deep_sort_pytorch folder into the yolo/v8/detect folder

#Do Tracking with mentioned command below

# video file

python tracking_vehicle_counting.py model=yolov8l.pt source="test.mp4" show=True
