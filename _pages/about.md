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
  /* 强制全局新罗马字体，提升学术感 */
  body, h1, h2, h3, h4, h5, h6, p, div, span, li, a, button {
    font-family: 'Times New Roman', Times, serif !important;
  }

  /* 链接颜色：深学术蓝 */
  a { color: #003366; text-decoration: none; }
  a:hover { text-decoration: underline; }

  /* 容器通用样式 */
  .container-box {
    background: #fff;
    padding: 15px;
    margin-bottom: 20px;
    border-radius: 8px;
    /* 增加一点微弱的阴影增加立体感 */
    box-shadow: 0 2px 5px rgba(0,0,0,0.03);
    border: 1px solid #f0f0f0;
  }

  /* 头部按钮网格 */
  .link-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 10px;
    margin-top: 15px;
    margin-bottom: 25px;
  }
  
  .link-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 8px 15px;
    background-color: #fff;
    border: 1px solid #e0e0e0;
    border-radius: 6px;
    color: #333 !important;
    font-size: 15px;
    font-weight: bold;
    transition: all 0.2s ease;
    text-decoration: none !important;
  }
  
  .link-btn:hover {
    background-color: #f9f9f9;
    border-color: #999;
    transform: translateY(-1px);
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
  }

  /* 双栏布局 (Education & Experience) */
  .split-layout {
    display: flex;
    flex-wrap: wrap;
    gap: 25px;
    margin-top: 20px;
  }
  
  .split-col {
    flex: 1;
    min-width: 300px; /* 移动端自动换行 */
  }

  /* 列表项样式 */
  .info-item {
    display: flex;
    margin-bottom: 15px;
    align-items: flex-start;
  }
  
  .info-logo {
    width: 45px; 
    height: 45px; 
    margin-right: 15px;
    object-fit: contain;
    border-radius: 4px;
  }
  
  .info-content {
    flex: 1;
  }
  
  .info-title {
    font-weight: bold;
    font-size: 16px;
    color: #000;
    margin-bottom: 2px;
  }
  
  .info-subtitle {
    font-size: 14px;
    color: #444;
    margin-bottom: 2px;
  }
  
  .info-date {
    font-size: 13px;
    color: #888;
    font-style: italic;
    float: right; /* 日期右对齐 */
  }

  /* News 滚动区域 */
  .news-scroll {
    max-height: 240px;
    overflow-y: auto;
    background-color: #fafafa;
    padding: 15px;
    border-radius: 6px;
    border: 1px solid #eee;
  }
  .news-scroll ul { padding-left: 20px; margin: 0; }
  .news-scroll li { margin-bottom: 8px; font-size: 15px; color: #333; }

  /* 论文列表样式优化 */
  .paper-badge {
    background-color: #003366; 
    color: white; 
    padding: 1px 6px; 
    font-size: 12px; 
    border-radius: 3px;
    vertical-align: middle;
    margin-right: 5px;
  }
  
  /* 标题样式 */
  h1.section-title {
    font-size: 22px;
    border-bottom: 2px solid #f2f2f2;
    padding-bottom: 10px;
    margin-top: 40px;
    margin-bottom: 20px;
    color: #111;
  }
  
  .icon-header { display: flex; align-items: center; gap: 10px; }
</style>


<!-- ================= BIO SECTION ================= -->
<div style="font-size: 17px; line-height: 1.7; text-align: justify; margin-bottom: 20px;">
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

<!-- ================= BUTTON GRID (Style Reference) ================= -->
<!-- 请在此处替换为您真实的链接 -->
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

<!-- ================= SPLIT LAYOUT: EDUCATION & EXPERIENCE ================= -->
<!-- 这里复刻参考图的双栏布局 -->

<div class="split-layout">
  
  <!-- LEFT COLUMN: EDUCATION -->
  <div class="split-col">
    <h3 class="icon-header">🎓 Education</h3>
    <div class="container-box">
      
      <!-- Ph.D. (Future) -->
      <div class="info-item">
        <!-- 请替换为学校 Logo -->
        <img src="../images/hkust.png" class="info-logo" alt="Logo"> 
        <div class="info-content">
          <div class="info-title">University of Science and Technology of China</div>
          <div class="info-subtitle">Ph.D. Student in Computer Science (Incoming)</div>
          <div class="info-date">Starting 2026</div>
        </div>
      </div>

      <!-- Master -->
      <div class="info-item">
        <img src="../images/hkust.png" class="info-logo" alt="Logo">
        <div class="info-content">
          <div class="info-title">University of Science and Technology of China</div>
          <div class="info-subtitle">M.Phil. in Computer Science</div>
          <div class="info-date">2022 - 2025</div>
        </div>
      </div>

      <!-- Bachelor -->
      <div class="info-item">
        <img src="../images/hkust.png" class="info-logo" alt="Logo">
        <div class="info-content">
          <div class="info-title">University of Science and Technology of China</div>
          <div class="info-subtitle">B.Eng. in Computer Science</div>
          <div class="info-date">2018 - 2022</div>
        </div>
      </div>

    </div>
  </div>

  <!-- RIGHT COLUMN: EXPERIENCE -->
  <div class="split-col">
    <h3 class="icon-header">💼 Experience</h3>
    <div class="container-box">

      <!-- Tencent Jarvis -->
      <div class="info-item">
        <img src="../images/tencent.png" class="info-logo" alt="Tencent">
        <div class="info-content">
          <div class="info-title">Jarvis Lab, Tencent</div>
          <div class="info-subtitle">Research Intern (Mentor: Xian Wu)</div>
          <div class="info-date">Aug. 2025 - Present</div>
        </div>
      </div>

      <!-- Tencent Hunyuan -->
      <div class="info-item">
        <img src="../images/tencent.png" class="info-logo" alt="Tencent">
        <div class="info-content">
          <div class="info-title">Hunyuan Large Model Team, Tencent</div>
          <div class="info-subtitle">Research Intern (Mentor: Jinbao Xue)</div>
          <div class="info-date">Aug. 2023 - Jul. 2025</div>
        </div>
      </div>

      <!-- HKUST(GZ) -->
      <div class="info-item">
        <img src="../images/hkust.png" class="info-logo" alt="HKUST">
        <div class="info-content">
          <div class="info-title">CityMind Lab, HKUST(GZ)</div>
          <div class="info-subtitle">Research Intern (Advisor: Yuxuan Liang)</div>
          <div class="info-date">May 2023 - Aug. 2023</div>
        </div>
      </div>

    </div>
  </div>
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
    <li><strong>2024.01.16</strong>: 1 paper accepted to <strong>ICLR 2024</strong> (<span style="color:#c62828">Spotlight</span>).</li>
    <li><strong>2022.10.09</strong>: Received <strong>National Scholarship</strong> (Top 0.1%).</li>
  </ul>
</div>


<!-- ================= SELECTED PAPERS (Thumbnails) ================= -->
<h1 class="section-title">🌟 Selected Publications</h1>

<div class='paper-box' style="margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #eee;">
  <div class='paper-box-image'>
    <div>
      <div class="badge">AAAI 2026</div>
      <img src='../images/fig_main.jpg' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
    [NeuralOM: Neural Ocean Model for Subseasonal-to-Seasonal Simulation](https://arxiv.org/abs/2505.21020)
    <br>
    Yuan Gao<sup>†</sup>, **Hao Wu**<sup>†</sup> <sup>‡ </sup>, Fan Xu, et al.
    <br>
    <span style="color:#c62828; font-style: italic;">(AAAI 2026, CCF Rank A)</span>
    <br>
    <a href="https://arxiv.org/abs/2505.21020" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/NeuralOM" target="_blank">Code</a>
    <img src="https://img.shields.io/github/stars/YuanGao-YG/NeuralOM?label=%F0%9F%8C%9F%20Star&color=blue" style="vertical-align: middle;">
  </div>
</div>

<div class='paper-box' style="margin-bottom: 20px; padding-bottom: 20px; border-bottom: 1px solid #eee;">
  <div class='paper-box-image'>
    <div>
      <div class="badge">ICML 2025</div>
      <img src='../images/one.png' alt="sym" width="100%">
    </div>
  </div>
  <div class='paper-box-text' markdown="1">
    [OneForecast: A Universal Framework for Global and Regional Weather Forecasting](https://arxiv.org/abs/2502.00338)
    <br>
    Yuan Gao, Hao Wu, et al.
    <br>
    <span style="color:#c62828; font-style: italic;">(ICML 2025, CCF Rank A)</span>
    <br>
    <a href="https://arxiv.org/abs/2502.00338" target="_blank">Paper</a> | <a href="https://github.com/YuanGao-YG/OneForecast" target="_blank">Code</a>
  </div>
</div>


<!-- ================= MISC ================= -->
<h1 class="section-title">💬 Invited Talks</h1>
<ul>
  <li><em>2024.03</em>, Application and Research of GNN in Meteorological Prediction. @ Sun Yat-sen University</li>
  <li><em>2023.12</em>, Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model. @ AI TIME </li>
</ul>

<h1 class="section-title">👨🏻 Miscellaneous</h1>
<ul>
  <li>🏀 Big fan of basketball (Kobe & Curry).</li>
  <li>👑 Interested in History.</li>
</ul>
