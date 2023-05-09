<div align="center">

[中文](./README_ZH.md) | English

🔥 This repo collects the latest research papers in the field of **Artificial Intelligence** from [arXiv]("https://arxiv.org/") and uses ChatGPT to summarize them, providing convenience for anyone who wants to study them



🛠️ The next step is to implement extensions for ![Chrome][Chrome-image] ![Edge][Edge-image], while continuously updating the topic of the paper.

🤗 Anyone who is interested is welcome to contribute to this repo! 

[Chrome-image]: https://img.shields.io/badge/-Chrome-brightgreen?logo=google-chrome&logoColor=white

[Edge-image]: https://img.shields.io/badge/-Edge-blue?logo=microsoft-edge&logoColor=white

---

[SLAM](#SLAM) | [NeRF](#NeRF)

> ### `Update(BJT)：2023-05-09 19:04:41`

## **SLAM**

| Publish Date | Title | Summary | Paper | Code |
|:-:|:-:|:-:|:-:|:-:|
|2023-05-07|Simulation of Dynamic Environments for SLAM|Simulation engines lack full control, ROS integration, realistic physics, or photorealism. GRADE is a framework for generating realistic animated dynamic environments. YOLO and Mask R-CNN models show the need for additional research in dynamic SLAM. Code and data are open-source.|[2305.04286](http://arxiv.org/pdf/2305.04286.pdf)|[Link](https://eliabntt.github.io/grade-rrSimulation)|
|2023-05-06|Robust optimization of control parameters for WEC arrays using stochastic methods|This work presents a computational optimization framework for robust control of Wave Energy Converters (WEC) in irregular waves. The power of WEC parks is maximized with respect to individual control coefficients. The results are robust to wave direction and a slamming constraint is enforced. Two stochastic optimization approaches are considered and results are presented for complex and realistic array configurations.|[2305.04130](http://arxiv.org/pdf/2305.04130.pdf)|
|2023-05-05|Multi S-graphs: A Collaborative Semantic SLAM architecture|Multi S-Graphs is a CSLAM algorithm that uses high-level semantic information in the form of Hierarchical Semantic Graphs to improve loop closure procedures and cooperative map generation among multiple robots, while minimizing information exchange. Experimental results show promising performance.|[2305.03441](http://arxiv.org/pdf/2305.03441.pdf)|
|2023-05-04|Edge-aware Consistent Stereo Video Depth Estimation|We propose a consistent method for dense video depth estimation using stereo videos and a left-right consistency loss to improve performance. Our edge-aware stereo video model can accurately estimate dense depth maps.|[2305.02645](http://arxiv.org/pdf/2305.02645.pdf)|
|2023-05-03|Direct LiDAR-Inertial Odometry and Mapping: Perceptive and Connective SLAM|This paper presents Direct LiDAR-Inertial Odometry and Mapping (DLIOM), a robust SLAM algorithm focusing on computational efficiency, operational reliability, and real-world efficacy. DLIOM contains key algorithmic innovations in both front-end and back-end subsystems to design a resilient LiDAR-inertial architecture that produces accurate localization and high-fidelity 3D mapping. The authors address common algorithmic failure points with proactive safe-guards to provide long-term operational reliability. They also detail innovations to localization accuracy and mapping resiliency to increase algorithmic speed, accuracy, and robustness. The paper includes insights gained from implementing such a complex system for real-time state estimation on resource-constrained systems, and experimental results show the increased performance of their method compared to state-of-the-art on both public benchmark and self-collected datasets.|[2305.01843](http://arxiv.org/pdf/2305.01843.pdf)|
|2023-05-02|EgoLocate: Real-time Motion Capture, Localization, and Mapping with Sparse Body-mounted Sensors|EgoLocate is a system that integrates inertial sensors and cameras for real-time human motion capture, localization, and mapping. It uses image-based SLAM for localization and inertial mocap for camera motion prior, improving localization accuracy compared to state of the art techniques. The code is available for research at https://xinyu-yi.github.io/EgoLocate/.|[2305.01599](http://arxiv.org/pdf/2305.01599.pdf)|[Link](https://xinyu-yi.github.io/EgoLocate/)|
|2023-04-30|LIMOT: A Tightly-Coupled System for LiDAR-Inertial Odometry and Multi-Object Tracking|This study proposes LIMOT, a tightly-coupled multi-object tracking and LiDAR-inertial SLAM system for autonomous driving. LIMOT uses 3D bounding boxes generated by an object detector and performs LiDAR odometry using IMU pre-integration. Object association is performed based on historical trajectories of tracked objects. A trajectory-based dynamic feature filtering method is used to filter out features belonging to moving objects. Factor graph-based optimization is then conducted to optimize IMU bias and pose estimation. Experiments show that LIMOT achieves better pose and tracking accuracy than baseline methods. Code is not provided.|[2305.00406](http://arxiv.org/pdf/2305.00406.pdf)|
|2023-04-29|Modality-invariant Visual Odometry for Embodied Vision|This study proposes a Transformer-based modality-invariant Visual Odometry (VO) approach that can deal with diverse or changing sensor suites of navigation agents. The model outperforms previous methods while training on only a fraction of the data. This method opens the door to a broader range of real-world applications that can benefit from flexible and learned VO models. Code is not provided.|[2305.00348](http://arxiv.org/pdf/2305.00348.pdf)|
|2023-04-27|Neural Implicit Dense Semantic SLAM|This paper presents an efficient online framework for solving the semantic Visual Simultaneous Localization and Mapping (V-SLAM) problem for indoor scenes using neural implicit scene representation. The proposed method disentangles tracking and 3D mapping pipeline for computing robust and accurate camera motion. Dense and multifaceted scene representation is provided using neural fields for SDF, semantics, RGB, and depth. The set of keyframes is shown to be sufficient for learning excellent scene representation, thereby improving the pipeline\'s train time. Multiple local mapping networks can be used to extend the pipeline for large-scale scenes. Extensive experiments show accurate tracking, mapping, and semantic labeling with noisy and sparse depth measurements. The pipeline can also easily extend to RGB image input. Code is not provided.|[2304.14560](http://arxiv.org/pdf/2304.14560.pdf)|
|2023-04-27|Co-SLAM: Joint Coordinate and Sparse Parametric Encodings for Neural Real-Time SLAM|This paper presents Co-SLAM, a neural RGB-D SLAM system based on a hybrid representation that performs real-time and robust camera tracking and high-fidelity surface reconstruction. Co-SLAM uses a multi-resolution hash-grid representation and one-blob encoding to exploit high convergence speed and ability to represent high-frequency local features, encouraging surface coherence and completion in unobserved areas. The joint parametric-coordinate encoding brings the best of both worlds: fast convergence and surface hole filling. Co-SLAM also performs global bundle adjustment over all keyframes, allowing for state-of-the-art scene reconstruction results and competitive tracking performance in various datasets and benchmarks. Project page: https://hengyiwang.github.io/projects/CoSLAM. Code is not provided.|[2304.14377](http://arxiv.org/pdf/2304.14377.pdf)|

<br>

## **NeRF**

| Publish Date | Title | Summary | Paper | Code |
|:-:|:-:|:-:|:-:|:-:|
|2023-05-08|AvatarReX: Real-time Expressive Full-body Avatars|AvatarReX is a method for learning NeRF-based full-body avatars from video data. The avatar supports real-time animation and rendering and is represented compositionally, with separate models for the body, hands, and face. Geometry and appearance are disentangled, enabling a two-pass training strategy and high-quality image synthesis. The method can automatically construct expressive avatars with real-time rendering capability and generate photo-realistic images for novel body motions and facial expressions.|[2305.04789](http://arxiv.org/pdf/2305.04789.pdf)|
|2023-05-07|HashCC: Lightweight Method to Improve the Quality of the Camera-less NeRF Scene Generation|Neural Radiance Fields is a popular method for scene generation via view synthesis, but requires camera pose information for each image in a dataset. Current approaches learn approximate camera positions alongside scene representations, but this requires complicated models and can result in low-quality images. This paper introduces Hash Color Correction (HashCC) - a lightweight method for improving image quality in situations where camera positions are unknown.|[2305.04296](http://arxiv.org/pdf/2305.04296.pdf)|
|2023-05-07|Multi-Space Neural Radiance Fields|This paper proposes a multi-space neural radiance field (MS-NeRF) to address the issue of blurry or distorted rendering caused by reflective objects in existing NeRF methods. The MS-NeRF represents the scene using a group of feature fields in parallel sub-spaces, which enhances the neural network's understanding of reflective and refractive objects. The approach is compatible with existing NeRF methods and requires only small computational overheads. Experiments on a dataset consisting of synthetic and real scenes with complex reflection and refraction show that MS-NeRF significantly outperforms existing single-space NeRF methods. Code and dataset are publicly available at https://zx-yin.github.io/msnerf.|[2305.04268](http://arxiv.org/pdf/2305.04268.pdf)|[Link](https://zx-yin.github.io/msnerf)|
|2023-05-04|NeRF-QA: Neural Radiance Fields Quality Assessment Database|This paper proposes the NeRF-QA database, which contains 48 videos of both real and synthetic 360-degree scenes synthesized using seven NeRF-based methods. The database includes subjective quality scores obtained from assessment tests to evaluate the suitability of existing objective quality metrics and develop new ones specific to this case.|[2305.03176](http://arxiv.org/pdf/2305.03176.pdf)|
|2023-05-04|NeuralEditor: Editing Neural Radiance Fields via Manipulating Point Clouds|This paper proposes NeuralEditor, which allows for shape editing of neural radiance fields (NeRFs) through explicit point cloud representation and a novel rendering scheme. NeuralEditor achieves state-of-the-art performance in shape deformation and scene morphing tasks, and supports zero-shot inference and fine-tuning. Code, benchmark, and demo video are available at https://immortalco.github.io/NeuralEditor.|[2305.03049](http://arxiv.org/pdf/2305.03049.pdf)|[Link](https://github.com/immortalco/NeuralEditor)|
|2023-05-04|Radiance Field Gradient Scaling for Unbiased Near-Camera Training|This work proposes a gradient scaling approach to counter the sampling bias in NeRF acquisition that causes background collapse and floating artifacts. Our method removes the need for near planes and is compatible with most NeRF implementations. It can be implemented in a few lines with no significant overhead.|[2305.02756](http://arxiv.org/pdf/2305.02756.pdf)|
|2023-05-04|Semantic-aware Generation of Multi-view Portrait Drawings|This paper proposes a Semantic-Aware GEnerator (SAGE) for synthesizing multi-view portrait drawings, overcoming the limitations of NeRF-based methods in generating such drawings. SAGE collaboratively synthesizes multi-view semantic maps and corresponding portrait drawings using facial semantic labels. A semantic-aware domain translator facilitates training, and data augmentation via synthesis mitigates collapsed results. SAGE achieves superior or highly competitive performance compared to existing 3D-aware image synthesis methods. Code is available at https://github.com/AiArt-HDU/SAGE.|[2305.02618](http://arxiv.org/pdf/2305.02618.pdf)|[Link](https://github.com/AiArt-HDU/SAGE)|
|2023-05-02|Neural LiDAR Fields for Novel View Synthesis|This paper presents Neural Fields for LiDAR (NFL), a method that optimizes a neural field scene representation from LiDAR measurements to synthesize realistic LiDAR scans from novel viewpoints. NFL combines the rendering power of neural fields with a physically motivated model of the LiDAR sensing process, accurately reproducing key sensor behaviors like beam divergence, secondary returns, and ray dropping. The method outperforms explicit reconstruct-then-simulate methods as well as other NeRF-style methods on LiDAR novel view synthesis tasks, as shown on both synthetic and real LiDAR scans. The improved realism of the synthesized views narrows the domain gap to real scans, resulting in better registration and semantic segmentation performance. Code is not provided.|[2305.01643](http://arxiv.org/pdf/2305.01643.pdf)|
|2023-05-02|LatentAvatar: Learning Latent Expression Code for Expressive Neural Head Avatar|This paper presents LatentAvatar, an expressive neural head avatar driven by latent expression codes learned in an end-to-end and self-supervised manner without templates. Existing approaches to animatable NeRF-based head avatars are heavily bound by the expression power and tracking accuracy of templates. LatentAvatar leverages a latent head NeRF to learn person-specific latent expression codes from monocular portrait videos and uses a Y-shaped network to learn shared latent expression codes of different subjects for cross-identity reenactment. By optimizing photometric reconstruction objectives in NeRF, the learned latent expression codes are 3D-aware and capture high-frequency detailed expressions, enabling LatentAvatar to perform expressive reenactment between different subjects. Experimental results show that LatentAvatar outperforms previous state-of-the-art solutions in both quantitative and qualitative comparisons, capturing challenging expressions and subtle movements of teeth and eyeballs. Project page: https://www.liuyebin.com/latentavatar. Code is not provided.|[2305.01190](http://arxiv.org/pdf/2305.01190.pdf)|
|2023-05-02|Federated Neural Radiance Fields|This paper presents a federated learning approach to training neural radiance fields (NeRFs) for scene representation. Previous approaches have relied on centralized learning, assuming that all training images are available on one compute node. In contrast, this paper considers federated learning, where multiple compute nodes each having acquired a distinct set of observations learn a common NeRF in parallel. This supports the scenario of cooperatively modeling a scene using multiple agents. The contribution is the first federated learning algorithm for NeRF that splits the training effort across multiple compute nodes and avoids the need to pool images at a central node. A technique based on low-rank decomposition of NeRF layers is introduced to reduce bandwidth consumption for aggregating model parameters. Transferring compressed models instead of raw data also enhances the privacy of the data collecting agents. Code is not provided.|[2305.01163](http://arxiv.org/pdf/2305.01163.pdf)|
|2023-05-01|GeneFace++: Generalized and Stable Real-Time Audio-Driven 3D Talking Face Generation|This paper addresses the challenge of generating talking person portraits with arbitrary speech audio, which is crucial for digital human and metaverse applications. The goal is to achieve generalized audio-lip synchronization, good video quality, and high system efficiency. Neural radiance field (NeRF) has become a popular rendering technique in this field due to its high-fidelity and 3D-consistent talking face generation capabilities with a few-minute-long training video. However, there are still several challenges for NeRF-based methods, including lip synchronization, video quality, and system efficiency. This paper proposes GeneFace++ to address these challenges by utilizing pitch contour as an auxiliary feature and introducing a temporal loss, proposing a landmark locally linear embedding method to regulate outliers in the predicted motion sequence, and designing a computationally efficient NeRF-based motion-to-video renderer for fast training and real-time inference. GeneFace++ is the first NeRF-based method that achieves stable and real-time talking face generation with generalized audio-lip synchronization. Extensive experiments show that GeneFace++ outperforms state-of-the-art baselines in both subjective and objective evaluation. Video samples are available at https://genefaceplusplus.github.io. Code is not provided.|[2305.00787](http://arxiv.org/pdf/2305.00787.pdf)|
|2023-04-30|Neural Radiance Fields (NeRFs): A Review and Some Recent Developments|Neural Radiance Field (NeRF) is a framework that represents a 3D scene using a fully connected neural network, known as the Multi-Layer Perception (MLP). It was introduced for the task of novel view synthesis and is capable of achieving state-of-the-art photorealistic image renderings from a given continuous viewpoint. NeRFs have become a popular field of research, as recent developments have expanded the performance and capabilities of the base framework. These developments include methods that require less images to train the model for view synthesis, as well as methods that are able to generate views from unconstrained and dynamic scene representations.|[2305.00375](http://arxiv.org/pdf/2305.00375.pdf)|

</div>