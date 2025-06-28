from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from YAML

# Train the model
results = model.train(data="/home/huskoc/Desktop/Fracture_Detection_Improved_YOLOv8-main/GRAZPEDWRI-DX/data/meta.yaml", epochs=100, imgsz=800, batch = 4)