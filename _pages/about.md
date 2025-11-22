---
permalink: /
title: ""
excerpt: "Hao Wu - Research Homepage"
author_profile: false
redirect_from: 
  - /about/
  - /about.html
layout: single
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
  /* 0. 基础重置与高定质感 */
  :root {
    --accent-color: #004080; /* 深邃学术蓝 */
    --text-primary: #1d1d1f;
    --text-secondary: #56565c;
    --bg-card: #ffffff;
    --bg-page: #fafafa;
  }

  /* 隐藏默认侧边栏，聚焦内容 */
  .sidebar { display: none !important; }
  
  .page__content {
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    background-color: var(--bg-page);
  }

  .page__inner-wrap {
    max-width: 1024px !important;
    margin: 0 auto;
    padding: 60px 40px;
    float: none !important;
  }

  /* 1. 字体系统：英文Georgia，中文楷体 */
  body, p, div, span, li, a, strong, b {
    /* 核心修改：英文优先 Georgia，中文回退到楷体 */
    font-family: Georgia, 'Times New Roman', Times, 'KaiTi', 'STKaiti', '华文楷体', serif !important;
    color: var(--text-primary);
    line-height: 1.6; 
  }

  /* 标题保持现代无衬线体，显得更清晰 */
  h1, h2, h3, h4, h5, h6 {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif !important;
    color: #111;
    letter-spacing: -0.02em;
  }

  a { 
    color: var(--accent-color); 
    text-decoration: none; 
    transition: all 0.2s ease; 
  }
  a:hover { 
    color: #00274d; 
    text-decoration: underline; 
  }

  /* 2. 容器与卡片通用样式 */
  .section-title {
    font-size: 28px;
    font-weight: 700;
    margin-top: 60px;
    margin-bottom: 30px;
    color: #000;
    position: relative;
    padding-bottom: 10px;
    border-bottom: 2px solid #eaeaea;
  }

  /* --- BIO 布局 --- */
  .bio-container {
    display: flex;
    justify-content: space-between;
    gap: 60px;
    margin-bottom: 60px;
    align-items: flex-start;
  }

  .bio-text-col { flex: 1; }
  
  .bio-name {
    font-size: 36px;
    font-weight: 700;
    margin-bottom: 10px;
    color: #000;
    /* 名字依然保持无衬线体显得更有力，如果想用楷体去掉下一行即可 */
    font-family: -apple-system, BlinkMacSystemFont, sans-serif !important;
  }
  
  .bio-sub {
    font-size: 18px;
    color: var(--text-secondary);
    margin-bottom: 25px;
  }

  .bio-desc {
    font-size: 17px;
    color: #333;
    text-align: justify;
    line-height: 1.8;
  }

  .bio-photo-col {
    flex: 0 0 240px !important;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .bio-photo {
    width: 200px;
    height: 200px; /* 如果原图不是正方形，建议去掉 height 限制或设为 auto */
    border-radius: 50%; /* 圆形头像 */
    box-shadow: 0 8px 25px rgba(0,0,0,0.1);
    object-fit: cover;
    border: 4px solid #fff;
  }

  /* 按钮链接组 */
  .link-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 30px;
  }
  
  .link-btn {
    display: inline-flex;
    align-items: center;
    padding: 6px 16px;
    background-color: #fff;
    border: 1px solid #d1d5da;
    border-radius: 6px;
    color: #24292e !important;
    font-size: 15px;
    font-weight: 600;
    /* 按钮文字用无衬线体更清晰 */
    font-family: -apple-system, sans-serif !important;
    transition: all 0.2s;
    box-shadow: 0 1px 3px rgba(0,0,0,0.04);
  }
  
  .link-btn svg { margin-right: 6px; fill: #555; }

  .link-btn:hover {
    background-color: #f6f8fa;
    border-color: var(--accent-color);
    color: var(--accent-color) !important;
    text-decoration: none;
  }

  /* --- NEWS SECTION --- */
  .news-wrapper {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #eee;
    padding: 15px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.02);
  }
  
  .news-scroll {
    max-height: 280px;
    overflow-y: auto;
    padding-right: 10px;
  }
  
  .news-scroll ul { padding-left: 20px; margin: 0; }
  .news-scroll li { 
    margin-bottom: 10px; 
    font-size: 16px; 
    color: #444; 
  }
  /* News里的日期保持无衬线体 */
  .news-scroll li strong { color: var(--accent-color); font-family: -apple-system, sans-serif !important; }

  /* --- EXPERIENCE --- */
  .exp-container {
    background: #fff;
    padding: 25px;
    border-radius: 8px;
    border: 1px solid #eee;
  }

  .exp-item {
    display: flex;
    align-items: flex-start;
    margin-bottom: 25px;
    padding-bottom: 25px;
    border-bottom: 1px solid #f0f0f0;
  }
  .exp-item:last-child { border-bottom: none; margin-bottom: 0; padding-bottom: 0; }
  
  .exp-logo {
    width: 60px; 
    height: 60px; 
    margin-right: 25px;
    object-fit: contain;
    border-radius: 8px;
    border: 1px solid #eee;
    padding: 4px;
    background: #fff;
  }
  
  .exp-content { flex: 1; }
  .exp-title { font-weight: bold; font-size: 19px; color: #111; margin-bottom: 4px; font-family: -apple-system, sans-serif !important;}
  .exp-subtitle { font-size: 17px; color: #555; margin-bottom: 4px; font-style: italic; }
  .exp-date { font-size: 15px; color: #888; font-family: -apple-system, sans-serif !important; }

  /* --- PUBLICATIONS (核心修改部分) --- */
  .pub-card {
    display: flex;
    background: #fff;
    border: 1px solid #e1e4e8;
    border-radius: 8px;
    margin-bottom: 30px;
    overflow: hidden;
    transition: box-shadow 0.3s;
  }
  
  .pub-card:hover {
    box-shadow: 0 10px 30px rgba(0,0,0,0.08);
    border-color: #ccc;
  }

  .pub-img-col {
    /* 增加宽度以适应宽图，确保图片不拥挤 */
    flex: 0 0 320px; 
    background: #fff; /* 背景改为白色，适应论文图表 */
    position: relative;
    display: flex;
    align-items: center; /* 垂直居中 */
    justify-content: center; /* 水平居中 */
    border-right: 1px solid #eee;
    padding: 15px; /* 增加内边距，让图片不贴边 */
  }
  
  .pub-img {
    width: 100%;       /* 宽度占满容器 */
    height: auto;      /* 高度自适应，保持比例 */
    object-fit: contain; /* 确保完整显示，不裁剪 */
    display: block;
    max-height: 250px; /* 防止过高 */
  }

  .pub-badge {
    position: absolute;
    top: 10px;
    left: 10px;
    background: #003366;
    color: white;
    padding: 3px 10px;
    font-size: 13px;
    font-weight: bold;
    border-radius: 4px;
    z-index: 2;
    opacity: 0.9;
    font-family: -apple-system, sans-serif !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  }

  .pub-content-col {
    flex: 1;
    padding: 20px 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }

  .pub-title {
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 10px;
    line-height: 1.3;
    color: #000;
  }
  .pub-title a { color: #000; }
  .pub-title a:hover { color: var(--accent-color); text-decoration: underline; }

  .pub-authors {
    font-size: 16px;
    color: #444;
    margin-bottom: 10px;
  }
  .pub-authors strong { color: #000; text-decoration: underline; }

  .pub-venue {
    font-size: 15px;
    color: #c62828;
    margin-bottom: 15px;
    font-weight: bold;
    font-style: italic;
  }

  .pub-links a {
    display: inline-block;
    font-size: 14px;
    font-weight: bold;
    margin-right: 15px;
    color: var(--accent-color);
    text-transform: uppercase;
    font-family: -apple-system, sans-serif !important;
  }
  
  /* --- MISC & SERVICE --- */
  .misc-box {
    background: #fcfcfc;
    padding: 20px;
    border-radius: 6px;
    border: 1px solid #eee;
    font-size: 16px;
  }

  /* 移动端适配 */
  @media (max-width: 850px) {
    .page__inner-wrap { padding: 30px 20px; }
    .bio-container { flex-direction: column-reverse; gap: 30px; text-align: center; }
    .bio-photo-col { width: 100%; margin: 0 auto; }
    .bio-text-col { width: 100%; }
    .link-grid { justify-content: center; }
    
    .pub-card { flex-direction: column; }
    .pub-img-col { flex: 0 0 auto; width: 100%; border-right: none; border-bottom: 1px solid #eee; padding: 0; }
    .pub-img { width: 100%; max-height: none; border-radius: 8px 8px 0 0; }
    .pub-content-col { padding: 20px; }
  }
</style>


<!-- ================= BIO SECTION ================= -->
<div class="bio-container">
  
  <!-- 左侧：文字介绍 -->
  <div class="bio-text-col">
    <div class="bio-name">Hao Wu (吴昊)</div>
    <div class="bio-sub">Ph.D. Student at Department. Computer Science (Incoming year-2026)</div>
    
    <div class="bio-desc">
      <p>
        My research journey began between 2019 and 2022, focusing on natural language understanding and Chinese semantic parsing. During this time, I designed <a href="https://arxiv.org/abs/2403.19936">SLFNet</a> to translate natural language into logical forms. However, the paradigm shift caused by ChatGPT in 2022 inspired me to pivot toward a new and challenging direction.
      </p>
      <p>
        In 2023, I transitioned to video prediction during a two-year internship at the <a href="https://github.com/Alexander-wu/Alexander-wu.github.io/blob/main/images/shixi.pdf">Tencent Hunyuan Large Model team</a>. This experience allowed me to master spatiotemporal modeling. Working alongside top researchers like <a href="https://scholar.google.com/citations?user=P4G6H7oAAAAJ&hl=en">Xingjian Shi</a>, <a href="https://yuxuanliang.com/">Yuxuan Liang</a>, and <a href="https://scholar.google.com/citations?hl=en&user=qfMSkBgAAAAJ&view_op=list_works&sortby=pubdate">Fan Xu</a>, I co-authored nearly 30 papers in top conferences (ICML, ICLR, NeurIPS), laying a solid foundation for freedom research.
      </p>
      <p>
        By late 2024, I applied my deep learning expertise to AI for Science, specifically accelerating partial differential equation (PDE) solving. I proposed <a href="https://dl.acm.org/doi/abs/10.1145/3637528.3671779">NMO</a> using manifold learning for efficiency and explored distillation techniques (@<a href="https://openaccess.thecvf.com/content/ICCV2025/html/Li_Frequency-Aligned_Knowledge_Distillation_for_Lightweight_Spatiotemporal_Forecasting_ICCV_2025_paper.html">ICCV2025</a>) for faster inference. In 2025, I collaborated with <a href="https://yuangao-yg.github.io/">Yuan Gao</a> to develop <a href="https://arxiv.org/abs/2505.19432">TritonCast</a>, an advanced AI model for long-term Earth system forecasting.
      </p>
      <p>
        In 2026, I will return to computer science for my PhD, focusing on video generation and the post-training and application of LLMs, Agents, and VLMs.
      </p>
    </div>

    <!-- 链接按钮 -->
    <div class="link-grid">
      <a href="mailto:wuhao2022@mail.ustc.edu.cn" class="link-btn">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>
        Email
      </a>
      <a href="https://scholar.google.com/citations?user=HdXMhfcAAAAJ&hl=en" class="link-btn">
         <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 24a7 7 0 1 1 0-14 7 7 0 0 1 0 14zm0-24L0 9.5l4.838 3.94A8 8 0 0 1 12 9a8 8 0 0 1 7.162 4.44L24 9.5z"/></svg>
         Google Scholar
      </a>
      
      <a href="https://github.com/Alexander-wu" class="link-btn">
        <svg height="18" viewBox="0 0 16 16" width="18" style="vertical-align: sub;">
           <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
        </svg>
        GitHub
      </a>
      
      <a href="YOUR_SEMANTIC_SCHOLAR_LINK" class="link-btn">
        <svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 2l-5.5 9h11z"/><path d="M12 22l5.5-9h-11z"/></svg>
        Semantic Scholar
      </a>
    </div>
  </div>
  
  <!-- 右侧：头像和邮箱 -->
  <div class="bio-photo-col"> 
    <img src="../images/wuhaodemo" class="bio-photo" alt="Hao Wu">
    <!-- 邮箱地址 -->
    <div style="text-align: center; margin-top: 15px; font-size: 14px; color: #666; font-family: -apple-system, sans-serif;">
      <a href="mailto:wuhao2022@mail.ustc.edu.cn" style="color: #666; text-decoration: none;">
        wuhao2022@mail.ustc.edu.cn
      </a>
    </div>
  </div>

</div>

<!-- ================= NEWS SECTION ================= -->
<h1 class="section-title" id='news'>🔥 News</h1>
<div class="news-wrapper">
  <div class="news-scroll">
    <ul>
      <li><strong>2025.11.08</strong>: 2 papers were accepted to AAAI2026, Main Track.</li>
      <li><strong>2025.09.18</strong>: 2 papers were accepted to NeurIPS2025.</li>
      <li><strong>2025.08.01</strong>: I have joined Tencent CSIG as a research intern @ Tencent Jarvis Research Center.</li>
      <li><strong>2025.06.26</strong>: 1 paper was accepted to ICCV2025 (Corresponding Author).</li>
      <li><strong>2025.06.18</strong>: I have graduated from USTC CS, and received the Outstanding Graduation Thesis award.</li>
      <li><strong>2025.05.01</strong>: 1 paper was accepted to ICML2025 (Co-First Author).</li>
      <li><strong>2025.01.22</strong>: 1 paper was accepted to ICLR2025 (Corresponding Author).</li>
      <li><strong>2024.11.16</strong>: 1 paper was accepted to KDD2025 ADS (First Author).</li>
      <li><strong>2024.09.26</strong>: 3 papers were accepted to NeurIPS2024 (First Author and Two co-author).</li>
      <li><strong>2024.07.16</strong>: 1 paper was accepted to ACM MM2024 (First Author).</li>
      <li><strong>2024.05.17</strong>: 1 paper was accepted to KDD2024 (First Author).</li>
      <li><strong>2024.05.01</strong>: 1 paper was accepted to ICML2024 (First Author).</li>
      <li><strong>2024.02.21</strong>: 1 paper was accepted to TKDE2024 (Co-First Author).</li>
      <li><strong>2024.01.16</strong>: 1 paper was accepted to ICLR2024 (<span style="color:#c62828">Spotlight</span>) (Co-First Author).</li>
      <li><strong>2023.12.09</strong>: 1 paper was accepted to AAAI2024 (First Author).</li>
      <li><strong>2023.09.22</strong>: 1 paper was accepted to NeurIPS2023 (Co-First Author).</li>
      <li><strong>2022.10.09</strong>: National Scholarship, China, 2022 (top 0.1% nation-wide, From USTC).</li>
    </ul>
  </div>
</div>

<!-- ================= EXPERIENCE ================= -->
<h1 class="section-title">💼 Research Experience</h1>
<div class="exp-container">

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


<!-- ================= SELECTED PUBLICATIONS ================= -->
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
      <img src="https://img.shields.io/github/stars/YuanGao-YG/NeuralOM?label=Star&style=social" style="vertical-align:middle; height: 16px;">
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
      <a href="https://openaccess.thecvf.com/content/ICCV2025/html/Li_Frequency-Aligned_Knowledge_Distillation_for_Lightweight_Spatiotemporal_Forecasting_ICCV_2025_paper.html">Frequency-Aligned Knowledge Distillation for Lightweight Spatiotemporal Forecasting</a>
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
<div class="misc-box">
  <ul style="line-height: 1.6; padding-left: 20px;">
    <li><em>2024.03</em>, Application and Research of GNN in Meteorological Prediction. @ Sun Yat-sen University</li>
    <li><em>2023.12</em>, Earthfarseer: versatile spatio-temporal dynamical systems modeling in one model. @ AI TIME </li>
  </ul>
</div>

<h1 class="section-title">💻 Academic Service</h1>
<div class="misc-box" style="background: #fcfcfc;">
  <strong>Conference Reviewer / PC Member:</strong><br>
  NeurIPS (2023-2025), ICLR (2024-2025), ICML (2024-2025), CVPR (2025), ICCV (2025), AAAI (2025), ACM MM (2024-2025), AISTATS (2025).
</div>

<h1 class="section-title">👨🏻 Miscellaneous</h1>
<div class="misc-box">
  <ul style="line-height: 1.6; padding-left: 20px;">
    <li>🏀 Big fan of basketball. I love Kobe Bryant and his Fadeaway Shot. Also a fan of Stephen Curry.</li>
    <li>👑 Deeply interested in History.</li>
  </ul>
</div>
