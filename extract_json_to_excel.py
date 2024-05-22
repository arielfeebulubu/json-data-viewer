import json
import pandas as pd
import glob
import os

# 获取所有 JSON 文件的路径，并按文件名排序
json_files = sorted(glob.glob(os.path.expanduser('~/Desktop/data/*.json')))

# 创建一个空的 DataFrame
df = pd.DataFrame()

# 逐个读取 JSON 文件并提取所有字段
for json_file in json_files:
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
        # 如果是列表，处理其中的每个元素
        if isinstance(data, list):
            temp_df = pd.json_normalize(data)
            df = pd.concat([df, temp_df], ignore_index=True)
        # 如果是字典，直接处理
        elif isinstance(data, dict):
            temp_df = pd.json_normalize([data])
            df = pd.concat([df, temp_df], ignore_index=True)

# 将 DataFrame 写入 Excel 文件
output_file = os.path.expanduser('~/Desktop/data/extracted_data.xlsx')
df.to_excel(output_file, index=False)

print(f"Data has been extracted and saved to '{output_file}'.")