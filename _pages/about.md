---
permalink: /
title: ""
excerpt: "Hao Wu - Research Homepage"
author_profile: false
layout: single
---

<span class='anchor' id='about-me'></span>

<!-- ================= MINIMALIST ACADEMIC STYLE ================= -->
<style>
  :root {
    --link-color: #0071e3;
    --text-primary: #1d1d1f;
    --text-secondary: #6e6e73;
    --bg-page: #ffffff;
  }

  /* 基础字体设置 */
  body, h1, h2, h3, p, div, span, a, li {
    font-family: Georgia, 'Times New Roman', Times, serif !important;
    color: var(--text-primary);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
  }

  body { 
    background-color: var(--bg-page); 
    margin: 0;
    padding: 0;
  }

  /* 强制隐藏侧边栏并让内容居中，增加两边留白 */
  .sidebar { display: none !important; }
  
  .page {
    width: 100% !important;
    padding-right: 0 !important;
  }

  .page__content {
    float: none !important;
    width: 100% !important;
  }

  /* 核心容器：缩小宽度至 800px 以增加两边留白 */
  .page__inner-wrap { 
    max-width: 800px !important; 
    margin-left: auto !important; 
    margin-right: auto !important; 
    padding: 80px 50px !important; 
    background-color: #fff;
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
    .page__inner-wrap { padding: 40px 20px !important; }
    .profile-header { flex-direction: column; text-align: center; align-items: center; }
    .exp-row { flex-direction: column; margin-bottom: 20px; }
    .exp-date { margin-left: 0; }
  }
</style>

<!-- ================= HEADER ================= -->
<div class="profile-header">
  <img src="../images/wuhaodemo" class="profile-photo" alt="Hao Wu">
  <div class="profile-info">
    <div class="name">Hao Wu (吴昊)</div>
    <div class="affiliation">School of Computer Science, Carnegie Mellon University</div>
    
    <div class="contact-info">
      <div style="margin-bottom: 10px;">
        <span class="email-text">Email: hw5@andrew.cmu.edu</span>
      </div>
      <a href="https://scholar.google.com/citations?user=HdXMhfcAAAAJ">Google Scholar</a>
      <a href="https://github.com/Alexander-wu">GitHub</a>
    </div>
  </div>
</div>

<!-- ================= BIOGRAPHY ================= -->
<div class="section-title">Biography</div>
<div class="bio-text">
  Following my doctoral research at <b>Tsinghua University</b>, I am about to embark on a new research journey and life at the <b>School of Computer Science, Carnegie Mellon University (CMU)</b>. 
</div>
<div class="bio-text">
  My previous work was rooted in <b>Scientific Computing (AI for Science)</b>, particularly in deep learning for physical simulations. Currently, I am transitioning my research focus toward <b>LLM Post-training</b> and the development of <b>Autonomous Agents</b> in scientific domains.
</div>

<!-- ================= EXPERIENCE ================= -->
<div class="section-title">Experience</div>

<div class="exp-row">
  <span><b>Tsinghua University</b>, Doctoral Student</span>
  <span class="exp-date">Prior to 2026</span>
</div>

<div class="exp-row">
  <span><b>Tencent</b>, Hunyuan Large Model Team, Research Intern</span>
  <span class="exp-date">2023 – 2025</span>
</div>

<div class="exp-row">
  <span><b>HKUST (GZ)</b>, CityMind Lab, Research Intern</span>
  <span class="exp-date">2023</span>
</div>

<div class="exp-row">
  <span><b>USTC</b>, B.S. in Computer Science</span>
  <span class="exp-date">Graduated 2025</span>
</div>

<!-- ================= SERVICE ================= -->
<div class="section-title">Academic Service</div>
<div class="bio-text" style="color: var(--text-secondary); font-size: 16px;">
  Reviewer for NeurIPS (2023-2025), ICLR (2024-2025), ICML (2024-2025), CVPR, ICCV, AAAI, and ACM MM.
</div>

<footer style="margin-top: 100px; font-size: 13px; color: #bbb; text-align: center; border-top: 1px solid #fcfcfc; padding-top: 20px;">
  Last updated: January 2026
</footer>
