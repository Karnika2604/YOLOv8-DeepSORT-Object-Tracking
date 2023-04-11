# -*- coding: utf-8 -*-
"""Vehicle tracking using YOLOv8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d482vsvhpXiL8wlQvVQDgZjRikDtm8Cc
"""

!git clone https://github.com/Karnika2604/YOLOv8-DeepSORT-Object-Tracking.git

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/YOLOv8-DeepSORT-Object-Tracking

!pip install -r requirements.txt

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/YOLOv8-DeepSORT-Object-Tracking
!pip install ultralytics==8.0.0

!gdown https://drive.google.com/uc?id=1sNDpfn-6JnGv6xyTrET60Z7R_dafIelT

!yolo task=detect mode=predict model=yolov8n.pt source="test1.mp4"

!rm "/content/result_compressed.mp4"

from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/YOLOv8-DeepSORT-Object-Tracking/runs/detect/predict/test1.mp4'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=600 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)

#Segmentation of Video

!yolo task=segment mode=predict  source="test1.mp4"

!rm "/content/result_compressed.mp4"

from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/YOLOv8-DeepSORT-Object-Tracking/runs/segment/predict/test1.mp4'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=600 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)

#IMPLEMENTING THE DeepSORT TRACKING

!apt-get install -y xvfb # Install X Virtual Frame Buffer
import os
os.system('Xvfb :1 -screen 0 1600x1200x16  &')    # create virtual display with size 1600x1200 and 16 bit color. Color can be changed to 24 or 8
os.environ['DISPLAY']=':1.0'

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/YOLOv8-DeepSORT-Object-Tracking/ultralytics/yolo/v8/detect

!gdown "https://drive.google.com/uc?id=1Dv38MpEF5Ee-myzj2VE8IGiVRtRsnLdt"

!unzip deep_sort_pytorch.zip

#  Running the DeepSORT Tracking for Detection

!python tracking.py model=yolov8l.pt source="/content/YOLOv8-DeepSORT-Object-Tracking/test1.mp4" show=True

!rm "/content/result_compressed.mp4"

from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/YOLOv8-DeepSORT-Object-Tracking/runs/detect/train/test1.mp4'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=600 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)

!gdown https://drive.google.com/uc?id=17ZETHZR26LPotRPNxqtKkYAZHlcGhTzp

!python tracking_vehicle_counting.py model=yolov8x.pt source="Test Video.mp4" show=True

!rm "/content/result_compressed.mp4"

from IPython.display import HTML
from base64 import b64encode
import os

# Input video path
save_path = '/content/YOLOv8-DeepSORT-Object-Tracking/runs/detect/train2/Testvideo.mp4'

# Compressed video path
compressed_path = "/content/result_compressed.mp4"

os.system(f"ffmpeg -i {save_path} -vcodec libx264 {compressed_path}")

# Show video
mp4 = open(compressed_path,'rb').read()
data_url = "data:video/mp4;base64," + b64encode(mp4).decode()
HTML("""
<video width=1000 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)