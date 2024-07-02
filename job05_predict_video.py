from ultralytics import YOLO
import cv2
import os
# YOLO 모델 로드
model = YOLO("훈련시킨 모델의 경로")

# 영상 파일 열기
video_source = '추론할 영상의 경로'
cap = cv2.VideoCapture(video_source)

# 출력 영상 설정
output_path = './output.mp4'
os.makedirs(output_path, exsit_ok=False)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # 비디오 코덱 설정
fps = cap.get(cv2.CAP_PROP_FPS)  # 입력 영상의 프레임 속도

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

# 프레임별로 추론 수행
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # YOLO 모델로 추론
    results = model.predict(source=frame)

    # 결과 프레임에 주석 추가
    annotated_frame = results[0].plot()  # 주석이 추가된 프레임

    # 출력 영상에 프레임 쓰기
    out.write(annotated_frame)

# 리소스 해제
cap.release()
out.release()
cv2.destroyAllWindows()

print(f"추론 결과가 {output_path}에 저장되었습니다.")
