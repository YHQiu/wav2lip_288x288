import pyarrow.parquet as pq
import pandas as pd
import os

if __name__ == "__main__":

    handle_data = "0008"

    # 读取 Parquet 文件
    default_path = 'todo_train_data'
    table = pq.read_table(os.path.join(default_path, f"{handle_data}.parquet"))

    # 将表格数据转换为 Pandas DataFrame
    df = table.to_pandas()

    # 创建用于保存数据的文件夹
    output_folder = f'todo_train_data/{handle_data}'
    os.makedirs(output_folder, exist_ok=True)

    # 遍历 DataFrame 中的每一行
    for index, row in df.iterrows():
        # 获取文件名和 URL
        file_name = row['__key__']
        url = row['__url__']

        # 获取视频数据
        video_data = row['mp4']

        # 将视频数据写入文件
        with open(os.path.join(output_folder, f"{index}.mp4"), 'wb') as f:
            f.write(video_data)

    print("视频文件已保存到 output_data 文件夹中。")
