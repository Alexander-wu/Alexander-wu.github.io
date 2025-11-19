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

<!-- 全局样式注入：强制新罗马字体与学术风格 -->
<style>
  /* 全局字体设置 */
  body, h1, h2, h3, h4, h5, h6, p, div, span, li, a {
    font-family: 'Times New Roman', Times, serif !important;
  }
  
  /* 正文排版优化 */
  p {
    font-size: 17px;
    line-height: 1.6;
    color: #333;
    text-align: justify; /* 两端对齐，更具论文感 */
    margin-bottom: 15px;
  }

  /* 链接样式：学术蓝 */
  a {
    color: #003366;
    text-decoration: none;
  }
  a:hover {
    text-decoration: underline;
    color: #0056b3;
  }

  /* News 滚动框美化 */
  .scrollable {
    max-height: 280px;
    overflow-y: auto;
    border: 1px solid #e0e0e0;
    background-color: #fcfcfc;
    padding: 15px;
    border-radius: 4px;
    box-shadow: inset 0 0 5px rgba(0,0,0,0.05);
  }
  /* 自定义滚动条 */
  .scrollable::-webkit-scrollbar {
    width: 6px;
  }
  .scrollable::-webkit-scrollbar-thumb {
    background-color: #ccc;
    border-radius: 3px;
  }
  .scrollable ul {
    margin: 0;
    padding-left: 20px;
  }
  .scrollable li {
    margin-bottom: 8px;
    font-size: 15px;
    color: #444;
  }
  
  /* 徽章微调 */
  .badge {
    font-family: 'Times New Roman', serif !important;
    font-weight: bold;
    letter-spacing: 0.5px;
  }
  
  /* 标题样式增强 */
  h1, h2 {
    color: #111;
    border-bottom: 2px solid #f0f0f0;
    padding-bottom: 10px;
    margin-top: 40px;
    margin-bottom: 20px;
  }
</style>

<!-- Bio Section -->
<div>
<p>
My research journey begins between 2019 and 2022, with a commitment to exploring the deep understanding of natural language. I delve into the evolution from LSTMs to the self-attention mechanism, focusing on the unique challenges of Chinese semantic parsing. During this period, I design and implement <a href="https://arxiv.org/abs/2403.19936">SLFNet</a>, an innovative framework aimed at accurately translating natural language into logical forms. However, the advent of ChatGPT in 2022 completely reshapes the technological paradigm of the NLP field. This disruptive change prompts me to reflect deeply and courageously decide to explore a new and more challenging field.
</p>

<p>
In 2023, I pivot to video prediction and begin a two-year internship (2023-2025) with the <a href="https://github.com/Alexander-wu/Alexander-wu.github.io/blob/main/images/shixi.pdf">Tencent Hunyuan Large Model team</a>. This valuable experience not only allows me to systematically master core models such as ConvLSTM and SimVP but, more importantly, it teaches me how to deeply understand and generate dynamic data from both temporal and spatial dimensions. I am honored to work alongside top researchers in the industry (such as <a href="https://scholar.google.com/citations?user=P4G6H7oAAAAJ&hl=en">Xingjian Shi</a>, <a href="https://yuxuanliang.com/">Yuxuan Liang</a>, <a href="https://scholar.google.com/citations?hl=en&user=qfMSkBgAAAAJ&view_op=list_works&sortby=pubdate">Fan Xu</a>, etc.), and our close collaboration leads to a "blowout period" of academic achievements: as a core author, I publish nearly 30 papers in top conferences such as ICML, ICLR, and NeurIPS. This gives me the freedom and confidence to pursue higher academic goals.
</p>

<p>
By the end of 2024, I transition the experience accumulated in the deep learning field toward a direction with more fundamental scientific value: using artificial intelligence to accelerate the solving of partial differential equations (PDEs). To overcome the bottleneck of computational efficiency, I propose the <a href="https://dl.acm.org/doi/abs/10.1145/3637528.3671779">NMO</a> method, which skillfully utilizes manifold learning to optimize the performance of neural networks and explores distillation (<a href="https://openaccess.thecvf.com/content/ICCV2025/html/Li_Frequency-Aligned_Knowledge_Distillation_for_Lightweight_Spatiotemporal_Forecasting_ICCV_2025_paper.html">ICCV2025</a>) techniques to achieve faster inference. My ultimate goal is to apply this technology to solve real-world challenges.
</p>

<p>
Entering 2025, I focus my research on the application of large-scale PDE solving in Earth sciences, particularly in weather and climate modeling. After accumulating experience and through unremitting efforts, including pre-training and fine-tuning on hundreds of Nvidia A100/A800 GPUs, I, in collaboration with <a href="https://yuangao-yg.github.io/">Yuan Gao</a>, successfully develop <a href="https://arxiv.org/abs/2505.19432">TritonCast</a>, an advanced AI model for long-term Earth system forecasting.
</p>

<p>
Next, in 2026, I will return to the department of computer science to continue my Phd studies, with my research direction focusing on video generation, and the post-training and application of LLM/Agent/VLM.
</p>
</div>

<div style="margin-top: 20px; font-size: 16px;">
  <strong>Email</strong>: <u>wuhao2022@mail.ustc.edu.cn</u> &nbsp; &nbsp; 
  <strong>Wechat</strong>: How_Alexander_Wu
</div>

<!-- News Section -->
<h1 id='news'>🔥 News</h1>

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
    <li><strong>2024.01.16</strong>: 1 paper was accepted to ICLR2024 (<span style="color:#c62828">Spotlight</span>) (Co-First Author).</li>
    <li><strong>2024.02.21</strong>: 1 paper was accepted to TKDE2024 (Co-First Author).</li>
    <li><strong>2023.12.09</strong>: 1 paper was accepted to AAAI2024 (First Author).</li>
    <li><strong>2023.09.22</strong>: 1 paper was accepted to NeurIPS2023 (Co-First Author).</li>
    <li><strong>2022.10.09</strong>: National Scholarship, China, 2022 (top 0.1% nation-wide, From USTC).</li>
  </ul>
</div>

<!-- Experience Section -->
<h1>📖 Research Experience</h1>

<div style="display: flex; align-items: center; margin-bottom: 25px;">
  <img src="../images/tencent.png" alt="Tencent" style="width: 80px; margin-right: 30px; margin-left: 10px;"/>
  <ul style="list-style-type: none; padding-left: 0; margin: 0;">
    <li style="font-weight: bold; font-size: 18px;">Jarvis Lab, Tencent</li>
    <li style="color: #555; font-style: italic;">2025.08 - Present, <strong>Research intern</strong></li>
    <li>Mentored by <a href="https://scholar.google.com/citations?user=lslB5jkAAAAJ&hl=zh-CN">Xian Wu</a></li>
  </ul>
</div>

<div style="display: flex; align-items: center; margin-bottom: 25px;">
  <img src="../images/tencent.png" alt="Tencent" style="width: 80px; margin-right: 30px; margin-left: 10px;"/>
  <ul style="list-style-type: none; padding-left: 0; margin: 0;">
    <li style="font-weight: bold; font-size: 18px;">Machine Learning Platform Department, Large Model Training Group, Tencent</li>
    <li style="color: #555; font-style: italic;">2023.08 - 2025.07, <strong>Research intern</strong></li>
    <li>Mentored by <a href="https://github.com/easylearningscores/Alexander-wu.github.io/blob/main/images/shixi.pdf">Jinbao Xue</a></li>
  </ul>
</div>

<div style="display: flex; align-items: center; margin-bottom: 25px;">
  <img src="../images/hkust.png" alt="HKUST" style="width: 80px; margin-right: 30px; margin-left: 10px;"/>
  <ul style="list-style-type: none; padding-left: 0; margin: 0;">
    <li style="font-weight: bold; font-size: 18px;">CityMind Lab, HKUST (Guangzhou)</li>
    <li style="color: #555; font-style: italic;">2023.05 - 2023.08, <strong>Research intern</strong></li>
    <li>Advisor <a href="http://buaahsh.github.io/">Yuxuan Liang</a></li>
  </ul>
</div>

<!-- Publications List -->
<h1>📝 Publications</h1>

<h4>Scientific Machine Learning</h4>

<ul>
  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">ICML 2025</span> <strong>OneForecast: A Universal Framework for Global and Regional Weather Forecasting</strong>. <br>Yuan Gao, Hao Wu, et al. <a href="https://arxiv.org/abs/2502.00338">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">NeurIPS 2024</span> <strong>PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling</strong>. <br><strong>Hao Wu</strong>, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo#. <a href="https://openreview.net/forum?id=z86knmjoUq">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">ICML 2024</span> <strong>Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE</strong>. <br><strong>Hao Wu</strong>, Huiyuan Wang, et al. <a href="https://openreview.net/forum?id=JsPvL6ExK8">[Paper]</a></li>

  <li><span style="background-color: #666; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">Arxiv</span> <strong>Spatio-temporal fluid dynamics modeling via physical-awareness and parameter diffusion guidance</strong>. <br><strong>Hao Wu</strong>, Fan Xu, et al. <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=HdXMhfcAAAAJ&citation_for_view=HdXMhfcAAAAJ:IWHjjKOFINEC">[Paper]</a></li>
</ul>

<h4>Spatio-temporal Prediction</h4>

<ul>
  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">ICCV 2025</span> <strong>Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting</strong>. <br>Yuqi Li... <strong>Hao Wu#</strong>. <a href="https://openreview.net/forum?id=sKEFrZ0wCj#discussion">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">KDD 2025</span> <strong>DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting</strong>. <br><strong>Hao Wu</strong>, Haomin Wen, et al. <a href="https://openreview.net/forum?id=sKEFrZ0wCj#discussion">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">AAAI 2024</span> <strong>Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model</strong>. <br><strong>Hao Wu</strong>, Yuxuan Liang, et al. <a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">ICLR 2024</span> <strong>NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling</strong>. <br><strong>Kun Wang^</strong>, <strong>Hao Wu^</strong>, et al. <a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521/30866">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">TKDE 2024</span> <strong>Modeling spatio-temporal dynamical systems with neural discrete learning and levels-of-experts</strong>. <br><strong>Kun Wang^</strong>, <strong>Hao Wu^</strong>, et al. <a href="https://scholar.google.com/citations?view_op=view_citation&hl=en&user=HdXMhfcAAAAJ&citation_for_view=HdXMhfcAAAAJ:Wp0gIr-vW9MC">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">ACM MM 2024</span> <strong>PastNet: introducing physical inductive biases for spatio-temporal video prediction</strong>. <br><strong>Hao Wu</strong>, et al. <a href="https://arxiv.org/abs/2305.11421">[Paper]</a></li>

  <li><span style="background-color: #666; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">Arxiv</span> <strong>BeamVQ: Aligning Space-Time Forecasting Model via Self-training on Physics-aware Metrics</strong>. <br><strong>Hao Wu</strong>, et al. <a href="https://openreview.net/forum?id=iL6FrLIc8K">[Paper]</a></li>
</ul>

<h4>Neural Operator Learning</h4>

<ul>
  <li><span style="background-color: #666; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">Arxiv</span> <strong>Turb-L1: Achieving Long-term Turbulence Tracing By Tackling Spectral Bias</strong>. <br>Hao Wu, et al. <a href="https://arxiv.org/abs/2505.19038">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">KDD 2024</span> <strong>Neural Manifold Operators for Learning the Evolution of Physical Dynamics</strong>. <br><strong>Hao Wu</strong>, Kangyu Weng, et al. <a href="https://openreview.net/pdf?id=r7n0Q4P66V">[Paper]</a></li>

  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">AI4TS(Oral)</span> <strong>Neural Manifold Operator for Geophysical Fluid Dynamics Prediction</strong>. <br>Wei Xiong... <strong>Hao Wu#</strong>. <a href="https://openreview.net/pdf?id=r7n0Q4P66V">[Paper]</a></li>
</ul>

<h4>Information Retrieval</h4>

<ul>
  <li><span style="background-color: #003366; color: white; padding: 2px 6px; font-size: 12px; border-radius: 3px;">NeurIPS 2023</span> <strong>IDEA: An Invariant Perspective for Efficient Domain Adaptive Image Retrieval</strong>. <br><strong>Haixin Wang^</strong>, <strong>Hao Wu^</strong>, et al. <a href="https://openreview.net/forum?id=77i6itptQW">[Paper]</a></li>
</ul>


<!-- Selected Publications with Thumbnails -->
<h2>Selected Publications</h2>
<hr style="border: 0; border-top: 1px solid #eee; margin-bottom: 30px;">

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2026</div><img src='../images/fig_main.jpg' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[NeuralOM: Neural Ocean Model for Subseasonal-to-Seasonal Simulation](https://arxiv.org/abs/2505.21020)

Yuan Gao<sup>†</sup>, **Hao Wu**<sup>†</sup> <sup>‡ </sup>, Fan Xu, Yanfei Xiang, Ruijian Gou,  Ruiqi Shu, Qingsong Wen, Xian Wu, Kun Wang<sup>*</sup>, Xiaomeng Huang<sup>*</sup>

<span style="color:#c62828; font-style: italic;">(AAAI2026, CCF Rank A)</span>  

<a href="https://arxiv.org/abs/2505.21020" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/NeuralOM" target="_blank">Code</a>
<img src="https://img.shields.io/github/stars/YuanGao-YG/NeuralOM?label=%F0%9F%8C%9F%20Star&color=blue"> <img src="https://img.shields.io/github/forks/YuanGao-YG/NeuralOM?label=%F0%9F%94%A7%20Fork&color=green">
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICCV 2025</div><img src='../images/iccv2025.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting](https://openreview.net/group?id=thecvf.com/ICCV/2025/Conference/Authors&referrer=%5BHomepage%5D(%2F))

Yuqi Li, Chuanguang Yang, Hansheng Zeng, Zeyu Dong, Zhulin An, Yongjun Xu, Yingli Tian, **Hao Wu#**

<span style="color:#c62828; font-style: italic;">(ICCV2025, CCF Rank A)</span>  

<a href="https://arxiv.org/abs/2502.00338" target="_blank">Paper</a> | <a href="https://github.com/itsnotacie/SDKD" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2025</div><img src='../images/one.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[OneForecast: A Universal Framework for Global and Regional Weather Forecasting](https://openreview.net/forum?id=A23C57icJt&referrer=%5BAuthor%20Console%5D(%2Fgroup%3Fid%3DICLR.cc%2F2025%2FConference%2FAuthors%23your-submissions))

Yuan Gao, Hao Wu, Ruiqi Shu, huanshuo dong, Fan Xu, Rui Ray Chen, Yibo Yan, Qingsong Wen, Xuming Hu, Kun Wang, Jiahao Wu, Li Qing, Hui Xiong, Xiaomeng Huang#

<span style="color:#c62828; font-style: italic;">(ICML2025, CCF Rank A)</span>  

<a href="https://arxiv.org/abs/2502.00338" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/OneForecast" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2025</div><img src='../images/openck.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Open-CK: A Large Multi-Physics Fields Coupling benchmarks in Combustion Kinetics](https://openreview.net/forum?id=A23C57icJt)

Zaige Fei, Fan Xu, Junyuan Mao, Yuxuan Liang, Qingsong Wen, Kun Wang, **Hao Wu#**, Yang Wang

<span style="color:#c62828; font-style: italic;">(ICLR2025, THU Rank A)</span>  

<a href="https://openreview.net/forum?id=A23C57icJt" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2025</div><img src='../images/DnyST.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting](https://arxiv.org/abs/2403.02914)

**Hao Wu**, Haomin Wen, Guibin Zhang, Yutong Xia, Yuxuan Liang, Yu Zheng, Qingsong Wen, Kun Wang

<span style="color:#c62828; font-style: italic;">(KDD2025, CCF Rank A)</span>  

<a href="https://arxiv.org/abs/2505.19432" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KDD 2024</div><img src='../images/NMO_main.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Neural Manifold Operators for Learning the Evolution of Physical Dynamics](https://dl.acm.org/doi/abs/10.1145/3637528.3671779)

**Hao Wu**, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang, Wei Xiong

<span style="color:#c62828; font-style: italic;">(KDD2024, CCF Rank A)</span>  

<a href="https://dl.acm.org/doi/10.1145/3637528.3671779" target="_blank">Paper</a> | <a href="https://github.com/AI4EarthLab/Neural-Manifold-Operators" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICML 2024</div><img src='../images/Prometheus.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE](https://openreview.net/forum?id=JsPvL6ExK8&referrer=%5Bthe%20profile%20of%20Hao%20Wu%5D(%2Fprofile%3Fid%3D~Hao_Wu39))

**Hao Wu**,  Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo

<span style="color:#c62828; font-style: italic;">(ICML2024, CCF Rank A)</span>  

<a href="https://proceedings.mlr.press/v235/wu24aa.html" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/DGODE_ood" target="_blank">Code</a> | <a href="https://huggingface.co/datasets/easylearning/Prometheus/tree/main" target="_blank">Benchmark</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACMMM 2024</div><img src='../images/pastnet.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[PastNet: Introducing Physical Inductive Biases for Spatio-temporal Video Prediction](https://openreview.net/forum?id=mL0KvSwXzk&referrer=%5Bthe%20profile%20of%20Xian-Sheng%20Hua%5D(%2Fprofile%3Fid%3D~Xian-Sheng_Hua1))

**Hao Wu**, Fan Xu, Chong Chen, Xian-Sheng Hua, Xiao Luo, Haixin Wang

<span style="color:#c62828; font-style: italic;">(ACM MM, CCF Rank A)</span>  

<a href="https://dl.acm.org/doi/10.1145/3664647.3681489" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/PastNet" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">AAAI 2024</div><img src='../images/Earthfarseer.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[Earthfarsser: Versatile Spatio-Temporal Dynamical Systems Modeling in One Model](https://ojs.aaai.org/index.php/AAAI/article/view/29521)

**Hao Wu**, Yuxuan Liang, Wei Xiong, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang

<span style="color:#c62828; font-style: italic;">(AAAI2024, CCF Rank A)</span>  

<a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/EarthFarseer" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NeurIPS 2024</div><img src='../images/pure.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling](https://easylearningscores.github.io/)

**Hao Wu**, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo 

<span style="color:#c62828; font-style: italic;">(NeurIPS2024, CCF Rank A)</span>  

<a href="https://neurips.cc/virtual/2024/poster/92971" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores" target="_blank">Code</a>
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ICLR 2024</div><img src='../images/nuwa.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">
[NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling](https://easylearningscores.github.io/)

**Kun Wang**, **Hao Wu**, Yifan Duan, Guibin Zhang, Kai Wang, Xiaojiang Peng, Yu Zheng, Yuxuan Liang, Yang Wang

<span style="color:#c62828; font-style: italic;">(ICLR2024, THU Rank A spotlight)</span>  

<a href="https://openreview.net/forum?id=sLdVl0q68X" target="_blank">Paper</a> | <a href="https://github.com/easylearningscores/NuwaDynamics" target="_blank">Code</a>
</div>
</div>
<hr style="border: 0; border-top: 1px solid #eee;">

<!-- Awards -->
<h1>🎖 Honors and Awards</h1>
<ul>
  <li><em>2024.09</em> First-class Academic Scholarship of the University of Science and Technology of China.</li>
  <li><em>2022.10</em> National Scholarship, China (top 0.1% nation-wide).</li>
  <li><em>2022.09</em> First-class Academic Scholarship of the University of Science and Technology of China.</li>
</ul>

<!-- Invited Talks -->
<h1>💬 Invited Talks</h1>
<ul>
  <li><em>2024.03</em>, Application and Research of GNN in Meteorological Prediction. @ Sun Yat-sen University</li>
  <li><em>2023.12</em>, Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model. @ AI TIME </li>
  <li><em>2023.06</em>, A Review of Spatio-Temporal Forecasting Models. @ Tsinghua University</li>
</ul>

<!-- Service -->
<h1>💻 Academic Service</h1>
<p style="font-size: 15px;">
  <strong>PC Member / Conference Reviewer:</strong><br>
  NeurIPS (2023, 2024, 2025), ICLR (2024, 2025), ICML (2024, 2025), AAAI (2025), CVPR/ICCV (2025), ACM MM (2024, 2025), AISTATS (2025).
</p>

<!-- Misc -->
<h1>👨🏻 Miscellaneous</h1>
<ul>
  <li>🏀 I am a big fan of basketball. I love Kobe Bryant and his Fadeaway Shot. I also like Stephen Curry.</li>
  <li>👑 I am very interested in history.</li>
</ul>
