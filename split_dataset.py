import os
import random
import shutil

image_folder = "dataset/images_all"
label_folder = "dataset/labels"

train_img = "dataset/images/train"
val_img = "dataset/images/val"
train_lbl = "dataset/labels/train"
val_lbl = "dataset/labels/val"

# Create folders
for folder in [train_img, val_img, train_lbl, val_lbl]:
    os.makedirs(folder, exist_ok=True)

images = [f for f in os.listdir(image_folder) if f.endswith(".png")]

random.shuffle(images)

split_index = int(0.8 * len(images))

train_files = images[:split_index]
val_files = images[split_index:]

def copy_files(files, img_dest, lbl_dest):
    for file in files:
        shutil.copy(os.path.join(image_folder, file), img_dest)

        label_file = file.replace(".png", ".txt")
        shutil.copy(os.path.join(label_folder, label_file), lbl_dest)

copy_files(train_files, train_img, train_lbl)
copy_files(val_files, val_img, val_lbl)

print("✅ Dataset split done")