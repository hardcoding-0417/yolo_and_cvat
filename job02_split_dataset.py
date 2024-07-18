import os
import shutil
import random

# 경로 설정
data_path = '내가 사용할 데이터셋의 경로'
images = [f for f in os.listdir(data_path) if f.endswith('.jpg', '.png')] # jpeg도 쓰고 싶다면 jpeg도 추가해줍니다.

# 전체 이미지 목록을 섞음
random.shuffle(images)

# 분할 비율 설정
train_ratio = 0.8
val_ratio = 0.1
test_ratio = 0.1

# 각 세트의 데이터 개수 계산
total_images = len(images)
train_count = int(total_images * train_ratio)
val_count = int(total_images * val_ratio)
test_count = total_images - train_count - val_count

# 데이터셋 분할
train_imgs = images[:train_count]
val_imgs = images[train_count:train_count + val_count]
test_imgs = images[train_count + val_count:]

# 디렉토리 생성
os.makedirs('dataset/train/images', exist_ok=True)
os.makedirs('dataset/train/labels', exist_ok=True)
os.makedirs('dataset/val/images', exist_ok=True)
os.makedirs('dataset/val/labels', exist_ok=True)
os.makedirs('dataset/test/images', exist_ok=True)
os.makedirs('dataset/test/labels', exist_ok=True)

# 파일 이동 함수
def copy_files(img_list, split):
    for img in img_list:
        label = img.replace('.jpg', '.txt')
        shutil.copy(os.path.join(data_path, img), os.path.join(f'dataset/{split}/images', img))
        shutil.copy(os.path.join(data_path, label), os.path.join(f'dataset/{split}/labels', label))

# 파일 이동
copy_files(train_imgs, 'train')
copy_files(val_imgs, 'val')
copy_files(test_imgs, 'test')
