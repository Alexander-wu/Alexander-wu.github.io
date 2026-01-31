---
permalink: /
title: ""
excerpt: "Hao Wu - Research Homepage"
author_profile: false
layout: single
---

<span class='anchor' id='about-me'></span>

<style>
  /* 1. 强制重置布局，解决两边没有留白的问题 */
  /* 隐藏所有侧边栏 */
  .sidebar, .page__sidebar, .sidebar__right {
    display: none !important;
    width: 0 !important;
    height: 0 !important;
  }

  /* 强制父容器全宽，去掉干扰 */
  body, .page, .page__content, .archive, .page__inner-wrap {
    width: 100% !important;
    max-width: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    float: none !important;
    background-color: #ffffff !important; /* 确保背景纯白 */
  }

  /* 2. 定义核心内容区域，制造两边的大面积留白 */
  .main-container {
    max-width: 720px !important; /* 限制内容宽度，两边自然留白 */
    margin: 0 auto !important;   /* 绝对居中 */
    padding-top: 80px;
    padding-bottom: 100px;
    padding-left: 20px;
    padding-right: 20px;
  }

  /* 3. 字体与样式 */
  :root {
    --link-color: #0071e3;
    --text-primary: #1d1d1f;
    --text-secondary: #6e6e73;
  }

  body, h1, h2, h3, p, div, span, a, li {
    font-family: Georgia, 'Times New Roman', Times, serif !important;
    color: var(--text-primary);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  /* Header Section */
  .profile-header { display: flex; gap: 50px; margin-bottom: 40px; align-items: flex-start; }
  .profile-photo { width: 170px; height: 170px; border-radius: 4px; object-fit: cover; box-shadow: 0 4px 20px rgba(0,0,0,0.05); }
  .profile-info { flex: 1; }
  .name { font-size: 36px; font-weight: 700; margin-bottom: 10px; color: #000; letter-spacing: -0.5px; }
  .affiliation { font-size: 20px; color: #333; margin-bottom: 15px; font-style: italic; }
  
  /* Links & Email */
  .contact-info { margin-bottom: 20px; font-size: 17px; }
  .contact-info a { color: var(--link-color); text-decoration: none; margin-right: 20px; }
  .contact-info a:hover { text-decoration: underline; }
  .email-text { color: var(--text-secondary); font-family: monospace !important; font-size: 16px; }

  /* Content Sections */
  .section-title { 
    font-size: 22px; 
    font-weight: 700; 
    margin-top: 50px; 
    margin-bottom: 15px; 
    border-bottom: 1px solid #eee; 
    padding-bottom: 8px; 
    text-transform: uppercase;
    letter-spacing: 1px;
  }
  .bio-text { font-size: 18px; margin-bottom: 20px; text-align: justify; }

  /* Experience List */
  .exp-row { display: flex; justify-content: space-between; margin-bottom: 12px; font-size: 18px; }
  .exp-date { color: var(--text-secondary); font-style: italic; white-space: nowrap; margin-left: 20px; }

  @media (max-width: 700px) {
    .profile-header { flex-direction: column; text-align: center; align-items: center; }
    .exp-row { flex-direction: column; margin-bottom: 20px; }
    .exp-date { margin-left: 0; }
  }
</style>

<!-- ================= MAIN CONTENT WRAPPER ================= -->
<div class="main-container">

  <!-- HEADER -->
  <div class="profile-header">
    <img src="../images/wuhaodemo" class="profile-photo" alt="Hao Wu">
    <div class="profile-info">
      <div class="name">Hao Wu (吴昊)</div>
<div class="affiliation" style="font-size: 0.98em;">
    School of Computer Science, Carnegie Mellon University
</div>      
      <div class="contact-info">
        <div style="margin-bottom: 10px;">
          <span class="email-text">Email: hw5@andrew.cmu.edu</span>
        </div>
        <a href="https://scholar.google.com/citations?user=HdXMhfcAAAAJ">Google Scholar</a>
        <a href="https://github.com/Alexander-wu">GitHub</a>
      </div>
    </div>
  </div>

  <!-- BIOGRAPHY (完全保留原话) -->
  <div class="section-title">Biography</div>
  <div class="bio-text">
    I am about to embark on a new research journey and life at the School of Computer Science, Carnegie Mellon University (CMU).
  </div>
  <div class="bio-text">
    My previous work was rooted in Scientific Computing (AI for Science), particularly in deep learning for physical simulations. Currently, I am transitioning my research focus toward LLM Post-training and the development of Autonomous Agents in scientific domains.
  </div>

  <!-- EXPERIENCE -->
  <div class="section-title">Experience</div>

  <div class="exp-row">
    <span><b>Tencent</b>, Hunyuan Large Model Team, Research Intern</span>
    <span class="exp-date">2023 – 2025</span>
  </div>

  <div class="exp-row">
    <span><b>HKUST (GZ)</b>, CityMind Lab, Research Intern</span>
    <span class="exp-date">2023</span>
  </div>

  <div class="exp-row">
    <span><b>USTC</b>, in Computer Science</span>
    <span class="exp-date">Graduated 2025</span>
  </div>

  <!-- SERVICE -->
  <div class="section-title">Academic Service</div>
  <div class="bio-text" style="color: var(--text-secondary); font-size: 16px;">
    Reviewer for NeurIPS (2023-2025), ICLR (2024-2025), ICML (2024-2025), CVPR, ICCV, AAAI, and ACM MM.
  </div>

  <footer style="margin-top: 100px; font-size: 13px; color: #bbb; text-align: center; border-top: 1px solid #fcfcfc; padding-top: 20px;">
    Last updated: January 2026
  </footer>

</div>
