import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#生成随机数据
from sklearn.datasets import make_blobs
# make_blobs：为聚类产生数据集
# n_samples：样本点数，n_features：数据的维度，centers:产生数据的中心点的个数，默认值3
# cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0，random_state：随机种子
X, y = make_blobs(n_samples=300, n_features=2, centers=2, cluster_std=1.5, random_state=2)
# c: 生成的样本点，y: 生成的样本点对应的标签
# s：样本点的大小，cmap：颜色映射

# 朴素贝叶斯分类器
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(X, y)

rng = np.random.RandomState(0)
X_test = [-6, -14] + [14 , 18] * rng.rand(2000, 2)
y_pred = model.predict(X_test)
# 将训练集和测试集的预测结果可视化
plt.scatter(X[:, 0], X[:, 1], c=y, s=50, cmap='RdBu', label='Training Data')
lim = plt.axis()
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, s=20, cmap='RdBu', alpha=0.1, label='Test Data')
plt.axis(lim)
plt.show()