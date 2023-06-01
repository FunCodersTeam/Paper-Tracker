<div align="center">

中文 | [English](./README.md)

🔥 该 repo 会自动收集 [arXiv](https://arxiv.org/) 上 **VSLAM** 领域的最新研究论文，并使用 [ChatGPT](https://chat.openai.com) 对论文进行总结

🔔 支持微信推送，[点击订阅](https://wxpusher.zjiecode.com/wxuser/?type=2&id=9888#/follow)

🛠️ 支持私有化部署，欢迎查看[部署文档](./DEPLOY.md#部署)

🤗 欢迎任何感兴趣的人一起为 repo 做贡献！

---

[SLAM](#SLAM) | [NeRF](#NeRF)

> ### `更新时间：2023-06-01 19:08:28`

<details><summary>

## **SLAM**

</summary>

| 发布时间 | 标题 | 总结 |
|:-:|:-:|:-:|
|2023-05-05|[多S图：一种协作式语义SLAM架构](http://arxiv.org/pdf/2305.03441.pdf)|Multi S-graphs是一种协作式语义SLAM架构，利用高级语义信息提高了SLAM算法的闭环检测和整体精度，同时最小化了机器人之间的信息交换。实验结果证明了该算法在地图生成任务中的良好性能。代码：未提供|
|2023-03-10|[协作式仿真双胞胎控制和自治的移动机器人](http://arxiv.org/pdf/2303.06172.pdf)|本文介绍了一种协作式仿真双胞胎策略，用于控制和管理资源受限的移动机器人。双胞胎通过将机器人系统分为虚拟和物理空间来实现自主导航。物理机器人跟踪模拟双胞胎的速度并通过与环境互动生成反馈。所提出的方法显示了实用性，并提供了性能改进，与典型的远程计算和数字孪生方法相比。代码：未提供|

</details>
<details><summary>

## **NeRF**

</summary>

| 发布时间 | 标题 | 总结 |
|:-:|:-:|:-:|
|2023-05-03|[将HoloLens与Instant-NeRFs相结合：先进的实时三维移动映射](http://arxiv.org/pdf/2304.14301.pdf)|本文将Microsoft HoloLens 2与Instant-NeRFs相结合，实现了基于RGB相机图像的实时三维重建。HoloLens作为多传感器平台用于SLAM-based相机姿态确定，而高性能PC负责训练和三维重建。通过特定的推断算法，可以在1秒内提取500万个场景点，性能比使用NeRFs进行网格点采样的性能优越多个数量级。所提出的方法代表了移动映射设置中重要的进步。代码：https://github.com/ivalab/Instant-NeRFs|
|2023-04-18|[SurfelNeRF：在线逼真重建室内场景的神经Surfel辐射场](http://arxiv.org/pdf/2304.08971.pdf)|SurfelNeRF是一种神经Surfel辐射场方法，将显式几何表示与NeRF渲染相结合，以实现大规模室内场景的高效在线重建和高质量渲染。SurfelNeRF采用灵活可扩展的神经Surfel表示存储几何属性和提取的外观特征，并使用可微栅格化方案进行高效渲染。实验结果表明，SurfelNeRF在ScanNet上实现了最先进的性能。代码：https://github.com/sxyu/SurfelNeRF|

</details>
</div>