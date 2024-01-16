import numpy as np
from keras.models import load_model
import heapq

text = open('Chinese_data.txt', 'r', encoding='utf-8').read().lower()
words = list(text)
existing_words = np.unique(words)  # 获取 words 列表中的存在（不重复）元素
existing_word_index = dict((c, i) for i, c in enumerate(existing_words))  # 为列表中每个元素配一个值

WORD_LENGTH = 5  # 获取预测的字符串长度
previous_word = []
next_word = []
for i in range(len(words) - WORD_LENGTH):
    previous_word.append(words[i:i + WORD_LENGTH])
    next_word.append(words[i + WORD_LENGTH])


# 加载模型
model = load_model('Chinese_LSTM_model.keras')


def process_input(text_):
    processed_text = np.zeros((1, WORD_LENGTH, len(existing_words)))  # 三维数组
    temp_text = list(text_)
    text_len = len(temp_text)
    subtract = WORD_LENGTH - text_len
    for t, word in enumerate(temp_text):  # enumerate 函数为每个单词赋予一个索引（从0开始）
        processed_text[0, t + subtract, existing_word_index[word]] = 1
    return processed_text


def get_words(previous_words, n_max):  # 从 previous_words 中获取出最大的 n_max 个结果
    previous_words = np.asarray(previous_words).astype('float64')  # 转换为 NumPy 数组
    previous_words = np.log(previous_words)  # 对数转换，改善取值小的预测的数值稳定性

    # heapq.nlargest函数找出 previous_words 数组中最大的 n_max 个元素
    return heapq.nlargest(n_max, range(len(previous_words)), previous_words.take)


def next_word(text_, n):
    if text_ == "":
        return "0"
    processed_text = process_input(text_)
    previous_words = model.predict(processed_text, verbose=0)[0]
    next_possible_word = get_words(previous_words, n)
    return [existing_words[idx] for idx in next_possible_word]
