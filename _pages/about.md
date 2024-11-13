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


I am Hao Wu, currently a third-year master's student in the Department of Computer Science at the [University of Science and Technology of China (USTC)](https://www.ustc.edu.cn/). I am also a joint training student in the large model training group of the Machine Learning Platform Department at [Tencent](https://www.tencent.com/en-us/). My research interests are as follows:

* **Spatio-temporal Prediction**: With the guidance of [Kun Wang](https://scholar.google.com/citations?user=UnyqjWQAAAAJ&hl=en) and [Yuxuan Liang](https://yuxuanliang.com/), I explore foundational models for spatiotemporal data mining. Additionally, I am honored to collaborate with [Xingjian Shi](https://sxjscience.github.io/), whose ConvLSTM introduced me to this field.

* **AI/ML for Science**: Under the guidance of [Xiao Luo](https://luoxiao12.github.io/), I study machine learning and fluid dynamics. We are currently researching the integration of LLMs and dynamical systems.

* **Scaling Law**: I am collaborating with my teammates to research the intersectional theory and applications of Scaling Law in large scientific computing models.



<span style="color:red">I am seeking a CS Ph.D. position starting from 2025 Fall. Feel free to contact me if you think I am a good fit.</span>


# 🔥 News
- *2024.0926*: &nbsp;🎉🎉 3 papers were accepted to NeurIPS2024 (First Author).
- *2024.0716*: &nbsp;🎉🎉 1 paper was accepted to ACM MM2024 (First Author).
- *2024.0517*: &nbsp;🎉🎉 2 papers were accepted to KDD2024 (First Author).
- *2024.0501*: &nbsp;🎉🎉 1 paper was accepted to ICML2024 (First Author).
- *2024.0116*: &nbsp;🎉🎉 1 paper was accepted to ICLR2024  (<span style="color:red">Spotlight</span>) (Co-First Author).
- *2024.0221*: &nbsp;🎉🎉 1 paper was accepted to TKDE2024 (Co-First Author).
- *2023.1209*: &nbsp;🎉🎉 1 paper was accepted to AAAI2024 (First Author).
- *2023.0922*: &nbsp;🎉🎉 1 paper was accepted to NeurIPS2023 (Co-First Author).
- *2022.1009*: &nbsp;🎉🎉 National Scholarship, China, 2023 (top 0.1% nation-wide).

#  📖 Research Experience

<div style="display: flex; align-items: center;">
  <img src="../images/tencent.png" alt="" style="width: 90px; margin-right: 50px; margin-left: 20px;"/>
  <ul style="list-style-type: disc; padding-left: 20px;">
    <li style="list-style-type: none;">Machine Learning Platform Department, Large model training group, Tencent</li>
    <li style="list-style-type: none;"><em>2023.08 - present</em>, <strong>Research intern</strong></li>
    <li style="list-style-type: none;">mentored by <a href="http://buaahsh.github.io/">Jinbao Xue</a></li>
  </ul>
</div>



<div style="display: flex; align-items: center;">
  <img src="../images/hkust.png" alt="" style="width: 90px; margin-right: 50px; margin-left: 20px;"/>
  <ul style="list-style-type: disc; padding-left: 20px;">
    <li style="list-style-type: none;">CityMind Lab, Hong Kong University of Science and Technology (Guangzhou)</li>
    <li style="list-style-type: none;"><em>2023.06 - 2024.06</em>, <strong>Research intern</strong></li>
    <li style="list-style-type: none;">Advisor <a href="http://buaahsh.github.io/">Yuxuan Liang</a></li>
  </ul>
</div>

# 📝 Publications 

#### Spatio-temporal Prediction

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``AAAI2024``</span> [Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model](https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866). **Hao Wu**, Yuxuan Liang, Wei Xiong#, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang#. AAAI, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ICLR2024``</span> [NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling](https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866). **Kun Wang^**, **Hao Wu^**, Yifan Duan, Guibin Zhang, Kai Wang, Xiaojiang Peng, Yu Zheng, Yuxuan Liang#, Yang Wang#. ICLR, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``TKDE2024``</span> [Modeling spatio-temporal dynamical systems with neural discrete learning and levels-of-experts](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=HdXMhfcAAAAJ&citation_for_view=HdXMhfcAAAAJ:Wp0gIr-vW9MC). **Kun Wang^**, **Hao Wu^**, Guibin Zhang, Junfeng Fang, Yuxuan Liang, Yuankai Wu, Roger Zimmermann, Yang Wang#. TKDE, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``TPAMI2024``</span> [Earthfarseer-V2: A Versatile All-in-One Model for Learning Complex Spatio-Temporal Dynamics](https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866). **Hao Wu**, Junfeng Fang, Yuxuan Liang, Guibin Zhang, Fan Xu, Wei Xiong, Qingsong Wen, Yu Zheng, Kun Wang#. TPAMI, 2024 (under review).


- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ACM MM2024``</span> [PastNet: introducing physical inductive biases for spatio-temporal video prediction](https://arxiv.org/abs/2305.11421).**Hao Wu**, Wei Xiong, Fan Xu, Xiao Luo#, Chong Chen, Xian-Sheng Hua, Haixin Wang#. ACM MM, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``Arxiv``</span> [BeamVQ: Aligning Space-Time Forecasting Model via Self-training on Physics-aware Metrics](https://openreview.net/forum?id=iL6FrLIc8K&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DNeurIPS.cc%2F2024%2FConference%2FAuthors%23your-submissions)).**Hao Wu**, Xingjian Shi, Ziyue Huang, Penghao Zhao, Wei Xiong, Jinbao Xue, Yangyu Tao, Xiaomeng Huang, Weiyan Wang #. Arxiv.

#### Neural Operator Learning 

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``KDD2024``</span> [Neural Manifold Operators for Learning the Evolution of Physical Dynamics](https://openreview.net/pdf?id=r7n0Q4P66V). **Hao Wu**, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang#, Wei Xiong#. KDD, 2024.


- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``AI4TS(Oral)``</span> [Neural Manifold Operator for Geophysical Fluid Dynamics Prediction](https://openreview.net/pdf?id=r7n0Q4P66V). Wei Xiong, Kun Wang, Yuxuan Liang, Hao Wu#, Xiaomeng Huang#.  AI for Time Series (AI4TS) Workshop @ AAAI, 2024.


#### Scientific Machine Learning
- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``NeurIPS2024``</span> [PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling]([https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2024%2FConference%2FAuthors%23your-submissions](https://openreview.net/forum?id=z86knmjoUq&referrer=%5Bthe%20profile%20of%20Hao%20Wu%5D(%2Fprofile%3Fid%3D~Hao_Wu39)))). **Hao Wu**, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo#. NeurIPS, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``ICML2024``</span> [Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE](https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICML.cc%2F2024%2FConference%2FAuthors%23your-submissions)). **Hao Wu**, Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo#. ICML, 2024.


- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``Arxiv``</span> [AI-GOMS: Large AI-Driven Global Ocean Modeling System](https://arxiv.org/abs/2308.03152). Wei Xiong, Yanfei Xiang, **Hao Wu**, Shuyi Zhou, Yuze Sun, Muyuan Ma, Xiaomeng Huang#. Arxiv, 2024.

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``Arxiv``</span> [Spatio-temporal fluid dynamics modeling via physical-awareness and parameter diffusion guidance](https://scholar.google.com/citations?view_op=view_citation&hl=en&user=HdXMhfcAAAAJ&citation_for_view=HdXMhfcAAAAJ:IWHjjKOFINEC). **Hao Wu**, Fan Xu, Yifan Duan, Ziwei Niu, Weiyan Wang, Gaofeng Lu, Kun Wang, Yuxuan Liang#, Yang Wang#. Arxiv, 2024.


### Information Retrieval

- <span style="background-color: #003366; color: white; padding: 1px 4px; font-size: 12px;">``NeurIPS2023``</span> [IDEA: An Invariant Perspective for Efficient Domain Adaptive Image Retrieval](https://openreview.net/forum?id=77i6itptQW&referrer=%5Bthe%20profile%20of%20Haixin%20Wang%5D(%2Fprofile%3Fid%3D~Haixin_Wang3)). **Haixin Wang^**, **Hao Wu^**, Jinan Sun, Shikun Zhang, Chong Chen, Xian-Sheng Hua, Xiao Luo#. NeurIPS, 2023.

## Selected Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/NMO_main.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Neural Manifold Operators for Learning the Evolution of Physical Dynamics](https://dl.acm.org/doi/abs/10.1145/3637528.3671779)


**Hao Wu**, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang, Wei Xiong

*Knowledge Discovery and Data Mining (KDD), 2024*  

<span style="color:red;">*(CCF Rank A)*</span>  


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/Prometheus.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE](https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5Bthe%20profile%20of%20Hao%20Wu%5D(%2Fprofile%3Fid%3D~Hao_Wu39))


**Hao Wu**,  Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo

*The International Conference on Machine Learning (ICML), 2024*  

<span style="color:red;">*(CCF Rank A)*</span>  


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/pastnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PastNet: Introducing Physical Inductive Biases for Spatio-temporal Video Prediction](https://openreview.net/forum?id=mL0KvSwXzk&referrer=%5Bthe%20profile%20of%20Xian-Sheng%20Hua%5D(%2Fprofile%3Fid%3D~Xian-Sheng_Hua1))


**Hao Wu**, Fan Xu, Chong Chen, Xian-Sheng Hua, Xiao Luo, Haixin Wang

*ACM Multimedia (MM), 2024*  

<span style="color:red;">*(CCF Rank A)*</span>  


</div>
</div>

---
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/Earthfarseer.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Earthfarsser: Versatile Spatio-Temporal Dynamical Systems Modeling in One Model](https://ojs.aaai.org/index.php/AAAI/article/view/29521)


**Hao Wu**, Yuxuan Liang, Wei Xiong, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang


*Association for the Advancement of Artificial Intelligence (AAAI), 2024*  

<span style="color:red;">*(CCF Rank A)*</span>  


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/pure.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling](https://easylearningscores.github.io/)


**Hao Wu**, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo 


*Conference on Neural Information Processing Systems (NeurIPS), 2024*  

<span style="color:red;">*(CCF Rank A)*</span>  


</div>
</div>

---

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/nuwa.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling](https://easylearningscores.github.io/)

**Kun Wang**, **Hao Wu**, Yifan Duan, Guibin Zhang, Kai Wang, Xiaojiang Peng, Yu Zheng, Yuxuan Liang, Yang Wang


*International Conference on Learning Representations (ICLR), 2024*  

<span style="color:red;">*(THU Rank A spotlight)*</span>  


</div>
</div>
---
<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><img src='../images/beam_search_mianfigure.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[BeamVQ: Aligning Space-Time Forecasting Model via Self-training on Physics-aware Metrics](https://easylearningscores.github.io/)

**Hao Wu**, Xingjian Shi, Ziyue Huang, Penghao Zhao, Wei Xiong, Jinbao Xue, Yangyu Tao, Xiaomeng Huang, Weiyan Wang 


*Arxiv*  



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

