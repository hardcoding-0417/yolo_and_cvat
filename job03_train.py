from ultralytics import YOLO


# 데이터셋 경로 설정
data_path = 'dataset.yaml'  # 데이터셋 폴더 구성 파일 경로

# 모델 초기화
model = YOLO('yolov8n.pt')  # YOLOv8 모델 불러오기

# 훈련
model.train(data=data_path, 
            epochs=100, 
            imgsz=640, 
            batch_size=16, 
            device='0')

# 평가
results = model.val()  # 평가 결과 얻기



