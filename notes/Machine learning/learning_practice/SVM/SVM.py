"""
SVM of linear version
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm

data = np.array([
    [0.1, 0.7],
    [0.3, 0.6],
    [0.4, 0.1],
    [0.5, 0.4],
    [0.8, 0.04],
    [0.42, 0.6],
    [0.9, 0.4],
    [0.6, 0.5],
    [0.7, 0.2],
    [0.7, 0.67],
    [0.27, 0.8],
    [0.5, 0.72]
])# 建立数据集 二维数据集

# labeling considaring the first 6 points as class 1 and the last 6 points as class 0
label = [1] * 6 + [0] * 6
x_min, x_max = data[:, 0].min() - 0.2, data[:, 0].max() + 0.2
y_min, y_max = data[:, 1].min() - 0.2, data[:, 1].max() + 0.2
xx , yy  = np.meshgrid(np.arange(x_min, x_max, 0.002),
                       np.arange(y_min, y_max, 0.002)) # 网格化数据
svm_model = svm.SVC(kernel='linear', C=0.001)  # 创建SVM模型
svm_model.fit(data, label)  # 训练模型
#计算筛选直线

Z = svm_model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
# 绘制决策边界
plt.contourf(xx, yy, Z,cmap = plt.cm.ocean, alpha=0.6)
plt.scatter(data[:6, 0], data[:6, 1], marker='o',color = 'r',s=100, lw=3)
plt.scatter(data[6:, 0], data[6:, 1], marker='x',color = 'k',s=100, lw=3)
plt.title('SVM Linear Kernel')
plt.legend()
plt.show()
