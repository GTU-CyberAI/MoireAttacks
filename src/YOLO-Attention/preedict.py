from ultralytics import YOLO

models_path = "runs/detect/train/weights/last.pt"
#models_path = "yolov8n.pt"

model = YOLO(models_path)  # build a new model from YAML

# Train the model
model.predict("../../tests/aa2.JPEG",save=True, imgsz=800)
model.predict("../../tests/bb2.JPEG", save=True, imgsz=800)
model.predict("../../tests/real_world.jpg", save=True,  imgsz=800)
