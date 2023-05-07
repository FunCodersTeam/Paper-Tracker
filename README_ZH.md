<div align="center">

中文 | [English](./README.md)

🔥 该 repo 会自动收集 [arXiv]("https://arxiv.org/") 上**人工智能**方向最新的论文，并使用 ChatGPT 对论文进行总结，供任何想对其进行研究的人使用

🔔 支持微信推送，[点击订阅](https://wxpusher.zjiecode.com/wxuser/?type=2&id=9888#/follow)

🛠️ 下一步将实现 ![Chrome][Chrome-image] ![Edge][Edge-image] 拓展，同时持续更新论文主题

🤗 欢迎任何感兴趣的人一起为 repo 做贡献！

[Chrome-image]: https://img.shields.io/badge/-Chrome-brightgreen?logo=google-chrome&logoColor=white

[Edge-image]: https://img.shields.io/badge/-Edge-blue?logo=microsoft-edge&logoColor=white

---

[SLAM](#SLAM) | [NeRF](#NeRF)

> ### `更新时间：2023-05-07 13:06:09`

## **SLAM**

| 发布时间 | 标题 | 总结 | 论文 | 代码 |
|:-:|:-:|:-:|:-:|:-:|
|2023-05-04|Edge-aware Consistent Stereo Video Depth Estimation|我们提出了一种一致的方法，使用立体视频和左右一致性损失来提高性能，进行密集视频深度估计。我们的边缘感知立体视频模型可以准确地估计密集深度图。|[2305.02645](http://arxiv.org/pdf/2305.02645.pdf)|
|2023-05-03|Direct LiDAR-Inertial Odometry and Mapping: Perceptive and Connective SLAM|本文提出了一种直接LiDAR-惯性里程计和建图（DLIOM）的鲁棒SLAM算法，专注于计算效率、操作可靠性和实际效果。DLIOM包含前端和后端子系统中的关键算法创新，设计出一种具有韧性的LiDAR-惯性体系结构，可感知环境并为自主机器人平台提供精确的定位和高保真的三维建图。作者通过采用积极的安全保护措施来解决常见的算法失效点，以提供长期的操作可靠性。他们还详细介绍了定位精度和建图弹性方面的创新，以全面提高算法速度、精度和鲁棒性。文章还包括了在资源受限系统上实现这种复杂系统进行实时状态估计所获得的见解，实验结果显示了他们的方法在公共基准和自采集数据集上与现有技术相比的性能提高。|[2305.01843](http://arxiv.org/pdf/2305.01843.pdf)|
|2023-05-02|EgoLocate: Real-time Motion Capture, Localization, and Mapping with Sparse Body-mounted Sensors|EgoLocate系统将惯性传感器和相机集成在一起，用于实时人体运动捕捉、定位和建图。它使用基于图像的SLAM进行定位，使用惯性mocap提供相机运动先验，相比于现有技术，提高了定位精度。我们的代码可在https://xinyu-yi.github.io/EgoLocate/上获取。|[2305.01599](http://arxiv.org/pdf/2305.01599.pdf)|[Link](https://xinyu-yi.github.io/EgoLocate/)|
|2023-04-30|LIMOT: A Tightly-Coupled System for LiDAR-Inertial Odometry and Multi-Object Tracking|该研究提出了一种紧密耦合的多目标跟踪和LiDAR惯性SLAM系统LIMOT，适用于自动驾驶。LIMOT使用由目标检测器生成的三维边界框，并使用IMU预积分进行LiDAR里程计计算。基于跟踪对象的历史轨迹，执行鲁棒的对象关联。采用基于轨迹的动态特征过滤方法来过滤属于移动对象的特征。然后进行因子图优化，以优化IMU偏差和姿态估计。实验表明，LIMOT比基准方法具有更好的姿态和跟踪精度。未提供代码。|[2305.00406](http://arxiv.org/pdf/2305.00406.pdf)|
|2023-04-29|Modality-invariant Visual Odometry for Embodied Vision|本研究提出了一种基于Transformer的模态不变Visual Odometry（VO）方法，可以处理导航代理的多样化或变化的传感器套件。该模型在只使用部分数据进行训练的情况下优于先前的方法。该方法为更广泛的实际应用开启了大门，可以从灵活和学习到的VO模型中受益。未提供代码。|[2305.00348](http://arxiv.org/pdf/2305.00348.pdf)|
|2023-04-27|Neural Implicit Dense Semantic SLAM|本文提出了一种使用神经隐式场景表示法解决语义视觉同时定位和地图构建（V-SLAM）问题的高效在线框架，适用于室内场景。所提出的方法将跟踪和3D映射流水线区分开来，用于计算稳健且准确的相机运动。使用神经场提供SDF、语义、RGB和深度的密集多面场景表示。通过实验表明，关键帧集合足以学习出优秀的场景表示，从而提高了流水线的训练时间，同时可以使用多个本地映射网络来扩展大规模场景的流水线。在多个基准数据集上进行了广泛实验，证明了该方法可以在噪声和稀疏深度测量的情况下进行准确的跟踪、地图构建和语义标注。该流水线也可以轻松扩展到RGB图像输入。未提供代码。|[2304.14560](http://arxiv.org/pdf/2304.14560.pdf)|
|2023-04-27|Co-SLAM: Joint Coordinate and Sparse Parametric Encodings for Neural Real-Time SLAM|本文提出了Co-SLAM，一种基于混合表示的神经RGB-D SLAM系统，可实现实时和稳健的相机跟踪和高保真度表面重建。Co-SLAM使用多分辨率哈希网格表示和“one-blob”编码，以利用高收敛速度和能够表示高频局部特征的能力，鼓励表面的连续性和完成性。联合参数坐标编码将快速收敛和表面孔填充的优点结合起来。Co-SLAM还在所有关键帧上执行全局束调整，从而实现了最先进的场景重建结果和各种数据集和基准测试中的竞争跟踪性能。项目页面：https://hengyiwang.github.io/projects/CoSLAM。未提供代码。|[2304.14377](http://arxiv.org/pdf/2304.14377.pdf)|

<br>

## **NeRF**

| 发布时间 | 标题 | 总结 | 论文 | 代码 |
|:-:|:-:|:-:|:-:|:-:|
|2023-05-04|NeuralEditor: Editing Neural Radiance Fields via Manipulating Point Clouds|本文提出了NeuralEditor，它通过显式点云表示和新颖的渲染方案，使神经辐射场（NeRFs）可进行形状编辑。NeuralEditor在形状变形和场景变形任务上实现了最先进的性能，并支持零样本推理和微调。代码、基准测试和演示视频可在https://immortalco.github.io/NeuralEditor获得。|[2305.03049](http://arxiv.org/pdf/2305.03049.pdf)|[Link](https://github.com/immortalco/NeuralEditor)|
|2023-05-04|Radiance Field Gradient Scaling for Unbiased Near-Camera Training|本文提出了一种梯度缩放方法，以抵消NeRF采集中的采样偏差，从而防止背景坍塌和浮动伪影。我们的方法不需要近平面，可以在大多数NeRF实现中使用，且仅需几行代码即可实现，没有任何显著的额外开销。|[2305.02756](http://arxiv.org/pdf/2305.02756.pdf)|
|2023-05-04|Semantic-aware Generation of Multi-view Portrait Drawings|本文提出了一种语义感知生成器（SAGE），用于合成多视角肖像画，克服了基于NeRF的方法在生成此类画作中的局限性。SAGE使用面部语义标签协同合成多视角语义地图和相应的肖像画。语义感知域转换器促进了训练，而通过合成进行的数据增强则减少了坍塌的结果。实验结果表明，与现有的3D感知图像合成方法相比，SAGE的性能明显优越或高度竞争。代码可在https://github.com/AiArt-HDU/SAGE获得。|[2305.02618](http://arxiv.org/pdf/2305.02618.pdf)|[Link](https://github.com/AiArt-HDU/SAGE)|
|2023-05-02|Neural LiDAR Fields for Novel View Synthesis|本文提出了用于LiDAR的神经场（NFL）方法，该方法从LiDAR测量中优化神经场场景表示，以从新视点合成逼真的LiDAR扫描。NFL将神经场的渲染能力与LiDAR感知过程的详细物理模型相结合，可以准确地再现关键传感器行为，如光束发散、二次回波和光线丢失。该方法在合成和真实LiDAR扫描上的表现均优于显式重建-模拟方法以及其他NeRF风格的LiDAR新视点合成方法。此外，我们证明合成视图的改进逼真度缩小了与真实扫描之间的领域差距，并转化为更好的配准和语义分割性能。未提供代码。|[2305.01643](http://arxiv.org/pdf/2305.01643.pdf)|
|2023-05-02|LatentAvatar: Learning Latent Expression Code for Expressive Neural Head Avatar|本文提出了一种表情自适应的神经头像生成方法LatentAvatar，其通过学习端到端和自监督的方式，使用潜在表情编码来驱动神经元渲染形式的头像生成。现有的基于NeRF的头像生成方法往往依赖于面部模板或使用表情系数作为驱动信号，其性能受到模板表情和跟踪精度的限制。LatentAvatar利用潜在头部NeRF从单目肖像视频中学习特定个体的潜在表情编码，并使用Y形网络学习不同主体的共享潜在表情编码，以实现跨身份重现。通过在NeRF中优化光度重建目标，学习的潜在表情编码具有3D感知能力，能够捕捉高频细节表情，使LatentAvatar能够在不同主体之间进行表情重现。实验结果表明，LatentAvatar在定量和定性比较中均优于先前的最先进解决方案，能够捕捉具有挑战性的表情和牙齿、眼球的微小运动。项目页面：https://www.liuyebin.com/latentavatar。未提供代码。|[2305.01190](http://arxiv.org/pdf/2305.01190.pdf)|
|2023-05-02|Federated Neural Radiance Fields|本文提出了一种基于联邦学习的方法，用于训练神经辐射场（NeRF）进行场景表示。先前的方法依赖于集中式学习，假定所有的训练图像都在一个计算节点上可用。相比之下，本文考虑了联邦学习，其中多个计算节点分别获取不同的观察数据，以并行方式学习共同的NeRF。这支持了使用多个代理协同建模场景的情况。本文的贡献是第一个针对NeRF的联邦学习算法，它将训练工作分布在多个计算节点上，并避免了在中心节点汇总图像的需要。引入了一种基于NeRF层的低秩分解技术，以减少聚合模型参数的带宽消耗。与其传输原始数据，传输压缩模型还可以提高数据收集代理的隐私性。未提供代码。|[2305.01163](http://arxiv.org/pdf/2305.01163.pdf)|
|2023-05-01|GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation|本文解决了使用任意语音音频生成说话人头像的挑战，这对数字人和元宇宙应用至关重要。目标是实现广义音频嘴唇同步、良好的视频质量和高系统效率。神经辐射场（NeRF）由于具有高保真度和3D一致的说话人脸生成能力而成为该领域的流行渲染技术，仅需几分钟的训练视频。然而，NeRF方法仍然存在一些挑战，包括嘴唇同步、视频质量和系统效率。本文提出了GeneFace++来解决这些挑战，通过将基频轮廓作为辅助特征并在面部运动预测过程中引入时间损失，提出了一个地标局部线性嵌入方法来调节预测运动序列中的异常值以避免鲁棒性问题，并设计了一个计算效率高的NeRF运动到视频渲染器以实现快速训练和实时推理。GeneFace++是第一个实现稳定和实时的NeRF方法，可以实现广义音频嘴唇同步的说话人脸生成。广泛的实验结果表明，GeneFace++在主观和客观评估方面优于最先进的基线方法。视频样本可在https://genefaceplusplus.github.io上获得。未提供代码。|[2305.00787](http://arxiv.org/pdf/2305.00787.pdf)|
|2023-04-30|Neural Radiance Fields (NeRFs): A Review and Some Recent Developments|神经辐射场（NeRF）是一种框架，它使用全连接神经网络（称为多层感知器，MLP）来表示3D场景。它被引入用于新视角合成任务，并能够从给定的连续视角实现最先进的逼真图像渲染。随着最近的发展，NeRF已成为研究的热门领域，这些发展扩展了基本框架的性能和功能。这些发展包括需要更少的图像来训练视角合成模型的方法，以及能够从无约束和动态场景表示生成视图的方法。|[2305.00375](http://arxiv.org/pdf/2305.00375.pdf)|

</div>