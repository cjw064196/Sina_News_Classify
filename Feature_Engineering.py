import os
import jieba
import random

def TextProcessing(folder_path,test_size=0.2):
    folder_list = os.listdir(folder_path)  # 查看folder_path下的文件
    data_list = []  # 训练集
    class_list = []
    #print(folder_list)
    for folder in folder_list:
        new_folder_path=os.path.join(folder_path,folder)
        files=os.listdir(new_folder_path)

        j=1
        for file in files:
            if j>100:
                break
            with open(os.path.join(new_folder_path,file),'r',encoding='utf-8') as f:
                raw=f.read()
            word_cut=jieba.cut(raw,cut_all=False)
            word_list=list(word_cut)

            data_list.append(word_list)
            class_list.append(folder)
            j+=1

    data_class_list=list(zip(data_list,class_list)) #zip压缩合并，将数据与标签对应压缩
    random.shuffle(data_class_list)                 #将data_class_list乱序
    index=int(len(data_class_list)*test_size)+1     #训练集和测试集切分的索引值
    train_list=data_class_list[index:]              #训练集
    test_list=data_class_list[:index]               #测试集
    train_data_list,train_class_list=zip(*train_list)#训练集解压缩
    test_data_list,test_class_list=zip(*test_list)    #测试集解压缩

    all_words_dict={}                                #统计训练集词频
    for word_list in train_data_list:
        for word in word_list:
            if word in all_words_dict.keys():
                all_words_dict[word]+=1
            else:
                all_words_dict[word]=1
    # 根据键的值倒序排序
    all_words_tuple_list=sorted(all_words_dict.items(),key=lambda f:f[1],reverse=True)
    all_words_list,all_words_nums=zip(*all_words_tuple_list)#解压缩
    all_words_list=list(all_words_list)                  #转换成列表
    return all_words_list,train_data_list,test_data_list,train_class_list,test_class_list


if __name__=='__main__':
    folder_path='./SogouC/Sample'
    all_words_list, train_data_list, test_data_list, train_class_list, test_class_list=TextProcessing(folder_path,test_size=0.2)
    print(all_words_list)