from sklearn import svm
#encoding=utf-8
from gensim.models import Word2Vec
import numpy as np
from sklearn import preprocessing
import math
from sklearn.externals import joblib

def get_class_statistic(train_data,trainLable):
    # 计算每一类样本的先验概率P，均值miu，协方差矩阵cov

    (data_num, dimension) = train_data.shape
    if data_num != len(trainLable):
        print('dimension not match')
        return
    count = []
    miu = []
    P = []
    cov = []
    data = []
    for i in range(0,2):
        count.append(0)
        data.append(np.zeros(train_data.shape))

    for i in range(0, data_num):
        data[trainLable[i]][count[trainLable[i]],:] = train_data[i,:]
        count[trainLable[i]] += 1  # 每一类的计数

    for i in range(0,2):
        data[i] = data[i][0: count[i], :]
        P.append(count[i] / float(data_num))  # 先验概率
        miu.append(np.mean(data[i], axis=0))
        cov.append(np.cov(data[i], rowvar=0))

    return P, miu, cov

def dataProcess():
    #训练数据预处理
    comfile = open('D:\python\homework\WebDataMining\FenciResult1.txt', 'r', encoding='utf-8')
    comments = comfile.readlines()
    model = Word2Vec.load('result.model')
    RowNum = 0
    TrainLabel = []
    train_data = np.zeros((len(comments), 100))
    # train_data = np.zeros((10001, 100))
    for sentence in comments:
        i = 0
        words = sentence.strip('\n').split(' ')
        data = np.zeros((len(words), 100))
        label  =  int(words[0])
        if (label == 0) or (label == 1):
            TrainLabel.append(label)
        else:
            print('第', RowNum, '行有问题')
        del words[0]  # 第一个元素是标签
        # print(len(words))
        for word in words:
            # print(word)
            try:
                data[i, :] = model[word]
                i += 1
                # print(model.most_similar(word))
            except BaseException:
                print(RowNum)
        # print(model[u"维系"])
        if (i) != len(words):
            for j in range(len(words) - i):
                data = np.delete(data, i, axis=0)
        mean = np.mean(data, axis=0)
        train_data[RowNum, :] = mean
        RowNum += 1


    # 测试数据预处理
    Testcomfile = open('D:\python\homework\WebDataMining\FenciResult2.txt', 'r', encoding='utf-8')
    TestComments = Testcomfile.readlines()
    TestRowNum = 0
    TestLabel = []
    test_data = np.zeros((len(TestComments), 100))
    # train_data = np.zeros((10001, 100))
    for sentence in TestComments:
        i = 0
        words = sentence.strip('\n').split(' ')
        data = np.zeros((len(words), 100))
        label = int(words[0])
        if (label == 0) or (label == 1):
            TestLabel.append(label)
        else:
            print('第', TestRowNum, '行有问题')
        del words[0]  # 第一个元素是标签
        # print(len(words))
        for word in words:
            # print(word)
            try:
                data[i, :] = model[word]
                i += 1
                # print(model.most_similar(word))
            except BaseException:
                print(TestRowNum)
        # print(model[u"维系"])
        if (i) != len(words):
            for j in range(len(words) - i):
                data = np.delete(data, i, axis=0)
        mean = np.mean(data, axis=0)
        test_data[TestRowNum, :] = mean
        TestRowNum += 1

    return train_data,TrainLabel,test_data, TestLabel




def qdf(test_data, test_labels, P, miu, cov):
    inv_cov = []
    reg = 0.01 * np.eye(cov[0].shape[0], dtype=float)
    for i in range(0, 2):
        inv_cov.append(np.linalg.inv(cov[i] + reg))

    Wi = []
    wi = []
    wi_0 = []
    for i in range(0, 2):
        a = -0.5 * inv_cov[i]
        b = inv_cov[i].dot(miu[i])
        c = -0.5 * (miu[i].dot(inv_cov[i].dot(miu[i].T))) - 0.5 * np.linalg.det(cov[i]) + math.log(P[i])
        Wi.append(a)
        wi.append(b)
        wi_0.append(c)

    test_num = test_data.shape[0]
    correct_num = 0
    for i in range(0, test_num):
        G = []
        for j in range(0, 2):
            g = test_data[i].dot(Wi[j].dot(test_data[i].T)) + test_data[i].dot(wi[j]) + wi_0[j]
            G.append(g)
        prediction = G.index(max(G))

        if prediction == test_labels[i]:
            correct_num += 1
        if prediction == 1:
            print(i)
    return correct_num/float(test_num)

if __name__ == '__main__':
    train_data,Label,test_data,testLabel = dataProcess()
    # clf = svm.SVC(max_iter=100000)  # class
    # clf.fit(train_data, Label)  # training the svc model
    clf = joblib.load("SVM_model.m")  #有训练模型以后，用这句话来调用训练模型
    # joblib.dump(clf, "SVM_model.m")  #存储训练模型
    print("begin predict")
    result = clf.predict(test_data)
    correctNum = 0
    nT = 0   #垃圾短信个数
    TP = 0
    FP = 0
    for i in range(len(testLabel)):
        if testLabel[i] == 1:
            nT += 1         #正例个数
        if result[i] == testLabel[i]:
            correctNum += 1
            if result[i] == 1:
                TP += 1   #真正例个数
        if result[i] == 1 and result[i] != testLabel[i]:
            FP += 1  #假正例个数

    FN = nT - TP
    P = TP / (TP + FP)  # 准确率
    R = TP / (TP + FN)  # 查全率
    F1 = 2 * P * R / (P + R)
    print(correctNum/float(len(testLabel)))  #accuracy
    print('P:',P)
    print('R:',R)
    print('正常短信误判为垃圾短信的个数：',FP)
    print('F1:',F1)


