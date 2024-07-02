import json
import os

def convert_coco_to_yolo(json_file, images_dir, labels_dir, class_mapping):
    # 입력 파일 및 디렉토리 유효성 검사
    if not os.path.isfile(json_file):
        raise FileNotFoundError(f"JSON 파일을 찾을 수 없습니다: {json_file}")
    if not os.path.isdir(images_dir):
        raise NotADirectoryError(f"이미지 디렉토리를 찾을 수 없습니다: {images_dir}")
    
    # 출력 디렉토리 생성
    os.makedirs(labels_dir, exist_ok=True)

    with open(json_file, 'r') as f:
        data = json.load(f)

    # 주석을 이미지 ID 별로 그룹화
    annotations = {}
    for annotation in data['annotations']:
        image_id = annotation['image_id']
        if image_id not in annotations:
            annotations[image_id] = []
        annotations[image_id].append(annotation)

    for image in data['images']:
        image_id = image['id']
        image_name = image['file_name']
        txt_file = os.path.splitext(image_name)[0] + '.txt'
        txt_path = os.path.join(labels_dir, txt_file)

        if image_id in annotations:
            with open(txt_path, 'w') as f:
                for annotation in annotations[image_id]:
                    category_id = annotation['category_id']
                    class_index = class_mapping.get(category_id, -1)  # 매핑되지 않은 클래스 처리
                    if class_index == -1:
                        print(f"경고: 카테고리 ID {category_id}가 class_mapping에 없습니다. 무시합니다.")
                        continue
                    bbox = annotation['bbox']
                    x_center = (bbox[0] + bbox[2] / 2) / image['width']
                    y_center = (bbox[1] + bbox[3] / 2) / image['height']
                    width = bbox[2] / image['width']
                    height = bbox[3] / image['height']
                    f.write(f"{class_index} {x_center} {y_center} {width} {height}\n")

    print(f"{json_file}을 YOLO 형식으로 변환했습니다.")

if __name__ == "__main__":
    json_file = 'COCO형식의 주석 경로/annotations/instances_default.json'
    images_dir = '이미지 경로'
    labels_dir = 'txt 레이블이 출력될 경로'
    class_mapping = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}

    try:
        convert_coco_to_yolo(json_file, images_dir, labels_dir, class_mapping)
    except Exception as e:
        print(f"에러가 발생했습니다: {e}")
