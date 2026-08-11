# Modern ML Math Roadmap

这个仓库用于组织一套面向工科背景读者的现代机器学习理论数学导读。它不是严格数学教材，而是一张路线图：帮助读者在读机器学习理论、模型结构或论文时，判断自己需要补哪一类数学语言。

## 怎么阅读

从 [docs/README.md](docs/README.md) 开始。`docs/` 是面向读者的文档根目录，里面按照代数、分析、几何和补充专题四条路线组织内容。

目录名使用英文，便于在 Git 仓库、静态站点或文档服务中稳定访问；页面标题和正文主要使用中文，方便阅读。

## 文档结构

- [docs/01-alegbra-for-machine-learning/](docs/01-alegbra-for-machine-learning/)：抽象代数、矩阵理论和矩阵分析。
- [docs/02-analysis-for-machine-learning/](docs/02-analysis-for-machine-learning/)：实变函数与测度论、最优化、泛函分析、凸分析、变分法、偏微分方程和动力系统。
- [docs/03-geometry-for-machine-learning/](docs/03-geometry-for-machine-learning/)：基础拓扑、微分几何、代数拓扑、微分拓扑、信息几何和最优传输。
- [docs/04-supplementary-for-machine-leanring/](docs/04-supplementary-for-machine-leanring/)：离散结构、对称性和特定理论方向里的专题工具。

## 写作约定

每篇文章尽量回答五个问题：

- 这个数学领域在看什么。
- 它历史上主要想解决什么问题。
- 它怎样连接到机器学习理论。
- 读者最低限度需要掌握哪些概念。
- 后续深入可以沿着哪些关键词或教材方向继续。

如果一篇文章不确定该放在哪条路线下，优先按它回答的机器学习问题归类，而不是只按数学课名归类。

## 发布方式

`docs/` 是主要文档入口。之后如果使用 GitHub Pages、静态文档站点或其他发布方式，应以 `docs/` 作为文档根目录。
