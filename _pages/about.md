---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html

---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

<font color="red">I am about (in year 2026) to return to the Department of Computer Science to pursue a Ph.D. in computer science.</font>


My research journey begins between 2019 and 2022, with a commitment to exploring the deep understanding of natural language. I delve into the evolution from LSTMs to the self-attention mechanism, focusing on the unique challenges of Chinese semantic parsing. During this period, I design and implement [SLFNet](https://arxiv.org/abs/2403.19936), an innovative framework aimed at accurately translating natural language into logical forms. However, the advent of ChatGPT in 2022 completely reshapes the technological paradigm of the NLP field. This disruptive change prompts me to reflect deeply and courageously decide to explore a new and more challenging field.

In 2023, I pivot to video prediction and begin a two-year internship (2023-2025) with the [Tencent Hunyuan Large Model team](https://github.com/easylearningscores/Alexander-wu.github.io/blob/main/images/shixi.pdf). This valuable experience not only allows me to systematically master core models such as ConvLSTM and SimVP but, more importantly, it teaches me how to deeply understand and generate dynamic data from both temporal and spatial dimensions. I am honored to work alongside top researchers in the industry (such as [Xingjian Shi](https://scholar.google.com/citations?user=P4G6H7oAAAAJ&hl=en), [Yuxuan Liang](https://yuxuanliang.com/), [Fan Xu](https://scholar.google.com/citations?hl=en&user=qfMSkBgAAAAJ&view_op=list_works&sortby=pubdate), etc.), and our close collaboration leads to a "blowout period" of academic achievements: as a core author, I publish nearly 20 papers in top conferences such as ICML, ICLR, and NeurIPS. This gives me the freedom and confidence to pursue higher academic goals.

By the end of 2024, I transition the experience accumulated in the deep learning field toward a direction with more fundamental scientific value: using artificial intelligence to accelerate the solving of partial differential equations (PDEs). To overcome the bottleneck of computational efficiency, I propose the [NMO](https://dl.acm.org/doi/abs/10.1145/3637528.3671779) method, which skillfully utilizes manifold learning to optimize the performance of neural networks and explores distillation techniques to achieve faster inference. My ultimate goal is to apply this technology to solve real-world challenges.

Entering 2025, I focus my research on the application of large-scale PDE solving in Earth sciences, particularly in weather and climate modeling. After accumulating experience and through unremitting efforts, including pre-training and fine-tuning on hundreds of cards, I, in collaboration with [Yuan Gao](https://yuangao-yg.github.io/), successfully develop [TritonCast](https://arxiv.org/abs/2505.19432), an advanced AI model for long-term Earth system prediction.

Next, in 2026, I will return to the computer science department to continue my doctoral studies, with my research direction focusing on video generation, and the post-training and application of LLM/Agent/VLM.

**Email**: <u>wuhao2022@mail.ustc.edu.cn</u>  &nbsp; &nbsp;  **Wechat**: How_Alexander_Wu


<h1 id='news'>🔥 News</h1>
<style>
  .scrollable {
    max-height: 260px; /* 设置最大高度 */
    overflow-y: scroll; /* 设置垂直滚动条 */
  }
</style>

<div class="scrollable">
  <ul>
    <li><strong>2025.11.08</strong>: 2 papers were accepted to AAAI2026, Main Track, Congrats to All !</li>
    <li><strong>2025.09.18</strong>: 2 papers were accepted to NeurIPS2025, Congrats to All !</li>
    <li><strong>2025.08.01</strong>: I have joined Tencent CSIG as a research intern @ Tencent Jarvis Research Center. </li>
    <li><strong>2025.06.26</strong>: 1 paper was accepted to ICCV2025 (Corresponding Author).</li>
    <li><strong>2025.06.18</strong>: I have graduated from USTC CS, and received the Outstanding Graduation Thesis award, which was given to only 3 people in my graduating class.</li>
    <li><strong>2025.05.01</strong>: 1 paper was accepted to ICML2025, Congrats to Yuan ! (Co-First Author).</li>
    <li><strong>2025.01.22</strong>: 1 paper was accepted to ICLR2025 (Corresponding Author).</li>
    <li><strong>2024.11.16</strong>: 1 paper was accepted to KDD2025 ADS (First Author).</li>
    <li><strong>2024.09.26</strong>: 3 papers were accepted to NeurIPS2024 (First Author and Two co-author).</li>
    <li><strong>2024.07.16</strong>: 1 paper was accepted to ACM MM2024 (First Author).</li>
    <li><strong>2024.05.17</strong>: 1 papers was accepted to KDD2024 (First Author).</li>
    <li><strong>2024.05.01</strong>: 1 paper was accepted to ICML2024 (First Author).</li>
    <li><strong>2024.01.16</strong>: 1 paper was accepted to ICLR2024 (<span style="color:red">Spotlight</span>) (Co-First Author).</li>
    <li><strong>2024.02.21</strong>: 1 paper was accepted to TKDE2024 (Co-First Author).</li>
    <li><strong>2023.12.09</strong>: 1 paper was accepted to AAAI2024 (First Author).</li>
    <li><strong>2023.09.22</strong>: 1 paper was accepted to NeurIPS2023 (Co-First Author).</li>
    <li><strong>2022.10.09</strong>: National Scholarship, China, 2022 (top 0.1% nation-wide, From USTC).</li>
  </ul>
</div>


#  📖 Research Experience

<div style="display: flex; align-items: center;">
  <img src="../images/tencent.png" alt="" style="width: 90px; margin-right: 50px; margin-left: 20px;"/>
  <ul style="list-style-type: disc; padding-left: 20px;">
    <li style="list-style-type: none;">Jarvis Lab, Tencent</li>
    <li style="list-style-type: none;"><em>2025.08 - Present</em>, <strong>Research intern</strong></li>
    <li style="list-style-type: none;">Mentored by <a href="https://scholar.google.com/citations?user=lslB5jkAAAAJ&hl=zh-CN">Xian Wu</a></li>
  </ul>
</div>


<div style="display: flex; align-items: center;">
  <img src="../images/tencent.png" alt="" style="width: 90px; margin-right: 50px; margin-left: 20px;"/>
  <ul style="list-style-type: disc; padding-left: 20px;">
    <li style="list-style-type: none;">Machine Learning Platform Department, Large model training group, Tencent</li>
    <li style="list-style-type: none;"><em>2023.08 - 2025.07</em>, <strong>Research intern</strong></li>
    <li style="list-style-type: none;">Mentored by <a href="https://github.com/easylearningscores/Alexander-wu.github.io/blob/main/images/shixi.pdf">Jinbao Xue</a></li>
  </ul>
</div>



<div style="display: flex; align-items: center;">
  <img src="../images/hkust.png" alt="" style="width: 90px; margin-right: 50px; margin-left: 20px;"/>
  <ul style="list-style-type: disc; padding-left: 20px;">
    <li style="list-style-type: none;">CityMind Lab, Hong Kong University of Science and Technology (Guangzhou)</li>
    <li style="list-style-type: none;"><em>2023.05 - 2023.08</em>, <strong>Research intern</strong></li>
    <li style="list-style-type: none;">Advisor <a href="http://buaahsh.github.io/">Yuxuan Liang</a></li>
  </ul>
</div>

# 📝 Publications 
#### Scientific Machine Learning

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ICML2025``</span> [OneForecast: A Universal Framework for Global and Regional Weather Forecasting]([https://arxiv.org/abs/2502.00338](https://arxiv.org/abs/2502.00338)). Yuan Gao, Hao Wu, Ruiqi Shu, huanshuo dong, Fan Xu, Rui Ray Chen, Yibo Yan, Qingsong Wen, Xuming Hu, Kun Wang, Jiahao Wu, Li Qing, Hui Xiong, Xiaomeng Huang#. ICML, 2025.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``NeurIPS2024``</span> [PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling]([https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2024%2FConference%2FAuthors%23your-submissions](https://openreview.net/forum?id=z86knmjoUq&referrer=%5Bthe%20profile%20of%20Hao%20Wu%5D(%2Fprofile%3Fid%3D~Hao_Wu39)))). **Hao Wu**, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo#. NeurIPS, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ICML2024``</span> [Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE](https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2024%2FConference%2FAuthors%23your-submissions)). **Hao Wu**, Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo#. ICML, 2024.


- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``Arxiv``</span> [Spatio-temporal fluid dynamics modeling via physical-awareness and parameter diffusion guidance](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=HdXMhfcAAAAJ&citation_for_view=HdXMhfcAAAAJ:IWHjjKOFINEC). **Hao Wu**, Fan Xu, Yifan Duan, Ziwei Niu, Weiyan Wang, Gaofeng Lu, Kun Wang, Yuxuan Liang#, Yang Wang#. Arxiv, 2024.


#### Spatio-temporal Prediction
- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ICCV2025``</span> [Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting
](https://openreview.net/forum?id=sKEFrZ0wCj#discussion). Yuqi Li, Chuanguang Yang, Hansheng Zeng, Zeyu Dong, Zhulin An, Yongjun Xu, Yingli Tian, **Hao Wu#**. ICCV, 2025.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``KDD2025``</span> [DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting](https://openreview.net/forum?id=sKEFrZ0wCj#discussion). **Hao Wu**, Haomin Wen, Guibin Zhang, Yutong Xia, Yuxuan Liang, Yu Zheng, Qingsong Wen, Kun Wang#. KDD, 2025.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``AAAI2024``</span> [Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model](https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866). **Hao Wu**, Yuxuan Liang, Wei Xiong#, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang#. AAAI, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ICLR2024``</span> [NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling](https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866). **Kun Wang^**, **Hao Wu^**, Yifan Duan, Guibin Zhang, Kai Wang, Xiaojiang Peng, Yu Zheng, Yuxuan Liang#, Yang Wang#. ICLR, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``TKDE2024``</span> [Modeling spatio-temporal dynamical systems with neural discrete learning and levels-of-experts](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=HdXMhfcAAAAJ&citation_for_view=HdXMhfcAAAAJ:Wp0gIr-vW9MC). **Kun Wang^**, **Hao Wu^**, Guibin Zhang, Junfeng Fang, Yuxuan Liang, Yuankai Wu, Roger Zimmermann, Yang Wang#. TKDE, 2024.



- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ACM MM2024``</span> [PastNet: introducing physical inductive biases for spatio-temporal video prediction](https://arxiv.org/abs/2305.11421).**Hao Wu**, Wei Xiong, Fan Xu, Xiao Luo#, Chong Chen, Xian-Sheng Hua, Haixin Wang#. ACM MM, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``Arxiv``</span> [BeamVQ: Aligning Space-Time Forecasting Model via Self-training on Physics-aware Metrics](https://openreview.net/forum?id=iL6FrLIc8K&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DNeurIPS.cc%2F2024%2FConference%2FAuthors%23your-submissions)).**Hao Wu**, Xingjian Shi, Ziyue Huang, Penghao Zhao, Wei Xiong, Jinbao Xue, Yangyu Tao, Xiaomeng Huang, Weiyan Wang #. Arxiv.

#### Neural Operator Learning 

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``Arxiv``</span> [Turb-L1: Achieving Long-term Turbulence Tracing By Tackling Spectral Bias](https://arxiv.org/abs/2505.19038). Hao Wu, Yuan Gao, Ruiqi Shu, Zean Han, Fan Xu, Zhihong Zhu, Qingsong Wen, Xian Wu, Kun Wang*, Xiaomeng Huang*.

  
- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``KDD2024``</span> [Neural Manifold Operators for Learning the Evolution of Physical Dynamics](https://openreview.net/pdf?id=r7n0Q4P66V). **Hao Wu**, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang#, Wei Xiong#. KDD, 2024.


- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``AI4TS(Oral)``</span> [Neural Manifold Operator for Geophysical Fluid Dynamics Prediction](https://openreview.net/pdf?id=r7n0Q4P66V). Wei Xiong, Kun Wang, Yuxuan Liang, Hao Wu#, Xiaomeng Huang#.  AI for Time Series (AI4TS) Workshop @ AAAI, 2024.




### Information Retrieval


- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``NeurIPS2023``</span> [IDEA: An Invariant Perspective for Efficient Domain Adaptive Image Retrieval](https://openreview.net/forum?id=77i6itptQW&referrer=%5Bthe%20profile%20of%20Haixin%20Wang%5D(%2Fprofile%3Fid%3D~Haixin_Wang3)). **Haixin Wang^**, **Hao Wu^**, Jinan Sun, Shikun Zhang, Chong Chen, Xian-Sheng Hua, Xiao Luo#. NeurIPS, 2023.


## Selected Publications

---


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='../images/fig_main.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[NeuralOM: Neural Ocean Model for Subseasonal-to-Seasonal Simulation](https://arxiv.org/abs/2505.21020)

Yuan Gao<sup>†</sup>, **Hao Wu**<sup>†</sup> <sup>‡ </sup>, Fan Xu, Yanfei Xiang, Ruijian Gou,  Ruiqi Shu, Qingsong Wen, Xian Wu, Kun Wang<sup>*</sup>, Xiaomeng Huang<sup>*</sup>

<span style="color:red;">*(AAAI2026, CCF Rank A)*</span>  


<a href="https://arxiv.org/abs/2505.21020" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/NeuralOM" target="_blank">Code</a>
<img src="https://img.shields.io/github/stars/YuanGao-YG/NeuralOM?label=%F0%9F%8C%9F%20Star&color=blue"> <img src="https://img.shields.io/github/forks/YuanGao-YG/NeuralOM?label=%F0%9F%94%A7%20Fork&color=green">


</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='../images/iccv2025.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting](https://openreview.net/group?id=thecvf.com/ICCV/2025/Conference/Authors&referrer=%5BHomepage%5D(%2F))


Yuqi Li, Chuanguang Yang, Hansheng Zeng, Zeyu Dong, Zhulin An, Yongjun Xu, Yingli Tian, **Hao Wu#**


<span style="color:red;">*(ICCV2025, CCF Rank A)*</span>  

<a href="https://arxiv.org/abs/2502.00338" target="_blank">Paper</a> | <a href="https://github.com/itsnotacie/SDKD" target="_blank">Code</a>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='../images/one.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OneForecast: A Universal Framework for Global and Regional Weather Forecasting](https://openreview.net/forum?id=A23C57icJt&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2025%2FConference%2FAuthors%23your-submissions))


Yuan Gao, Hao Wu, Ruiqi Shu, huanshuo dong, Fan Xu, Rui Ray Chen, Yibo Yan, Qingsong Wen, Xuming Hu, Kun Wang, Jiahao Wu, Li Qing, Hui Xiong, Xiaomeng Huang#



<span style="color:red;">*(ICML2025, CCF Rank A)*</span>  

<a href="https://arxiv.org/abs/2502.00338" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/OneForecast" target="_blank">Code</a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='../images/openck.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Open-CK: A Large Multi-Physics Fields Coupling benchmarks in Combustion Kinetics](https://openreview.net/forum?id=A23C57icJt)


Zaige Fei, Fan Xu, Junyuan Mao, Yuxuan Liang, Qingsong Wen, Kun Wang, **Hao Wu#**, Yang Wang

<span style="color:red;">*(ICLR2025, THU Rank A)*</span>  

<a href="https://openreview.net/forum?id=A23C57icJt" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>


</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2025</div><img src='../images/DnyST.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting](https://arxiv.org/abs/2403.02914)


**Hao Wu**, Haomin Wen, Guibin Zhang, Yutong Xia, Yuxuan Liang, Yu Zheng, Qingsong Wen, Kun Wang

<span style="color:red;">*(KDD2025, CCF Rank A)*</span>  

<a href="https://arxiv.org/abs/2505.19432" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2024</div><img src='../images/NMO_main.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Neural Manifold Operators for Learning the Evolution of Physical Dynamics](https://dl.acm.org/doi/abs/10.1145/3637528.3671779)


**Hao Wu**, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang, Wei Xiong

<span style="color:red;">*(KDD2024, CCF Rank A)*</span>  

<a href="https://dl.acm.org/doi/10.1145/3637528.3671779" target="_blank">Paper</a> | <a href="https://github.com/AI4EarthLab/Neural-Manifold-Operators" target="_blank">Code</a>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2024</div><img src='../images/Prometheus.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE](https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5Bthe%20profile%20of%20Hao%20Wu%5D(%2Fprofile%3Fid%3D~Hao_Wu39))


**Hao Wu**,  Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo

<span style="color:red;">*(ICML2024, CCF Rank A)*</span>  
 
<a href="https://proceedings.mlr.press/v235/wu24aa.html" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/DGODE_ood" target="_blank">Code</a> | <a href="https://huggingface.co/datasets/easylearning/Prometheus/tree/main" target="_blank">Benchmark</a>


</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACMMM  2024</div><img src='../images/pastnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PastNet: Introducing Physical Inductive Biases for Spatio-temporal Video Prediction](https://openreview.net/forum?id=mL0KvSwXzk&referrer=%5Bthe%20profile%20of%20Xian-Sheng%20Hua%5D(%2Fprofile%3Fid%3D~Xian-Sheng_Hua1))


**Hao Wu**, Fan Xu, Chong Chen, Xian-Sheng Hua, Xiao Luo, Haixin Wang

<span style="color:red;">*(ACM MM, CCF Rank A)*</span>  

<a href="https://dl.acm.org/doi/10.1145/3664647.3681489" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/PastNet" target="_blank">Code</a>




</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='../images/Earthfarseer.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Earthfarsser: Versatile Spatio-Temporal Dynamical Systems Modeling in One Model](https://ojs.aaai.org/index.php/AAAI/article/view/29521)


**Hao Wu**, Yuxuan Liang, Wei Xiong, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang



<span style="color:red;">*(AAAI2024, CCF Rank A)*</span>  

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/EarthFarseer" target="_blank">Code</a>


</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='../images/pure.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling](https://easylearningscores.github.io/)


**Hao Wu**, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo 


<span style="color:red;">*(NeurIPS2024, CCF Rank A)*</span>  

<a href="https://neurips.cc/virtual/2024/poster/92971" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>


</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2024</div><img src='../images/nuwa.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling](https://easylearningscores.github.io/)

**Kun Wang**, **Hao Wu**, Yifan Duan, Guibin Zhang, Kai Wang, Xiaojiang Peng, Yu Zheng, Yuxuan Liang, Yang Wang


<span style="color:red;">*(ICLR2024, THU Rank A spotlight)*</span>  

<a href="https://openreview.net/forum?id=sLdVl0q68X" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/NuwaDynamics" target="_blank">Code</a>


</div>
</div>
---





# 🎖 Honors and Awards

- *2024.09* First-class Academic Scholarship of the University of Science and Technology of China.
- *2022.10* National Scholarship, China (top 0.1% nation-wide).
- *2022.09* First-class Academic Scholarship of the University of Science and Technology of China.


# 💬 Invited Talks

- *2024.03*, Application and Research of GNN in Meteorological Prediction. @ Sun Yat-sen University
- *2023.12*, Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model. @ AI TIME 
- *2023.06*, A Review of Spatio-Temporal Forecasting Models. @ Tsinghua University

# 💻 Academic service

- PC Member/Conference Reviewer:
  NeurIPS2023 Conference Reviewers,  NeurIPS2024 Conference Reviewers,  NeurIPS 2024 Datasets and Benchmarks Track Reviewers, ICLR 2024 Conference Reviewers, ICML 2024 Conference Reviewers, ACMMM 2024 Conference Reviewers,  ICLR2025 Conference Reviewers, NeurIPS 2024 Datasets and Benchmarks Track Reviewers, AISTATS 2025 Conference Reviewers, AAAI 2025 Conference Program Committee,  NeurIPS2025 Conference Reviewers, ACMMM 2025 Conference Reviewers, ICCV 2025 Conference Reviewers, ICML 2025 Conference Reviewers.


# 👨🏻 Miscellaneous

- 🏀 I am a big fan of basketball, i love Kobe Bryant and i like Fadeaway Shot. I also like Curry.
- 👑 I am very interested in history.

<div style="width: 200px; height: 200px;">
    <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=hivJ3nYFAlIUly-VIveCQXOLkcQRWlgrfu6llYfxHoU"></script>
</div>

