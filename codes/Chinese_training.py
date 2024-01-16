from keras.layers import LSTM
from keras.layers import Dense, Activation
from keras.optimizers import RMSprop
from keras.models import Sequential
import numpy as np
import pickle
import Chinese_process


WORD_LENGTH = 5


def train_model(existing_words, existing_words_index, previous_word, next_word):
    X = np.zeros((len(previous_word), WORD_LENGTH, len(existing_words)), dtype=bool)

    Y = np.zeros((len(next_word), len(existing_words)), dtype=bool)

    for i, each_words in enumerate(previous_word):
        for j, each_word in enumerate(each_words):
            X[i, j, existing_words_index[each_word]] = 1

        Y[i, existing_words_index[next_word[i]]] = 1

    model = Sequential()
    model.add(LSTM(128, input_shape=(WORD_LENGTH, len(existing_words))))
    model.add(Dense(len(existing_words)))
    model.add(Activation('softmax'))
    optimizer = RMSprop(learning_rate=0.01)

    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    # history存储模型训练过程中的历史记录
    history = model.fit(X, Y, validation_split=0.05, batch_size=128, epochs=100, shuffle=True).history

    # 保存模型
    model.save('Chinese_LSTM_model.keras')

    # 保存历史数据
    pickle.dump(history, open("Chinese_LSTM_model_history.p", "wb"))


train_model(Chinese_process.existing_words, Chinese_process.existing_word_index, Chinese_process.previous_word, Chinese_process.next_word)
