import os
import shutil
import random

image_dir = "dataset/images"
label_dir = "dataset/yolo_labels"

train_img_dir = "dataset/images/train"
val_img_dir = "dataset/images/val"
train_lbl_dir = "dataset/labels/train"
val_lbl_dir = "dataset/labels/val"

os.makedirs(train_img_dir, exist_ok=True)
os.makedirs(val_img_dir, exist_ok=True)
os.makedirs(train_lbl_dir, exist_ok=True)
os.makedirs(val_lbl_dir, exist_ok=True)

images = os.listdir(image_dir)
random.shuffle(images)

split = int(0.8 * len(images))

train_files = images[:split]
val_files = images[split:]

for file in train_files:
    shutil.move(f"{image_dir}/{file}", train_img_dir)
    shutil.move(f"{label_dir}/{file.replace('.png','.txt')}", train_lbl_dir)

for file in val_files:
    shutil.move(f"{image_dir}/{file}", val_img_dir)
    shutil.move(f"{label_dir}/{file.replace('.png','.txt')}", val_lbl_dir)