# YOLO and CVAT Guide

이 레포는 학생들이 CVAT을 사용하여 데이터를 레이블링하고,  
YOLO를 사용해 실제로 모델을 만들어볼 수 있도록 지원하는  
실습 자료실입니다.


천천히 하나 씩 따라해보세요.

## 2. 데이터셋 준비

1. 특정 객체에 대한 이미지를 수집합니다.
2. CVAT으로 수집한 이미지들을 레이블링합니다.
3. 레이블링된 데이터를 COCO 어노테이션 포맷으로 export합니다.
4. `job01_convert_coco_to_yolo.py` 스크립트로 COCO주석을 YOLO형식의 주석으로 변환합니다.
5. `job02_split_dataset.py` 스크립트로 데이터셋을 분할합니다.
6. (`dataset.yaml`)을 작성합니다.

## 3. 훈련과 추론

1. `job03_train.py` 스크립트로 모델을 학습시킵니다.
2. `job04_predict_image.py` 스크립트로 이미지에 대한 추론을 진행합니다.
3. `job05_predict_video.py` 스크립트로 비디오도 추론해봅니다.

## 4. 참고 자료

- [CVAT 공식 문서](https://cvat.org/documentation)
- [Ultralytics 공식문서](https://docs.ultralytics.com/)

