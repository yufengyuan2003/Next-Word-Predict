import os
import hashlib
import pickle
from collections import OrderedDict

data_filename = 'English_data.txt'
model_filename = 'English_markov_model.pkl'
input_filename = 'English_input.txt'

next_word = {}
#扩充字典,key->next_probability_word:value
def expand_dictionary(dictionary,key,value):
    if key not in dictionary:
        dictionary[key]=[]
    dictionary[key].append(value)

#合并相同项并计算次数,返回dictionary类型,key:probability_word,value:num
def union(words):
    probability_dict={}
    for item in words:
        probability_dict[item]=probability_dict.get(item,0)+1
    #根据出现概率进行从大到小的排序
    sorted_items = sorted(probability_dict.items(), key=lambda x: x[1], reverse=True)
    sorted_dict = OrderedDict(sorted_items)
    return sorted_dict

#训练并建立字典
def train_Markov_Model(filename):
    for line in open(filename, 'r', encoding='utf-8'):
        tokens = line.lower().rstrip().split()
        tokens_length=len(tokens)
        for i in range(tokens_length):
            if i==0:
                continue
            elif i == 1:
                expand_dictionary(next_word, tokens[i-1], tokens[i])
            else:
                expand_dictionary(next_word,tokens[i-1],tokens[i])
                expand_dictionary(next_word,(tokens[i-2],tokens[i-1]),tokens[i])

#获得下一个可能字
def next_words(x):
    ans = next_word.get(x)
    if (ans is not None):
        return list(ans.keys())
    else:
        return ''

def calculate_file_hash(filename):
    # 使用 SHA-256 哈希算法计算文件内容的哈希值
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as file:
        # 逐块更新哈希值
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)
    return sha256.hexdigest()

def has_data_changed(data_filename, model_filename):
    # 计算训练数据文件的哈希值
    data_hash = calculate_file_hash(data_filename)

    # 检查模型文件的存在性
    if not os.path.exists(model_filename):
        return True  # 模型文件不存在，可能是第一次运行

    # 读取保存的哈希值
    if os.path.exists(model_filename + '.hash'):
        with open(model_filename + '.hash', 'r') as hash_file:
            saved_hash = hash_file.read()

        # 比较计算得到的哈希值和保存的哈希值
        return data_hash != saved_hash

    return True  # 没有保存的哈希值文件，认为数据已修改

def save_markov_model(filename):
    with open(filename, 'wb') as file:
        pickle.dump(next_word, file)

def load_markov_model(filename):
    with open(filename, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model

def save_data_hash(data_filename, model_filename):
    data_hash = calculate_file_hash(data_filename)
    with open(model_filename + '.hash', 'w') as hash_file:
        hash_file.write(data_hash)


if has_data_changed(data_filename, model_filename):
    print("英文训练数据已修改，需要重新训练模型。")
    train_Markov_Model(data_filename)
    save_markov_model(model_filename)
    save_data_hash(data_filename, model_filename)
else:
    print("英文训练数据没有修改，可以使用现有的模型。")

# 加载模型
next_word = load_markov_model(model_filename)
# 添加输入数据集
train_Markov_Model(input_filename)
save_markov_model(model_filename)
for key, value in next_word.items():
    next_word[key] = union(next_word.get(key))

def merge_and_clear(file1, file2):
    with open(file1, 'a', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        content2 = f2.read()
        f1.write(content2)
    # 清空file2
    with open(file2, 'w', encoding='utf-8') as f2:
        f2.write("")
    save_data_hash(data_filename, model_filename)
    print("英文训练数据合并完成。")


merge_and_clear(data_filename, input_filename)
