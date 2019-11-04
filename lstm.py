import os
from keras.preprocessing.text import Tokenizer
from keras.models import load_model
from keras.preprocessing.sequence import pad_sequences
import numpy as np

def remove_punct(docs):
    for x in range(0, len(docs)):
        docs[x] = docs[x].replace(',', '')
    return docs


def get_tokens(documents):
    documents = [string.lower() for string in documents]
    tokenizer = Tokenizer(filters='!".#$%&()*+,/:;<=>?@[\\]^_`{|}~\t\n')
    documents = remove_punct(documents)
    tokenizer.fit_on_texts(documents)
    return tokenizer


def load_SICK(filename):
    f = open(filename, 'r')  # open the file for reading
    sentence_1 = []
    sentence_2 = []
    similarity_score = []
    for row_num, line in enumerate(f):
        if (row_num > 1):
            values = line.strip().split('\t')
            sentence_1.append(values[1])
            sentence_2.append(values[2])
            similarity_score.append(values[3])
    f.close()  # close the file

    return (sentence_1, sentence_2, similarity_score)


def create_test_data(tokenizer, test_sentences_pair, max_sequence_length):
    test_sentences1 = [x[0].lower() for x in test_sentences_pair]
    test_sentences2 = [x[1].lower() for x in test_sentences_pair]

    test_sequences_1 = tokenizer.texts_to_sequences(test_sentences1)
    test_sequences_2 = tokenizer.texts_to_sequences(test_sentences2)
    leaks_test = [[len(set(x1)), len(set(x2)), len(set(x1).intersection(x2))]
                  for x1, x2 in zip(test_sequences_1, test_sequences_2)]

    leaks_test = np.array(leaks_test)
    test_data_1 = pad_sequences(test_sequences_1, maxlen=max_sequence_length)
    test_data_2 = pad_sequences(test_sequences_2, maxlen=max_sequence_length)

    return test_data_1, test_data_2, leaks_test


def createList(path,doc):
    returnList=[]
    returnList1 = []
    for i in range(0, len(doc)):
        file1 = open(path+"/"+doc[i])
        text = file1.read()
        returnList1.append(text)
        text = text.replace("\n", " ")
        returnList.append(text)
    return returnList,returnList1

def predict_relevancy(uploadFile,query):

    sentence1, sentence2, similarity_score = load_SICK('SICK_train.txt')
    tokenizer = get_tokens(sentence1 + sentence2)
    model = load_model(r'lstm_75_37_0.17_0.25.h5')
    test_sentence_pairs = []
    doc = os.listdir(uploadFile)  # browse function text as input
    doc,doc_op = createList(uploadFile,doc)
    for j in doc:
        test_sentence_pairs.append((query, j))

    test_data_x1, test_data_x2, leaks_test = create_test_data(tokenizer, test_sentence_pairs, 20)
    preds = list(model.predict([test_data_x1, test_data_x2, leaks_test], verbose=1).ravel())
    relevent_doc = sorted(range(len(preds)), key=lambda k: preds[k])
    relevent_doc .reverse()

    results = []
    for i in range(0,5):
        results.append(doc_op[relevent_doc[i]])

    return results
