

import os
import re
import scipy
import numpy as np
from nltk.corpus import stopwords

gloveFile = "glove.6B.50d.txt"


def createList(path,doc):
    returnList=[]
    returnList1=[]
    for i in range(0, len(doc)):
        file1 = open(path+"/"+doc[i])
        text = file1.read()
        returnList1.append(text)
        text = text.replace("\n", " ")
        returnList.append(text)
    return returnList,returnList1




def preprocess(raw_text):

    # keep only words
    letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

    # convert to lower case and split
    words = letters_only_text.lower().split()

    # remove stopwords
    #stopword_set = set(stopwords.words("english"))
    #cleaned_words = list(set([w for w in words if w not in stopword_set]))
    cleaned_words = list(set(words))

    return cleaned_words

def cleanUp(type):
    result=[]
    for i in range(0, len(type)):
        result.append(preprocess(type[i]))
    return result


def loadGloveModel(gloveFile):
    print ("Loading Glove Model")
    with open(gloveFile, encoding="utf8" ) as f:
        content = f.readlines()
    model = {}
    for line in content:
        splitLine = line.split()
        word = splitLine[0]
        embedding = np.array([float(val) for val in splitLine[1:]])
        model[word] = embedding
    print ("Done.",len(model)," words loaded!")
    return model



def cosine_distance_wordembedding_method(s1, s2,model):

    vector_1 = np.mean([model[word] for word in s1 if word in model],axis=0)
    vector_2 = np.mean([model[word] for word in s2 if word in model],axis=0)
    cosine = scipy.spatial.distance.cosine(vector_1, vector_2)
    return (round((1-cosine)*100,2))



def output(question,doc,model):

    result=[]
    for j in range(0,len(doc)):
        result.append(cosine_distance_wordembedding_method(question, doc[j],model))

    return result



def main(uploadFile,input):
    print(uploadFile)
    doc = os.listdir(uploadFile)#browse function text as input
    doc,doc_op=createList(uploadFile,doc)
    docUnpacked = cleanUp(doc)
    model = loadGloveModel(gloveFile)

    question = input
    question = preprocess(question)

    op=output(question,docUnpacked,model)

    relevent_doc=sorted(range(len(op)), key=lambda k: op[k])
    relevent_doc.reverse()

    final_result=[]
    for i in range(0,5):
        final_result.append(doc_op[relevent_doc[i]])

    return final_result








