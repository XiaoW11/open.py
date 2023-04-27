import json
from collections import deque
file_path = "../dataset.json"  # 请替换为您的JSON文件路径


num_labels_to_read = 5000

with open(file_path, "r") as json_file:
    json_data = json.load(json_file)

labels = json_data["labels"]

# 截取前1000个标签
first_1000_labels = labels[:num_labels_to_read]

# 现在 first_1000_labels 包含了前1000个标签
print(first_1000_labels)