from ultralytics import YOLO

model = YOLO("yolov8x.pt")
results = model.predict(source="https://ultralytics.com/images/bus.jpg", save=True, device="mps")


