# decision tree

**this part i need to learn 信息熵**
it means that the machine will make decisions step by step like a tree
it can be understood as a structure that combined with many if-else statements
`representation`
1.ID3 based on information entropy
2.C4.5 based on information gain ratio
3.CART based on Gini impurity

## information entropy

$$
H(X)=-\sum_{i=1}^{n}p(x_i)\log(x_i)
$$

## information gein ratio

条件熵
$$
H(Y | X)=\sum_{x \in X}p(x)H(Y|X=x)
$$

信息增益
$$
g(D,A) = H(D)-H(D|A)
$$

在信息增益的基础上除A特征的熵是因为信息增益偏向于选择取值较多的特征，容易过拟合。所以引进信息增益比
 $$ g_{R}(D, X)=\frac{g(D, X)}{H_{X}(D)} $$

基尼指数的定义如下： $$ \operatorname{Gini}(D)=\sum_{k=1}^{K} \sum_{k^{\prime} \neq k} p_{k} p_{k^{\prime}}=1-\sum_{k=1}^{K} p_{k}^{2} $$ 其中$p_{k}=\frac{\left|C_{k}\right|}{|D|}$是数据集中 𝑘类样本的比例，所以有： $$ \operatorname{Gini}(D)=1-\sum_{k=1}^{K}\left(\frac{\left|C_{k}\right|}{|D|}\right)^{2} $$ 基尼指数就是从数据集D中随机抽取两个样本，其类别不同的概率，基尼指数越小，说明数据集D中的相同类别样本越多，纯度越高。

将基尼指数按属性a（特征）来划分，则其基尼指数为： $$ \operatorname{Gini}(D, a)=\sum_{v=1}^{V} \frac{\left|D^{v}\right|}{|D|} \operatorname{Gini}\left(D^{v}\right) $$
