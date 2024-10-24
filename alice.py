from pathlib import Path
import json

def count_words(path):
    """计算一个文件大致包含多少单词"""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")  # 用pass让python什么都不用做
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

path = Path('alice.txt')
count_words(path)

# 存储数据
numbers = [2, 3, 5, 7, 11, 13]
path = Path('numbers.json')
# contents = json.dumps(numbers)
# path.write_text(contents)
contents = path.read_text()
numbers = json.loads(contents)
print(numbers)