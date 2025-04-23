import os
import chardet
import re

def remove_comments(content):
    # 去除C语言和C++语言中的注释
    content = re.sub(r'//.*', '', content)  # 去除单行注释
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)  # 去除多行注释
    return content

def copy_files_content(source_folder, target_txt):
    print(f"开始复制文件内容从 {source_folder} 到 {target_txt}")
    with open(target_txt, 'a', encoding='utf-8') as out_file:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                if file.endswith(('.c', '.h', '.cpp', '.hpp')):  # 支持C、C++文件
                    file_path = os.path.join(root, file)
                    # 检测文件编码
                    with open(file_path, 'rb') as in_file:
                        raw_data = in_file.read()
                        encoding = chardet.detect(raw_data)['encoding']
                    # 使用检测到的编码打开文件
                    with open(file_path, 'r', encoding=encoding, errors='ignore') as in_file:
                        content = in_file.read()
                        # 去除注释
                        content = remove_comments(content)
                        out_file.write(f"文件名: {file}\n")
                        out_file.write(content + "\n\n")
                    print(f"已复制文件 {file} 的内容到 {target_txt}")
    print("文件内容复制完成。")

# 使用示例，替换成你实际的文件夹路径和目标txt文件路径
source_folder = r'D:\STM32Project\\-RM-Robomaster-NWAFU-master\\Inc'
target_txt = r'D:\STM32Project\\-RM-Robomaster-NWAFU-master\\步兵.txt'
source_folder = os.path.normpath(source_folder)
target_txt = os.path.normpath(target_txt)
copy_files_content(source_folder, target_txt)
