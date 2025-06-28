import cv2
import os

image_path = "/home/huskoc/Desktop/Fracture_Detection_Improved_YOLOv8-main/GRAZPEDWRI-DX/data/images/train/"
label_path = "/home/huskoc/Desktop/Fracture_Detection_Improved_YOLOv8-main/GRAZPEDWRI-DX/data/labels/train/"


ctr = 0
for txt_fie in sorted(os.listdir(label_path)):
    if ctr < 11:
        ctr+=1
        continue
    with open(os.path.join(label_path, txt_fie), "r") as f:
        lines = f.readlines()

    print(txt_fie)
    img = cv2.imread(os.path.join(image_path, txt_fie.replace(".txt", ".JPEG")))
    h, w = img.shape[:2]

    print(txt_fie.replace(".txt", ".JPEG"))
    for line in lines:
        class_id, x_center, y_center, box_w, box_h = map(float, line.strip().split()[:5])

        # Convert YOLO format (normalized) to pixel values
        x_center *= w
        y_center *= h
        box_w *= w
        box_h *= h

        x1 = int(x_center - box_w / 2)
        y1 = int(y_center - box_h / 2)
        x2 = int(x_center + box_w / 2)
        y2 = int(y_center + box_h / 2)

        # Draw rectangle and class id
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f"Class {int(class_id)}", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Show result
    cv2.imshow("YOLO Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
