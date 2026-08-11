# 学习现代机器学习理论，需要补哪些数学课？

这套文档面向已经学过工科基础数学的读者：默认你熟悉微积分、线性代数、概率论与数理统计，并能理解传统机器学习入门内容。这里要补的不是“从零学数学”，而是给现代机器学习理论准备更合适的数学坐标系。

现代机器学习理论经常会问更抽象的问题：模型为什么能泛化？训练过程为什么稳定？神经网络在函数空间里到底学到了什么？数据是否藏在某种几何结构上？模型怎样尊重图、集合、旋转、平移或置换这类结构？这些问题会自然把我们带到代数、分析、几何和一些专题工具。

## 目录

### 一、代数视角：结构、矩阵与变换

[代数与机器学习](01-alegbra-for-machine-learning/) 组织抽象代数、矩阵理论和矩阵分析相关内容。

- [抽象代数](01-alegbra-for-machine-learning/01-abstract-algebra/)：理解集合上的运算、群、环、域、同态、商结构、作用和不变量，为对称性和结构化建模打基础。
- [矩阵理论](01-alegbra-for-machine-learning/02-matrix-theory/)：理解特征值、特征向量、正定性、分解、投影和低秩结构，支撑 PCA、谱方法和高维表示。
- [矩阵分析](01-alegbra-for-machine-learning/03-matrix-analysis/)：研究矩阵范数、扰动、条件数和矩阵不等式，帮助分析稳定性、鲁棒性和泛化控制。

### 二、分析视角：极限、函数空间与优化

[分析与机器学习](02-analysis-for-machine-learning/) 组织实变函数、测度论、最优化、泛函分析、凸分析、变分法、偏微分方程和动力系统相关内容。

- [最优化理论](02-analysis-for-machine-learning/02-optimization-theory/)：理解梯度下降、约束优化、KKT 条件、正则化和训练动态。
- [实变函数与测度论](02-analysis-for-machine-learning/01-real-analysis-and-measure-theory/)：为概率分布、积分、几乎处处、收敛和泛化分析提供严格语言。
- [泛函分析](02-analysis-for-machine-learning/03-functional-analysis/)：把线性代数的空间观念推广到函数空间，连接核方法、函数逼近、正则化和算子学习。
- [凸分析](02-analysis-for-machine-learning/04-convex-analysis/)：研究凸集、凸函数、对偶性和次梯度，帮助理解哪些学习问题更容易被稳定求解。
- [变分法](02-analysis-for-machine-learning/05-calculus-of-variations/)：把优化对象从有限维参数推广到函数本身，连接泛函导数、最优控制和连续模型。
- [偏微分方程和动力系统](02-analysis-for-machine-learning/06-pde-and-dynamical-systems/)：描述连续时间或连续空间中的演化过程，连接神经 ODE、扩散模型、连续优化和 mean-field 分析。

### 三、几何视角：形状、空间与分布

[几何与机器学习](03-geometry-for-machine-learning/) 组织拓扑、微分几何、代数拓扑、微分拓扑、信息几何和最优传输相关内容。

- [微分几何](03-geometry-for-machine-learning/01-differential-geometry/)：研究流形、切空间、度量和曲率，帮助理解流形假设、表示学习和自然梯度。
- [基础拓扑](03-geometry-for-machine-learning/02-basic-topology/)：理解开集、连续、紧致、连通等概念，为“空间结构是否被保留”提供语言。
- [代数拓扑和微分拓扑](03-geometry-for-machine-learning/03-algebraic-and-differential-topology/)：用连通性、洞、临界点和流形结构理解损失景观和高维空间形状。
- [信息几何和最优传输](03-geometry-for-machine-learning/04-information-geometry-and-optimal-transport/)：把概率分布看成有几何结构的对象，连接 Fisher 信息、KL 散度、自然梯度和 Wasserstein 距离。

### 四、补充路线：问题驱动的专题工具

[补充路线](04-supplementary-for-machine-leanring/) 收集不一定属于主干、但在特定研究方向中经常出现的工具。

- [离散结构问题](04-supplementary-for-machine-leanring/01-discrete-structures/)：理解图、组合结构、匹配、割、路径和复杂度，连接图神经网络、知识图谱和结构化数据。
- [对称性问题](04-supplementary-for-machine-leanring/02-symmetry/)：理解不变性、等变性和群作用，连接等变网络、几何深度学习和物理机器学习。
- [特定理论方向里的专题工具](04-supplementary-for-machine-leanring/03-specialized-theoretical-tools/)：收集随机过程、信息论、统计物理等在特定理论方向中会用到的工具。

## 怎么使用这张地图

不要试图一次性学完所有分支。更好的方式是先判断你正在读的问题属于哪一种视角：它是在研究矩阵和线性结构，还是函数空间和极限？是在研究几何形状和分布距离，还是离散结构与对称性？方向感建立以后，再回到定义、定理和证明，学习会轻很多。

每个主题页后续会尽量保持同一种写法：先解释这个领域在看什么，再说明它历史上主要想解决什么问题，最后用机器学习里的具体例子把它接上。目标不是替代教材，而是让第一次进入这些数学分支的读者知道自己为什么要学它、将来会在哪里用到它。
