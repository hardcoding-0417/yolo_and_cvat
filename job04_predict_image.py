from ultralytics import YOLO


model = YOLO("훈련시킨 모델의 경로")
model.predict(source='추론할 이미지', save=True)  # 추론 및 결과 저장
