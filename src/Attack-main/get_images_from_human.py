import os
import random
import shutil

image_source_dir = "/home/huskoc/datasets/coco_human/images"
label_source_dir = "/home/huskoc/datasets/coco_human/labels"

image_target_dir = "/home/huskoc/datasets/selected_human/images"
label_target_dir = "/home/huskoc/datasets/selected_human/labels"

os.makedirs(image_target_dir, exist_ok=True)
os.makedirs(label_target_dir, exist_ok=True)

image_files = [f for f in os.listdir(image_source_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

random_images = random.sample(image_files, min(10000, len(image_files)))

for img_name in random_images:
    src_img_path = os.path.join(image_source_dir, img_name)
    dst_img_path = os.path.join(image_target_dir, img_name)
    shutil.copyfile(src_img_path, dst_img_path)

    label_name = os.path.splitext(img_name)[0] + ".txt"
    src_label_path = os.path.join(label_source_dir, label_name)
    dst_label_path = os.path.join(label_target_dir, label_name)

    if os.path.exists(src_label_path):
        shutil.copyfile(src_label_path, dst_label_path)

print(f"{len(random_images)} görüntü ve varsa label dosyaları kopyalandı.")
