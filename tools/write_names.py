import os
import random

# 数据集路径
dataset_path = "/home/user/dsj_files/datasets/eyes"

# 图像和标签文件夹路径
image_folder = os.path.join(dataset_path, "Original_Images")
label_folder = os.path.join(dataset_path, "Meibomian_Gland_Labels")

# 获取图像和标签文件列表
image_files = os.listdir(image_folder)
label_files = os.listdir(label_folder)

# 随机打乱文件列表
random.shuffle(image_files)
random.shuffle(label_files)

# 检查文件名是否存在
missing_files = []
for image_file, label_file in zip(image_files, label_files):
    image_path = os.path.join(image_folder, image_file)
    label_path = os.path.join(label_folder, label_file)
    if not os.path.isfile(image_path) or not os.path.isfile(label_path):
        missing_files.append((image_path, label_path))

# 打印缺失文件信息
if missing_files:
    print("以下文件不存在：")
    for image_path, label_path in missing_files:
        print(f"图像文件：{image_path}")
        print(f"标签文件：{label_path}")
    exit()

# 数据集长度
dataset_length = len(image_files)

# 切分比例
train_ratio = 0.7
val_ratio = 0.2
test_ratio = 0.1

# 切分索引
train_split = int(dataset_length * train_ratio)
val_split = int(dataset_length * (train_ratio + val_ratio))

# 切分数据集
train_files = image_files[:train_split]
val_files = image_files[train_split:val_split]
test_files = image_files[val_split:]

# 写入train.txt文件
with open(os.path.join(dataset_path, "train.txt"), "w") as f:
    for image_file in train_files:
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, image_file[:-3] + "png")
        f.write(f"{image_path}  {label_path}\n")

# 写入val.txt文件
with open(os.path.join(dataset_path, "val.txt"), "w") as f:
    for image_file in val_files:
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, image_file[:-3] + "png")
        f.write(f"{image_path}  {label_path}\n")

# 写入test.txt文件
with open(os.path.join(dataset_path, "test.txt"), "w") as f:
    for image_file in test_files:
        image_path = os.path.join(image_folder, image_file)
        label_path = os.path.join(label_folder, image_file[:-3] + "png")
        f.write(f"{image_path}  {label_path}\n")
