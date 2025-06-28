import json
import os
import shutil

coco_annotation_path = '/home/huskoc/coco_test/annotations/instances_train2017.json'
coco_images_path = '/home/huskoc/coco_test/train2017'
output_images_path = '/home/huskoc/output/images'
output_labels_path = '/home/huskoc/output/labels'

os.makedirs(output_images_path, exist_ok=True)
os.makedirs(output_labels_path, exist_ok=True)

with open(coco_annotation_path, 'r') as f:
    coco = json.load(f)

person_category_id = 1
image_id_to_annotations = {}

for ann in coco['annotations']:
    if ann['category_id'] == person_category_id:
        image_id = ann['image_id']
        if image_id not in image_id_to_annotations:
            image_id_to_annotations[image_id] = []
        image_id_to_annotations[image_id].append(ann)

image_id_to_info = {img['id']: img for img in coco['images']}

def coco_to_yolo(bbox, img_w, img_h):
    x, y, w, h = bbox
    x_center = (x + w / 2) / img_w
    y_center = (y + h / 2) / img_h
    w /= img_w
    h /= img_h
    return x_center, y_center, w, h

for image_id, anns in image_id_to_annotations.items():
    image_info = image_id_to_info[image_id]
    filename = image_info['file_name']
    img_w, img_h = image_info['width'], image_info['height']

    src_path = os.path.join(coco_images_path, filename)
    dst_path = os.path.join(output_images_path, filename)

    shutil.copyfile(src_path, dst_path)

    label_lines = []
    for ann in anns:
        bbox = ann['bbox']
        x_center, y_center, w_box, h_box = coco_to_yolo(bbox, img_w, img_h)
        label_lines.append(f"0 {x_center:.6f} {y_center:.6f} {w_box:.6f} {h_box:.6f}")

    label_filename = os.path.splitext(filename)[0] + ".txt"
    label_path = os.path.join(output_labels_path, label_filename)
    with open(label_path, 'w') as f:
        f.write('\n'.join(label_lines))

print("Extraction complete.")
