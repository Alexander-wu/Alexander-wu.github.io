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
  /* 1. 字体升级：使用现代无衬线字体 (High-end Academic Look) */
  body, h1, h2, h3, h4, h5, h6, p, div, span, li, a, button {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol" !important;
    color: #24292e;
  }

  /* 链接颜色：更深邃的科技蓝 */
  a { color: #0366d6; text-decoration: none; transition: color 0.2s; }
  a:hover { color: #0056b3; text-decoration: underline; }

  /* 容器通用样式：卡片化 */
  .container-box {
    background: #fff;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 8px;
    border: 1px solid #e1e4e8;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }

  /* 头部按钮网格 */
  .link-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 12px;
    margin-top: 20px;
    margin-bottom: 30px;
  }
  
  .link-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 10px 16px;
    background-color: #f6f8fa;
    border: 1px solid #d1d5da;
    border-radius: 6px;
    color: #24292e !important;
    font-size: 14px;
    font-weight: 600;
    transition: all 0.2s ease;
  }
  
  .link-btn:hover {
    background-color: #fff;
    border-color: #0366d6;
    color: #0366d6 !important;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.05);
  }

  /* Experience 列表项 */
  .exp-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #eaecef;
  }
  .exp-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
  
  .exp-logo {
    width: 56px; 
    height: 56px; 
    margin-right: 18px;
    object-fit: contain;
    border-radius: 8px;
    border: 1px solid #eee;
    padding: 2px;
    background: #fff;
  }
  
  .exp-content { flex: 1; }
  .exp-title { font-weight: 700; font-size: 16px; color: #000; margin-bottom: 4px; }
  .exp-subtitle { font-size: 14px; color: #586069; margin-bottom: 4px; }
  .exp-date { font-size: 13px; color: #6a737d; font-family: 'SF Mono', Consolas, monospace; }

  /* News 滚动区域 */
  .news-scroll {
    max-height: 260px;
    overflow-y: auto;
    background-color: #f6f8fa;
    padding: 15px 20px;
    border-radius: 8px;
    border: 1px solid #e1e4e8;
  }
  .news-scroll ul { padding-left: 20px; margin: 0; }
  .news-scroll li { margin-bottom: 10px; font-size: 14px; line-height: 1.6; }

  /* --- SELECTED PUBLICATIONS (修复显示问题的核心样式) --- */
  .pub-card {
    display: flex;
    flex-wrap: wrap; /* 移动端自动换行 */
    background: #fff;
    border: 1px solid #e1e4e8;
    border-radius: 10px;
    margin-bottom: 25px;
    overflow: hidden;
    transition: transform 0.2s, box-shadow 0.2s;
  }
  .pub-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.08);
    border-color: #c8e1ff;
  }

  .pub-img-col {
    flex: 0 0 320px; /* 左侧图片固定宽度 */
    position: relative;
    background: #f9f9f9;
    display: flex;
    align-items: center;
    justify-content: center;
    border-right: 1px solid #eaecef;
    padding: 10px;
  }
  
  .pub-img {
    width: 100%;
    height: auto;
    display: block;
    border-radius: 4px;
  }

  /* 悬浮在图片左上角的 Badge */
  .pub-badge {
    position: absolute;
    top: 12px;
    left: 0;
    background: #005cc5; /* 科技蓝 */
    color: white;
    padding: 4px 12px;
    font-size: 12px;
    font-weight: bold;
    border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    box-shadow: 2px 2px 4px rgba(0,0,0,0.2);
    z-index: 2;
  }

  .pub-content-col {
    flex: 1;
    padding: 20px 25px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-width: 300px;
  }

  .pub-title {
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
    line-height: 1.4;
    color: #24292e;
  }
  .pub-title a { color: #24292e; }
  .pub-title a:hover { color: #0366d6; }

  .pub-authors {
    font-size: 15px;
    color: #444;
    margin-bottom: 10px;
    line-height: 1.5;
  }
  .pub-authors strong { color: #000; border-bottom: 2px solid #c8e1ff; } /* 高亮自己 */

  .pub-venue {
    font-size: 14px;
    font-style: italic;
    color: #d73a49; /* 红色高亮 CCF Rank */
    margin-bottom: 12px;
    font-weight: 500;
  }

  .pub-links a {
    display: inline-block;
    font-size: 13px;
    font-weight: 600;
    margin-right: 15px;
    color: #0366d6;
  }
  .pub-links img { vertical-align: middle; margin-left: 5px; }

  /* 标题样式 */
  h1.section-title {
    font-size: 24px;
    font-weight: 800;
    border-bottom: 2px solid #eaecef;
    padding-bottom: 10px;
    margin-top: 50px;
    margin-bottom: 25px;
    color: #24292e;
    display: flex;
    align-items: center;
  }
  
  /* 移动端适配 */
  @media (max-width: 768px) {
    .pub-img-col { flex: 0 0 100%; border-right: none; border-bottom: 1px solid #eaecef; height: auto; }
    .pub-card { flex-direction: column; }
    .link-grid { grid-template-columns: repeat(2, 1fr); }
  }
</style>


<!-- ================= BIO SECTION ================= -->
<div style="font-size: 16px; line-height: 1.8; text-align: justify; margin-bottom: 25px; color: #333;">
  <p>
    <strong>Hi, I am Hao Wu.</strong> My research journey begins between 2019 and 2022, focusing on Chinese semantic parsing. During this period, I designed <a href="https://arxiv.org/abs/2403.19936">SLFNet</a> for translating natural language into logical forms. The advent of ChatGPT in 2022 prompted me to explore more challenging fields.
  </p>
  <p>
    In 2023, I pivoted to video prediction, interning at the <a href="#">Tencent Hunyuan Large Model team</a> (2023-2025). I mastered models like ConvLSTM/SimVP and published nearly 30 papers in <strong>ICML, ICLR, and NeurIPS</strong> with top researchers.
  </p>
  <p>
    Currently, I focus on <strong>AI for Earth Sciences (AI4Science)</strong>. I proposed the <a href="#">NMO</a> method and explored distillation techniques (ICCV2025). Recently, I co-developed <a href="https://arxiv.org/abs/2505.19432">TritonCast</a>, an advanced AI model for Earth system forecasting. In 2026, I will continue my Ph.D. studies focusing on video generation and LLM/Agent applications.
  </p>
</div>

<!-- ================= BUTTON GRID ================= -->
<div class="link-grid">
  <a href="mailto:wuhao2022@mail.ustc.edu.cn" class="link-btn">
    ✉️ Email
  </a>
  <a href="YOUR_GOOGLE_SCHOLAR_LINK" class="link-btn">
    🎓 Google Scholar
  </a>
  <a href="YOUR_GITHUB_LINK" class="link-btn">
    🐙 GitHub
  </a>
  <a href="YOUR_SEMANTIC_SCHOLAR_LINK" class="link-btn">
    📚 Semantic Scholar
  </a>
</div>

<!-- ================= NEWS SECTION ================= -->
<h1 class="section-title" id='news'>🔥 News</h1>
<div class="news-scroll">
  <ul>
    <li><strong>2025.11.08</strong>: 2 papers accepted to <strong>AAAI 2026 Main Track</strong>.</li>
    <li><strong>2025.09.18</strong>: 2 papers accepted to <strong>NeurIPS 2025</strong>.</li>
    <li><strong>2025.08.01</strong>: Joined Tencent CSIG (Jarvis Lab) as a research intern.</li>
    <li><strong>2025.06.26</strong>: 1 paper accepted to <strong>ICCV 2025</strong> (Corresponding Author).</li>
    <li><strong>2025.06.18</strong>: Graduated from USTC CS with <strong>Outstanding Graduation Thesis Award</strong> (Top 3).</li>
    <li><strong>2025.05.01</strong>: 1 paper accepted to <strong>ICML 2025</strong> (Co-First Author).</li>
    <li><strong>2025.01.22</strong>: 1 paper accepted to <strong>ICLR 2025</strong> (Corresponding Author).</li>
    <li><strong>2024.11.16</strong>: 1 paper accepted to <strong>KDD 2025 ADS</strong> (First Author).</li>
    <li><strong>2024.01.16</strong>: 1 paper accepted to <strong>ICLR 2024</strong> (<span style="color:#d73a49; font-weight:bold;">Spotlight</span>).</li>
    <li><strong>2022.10.09</strong>: Received <strong>National Scholarship</strong> (Top 0.1%).</li>
  </ul>
</div>

<!-- ================= EXPERIENCE ================= -->
<h1 class="section-title">💼 Research Experience</h1>
<div class="container-box">

  <!-- Item 1 -->
  <div class="exp-item">
    <img src="../images/tencent.png" class="exp-logo" alt="Tencent">
    <div class="exp-content">
      <div class="exp-title">Jarvis Lab, Tencent</div>
      <div class="exp-subtitle">Research Intern &nbsp; | &nbsp; Mentor: <a href="#">Xian Wu</a></div>
      <div class="exp-date">Aug. 2025 - Present</div>
    </div>
  </div>

  <!-- Item 2 -->
  <div class="exp-item">
    <img src="../images/tencent.png" class="exp-logo" alt="Tencent">
    <div class="exp-content">
      <div class="exp-title">Machine Learning Platform Dept., Tencent</div>
      <div class="exp-subtitle">Research Intern (Hunyuan Large Model) &nbsp; | &nbsp; Mentor: <a href="#">Jinbao Xue</a></div>
      <div class="exp-date">Aug. 2023 - Jul. 2025</div>
    </div>
  </div>

  <!-- Item 3 -->
  <div class="exp-item">
    <img src="../images/hkust.png" class="exp-logo" alt="HKUST">
    <div class="exp-content">
      <div class="exp-title">CityMind Lab, HKUST (Guangzhou)</div>
      <div class="exp-subtitle">Research Intern &nbsp; | &nbsp; Advisor: <a href="#">Yuxuan Liang</a></div>
      <div class="exp-date">May 2023 - Aug. 2023</div>
    </div>
  </div>

</div>


<!-- ================= SELECTED PUBLICATIONS (Fixing the Layout) ================= -->
<h1 class="section-title">🌟 Selected Publications</h1>

<!-- Paper 1: NeuralOM -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">AAAI 2026</div>
    <img src="../images/fig_main.jpg" class="pub-img" alt="NeuralOM">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://arxiv.org/abs/2505.21020">NeuralOM: Neural Ocean Model for Subseasonal-to-Seasonal Simulation</a>
    </div>
    <div class="pub-authors">
      Yuan Gao<sup>†</sup>, <strong>Hao Wu</strong><sup>†‡</sup>, Fan Xu, Yanfei Xiang, Ruijian Gou, Ruiqi Shu, Qingsong Wen, Xian Wu, Kun Wang*, Xiaomeng Huang*
    </div>
    <div class="pub-venue">
      AAAI 2026 (CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2505.21020">📄 Paper</a>
      <a href="https://github.com/YuanGao-YG/NeuralOM">💻 Code</a>
      <img src="https://img.shields.io/github/stars/YuanGao-YG/NeuralOM?label=Star&style=social">
    </div>
  </div>
</div>

<!-- Paper 2: OneForecast -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICML 2025</div>
    <img src="../images/one.png" class="pub-img" alt="OneForecast">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://arxiv.org/abs/2502.00338">OneForecast: A Universal Framework for Global and Regional Weather Forecasting</a>
    </div>
    <div class="pub-authors">
      Yuan Gao, <strong>Hao Wu</strong>, Ruiqi Shu, Huanshuo Dong, Fan Xu, Rui Ray Chen, Yibo Yan, Qingsong Wen, Xuming Hu, Kun Wang, Jiahao Wu, Li Qing, Hui Xiong, Xiaomeng Huang#
    </div>
    <div class="pub-venue">
      ICML 2025 (CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2502.00338">📄 Paper</a>
      <a href="https://github.com/YuanGao-YG/OneForecast">💻 Code</a>
    </div>
  </div>
</div>

<!-- Paper 3: ICCV 2025 -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">ICCV 2025</div>
    <img src="../images/iccv2025.png" class="pub-img" alt="ICCV Paper">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="#">Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting</a>
    </div>
    <div class="pub-authors">
      Yuqi Li, Chuanguang Yang, Hansheng Zeng, Zeyu Dong, Zhulin An, Yongjun Xu, Yingli Tian, <strong>Hao Wu#</strong>
    </div>
    <div class="pub-venue">
      ICCV 2025 (CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="#">📄 Paper</a>
      <a href="https://github.com/itsnotacie/SDKD">💻 Code</a>
    </div>
  </div>
</div>

<!-- Paper 4: KDD 2025 -->
<div class="pub-card">
  <div class="pub-img-col">
    <div class="pub-badge">KDD 2025</div>
    <img src="../images/DnyST.png" class="pub-img" alt="DynST">
  </div>
  <div class="pub-content-col">
    <div class="pub-title">
      <a href="https://arxiv.org/abs/2403.02914">DynST: Dynamic Sparse Training for Resource-Constrained Spatio-Temporal Forecasting</a>
    </div>
    <div class="pub-authors">
      <strong>Hao Wu</strong>, Haomin Wen, Guibin Zhang, Yutong Xia, Yuxuan Liang, Yu Zheng, Qingsong Wen, Kun Wang
    </div>
    <div class="pub-venue">
      KDD 2025 (CCF Rank A)
    </div>
    <div class="pub-links">
      <a href="https://arxiv.org/abs/2403.02914">📄 Paper</a>
      <a href="https://github.com/easylearningscores">💻 Code</a>
    </div>
  </div>
</div>


<!-- ================= MISC ================= -->
<h1 class="section-title">💬 Invited Talks</h1>
<ul style="line-height: 1.8; color: #444;">
  <li><em>2024.03</em>, Application and Research of GNN in Meteorological Prediction. @ Sun Yat-sen University</li>
  <li><em>2023.12</em>, Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model. @ AI TIME </li>
</ul>

<h1 class="section-title">💻 Academic Service</h1>
<div style="background: #f9f9f9; padding: 15px; border-radius: 6px; font-size: 15px; color: #444; line-height: 1.6;">
  <strong>Conference Reviewer / PC Member:</strong><br>
  NeurIPS (2023-2025), ICLR (2024-2025), ICML (2024-2025), CVPR (2025), ICCV (2025), AAAI (2025), ACM MM (2024-2025), AISTATS (2025).
</div>

<h1 class="section-title">👨🏻 Miscellaneous</h1>
<ul style="line-height: 1.8; color: #444;">
  <li>🏀 Big fan of basketball. I love Kobe Bryant and his Fadeaway Shot. Also a fan of Stephen Curry.</li>
  <li>👑 Deeply interested in History.</li>
</ul>
