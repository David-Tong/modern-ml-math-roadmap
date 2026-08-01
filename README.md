# Modern ML Math Roadmap

这个仓库用于组织一套面向工科背景读者的现代机器学习理论数学导读。项目的目标不是写严格数学教材，而是帮助读者先建立方向感：读到一个机器学习理论问题时，知道它大概需要矩阵、优化、概率、函数空间、几何、拓扑、结构还是对称性的视角。

## 怎么阅读

从 [docs/README.md](docs/README.md) 开始。这个文件是整套文档的导论，说明为什么传统工科数学基础足够支持机器学习工程入门，但在阅读现代机器学习理论时还需要补充哪些现代数学分支。

导论之后，后续章节会放在 `docs/` 下的对应目录中。目录名使用英文，方便通过 Git 文档服务、静态站点或仓库页面稳定访问。

## 文档结构

- [docs/README.md](docs/README.md)：导论与完整路线图。
- [docs/02-matrix-numerical-computing-and-optimization/](docs/02-matrix-numerical-computing-and-optimization/)：矩阵、数值计算与优化。
- [docs/03-functional-view-of-machine-learning/](docs/03-functional-view-of-machine-learning/)：函数空间、泛函分析、凸分析与变分观点。
- [docs/04-geometric-view-of-machine-learning/](docs/04-geometric-view-of-machine-learning/)：几何、拓扑、信息几何与最优传输。
- [docs/05-supplementary-routes/](docs/05-supplementary-routes/)：离散结构、对称性和专题工具。

## 怎么贡献内容

新增文章时，请放到 `docs/` 下对应主题目录中。每篇文章建议保持同一种写法：

- 这个数学领域在看什么。
- 它历史上主要想解决什么问题。
- 它怎样连接到机器学习理论。
- 最低限度概念清单。
- 后续深入的关键词或教材方向。

如果某篇文章不确定属于哪个目录，优先根据它回答的机器学习问题来放置，而不是根据数学课名本身来放置。

## 发布方式

`docs/` 是面向读者的文档根目录。之后如果使用 GitHub Pages、Git 文档站点或其他静态文档服务，应以 `docs/` 作为主要文档入口。
