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

> ### `更新时间：2023-05-14 13:05:30`

## **SLAM**

| 发布时间 | 标题 | 总结 | 论文 | 代码 |
|:-:|:-:|:-:|:-:|:-:|
|2023-05-09|Understanding why SLAM algorithms fail in modern indoor environments|本文提出了一种评估策略和数据集，用于在复杂的室内环境中测试和比较同时定位和地图构建（SLAM）算法。基于轨迹误差、尺度漂移和地图精度等指标，分析了最先进的SLAM算法。结果表明，在具有动态物体、反射/透明表面的复杂环境中，SLAM算法经常失败。成功的回环检测对算法性能产生了重大影响，强调了需要进一步研究以提高算法在实际环境中的鲁棒性。|[2305.05313](http://arxiv.org/pdf/2305.05313.pdf)|
|2023-05-07|Simulation of Dynamic Environments for SLAM|仿真引擎缺乏完全的控制、ROS集成、逼真的物理效果或照片般的真实感。GRADE是一个生成逼真的动态环境的框架。YOLO和Mask R-CNN模型表明需要在动态SLAM方面进行额外的研究。代码和数据是开源的。|[2305.04286](http://arxiv.org/pdf/2305.04286.pdf)|[Link](https://eliabntt.github.io/grade-rrSimulation)|
|2023-05-06|Robust optimization of control parameters for WEC arrays using stochastic methods|本文提出了一个计算优化框架，用于在不规则波中对波浪能转换器（WEC）的公园进行鲁棒控制。WEC公园的功率是针对每个设备的控制阻尼和刚度系数进行最大化的。结果对入射波方向具有鲁棒性，并施加了一个撞击约束以确保结果在物理上是真实的。我们展示了随机优化问题是良好定义的。然后考虑了两种处理随机性的优化方法：随机逼近和样本平均逼近。然后讨论了针对可能具有工程意义的复杂和逼真的阵列配置的优化结果。广泛的数值实验结果表明所提出的计算框架的效率。|[2305.04130](http://arxiv.org/pdf/2305.04130.pdf)|
|2023-05-05|Multi S-graphs: A Collaborative Semantic SLAM architecture|Multi S-Graphs是一种CSLAM算法，它利用分层语义图的高级语义信息，改善多个机器人之间的循环闭合过程和协同地图生成，同时最小化机器人之间的信息交换。实验结果表明，该算法在地图生成任务中表现出了良好的性能。|[2305.03441](http://arxiv.org/pdf/2305.03441.pdf)|
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
|2023-05-10|Generative AI meets 3D: A Survey on Text-to-3D in AIGC Era|本文讨论了生成式人工智能的进展，特别是以文本为导向的内容生成和新兴的文本到三维领域。文章提供了关于文本到三维的全面调查，包括三维数据表示、基础技术、最近的研究和各种应用。|[2305.06131](http://arxiv.org/pdf/2305.06131.pdf)|
|2023-05-10|NeRF$^\textbf{2}$: Neural Radio-Frequency Radiance Fields|本文讨论使用神经射频辐射场NeRF$^\textbf{2}$来模拟复杂环境中射频信号的传播。NeRF$^\textbf{2}$可以生成一个合成数据集，通过turbo-learning来提高应用层人工神经网络（ANNs）的性能。本文还展示了NeRF$^\textbf{2}$在室内定位和5G MIMO领域的应用。|[2305.06118](http://arxiv.org/pdf/2305.06118.pdf)|
|2023-05-09|Instant-NeRF: Instant On-Device Neural Radiance Field Training via Algorithm-Accelerator Co-Designed Near-Memory Processing|本文讨论了一种近存储器处理（NMP）框架Instant-NeRF的开发，该框架专门用于实现即时的设备端神经辐射场（NeRFs）训练，以实现沉浸式AR/VR体验。文章强调了NeRFs的独特工作负载和NMP面临的挑战，但是实验结果表明Instant-NeRF在八个数据集上的有效性始终得到验证。|[2305.05766](http://arxiv.org/pdf/2305.05766.pdf)|
|2023-05-09|PET-NeuS: Positional Encoding Tri-Planes for Neural Surfaces|本文介绍PET-NeuS，这是一种使用由MLP参数化的有符号距离函数（SDF）进行神经表面重建的NeuS方法的扩展。PET-NeuS引入了三个新组件：三面体平面表示法以改进数据结构，新的位置编码以对抗噪声，以及使用自注意力卷积进行可学习卷积操作以生成具有不同频带的特征。实验结果表明，PET-NeuS在标准数据集上实现了高保真表面重建，在Nerf-synthetic上改进了57％，在DTU上改进了15.5％。代码可在提供的GitHub链接中找到。|[2305.05594](http://arxiv.org/pdf/2305.05594.pdf)|[Link](https://github.com/yiqun-wang/PET-NeuS)|
|2023-05-08|NerfAcc: Efficient Sampling Accelerates NeRFs|本文研究并比较多种采样方法，以优化和渲染神经辐射场（NeRF），并表明在透射率估计器的统一概念下，改进采样通常适用于各种NeRF变体。作者开发了NerfAcc，这是一个Python工具箱，提供了灵活的API，可将高级采样方法纳入NeRF相关方法中，最小限度地修改现有代码库即可将几种最近的NeRF方法的训练时间缩短1.5倍至20倍。此外，可以使用NerfAcc在本地PyTorch中实现高度定制的NeRF，例如Instant-NGP。|[2305.04966](http://arxiv.org/pdf/2305.04966.pdf)|
|2023-05-08|AvatarReX: Real-time Expressive Full-body Avatars|AvatarReX是一种从视频数据中学习基于NeRF的全身分身的方法。该分身支持实时动画和渲染，并以组合方式表示，分别对身体、手和脸进行建模，以适当利用参数化网格模板的结构先验，而不影响表示灵活性。此外，我们对每个部分的几何和外观进行了解耦，提出了一种专门的延迟渲染管道，可以以实时帧速率执行，合成高质量的自由视图图像。几何和外观的解耦还使我们能够设计一种两步训练策略，将体积渲染和表面渲染相结合进行网络训练。综上所述，我们的方法实现了具有实时渲染能力的表达丰富的全身分身的自动构建，并能够为新颖的身体动作和面部表情生成具有动态细节的照片般逼真的图像。|[2305.04789](http://arxiv.org/pdf/2305.04789.pdf)|
|2023-05-07|HashCC: Lightweight Method to Improve the Quality of the Camera-less NeRF Scene Generation|神经辐射场已成为通过视图合成生成场景的重要方法。原始算法学习有意义的场景表示的一个关键要求是每个图像的相机姿态信息。当前的方法尝试通过学习场景的神经表示来绕过这个假设，但效果一般。这需要复杂的相机模型，导致长时间和复杂的训练过程，或者在渲染场景时缺乏纹理和清晰细节。本文介绍了哈希颜色校正(HashCC)——一种轻量级的方法，用于提高神经辐射场渲染图像的质量，也适用于给定图像集的相机位置未知的情况。|[2305.04296](http://arxiv.org/pdf/2305.04296.pdf)|
|2023-05-07|Multi-Space Neural Radiance Fields|本文提出了一种多空间神经辐射场(MS-NeRF)方法，以解决现有的NeRF方法中由反射物体引起的模糊或扭曲渲染问题。MS-NeRF使用一组特征场在并行子空间中表示场景，增强了神经网络对反射和折射物体的理解。该方法与现有NeRF方法兼容，只需要很小的计算开销。在由25个合成场景和7个具有复杂反射和折射的实际拍摄场景组成的数据集上进行的实验表明，MS-NeRF明显优于现有的单空间NeRF方法，可以渲染出通过镜面物体的复杂光路径的高质量场景。代码和数据集可在https://zx-yin.github.io/msnerf上公开获取。|[2305.04268](http://arxiv.org/pdf/2305.04268.pdf)|[Link](https://zx-yin.github.io/msnerf)|
|2023-05-04|NeRF-QA: Neural Radiance Fields Quality Assessment Database|本文提出了NeRF-QA数据库，其中包含48个视频，这些视频使用七种基于NeRF的方法合成，包括真实的和合成的360度场景，并附有主观质量评分。该数据库将允许评估现有客观质量度量方法对于NeRF合成视图的适用性，以及开发特定于此案例的新的质量度量方法。|[2305.03176](http://arxiv.org/pdf/2305.03176.pdf)|
|2023-05-04|NeuralEditor: Editing Neural Radiance Fields via Manipulating Point Clouds|本文提出了NeuralEditor，它通过显式点云表示和新颖的渲染方案，使神经辐射场（NeRFs）可进行形状编辑。NeuralEditor在形状变形和场景变形任务上实现了最先进的性能，并支持零样本推理和微调。代码、基准测试和演示视频可在https://immortalco.github.io/NeuralEditor获得。|[2305.03049](http://arxiv.org/pdf/2305.03049.pdf)|[Link](https://github.com/immortalco/NeuralEditor)|
|2023-05-04|Radiance Field Gradient Scaling for Unbiased Near-Camera Training|本文提出了一种梯度缩放方法，以抵消NeRF采集中的采样偏差，从而防止背景坍塌和浮动伪影。我们的方法不需要近平面，可以在大多数NeRF实现中使用，且仅需几行代码即可实现，没有任何显著的额外开销。|[2305.02756](http://arxiv.org/pdf/2305.02756.pdf)|
|2023-05-04|Semantic-aware Generation of Multi-view Portrait Drawings|本文提出了一种语义感知生成器（SAGE），用于合成多视角肖像画，克服了基于NeRF的方法在生成此类画作中的局限性。SAGE使用面部语义标签协同合成多视角语义地图和相应的肖像画。语义感知域转换器促进了训练，而通过合成进行的数据增强则减少了坍塌的结果。实验结果表明，与现有的3D感知图像合成方法相比，SAGE的性能明显优越或高度竞争。代码可在https://github.com/AiArt-HDU/SAGE获得。|[2305.02618](http://arxiv.org/pdf/2305.02618.pdf)|[Link](https://github.com/AiArt-HDU/SAGE)|
|2023-05-02|Neural LiDAR Fields for Novel View Synthesis|本文提出了用于LiDAR的神经场（NFL）方法，该方法从LiDAR测量中优化神经场场景表示，以从新视点合成逼真的LiDAR扫描。NFL将神经场的渲染能力与LiDAR感知过程的详细物理模型相结合，可以准确地再现关键传感器行为，如光束发散、二次回波和光线丢失。该方法在合成和真实LiDAR扫描上的表现均优于显式重建-模拟方法以及其他NeRF风格的LiDAR新视点合成方法。此外，我们证明合成视图的改进逼真度缩小了与真实扫描之间的领域差距，并转化为更好的配准和语义分割性能。未提供代码。|[2305.01643](http://arxiv.org/pdf/2305.01643.pdf)|
|2023-05-02|LatentAvatar: Learning Latent Expression Code for Expressive Neural Head Avatar|本文提出了一种表情自适应的神经头像生成方法LatentAvatar，其通过学习端到端和自监督的方式，使用潜在表情编码来驱动神经元渲染形式的头像生成。现有的基于NeRF的头像生成方法往往依赖于面部模板或使用表情系数作为驱动信号，其性能受到模板表情和跟踪精度的限制。LatentAvatar利用潜在头部NeRF从单目肖像视频中学习特定个体的潜在表情编码，并使用Y形网络学习不同主体的共享潜在表情编码，以实现跨身份重现。通过在NeRF中优化光度重建目标，学习的潜在表情编码具有3D感知能力，能够捕捉高频细节表情，使LatentAvatar能够在不同主体之间进行表情重现。实验结果表明，LatentAvatar在定量和定性比较中均优于先前的最先进解决方案，能够捕捉具有挑战性的表情和牙齿、眼球的微小运动。项目页面：https://www.liuyebin.com/latentavatar。未提供代码。|[2305.01190](http://arxiv.org/pdf/2305.01190.pdf)|
|2023-05-02|Federated Neural Radiance Fields|本文提出了一种基于联邦学习的方法，用于训练神经辐射场（NeRF）进行场景表示。先前的方法依赖于集中式学习，假定所有的训练图像都在一个计算节点上可用。相比之下，本文考虑了联邦学习，其中多个计算节点分别获取不同的观察数据，以并行方式学习共同的NeRF。这支持了使用多个代理协同建模场景的情况。本文的贡献是第一个针对NeRF的联邦学习算法，它将训练工作分布在多个计算节点上，并避免了在中心节点汇总图像的需要。引入了一种基于NeRF层的低秩分解技术，以减少聚合模型参数的带宽消耗。与其传输原始数据，传输压缩模型还可以提高数据收集代理的隐私性。未提供代码。|[2305.01163](http://arxiv.org/pdf/2305.01163.pdf)|
|2023-05-01|GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation|本文解决了使用任意语音音频生成说话人头像的挑战，这对数字人和元宇宙应用至关重要。目标是实现广义音频嘴唇同步、良好的视频质量和高系统效率。神经辐射场（NeRF）由于具有高保真度和3D一致的说话人脸生成能力而成为该领域的流行渲染技术，仅需几分钟的训练视频。然而，NeRF方法仍然存在一些挑战，包括嘴唇同步、视频质量和系统效率。本文提出了GeneFace++来解决这些挑战，通过将基频轮廓作为辅助特征并在面部运动预测过程中引入时间损失，提出了一个地标局部线性嵌入方法来调节预测运动序列中的异常值以避免鲁棒性问题，并设计了一个计算效率高的NeRF运动到视频渲染器以实现快速训练和实时推理。GeneFace++是第一个实现稳定和实时的NeRF方法，可以实现广义音频嘴唇同步的说话人脸生成。广泛的实验结果表明，GeneFace++在主观和客观评估方面优于最先进的基线方法。视频样本可在https://genefaceplusplus.github.io上获得。未提供代码。|[2305.00787](http://arxiv.org/pdf/2305.00787.pdf)|
|2023-04-30|Neural Radiance Fields (NeRFs): A Review and Some Recent Developments|神经辐射场（NeRF）是一种框架，它使用全连接神经网络（称为多层感知器，MLP）来表示3D场景。它被引入用于新视角合成任务，并能够从给定的连续视角实现最先进的逼真图像渲染。随着最近的发展，NeRF已成为研究的热门领域，这些发展扩展了基本框架的性能和功能。这些发展包括需要更少的图像来训练视角合成模型的方法，以及能够从无约束和动态场景表示生成视图的方法。|[2305.00375](http://arxiv.org/pdf/2305.00375.pdf)|

</div>