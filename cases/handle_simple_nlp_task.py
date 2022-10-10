"""
需求：一个简单的自然语言处理任务
    1. 读取文件in.txt
    2.去掉所有标点符号和换行符，并把所有大写转小写
    3.合并相同的词，统计每个词出现的频率，并按照词频从大到小排序
    4.将结果按行输出到out.txt中
"""

import re 


def parse(text):
    # 使用正则去掉标点符号和换行符
    text = re.sub(r'[^\w]', ' ', text)
    text = text.lower()
    
    # 生成所有单词的列表
    word_list = text.split(' ')
    
    # 去掉空白单词
    word_list = filter(None, word_list)
    
    # 生成单词和词频的字典
    word_cnt = {}
    for w in word_list:
        if w not in word_cnt:
            word_cnt[w] = 0
        word_cnt[w] += 1
    
    # 按词频排序
    sorted_word_cnt = sorted(word_cnt.items(), key=lambda x: x[1], reverse=True)
    print(sorted_word_cnt)
    
    return sorted_word_cnt


with open('text/in.txt', 'r') as f:
    text = f.read()
    
word_and_freq = parse(text)

with open('text/out.txt', 'w') as f:
    for word, freq in word_and_freq:
        print(word, freq)
        f.write(f'{word} {freq}\n')
    