from ultralytics import YOLO

# Load the model
model = YOLO('yolov8n.pt')

# Train the model
model.train(data='data.yaml', epochs=10, imgsz=1275, hyp='hyp.yaml', name='pothole_augmented')
model.val(data='data.yaml')
metrics = model.val()
print(metrics)
results = model.predict(source='istockphoto-502561495-612x612.jpg', save=True, conf=0.3)
