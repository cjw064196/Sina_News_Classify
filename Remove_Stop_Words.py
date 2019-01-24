from Text_Process import TextProcessing
from Feature_Engineering import *

def MakeWordSet(word_file):
    word_set=set()
    with open(word_file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            word=line.strip()
            if len(word)>0:
                word_set.add(word)
        return word_set

def words_dict(all_words_list,deleteN,stopwords_set=set()):
    feature_words=[]
    n=1
    for t in range(deleteN,len(all_words_list),1):
        if n>1000:            #feature_words的维度为1000
            break
        if not all_words_list[t].isdigit() and all_words_list[t] not in stopwords_set and 1<len(all_words_list[t])<5:
            feature_words.append(all_words_list[t])
        n+=1
    return feature_words

if __name__=='__main__':
    folder_path = './SogouC/Sample'
    all_words_list, train_data_list, test_data_list, train_class_list, test_class_list = TextProcessing(folder_path,
                                                                                                        test_size=0.2)
    stopwords_file='./stopwords_cn.txt'
    stopwords_set=MakeWordSet(stopwords_file)
    feature_words=words_dict(all_words_list,100,stopwords_set)
    print(feature_words)