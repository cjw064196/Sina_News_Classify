from Remove_Stop_Words import *

"""
函数说明:根据feature_words将文本向量化

Parameters:
    train_data_list - 训练集
    test_data_list - 测试集
    feature_words - 特征集
Returns:
    train_feature_list - 训练集向量化列表
    test_feature_list - 测试集向量化列表
"""

def TextFeatures(train_data_list,test_data_list,feature_words):
    def text_features(text,feature_words):   #出现在特征集中，则置1
        text_words=set(text)
        features=[1 if word in text_words else 0 for word in feature_words]
        return features
    train_feature_list=[text_features(text,feature_words) for text in train_data_list]
    test_feature_list=[text_features(text,feature_words) for text in test_data_list]
    return train_feature_list,test_feature_list


"""
函数说明:新闻分类器

Parameters:
    train_feature_list - 训练集向量化的特征文本
    test_feature_list - 测试集向量化的特征文本
    train_class_list - 训练集分类标签
    test_class_list - 测试集分类标签
Returns:
    test_accuracy - 分类器精度
"""
def TextClassifier(train_feature_list,test_feature_list,train_class_list,test_class_list)
