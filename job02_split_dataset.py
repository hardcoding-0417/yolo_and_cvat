import os
import random
import shutil

def split_dataset(dataset_dir, output_dir, train_ratio, val_ratio, test_ratio):
    assert train_ratio + val_ratio + test_ratio == 1.0

    images_dir = os.path.join(dataset_dir, 'images')
    labels_dir = os.path.join(dataset_dir, 'labels')

    subsets = ['train', 'val', 'test']
    for subset in subsets:
        os.makedirs(os.path.join(output_dir, 'images', subset), exist_ok=True)
        os.makedirs(os.path.join(output_dir, 'labels', subset), exist_ok=True)

    image_files = os.listdir(images_dir)
    random.shuffle(image_files)

    train_size = int(len(image_files) * train_ratio)
    val_size = int(len(image_files) * val_ratio)

    train_images = image_files[:train_size]
    val_images = image_files[train_size:train_size+val_size]
    test_images = image_files[train_size+val_size:]

    for subset, subset_images in [('train', train_images), ('val', val_images), ('test', test_images)]:
        for image_file in subset_images:
            image_path = os.path.join(images_dir, image_file)
            label_file = os.path.splitext(image_file)[0] + '.txt'
            label_path = os.path.join(labels_dir, label_file)

            shutil.copy(image_path, os.path.join(output_dir, 'images', subset))
            shutil.copy(label_path, os.path.join(output_dir, 'labels', subset))

    print(f"{output_dir} 폴더가 생성됐습니다.")

if __name__ == "__main__":
    dataset_dir = '데이터셋 경로'
    output_dir = 'train, val, test로 나누어진 데이터셋 폴더들이 출력될 경로'
    train_ratio = 0.8
    val_ratio = 0.1
    test_ratio = 0.1

    split_dataset(dataset_dir, output_dir, train_ratio, val_ratio, test_ratio)
