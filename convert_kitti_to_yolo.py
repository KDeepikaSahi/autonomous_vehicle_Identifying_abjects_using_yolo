import os

# Define class mapping
classes = ['Car', 'Pedestrian', 'Cyclist', 'van', 'Person_sitting', 'truck', 'tram']

def convert_label(data_label, img_width, img_height):
    cls = data_label[0]
    if cls not in classes:
        return None
    
    class_id = classes.index(cls)

    x1, y1, x2, y2 = map(float, data_label[4:8])

    x_center = ((x1 + x2) / 2) / img_width
    y_center = ((y1 + y2) / 2) / img_height
    width = (x2 - x1) / img_width
    height = (y2 - y1) / img_height

    return f"{class_id} {x_center} {y_center} {width} {height}"

# Process files
label_dir = "dataset/labels"
output_dir = "dataset/yolo_labels"

os.makedirs(output_dir, exist_ok=True)

for file in os.listdir(label_dir):
    with open(os.path.join(label_dir, file), 'r') as f:
        lines = f.readlines()

    img_width, img_height = 1242, 375  # data default

    yolo_lines = []
    for line in lines:
        parts = line.strip().split()
        if converted := convert_label(parts, img_width, img_height):
            yolo_lines.append(converted)

    with open(os.path.join(output_dir, file), 'w') as f:
        f.write("\n".join(yolo_lines))