<div align="center">

[中文](./README_ZH.md) | English

🔥 This repo collects the latest research papers in the field of **VSLAM** from [arXiv](https://arxiv.org/) and uses [ChatGPT](https://chat.openai.com) to summarize them

🛠️ Support privatized deployment, welcome to view [deployment document](./DEPLOY.md#deploy)

🤗 Anyone who is interested is welcome to contribute to this repo! 

---

[SLAM](#SLAM) | [NeRF](#NeRF)

> ### `Update(BJT)：2023-08-28 13:09:59`

<details><summary>

## **SLAM**

</summary>

| Publish Date | Title | Summary |
|:-:|:-:|:-:|
|2023-06-07|[Towards Decentralized Heterogeneous Multi-Robot SLAM and Target Tracking](http://arxiv.org/pdf/2306.04570.pdf)|This paper proposes a decentralized heterogeneous multi-robot SLAM and target tracking system that enables collaboration between robots with different capabilities and estimation algorithms. The system leverages factor graphs to efficiently share information and fuse overlapping probability density functions. The approach focuses on multi-robot SLAM and tracking, allowing robots to use different local landmark, dense, or metric-semantic SLAM algorithms.|
|2023-05-05|[Multi S-graphs: A Collaborative Semantic SLAM architecture](http://arxiv.org/pdf/2305.03441.pdf)|Multi S-graphs is a collaborative semantic SLAM architecture that uses high-level semantic information to improve loop closure procedures and overall precision of SLAM algorithms. It minimizes information exchange between robots and demonstrates promising results in map generation tasks. Code: Not provided|
|2023-03-10|[Mobile Robot Control and Autonomy Through Collaborative Simulation Twin](http://arxiv.org/pdf/2303.06172.pdf)|This paper introduces a collaborative Simulation Twin (ST) strategy for control and autonomy on resource-constrained mobile robots. ST divides the robot system into a cyber and physical space to implement autonomous navigation through an SLAM-based path planning algorithm. The physical robot tracks the simulated twin’s velocity and communicates feedback generated through interaction with its environment. The proposed approach shows practicality and provides performance improvements compared to typical remote computing and digital twin approaches. Code: Not provided|

</details>
<details><summary>

## **NeRF**

</summary>

| Publish Date | Title | Summary |
|:-:|:-:|:-:|
|2023-05-03|[Combining HoloLens with Instant-NeRFs: Advanced Real-Time 3D Mobile Mapping](http://arxiv.org/pdf/2304.14301.pdf)|This work combines a Microsoft HoloLens 2 with Instant-NeRFs to achieve real-time 3D reconstruction from RGB camera images. The HoloLens acts as a multisensor platform for SLAM-based camera-pose determination, while a high-performance PC is responsible for training and 3D reconstruction. With a specialized inference algorithm, five million scene points can be extracted within 1 second, outperforming grid point sampling with NeRFs by multiple orders of magnitude. The proposed method represents a significant advancement in mobile mapping setup. Code: https://github.com/ivalab/Instant-NeRFs|
|2023-04-18|[SurfelNeRF: Neural Surfel Radiance Fields for Online Photorealistic Reconstruction of Indoor Scenes](http://arxiv.org/pdf/2304.08971.pdf)|SurfelNeRF is a neural surfel radiance field method that combines explicit geometric representation with NeRF rendering to achieve efficient online reconstruction and high-quality rendering of large-scale indoor scenes. SurfelNeRF employs a flexible and scalable neural surfel representation to store geometric attributes and extracted appearance features, and uses a differentiable rasterization scheme for efficient rendering. Experimental results show that SurfelNeRF achieves state-of-the-art performance on ScanNet. Code: https://github.com/sxyu/SurfelNeRF|

</details>
</div>