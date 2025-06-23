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

I am Hao Wu, currently a first-year PhD student in the School of Science at [Tsinghua University](https://www.tsinghua.edu.cn/) (2025 - 2028 (expected)), advised by Prof. [Xiaomeng Huang](https://scholar.google.com/citations?hl=en&user=yH9OkqYAAAAJ&view_op=list_works&sortby=pubdate). Previously, I graduated from the Department of Computer Science at the [USTC](https://www.ustc.edu.cn/). During my Master's studies at USTC, I was also a joint training student in the large model training group of the Machine Learning Platform Department at [Tencent](https://www.tencent.com/en-us/). My research interests are as follows:


* **Scientific Machine Learning**: The ultimate goal of Scientific Machine Learning (SciML) is to accelerate scientific discovery and address complex scientific and engineering challenges by fusing domain knowledge with machine learning. It aims to develop more accurate, efficient, and interpretable predictive models, thereby deepening our understanding of the world and driving innovation.

* **Vision-Language Models for Robotics**: The ultimate goal of Vision-Language Models (VLMs) for Robotics is to enable robots to deeply understand and interact with the world by grounding language in visual perception for intelligent action. It aims to build more versatile, collaborative, and general-purpose robots capable of understanding nuanced human instructions and performing complex tasks in real-world environments.

I have had the privilege of working closely with several esteemed experts, including [Dr. Kun Wang](https://scholar.google.com/citations?user=UnyqjWQAAAAJ&hl=en), [Prof. Qingsong Wen](https://sites.google.com/site/qingsongwen8/), [Prof. Yuxuan Liang](https://yuxuanliang.com/), [Dr. Xiao Luo](https://scholar.google.com.hk/citations?user=yJgX8agAAAAJ&hl=zh-CN), [Prof. Yu Zheng](https://scholar.google.com/citations?user=juUcdgYAAAAJ&hl=en), and [Dr. Xingjian Shi](https://sxjscience.github.io/).

<span style="color:red;">So, Please feel free to contact me for communication and collaboration.</span>

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
    <li><strong>2025.06.21</strong>: I will soon join Tencent CSIG as a research intern @ Tencent Jarvis Research Center. (In progress)</li>
    <li><strong>2025.06.18</strong>: I have graduated from USTC CS.</li>
    <li><strong>2025.05.01</strong>: 1 paper was accepted to ICML2025, Congrats to Yuan and Ruiqi! (Co-First Author).</li>
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
    <li style="list-style-type: none;">Machine Learning Platform Department, Large model training group, Tencent</li>
    <li style="list-style-type: none;"><em>2023.08 - 2025.07</em>, <strong>Research intern</strong></li>
    <li style="list-style-type: none;">mentored by <a href="http://buaahsh.github.io/">Jinbao Xue</a></li>
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

## Preprints
---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/nips_t1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Turb-L1: Achieving Long-term Turbulence Tracing By Tackling Spectral Bias](https://arxiv.org/abs/2505.19038)


Hao Wu, Yuan Gao, Ruiqi Shu, Zean Han, Fan Xu, Zhihong Zhu, Qingsong Wen, Xian Wu, Kun Wang*, Xiaomeng Huang*

*Arxiv, 2025*  


<a href="https://arxiv.org/abs/2505.19432" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/TurbL1_AI4Science" target="_blank">Code</a>


</div>
</div>


---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/triton_v1.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Advanced long-term earth system forecasting by learning the small-scale nature](https://arxiv.org/abs/2505.19432)


Hao Wu, Yuan Gao, Ruiqi Shu, Kun Wang, Ruijian Gou, Chuhan Wu, Xinliang Liu, Juncai He, Shuhao Cao, Junfeng Fang, Xingjian Shi, Feng Tao, Qi Song, Shengxuan Ji, Yanfei Xiang, Yuze Sun, Jiahao Li, Fan Xu, Huanshuo Dong, Haixin Wang, Fan Zhang, Penghao Zhao, Xian Wu, Qingsong Wen, Deliang Chen, Xiaomeng Huang*

<a href="https://arxiv.org/abs/2505.19432" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/Triton_AI4Earth" target="_blank">Code</a>



</div>
</div>


## Selected Publications


---
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/one.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[OneForecast: A Universal Framework for Global and Regional Weather Forecasting](https://openreview.net/forum?id=A23C57icJt&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2025%2FConference%2FAuthors%23your-submissions))


Yuan Gao, Hao Wu, Ruiqi Shu, huanshuo dong, Fan Xu, Rui Ray Chen, Yibo Yan, Qingsong Wen, Xuming Hu, Kun Wang, Jiahao Wu, Li Qing, Hui Xiong, Xiaomeng Huang#



<span style="color:red;">*(ICML2025, CCF Rank A)*</span>  

<a href="https://arxiv.org/abs/2502.00338" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/OneForecast" target="_blank">Code</a>


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/DnyST.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting](https://arxiv.org/abs/2403.02914)


**Hao Wu**, Haomin Wen, Guibin Zhang, Yutong Xia, Yuxuan Liang, Yu Zheng, Qingsong Wen, Kun Wang

<span style="color:red;">*(KDD2025, CCF Rank A)*</span>  

<a href="https://arxiv.org/abs/2505.19432" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>


</div>
</div>

---
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/NMO_main.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Neural Manifold Operators for Learning the Evolution of Physical Dynamics](https://dl.acm.org/doi/abs/10.1145/3637528.3671779)


**Hao Wu**, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang, Wei Xiong

<span style="color:red;">*(KDD2025, CCF Rank A)*</span>  

<a href="https://dl.acm.org/doi/10.1145/3637528.3671779" target="_blank">Paper</a> | <a href="https://github.com/AI4EarthLab/Neural-Manifold-Operators" target="_blank">Code</a>

</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/Prometheus.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE](https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5Bthe%20profile%20of%20Hao%20Wu%5D(%2Fprofile%3Fid%3D~Hao_Wu39))


**Hao Wu**,  Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo

<span style="color:red;">*(ICML2024, CCF Rank A)*</span>  
 
<a href="https://proceedings.mlr.press/v235/wu24aa.html" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/DGODE_ood" target="_blank">Code</a> | <a href="https://huggingface.co/datasets/easylearning/Prometheus/tree/main" target="_blank">Benchmark</a>


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/pastnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PastNet: Introducing Physical Inductive Biases for Spatio-temporal Video Prediction](https://openreview.net/forum?id=mL0KvSwXzk&referrer=%5Bthe%20profile%20of%20Xian-Sheng%20Hua%5D(%2Fprofile%3Fid%3D~Xian-Sheng_Hua1))


**Hao Wu**, Fan Xu, Chong Chen, Xian-Sheng Hua, Xiao Luo, Haixin Wang

<span style="color:red;">*(ACM MM, CCF Rank A)*</span>  

<a href="https://dl.acm.org/doi/10.1145/3664647.3681489" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/PastNet" target="_blank">Code</a>




</div>
</div>

---
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/Earthfarseer.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Earthfarsser: Versatile Spatio-Temporal Dynamical Systems Modeling in One Model](https://ojs.aaai.org/index.php/AAAI/article/view/29521)


**Hao Wu**, Yuxuan Liang, Wei Xiong, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang



<span style="color:red;">*(AAAI2024, CCF Rank A)*</span>  

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/EarthFarseer" target="_blank">Code</a>


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/pure.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling](https://easylearningscores.github.io/)


**Hao Wu**, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo 


<span style="color:red;">*(NeurIPS2024, CCF Rank A)*</span>  

<a href="https://neurips.cc/virtual/2024/poster/92971" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/nuwa.png' alt="sym" width="100%"></div></div>
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
  NeurIPS2023 Conference Reviewers,  NeurIPS2024 Conference Reviewers,  NeurIPS 2024 Datasets and Benchmarks Track Reviewers, ICLR 2024 Conference Reviewers, ICML 2024 Conference Reviewers, ACMMM 2024 Conference Reviewers,  ICLR2025 Conference Reviewers, NeurIPS 2024 Datasets and Benchmarks Track Reviewers, AISTATS 2025 Conference Reviewers, AAAI 2025 Conference Program Committee


# 👨🏻 Miscellaneous

- 🏀 I am a big fan of basketball, i love Kobe Bryant and i like Fadeaway Shot. I also like Curry.
- 👑 I am very interested in history.

<div style="width: 200px; height: 200px;">
    <script type="text/javascript" id="clstr_globe" src="//clustrmaps.com/globe.js?d=hivJ3nYFAlIUly-VIveCQXOLkcQRWlgrfu6llYfxHoU"></script>
</div>

