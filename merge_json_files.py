import json
import glob
import os

# 获取所有 JSON 文件的路径，并按文件名排序
json_files = sorted(glob.glob(os.path.expanduser('~/Desktop/data/*.json')))

# 合并所有 JSON 文件
all_data = []

for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        if isinstance(data, list):
            all_data.extend(data)
        elif isinstance(data, dict):
            all_data.append(data)

# 写入到 data.json 文件
output_file = os.path.expanduser('~/Desktop/data/data.json')
with open(output_file, 'w', encoding='utf-8') as file:
    json.dump(all_data, file, ensure_ascii=False, indent=4)

print(f"Data has been extracted and saved to '{output_file}'.")