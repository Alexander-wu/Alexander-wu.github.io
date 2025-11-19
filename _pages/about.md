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

<!-- ================= GLOBAL STYLES ================= -->
<style>
  /* 1. 页面宽度调整：强制变宽 */
  /* 针对常见的 Jekyll 主题 (Minimal Mistakes) 进行宽度覆盖 */
  .page__inner-wrap {
    max-width: 1280px !important; /* 加宽主内容区域 */
    margin-left: auto;
    margin-right: auto;
    padding-right: 1em;
    padding-left: 1em;
  }
  .archive {
    width: 100% !important;
    max-width: 1280px !important;
  }

  /* 2. 全局字体：Times New Roman */
  body, h1, h2, h3, h4, h5, h6, p, div, span, li, a, button, strong {
    font-family: 'Times New Roman', Times, serif !important;
    color: #222;
  }

  /* 链接颜色 */
  a { color: #003366; text-decoration: none; transition: all 0.2s; }
  a:hover { color: #0056b3; text-decoration: underline; }

  /* 容器卡片 */
  .container-box {
    background: #fff;
    padding: 25px;
    margin-bottom: 30px;
    border-radius: 8px;
    border: 1px solid #eee;
    box-shadow: 0 4px 10px rgba(0,0,0,0.03);
  }

  /* --- 顶部 BIO 布局 (左文右图) --- */
  .bio-container {
    display: flex;
    justify-content: space-between;
    gap: 40px; /* 文字和图片之间的间距 */
    margin-bottom: 40px;
    align-items: flex-start;
  }

  .bio-text-col {
    flex: 1; /* 占据剩余空间 */
  }

  .bio-photo-col {
    flex: 0 0 280px; /* 固定图片容器宽度 */
  }

  .bio-photo {
    width: 100%;
    height: auto;
    border-radius: 8px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    object-fit: cover;
    border: 1px solid #ddd;
  }

  /* 头部按钮网格 (现在放在自我介绍下方) */
  .link-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 15px;
    margin-top: 25px;
  }
  
  .link-btn {
    display: inline-flex;
    align-items: center;
    padding: 6px 12px;
    background-color: #f4f4f4;
    border: 1px solid #ccc;
    border-radius: 4px;
    color: #333 !important;
    font-size: 15px;
    font-weight: bold;
  }
  .link-btn:hover {
    background-color: #e0e0e0;
    border-color: #003366;
    color: #003366 !important;
  }

  /* Experience 列表 */
  .exp-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 25px;
    padding-bottom: 25px;
    border-bottom: 1px solid #eee;
  }
  .exp-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
  
  .exp-logo {
    width: 65px; 
    height: 65px; 
    margin-right: 25px;
    object-fit: contain;
    border-radius: 4px;
    border: 1px solid #ddd;
    padding: 4px;
    background: #fff;
  }
  
  .exp-content { flex: 1; }
  .exp-title { font-weight: bold; font-size: 19px; color: #000; margin-bottom: 6px; }
  .exp-subtitle { font-size: 17px; color: #444; margin-bottom: 6px; font-style: italic; }
  .exp-date { font-size: 16px; color: #666; }

  /* News 滚动区域 */
  .news-scroll {
    max-height: 300px;
    overflow-y: auto;
    background-color: #fafafa;
    padding: 20px;
    border-radius: 8px;
    border: 1px solid #ddd;
  }
  .news-scroll ul { padding-left: 20px; margin: 0; }
  .news-scroll li { margin-bottom: 12px; font-size: 17px; line-height: 1.5; }

  /* --- SELECTED PUBLICATIONS (11篇全) --- */
  .pub-card {
    display: flex;
    flex-wrap: wrap;
    background: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    margin-bottom: 25px;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .pub-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.08);
    border-color: #aaa;
  }

  .pub-img-col {
    flex: 0 0 320px; /* 图片宽度略微加大 */
    position: relative;
    background: #f9f9f9;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #eee;
    padding: 10px;
  }
  
  .pub-img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 2px;
  }

  /* Badge */
  .pub-badge {
    position: absolute;
    top: 12px;
    left: 0;
    background: #003366;
    color: white;
    padding: 4px 12px;
    font-size: 14px;
    font-weight: bold;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    box-shadow: 2px 2px 5px rgba(0,0,0,0.2);
    z-index: 2;
    font-family: 'Times New Roman', serif;
  }

  .pub-content-col {
    flex: 1;
    padding: 20px 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 350px;
  }

  .pub-title {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 12px;
    line-height: 1.3;
    color: #111;
  }
  .pub-title a { color: #111; }
  .pub-title a:hover { color: #003366; }

  .pub-authors {
    font-size: 17px;
    color: #333;
    margin-bottom: 12px;
    line-height: 1.5;
  }
  .pub-authors strong { color: #000; text-decoration: underline; }

  .pub-venue {
    font-size: 16px;
    font-style: italic;
    color: #c62828;
    margin-bottom: 15px;
    font-weight: bold;
  }

  .pub-links a {
    display: inline-block;
    font-size: 15px;
    font-weight: bold;
    margin-right: 20px;
    color: #003366;
    text-transform: uppercase;
  }
  
  /* 标题样式 */
  h1.section-title {
    font-size: 28px;
    font-weight: bold;
    border-bottom: 2px solid #eee;
    padding-bottom: 12px;
    margin-top: 60px;
    margin-bottom: 30px;
    color: #111;
  }

  /* 移动端适配 */
  @media (max-width: 850px) {
    .bio-container { flex-direction: column-reverse; gap: 20px; }
    .bio-photo-col { flex: 0 0 auto; width: 100%; max-width: 250px; margin: 0 auto; }
    .pub-img-col { flex: 0 0 100%; border-right: none; border-bottom: 1px solid #eee; }
    .pub-card { flex-direction: column; }
  }
</style>


<!-- ================= BIO SECTION (LEFT TEXT, RIGHT IMAGE) ================= -->
<div class="bio-container">
  
  <!-- 左侧：文字介绍 + 按钮链接 -->
  <div class="bio-text-col">
    <div style="font-size: 24px; font-weight: bold; margin-bottom: 10px;">Hao Wu (吴浩)</div>
    <div style="font-size: 18px; color: #555; margin-bottom: 20px;">Ph.D. Student at USTC (Incoming 2026)</div>
    
    <div style="font-size: 18px; line-height: 1.7; text-align: justify; color: #222;">
      <p>
        My research journey begins between 2019 and 2022, focusing on Chinese semantic parsing. During this period, I designed <a href="https://arxiv.org/abs/2403.19936">SLFNet</a> for translating natural language into logical forms. The advent of ChatGPT in 2022 prompted me to explore more challenging fields.
      </p>
      <p>
        In 2023, I pivoted to video prediction, interning at the <a href="#">Tencent Hunyuan Large Model team</a> (2023-2025). I mastered models like ConvLSTM/SimVP and published nearly 30 papers in <strong>ICML, ICLR, and NeurIPS</strong> with top researchers.
      </p>
      <p>
        Currently, I focus on <strong>AI for Earth Sciences (AI4Science)</strong>. I proposed the <a href="#">NMO</a> method and explored distillation techniques (ICCV2025). Recently, I co-developed <a href="https://arxiv.org/abs/2505.19432">TritonCast</a>, an advanced AI model for Earth system forecasting.
      </p>
    </div>

    <!-- 链接按钮组 -->
    <div class="link-grid">
      <a href="mailto:wuhao2022@mail.ustc.edu.cn" class="link-btn">✉️ Email</a>
      <a href="YOUR_GOOGLE_SCHOLAR_LINK" class="link-btn">🎓 Google Scholar</a>
      <a href="YOUR_GITHUB_LINK" class="link-btn">🐙 GitHub</a>
      <a href="YOUR_SEMANTIC_SCHOLAR_LINK" class="link-btn">📚 Semantic Scholar</a>
    </div>
  </div>

  <!-- 右侧：头像 (请替换 src) -->
  <div class="bio-photo-col">
    <!-- 请务必将下方的 src 替换为您真实的图片路径 -->
    <img src="../images/wuhaodemo" class="bio-photo" alt="Hao Wu">
  </div>

</div>


<!-- ================= NEWS SECTION ================= -->
<h1 class="section-title" id='news'>🔥 News</h1>
<div class="news-scroll">
  <ul>
    <li><strong>2025.11.08</strong>: 2 papers accepted to AAAI2026 Main Track.</li>
    <li><strong>2025.09.18</strong>: 2 papers accepted to NeurIPS2025.</li>
    <li><strong>2025.08.01</strong>: Joined Tencent CSIG (Jarvis Lab) as a research intern.</li>
    <li><strong>2025.06.26</strong>: 1 paper accepted to ICCV2025 (Corresponding Author).</li>
    <li><strong>2025.06.18</strong>: Graduated from USTC CS with Outstanding Graduation Thesis Award.</li>
    <li><strong>2025.05.01</strong>: 1 paper accepted to ICML2025 (Co-First Author).</li>
    <li><strong>2025.01.22</strong>: 1 paper accepted to ICLR2025 (Corresponding Author).</li>
    <li><strong>2024.11.16</strong>: 1 paper accepted to KDD2025 ADS (First Author).</li>
    <li><strong>2024.01.16</strong>: 1 paper accepted to ICLR2024 (<span style="color:#c62828">Spotlight</span>).</li>
    <li><strong>2022.10.09</strong>: Received National Scholarship (Top 0.1%).</li>
  </ul>
</div>

<!-- ================= EXPERIENCE ================= -->
<h1 class="section-title">💼 Research Experience</h1>
<div class="container-box">

  <div class="exp-item">
    <img src="../images/tencent.png" class="exp-logo" alt="Tencent">
    <div class="exp-content">
      <div class="exp-title">Jarvis Lab, Tencent</div>
      <div class="exp-subtitle">Research Intern &nbsp; | &nbsp; Mentor: <a href="#">Xian Wu</a></div>
      <div class="exp-date">Aug. 2025 - Present</div>
    </div>
  </div>

  <div class="exp-item">
    <img src="../images/tencent.png" class="exp-logo" alt="Tencent">
    <div class="exp-content">
      <div class="exp-title">Machine Learning Platform Dept., Tencent</div>
      <div class="exp-subtitle">Research Intern (Hunyuan Large Model) &nbsp; | &nbsp; Mentor: <a href="#">Jinbao Xue</a></div>
      <div class="exp-date">Aug. 2023 - Jul. 2025</div>
    </div>
  </div>

  <div class="exp-item">
    <img src="../images/hkust.png" class="exp-logo" alt="HKUST">
    <div class="exp-content">
      <div class="exp-title">CityMind Lab, HKUST (Guangzhou)</div>
      <div class="exp-subtitle">Research Intern &nbsp; | &nbsp; Advisor: <a href="#">Yuxuan Liang</a></div>
      <div class="exp-date">May 2023 - Aug. 2023</div>
    </div>
  </div>

</div>


<!-- ================= SELECTED PUBLICATIONS (11 Papers) ================= -->
<h1 class="section-title">🌟 Selected Publications</h1>

<!-- 1. NeuralOM -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">AAAI 2026</div>
    <img src="../images/fig_main.jpg" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://arxiv.org/abs/2505.21020">NeuralOM: Neural Ocean Model for Subseasonal-to-Seasonal Simulation</a>
    </div>
    <div class="pub-authors">
      Yuan Gao<sup>†</sup>, <strong>Hao Wu</strong><sup>†‡</sup>, Fan Xu, Yanfei Xiang, Ruijian Gou, Ruiqi Shu, Qingsong Wen, Xian Wu, Kun Wang*, Xiaomeng Huang*
    </div>
    <div class="pub-venue">
      (AAAI 2026, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2505.21020">Paper</a>
      <a href="https://github.com/YuanGao-YG/NeuralOM">Code</a>
      <img src="https://img.shields.io/github/stars/YuanGao-YG/NeuralOM?label=Star&style=social" style="vertical-align:middle;">
    </div>
  </div>
</div>

<!-- 2. ICCV 2025 -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICCV 2025</div>
    <img src="../images/iccv2025.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="#">Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting</a>
    </div>
    <div class="pub-authors">
      Yuqi Li, Chuanguang Yang, Hansheng Zeng, Zeyu Dong, Zhulin An, Yongjun Xu, Yingli Tian, <strong>Hao Wu#</strong>
    </div>
    <div class="pub-venue">
      (ICCV 2025, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="#">Paper</a>
      <a href="https://github.com/itsnotacie/SDKD">Code</a>
    </div>
  </div>
</div>

<!-- 3. OneForecast -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICML 2025</div>
    <img src="../images/one.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://arxiv.org/abs/2502.00338">OneForecast: A Universal Framework for Global and Regional Weather Forecasting</a>
    </div>
    <div class="pub-authors">
      Yuan Gao, <strong>Hao Wu</strong>, Ruiqi Shu, Huanshuo Dong, Fan Xu, Rui Ray Chen, Yibo Yan, Qingsong Wen, Xuming Hu, Kun Wang, Jiahao Wu, Li Qing, Hui Xiong, Xiaomeng Huang#
    </div>
    <div class="pub-venue">
      (ICML 2025, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2502.00338">Paper</a>
      <a href="https://github.com/YuanGao-YG/OneForecast">Code</a>
    </div>
  </div>
</div>

<!-- 4. Open-CK -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICLR 2025</div>
    <img src="../images/openck.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://openreview.net/forum?id=A23C57icJt">Open-CK: A Large Multi-Physics Fields Coupling benchmarks in Combustion Kinetics</a>
    </div>
    <div class="pub-authors">
      Zaige Fei, Fan Xu, Junyuan Mao, Yuxuan Liang, Qingsong Wen, Kun Wang, <strong>Hao Wu#</strong>, Yang Wang
    </div>
    <div class="pub-venue">
      (ICLR 2025, THU Rank A)
    </div>
    <div class="pub-links">
      <a href="https://openreview.net/forum?id=A23C57icJt">Paper</a>
      <a href="https://github.com/easylearningscores">Code</a>
    </div>
  </div>
</div>

<!-- 5. DynST -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">KDD 2025</div>
    <img src="../images/DnyST.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://arxiv.org/abs/2403.02914">DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Haomin Wen, Guibin Zhang, Yutong Xia, Yuxuan Liang, Yu Zheng, Qingsong Wen, Kun Wang
    </div>
    <div class="pub-venue">
      (KDD 2025, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2505.19432">Paper</a>
      <a href="https://github.com/easylearningscores">Code</a>
    </div>
  </div>
</div>

<!-- 6. NMO -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">KDD 2024</div>
    <img src="../images/NMO_main.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://dl.acm.org/doi/abs/10.1145/3637528.3671779">Neural Manifold Operators for Learning the Evolution of Physical Dynamics</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Kangyu Weng, Shuyi Zhou, Xiaomeng Huang, Wei Xiong
    </div>
    <div class="pub-venue">
      (KDD 2024, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://dl.acm.org/doi/10.1145/3637528.3671779">Paper</a>
      <a href="https://github.com/AI4EarthLab/Neural-Manifold-Operators">Code</a>
    </div>
  </div>
</div>

<!-- 7. Prometheus -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICML 2024</div>
    <img src="../images/Prometheus.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://openreview.net/forum?id=JsPvL6ExK8">Prometheus: Out-of-distribution Fluid Dynamics Modeling with Disentangled Graph ODE</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Huiyuan Wang, Kun Wang, Weiyan Wang, ChanganYe, Yangyu Tao, Chong Chen, Xian-Sheng Hua, Xiao Luo
    </div>
    <div class="pub-venue">
      (ICML 2024, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://proceedings.mlr.press/v235/wu24aa.html">Paper</a>
      <a href="https://github.com/easylearningscores/DGODE_ood">Code</a>
      <a href="https://huggingface.co/datasets/easylearning/Prometheus/tree/main">Benchmark</a>
    </div>
  </div>
</div>

<!-- 8. PastNet -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ACM MM 2024</div>
    <img src="../images/pastnet.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://openreview.net/forum?id=mL0KvSwXzk">PastNet: Introducing Physical Inductive Biases for Spatio-temporal Video Prediction</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Fan Xu, Chong Chen, Xian-Sheng Hua, Xiao Luo, Haixin Wang
    </div>
    <div class="pub-venue">
      (ACM MM 2024, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://dl.acm.org/doi/10.1145/3664647.3681489">Paper</a>
      <a href="https://github.com/easylearningscores/PastNet">Code</a>
    </div>
  </div>
</div>

<!-- 9. Earthfarseer -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">AAAI 2024</div>
    <img src="../images/Earthfarseer.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521">Earthfarseer: Versatile Spatio-Temporal Dynamical Systems Modeling in One Model</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Yuxuan Liang, Wei Xiong, Zhengyang Zhou, Wei Huang, Shilong Wang, Kun Wang
    </div>
    <div class="pub-venue">
      (AAAI 2024, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://ojs.aaai.org/index.php/AAAI/article/view/29521">Paper</a>
      <a href="https://github.com/easylearningscores/EarthFarseer">Code</a>
    </div>
  </div>
</div>

<!-- 10. PURE -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">NeurIPS 2024</div>
    <img src="../images/pure.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://neurips.cc/virtual/2024/poster/92971">PURE: Prompt Evolution with Graph ODE for Out-of-distribution Fluid Dynamics Modeling</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Changhu Wang, Fan Xu, Jinbao Xue, Chong Chen, Xian-Sheng Hua, Xiao Luo
    </div>
    <div class="pub-venue">
      (NeurIPS 2024, CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://neurips.cc/virtual/2024/poster/92971">Paper</a>
      <a href="https://github.com/easylearningscores">Code</a>
    </div>
  </div>
</div>

<!-- 11. NuwaDynamics -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICLR 2024</div>
    <img src="../images/nuwa.png" class="pub-img" alt="Paper Image">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://openreview.net/forum?id=sLdVl0q68X">NuwaDynamics: Discovering and Updating in Causal Spatio-Temporal Modeling</a>
    </div>
    <div class="pub-authors">
      <strong>Kun Wang</strong>, <strong>Hao Wu</strong>, Yifan Duan, Guibin Zhang, Kai Wang, Xiaojiang Peng, Yu Zheng, Yuxuan Liang, Yang Wang
    </div>
    <div class="pub-venue">
      (ICLR 2024, THU Rank A Spotlight)
    </div>
    <div class="pub-links">
      <a href="https://openreview.net/forum?id=sLdVl0q68X">Paper</a>
      <a href="https://github.com/easylearningscores/NuwaDynamics">Code</a>
    </div>
  </div>
</div>


<!-- ================= MISC ================= -->
<h1 class="section-title">💬 Invited Talks</h1>
<ul style="line-height: 1.6; font-size: 17px;">
  <li><em>2024.03</em>, Application and Research of GNN in Meteorological Prediction. @ Sun Yat-sen University</li>
  <li><em>2023.12</em>, Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model. @ AI TIME </li>
</ul>

<h1 class="section-title">💻 Academic Service</h1>
<div style="background: #fbfbfb; padding: 20px; border-radius: 6px; font-size: 17px; border: 1px solid #eee; line-height: 1.6;">
  <strong>Conference Reviewer / PC Member:</strong><br>
  NeurIPS (2023-2025), ICLR (2024-2025), ICML (2024-2025), CVPR (2025), ICCV (2025), AAAI (2025), ACM MM (2024-2025), AISTATS (2025).
</div>

<h1 class="section-title">👨🏻 Miscellaneous</h1>
<ul style="line-height: 1.6; font-size: 17px;">
  <li>🏀 Big fan of basketball. I love Kobe Bryant and his Fadeaway Shot. Also a fan of Stephen Curry.</li>
  <li>👑 Deeply interested in History.</li>
</ul>
