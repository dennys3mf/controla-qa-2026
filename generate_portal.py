import os

html_code = """<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Controla.pe • Informe QA Profesional | Plaeis Entertainment</title>
  
  <style>
    /* ── E-UKRAINE FONTS ── */
    @font-face {
      font-family: 'e-Ukraine';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-Ukraine-Regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'e-Ukraine';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-Ukraine-Medium.woff2') format('woff2');
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'e-Ukraine';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-Ukraine-Bold.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'e-UkraineHead';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-UkraineHead-Regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'e-UkraineHead';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-UkraineHead-Medium.woff2') format('woff2');
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }
    @font-face {
      font-family: 'e-UkraineHead';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-UkraineHead-Bold.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }

    :root {
      --primary: #1B59F8;
      --primary-light: #EFF6FF;
      --primary-dark: #1040C0;
      --success: #10B981;
      --success-light: #ECFDF5;
      --danger: #EF4444;
      --danger-light: #FEE8E1;
      --warning: #F59E0B;
      --warning-light: #FEF3C7;
      --cyan: #2294E3;
      --cyan-light: #E0F2FE;
      --bg: #F4F6F9;
      --surface: #FFFFFF;
      --border: #E5E7EB;
      --text: #0F172A;
      --text-muted: #64748B;
      --radius-card: 28px;
      --radius-pill: 999px;
      --radius-badge: 12px;
      --shadow-card: 0 4px 24px rgba(0,0,0,0.03), 0 1px 3px rgba(0,0,0,0.02);
      --shadow-hover: 0 12px 36px rgba(0,0,0,0.08);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--bg);
      color: var(--text);
      font-family: 'e-Ukraine', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 100px;
    }

    /* ── TOPBAR ── */
    .topbar {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 40px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .topbar-inner {
      max-width: 1400px;
      margin: 0 auto;
      height: 64px;
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .brand-logo-img { height: 28px; width: auto; }
    .brand-divider { width: 1px; height: 20px; background: var(--border); }
    .brand-badge {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      background: var(--primary-light);
      color: var(--primary);
      padding: 3px 10px;
      border-radius: 6px;
    }

    /* ── HERO ── */
    .hero {
      background: linear-gradient(135deg, #1B59F8 0%, #0D3DB0 100%);
      padding: 44px 40px 38px;
    }
    .hero-inner { max-width: 1400px; margin: 0 auto; }
    .hero-eyebrow {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 1.2px;
      color: rgba(255,255,255,0.7);
      text-transform: uppercase;
      margin-bottom: 8px;
    }
    .hero h1 {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 32px;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.5px;
      line-height: 1.2;
    }
    .hero-stats {
      display: flex;
      gap: 36px;
      margin-top: 28px;
      flex-wrap: wrap;
    }
    .hero-stat-val {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 34px;
      font-weight: 700;
      color: #fff;
      line-height: 1;
    }
    .hero-stat-label {
      font-size: 12px;
      color: rgba(255,255,255,0.7);
      margin-top: 4px;
    }
    .hero-stat-divider { width: 1px; background: rgba(255,255,255,0.2); }

    /* ── NAV TABS ── */
    .nav-wrap {
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 40px;
    }
    .nav-bar {
      max-width: 1400px;
      margin: 0 auto;
      display: flex;
      gap: 8px;
    }
    .nav-tab {
      font-family: 'e-UkraineHead', sans-serif;
      padding: 16px 22px;
      background: none;
      border: none;
      border-bottom: 2px solid transparent;
      margin-bottom: -1px;
      font-size: 14px;
      font-weight: 700;
      color: var(--text-muted);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 8px;
      transition: color 0.15s;
      white-space: nowrap;
    }
    .nav-tab:hover { color: var(--primary); }
    .nav-tab.active { color: var(--primary); border-bottom-color: var(--primary); }

    /* ── CONTAINER ── */
    .container {
      max-width: 1400px;
      margin: 0 auto;
      padding: 36px 40px 0;
    }
    .pane { display: none; }
    .pane.active { display: block; animation: fadeIn 0.18s ease-out; }
    @keyframes fadeIn { from { opacity: 0; transform: translateY(6px); } to { opacity: 1; transform: translateY(0); } }

    /* ── DIIA DEFECT CARD DESIGN ── */
    .qa-card {
      background: var(--surface);
      border: 1px solid #ECEFF3;
      border-radius: var(--radius-card);
      box-shadow: var(--shadow-card);
      padding: 36px 40px;
      margin-bottom: 28px;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .qa-card:hover {
      box-shadow: var(--shadow-hover);
    }
    .qa-card-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #EFEFEF;
      padding-bottom: 24px;
      margin-bottom: 28px;
      flex-wrap: wrap;
      gap: 16px;
    }
    .qa-card-title-group {
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }
    .qa-id-badge {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #000000;
      background: #FEE8E1;
      padding: 8px 18px;
      border-radius: var(--radius-badge);
      letter-spacing: -0.2px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
    }
    .qa-id-badge.badge-obs { background: #FEF3C7; color: #92400E; }
    .qa-id-badge.badge-info { background: #E0F2FE; color: #075985; }

    .qa-card-title {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #000000;
      letter-spacing: -0.4px;
    }
    .qa-card-meta-group {
      display: flex;
      align-items: center;
      gap: 14px;
      flex-wrap: wrap;
    }
    .qa-meta-pill {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 13px;
      font-weight: 600;
      color: #000000;
      background: #FEE8E1;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }
    .qa-meta-pill.pill-obs { background: #FEF3C7; color: #92400E; }
    .qa-meta-pill.pill-info { background: #E0F2FE; color: #075985; }
    .qa-meta-divider { width: 1px; height: 20px; background: #D1D5DB; }
    .qa-module-badge {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 14px;
      font-weight: 700;
      color: #000000;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }

    .qa-card-body {
      display: grid;
      grid-template-columns: 1fr 1.25fr;
      gap: 40px;
      align-items: start;
    }
    @media (max-width: 980px) {
      .qa-card-body { grid-template-columns: 1fr; gap: 28px; }
    }
    .qa-col-left { display: flex; flex-direction: column; }
    .qa-section-label {
      font-family: 'e-Ukraine', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: #71717A;
      margin-bottom: 14px;
    }
    .qa-problem-statement {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 21px;
      font-weight: 700;
      color: #000000;
      line-height: 1.34;
      letter-spacing: -0.2px;
      margin-bottom: 28px;
    }

    .qa-accordion {
      border-top: 1px solid #ECEFF3;
      margin-top: auto;
    }
    .qa-accordion-trigger {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 16px 0;
      cursor: pointer;
      user-select: none;
    }
    .qa-accordion-title {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: #000000;
    }
    .qa-accordion-icon {
      transition: transform 0.25s ease;
      color: #000000;
      flex-shrink: 0;
    }
    .qa-accordion-trigger.open .qa-accordion-icon {
      transform: rotate(180deg);
    }
    .qa-accordion-content {
      display: none;
      padding-bottom: 16px;
      font-family: 'e-Ukraine', sans-serif;
      font-size: 14px;
      line-height: 1.6;
      color: #475569;
    }
    .qa-accordion-content.open {
      display: block;
      animation: fadeIn 0.2s ease-out;
    }

    .qa-col-right { display: flex; flex-direction: column; }
    .qa-evidence-box {
      border: 1px solid #E2E8F0;
      border-radius: 20px;
      overflow: hidden;
      background: #F8FAFC;
      cursor: pointer;
      position: relative;
      transition: transform 0.2s, box-shadow 0.2s;
    }
    .qa-evidence-box:hover {
      transform: scale(1.01);
      box-shadow: 0 8px 24px rgba(0,0,0,0.06);
    }
    .qa-evidence-img {
      width: 100%;
      height: 260px;
      object-fit: cover;
      display: block;
    }

    /* ══════════════════════════════════════════════════════════════ */
    /* ── EXCEL SPREADSHEET STYLE FOR MATRIZ DE CASOS DE PRUEBA ── */
    /* ══════════════════════════════════════════════════════════════ */
    .excel-container {
      background: #FFFFFF;
      border: 1px solid #D1D5DB;
      border-radius: 20px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
      overflow: hidden;
      margin-bottom: 40px;
    }

    /* Spreadsheet Toolbar */
    .excel-toolbar {
      background: #F8FAFC;
      border-bottom: 1px solid #E2E8F0;
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }
    .excel-title-group {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .excel-sheet-icon {
      width: 32px;
      height: 32px;
      background: #107C41; /* Excel green */
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-family: 'e-UkraineHead', sans-serif;
      font-weight: 700;
      font-size: 16px;
      box-shadow: 0 2px 6px rgba(16,124,65,0.25);
    }
    .excel-title {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 18px;
      font-weight: 700;
      color: #0F172A;
    }
    .excel-subtitle {
      font-size: 12px;
      color: #64748B;
    }

    .excel-controls {
      display: flex;
      align-items: center;
      gap: 12px;
      flex-wrap: wrap;
    }
    .excel-search-input {
      font-family: 'e-Ukraine', sans-serif;
      font-size: 13px;
      padding: 8px 16px;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      outline: none;
      width: 260px;
      background: #FFFFFF;
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .excel-search-input:focus {
      border-color: #1B59F8;
      box-shadow: 0 0 0 3px rgba(27,89,248,0.12);
    }

    .excel-filters {
      display: flex;
      gap: 6px;
      flex-wrap: wrap;
    }
    .excel-fpill {
      font-family: 'e-UkraineHead', sans-serif;
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 12px;
      font-weight: 700;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s;
    }
    .excel-fpill:hover {
      background: #F1F5F9;
      color: #0F172A;
    }
    .excel-fpill.active {
      background: #0F172A;
      color: #FFFFFF;
      border-color: #0F172A;
    }

    /* Spreadsheet Table Grid */
    .excel-table-wrap {
      overflow-x: auto;
      background: #FFFFFF;
    }
    .excel-table {
      width: 100%;
      border-collapse: collapse;
      font-family: 'e-Ukraine', sans-serif;
      font-size: 13px;
      color: #0F172A;
      text-align: left;
    }
    .excel-table th {
      background: #F1F5F9;
      color: #334155;
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.5px;
      padding: 12px 14px;
      border-right: 1px solid #CBD5E1;
      border-bottom: 2px solid #CBD5E1;
      white-space: nowrap;
      user-select: none;
    }
    .excel-table th:last-child {
      border-right: none;
    }
    .excel-table td {
      padding: 13px 14px;
      border-right: 1px solid #E2E8F0;
      border-bottom: 1px solid #E2E8F0;
      vertical-align: top;
      line-height: 1.45;
    }
    .excel-table td:last-child {
      border-right: none;
    }
    .excel-table tbody tr:nth-child(even) {
      background: #FAFBFD;
    }
    .excel-table tbody tr:hover {
      background: #EFF6FF !important;
    }

    /* Spreadsheet Cell Badges */
    .excel-id {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 12.5px;
      font-weight: 700;
      color: #1B59F8;
      background: #EFF6FF;
      padding: 4px 8px;
      border-radius: 6px;
      display: inline-block;
      white-space: nowrap;
    }
    .excel-badge-status {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
    }
    .excel-status-pass {
      background: #DCFCE7;
      color: #166534;
      border: 1px solid #BBF7D0;
    }
    .excel-status-fail {
      background: #FEE8E1;
      color: #991B1B;
      border: 1px solid #FECACA;
    }
    .excel-status-obs {
      background: #FEF3C7;
      color: #92400E;
      border: 1px solid #FDE68A;
    }

    .excel-type-tag {
      font-size: 11px;
      font-weight: 600;
      background: #F1F5F9;
      color: #475569;
      padding: 3px 8px;
      border-radius: 4px;
      display: inline-block;
      white-space: nowrap;
    }

    .excel-defect-link {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      background: #FEE8E1;
      color: #DC2626;
      padding: 3px 8px;
      border-radius: 6px;
      display: inline-block;
      white-space: nowrap;
    }
    .excel-obs-link {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      background: #FEF3C7;
      color: #D97706;
      padding: 3px 8px;
      border-radius: 6px;
      display: inline-block;
      white-space: nowrap;
    }

    .excel-btn-ev {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      background: #FFFFFF;
      color: #1B59F8;
      border: 1px solid #CBD5E1;
      padding: 5px 10px;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 5px;
      white-space: nowrap;
      transition: all 0.15s;
    }
    .excel-btn-ev:hover {
      background: #1B59F8;
      color: #FFFFFF;
      border-color: #1B59F8;
    }

    /* Spreadsheet Footer / Status Bar */
    .excel-statusbar {
      background: #F8FAFC;
      border-top: 1px solid #E2E8F0;
      padding: 10px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 11.5px;
      color: #64748B;
      flex-wrap: wrap;
      gap: 12px;
    }
    .excel-statusbar-left {
      display: flex;
      align-items: center;
      gap: 16px;
    }
    .excel-statusbar-right {
      display: flex;
      align-items: center;
      gap: 16px;
      font-family: 'e-UkraineHead', sans-serif;
      font-weight: 600;
    }

    /* ── MODAL ── */
    .modal-overlay {
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15,23,42,0.8);
      backdrop-filter: blur(8px);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      padding: 24px;
    }
    .modal-overlay.active { display: flex; }
    .modal-card {
      background: #fff;
      border-radius: 24px;
      max-width: 1200px;
      width: 100%;
      max-height: 92vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 24px 60px rgba(0,0,0,0.3);
    }
    .modal-hd {
      padding: 20px 28px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid var(--border);
    }
    .modal-hd h3 {
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: #000000;
    }
    .modal-close {
      background: #F1F5F9;
      border: none;
      width: 34px;
      height: 34px;
      border-radius: 50%;
      font-size: 18px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-muted);
    }
    .modal-close:hover { background: #FEE2E2; color: #DC2626; }
    .modal-body { padding: 24px 28px; overflow: auto; text-align: center; }
    .modal-body img { max-width: 100%; max-height: 74vh; border-radius: 12px; }
  </style>
</head>
<body>

<!-- TOPBAR -->
<header class="topbar">
  <div class="topbar-inner">
    <img src="assets/logo_controla.png" alt="Controla" class="brand-logo-img">
    <div class="brand-divider"></div>
    <span class="brand-badge">QA REPORT</span>
  </div>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <div class="hero-eyebrow">Plaeis Entertainment • plaeis.controla.pe</div>
    <h1>Informe de Calidad Funcional &amp; Defectos</h1>
    <div class="hero-stats">
      <div class="hero-stat">
        <div class="hero-stat-val">11</div>
        <div class="hero-stat-label">Casos de prueba</div>
      </div>
      <div class="hero-stat-divider"></div>
      <div class="hero-stat">
        <div class="hero-stat-val" style="color:#6EE7B7;">8</div>
        <div class="hero-stat-label">Aprobados</div>
      </div>
      <div class="hero-stat-divider"></div>
      <div class="hero-stat">
        <div class="hero-stat-val" style="color:#FCA5A5;">3</div>
        <div class="hero-stat-label">Defectos</div>
      </div>
      <div class="hero-stat-divider"></div>
      <div class="hero-stat">
        <div class="hero-stat-val" style="color:#FCD34D;">3</div>
        <div class="hero-stat-label">Observaciones</div>
      </div>
    </div>
  </div>
</section>

<!-- NAV TABS -->
<div class="nav-wrap">
  <nav class="nav-bar">
    <button class="nav-tab active" onclick="switchTab('defectos', event)">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
      Registro de Defectos
    </button>
    <button class="nav-tab" onclick="switchTab('matriz', event)">
      <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3h18v18H3zM3 9h18M3 15h18M9 3v18M15 3v18"/></svg>
      Matriz de Casos de Prueba (Tabla Excel)
    </button>
  </nav>
</div>

<main class="container">

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- TAB 1: REGISTRO DE DEFECTOS (DISEÑO DIIA EXACTO A LA IMAGEN) -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <div id="tab-defectos" class="pane active">

    <!-- DEF-01 -->
    <div class="qa-card">
      <div class="qa-card-header">
        <div class="qa-card-title-group">
          <span class="qa-id-badge">DEF-01</span>
          <h2 class="qa-card-title">Solapamiento en Highcharts</h2>
        </div>
        <div class="qa-card-meta-group">
          <span class="qa-meta-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
            S3 • Media
          </span>
          <div class="qa-meta-divider"></div>
          <span class="qa-module-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>
            Dashboard
          </span>
        </div>
      </div>
      <div class="qa-card-body">
        <div class="qa-col-left">
          <div class="qa-section-label">QUÉ SUCEDE</div>
          <div class="qa-problem-statement">
            Las leyendas de los gráficos superiores invaden los títulos de “Usuarios por Estado” y “Usuarios por Rol”.
          </div>
          <div class="qa-accordion">
            <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-def-01', this)">
              <span class="qa-accordion-title">Causa técnica</span>
              <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
            </div>
            <div id="cause-def-01" class="qa-accordion-content">
              El contenedor de Highcharts carece de <code>overflow: hidden</code> y de margen inferior suficiente (<code>padding-bottom</code>) para alojar las etiquetas flotantes generadas por la serie de datos en pantalla de escritorio.
            </div>
          </div>
        </div>
        <div class="qa-col-right">
          <div class="qa-section-label">EVIDENCIA</div>
          <div class="qa-evidence-box" onclick="openModal('evidencias/DEF-01_solapamiento_leyendas_dashboard.png','DEF-01: Solapamiento visual de leyendas Highcharts')">
            <img class="qa-evidence-img" src="evidencias/DEF-01_solapamiento_leyendas_dashboard.png" alt="DEF-01 Evidencia">
          </div>
        </div>
      </div>
    </div>

    <!-- DEF-02 -->
    <div class="qa-card">
      <div class="qa-card-header">
        <div class="qa-card-title-group">
          <span class="qa-id-badge">DEF-02</span>
          <h2 class="qa-card-title">Recurso de Logo Faltante (HTTP 404)</h2>
        </div>
        <div class="qa-card-meta-group">
          <span class="qa-meta-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 20V14M12 20V10M6 20v-2"/></svg>
            S4 • Baja
          </span>
          <div class="qa-meta-divider"></div>
          <span class="qa-module-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/></svg>
            Shell Global
          </span>
        </div>
      </div>
      <div class="qa-card-body">
        <div class="qa-col-left">
          <div class="qa-section-label">QUÉ SUCEDE</div>
          <div class="qa-problem-statement">
            Petición fallida a GET /assets/logo/company retorna HTTP 404 Not Found. Al contraer el menú lateral, la esquina superior izquierda queda completamente vacía.
          </div>
          <div class="qa-accordion">
            <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-def-02', this)">
              <span class="qa-accordion-title">Causa técnica</span>
              <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
            </div>
            <div id="cause-def-02" class="qa-accordion-content">
              El archivo de imagen no existe en el servidor y la etiqueta <code>&lt;img&gt;</code> carece de un fallback vectorial inline (SVG) que se muestre cuando el recurso no responde.
            </div>
          </div>
        </div>
        <div class="qa-col-right">
          <div class="qa-section-label">EVIDENCIA</div>
          <div class="qa-evidence-box" onclick="openModal('evidencias/DEF-02_error_404_logo.png','DEF-02: Recurso 404 en Logotipo')">
            <img class="qa-evidence-img" src="evidencias/DEF-02_error_404_logo.png" alt="DEF-02 Evidencia">
          </div>
        </div>
      </div>
    </div>

    <!-- DEF-03 -->
    <div class="qa-card">
      <div class="qa-card-header">
        <div class="qa-card-title-group">
          <span class="qa-id-badge">DEF-03</span>
          <h2 class="qa-card-title">Truncamiento de Breadcrumbs</h2>
        </div>
        <div class="qa-card-meta-group">
          <span class="qa-meta-pill">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
            S3 • Media
          </span>
          <div class="qa-meta-divider"></div>
          <span class="qa-module-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m9 18 6-6-6-6"/></svg>
            Navbar / Sucursales
          </span>
        </div>
      </div>
      <div class="qa-card-body">
        <div class="qa-col-left">
          <div class="qa-section-label">QUÉ SUCEDE</div>
          <div class="qa-problem-statement">
            En anchos intermedios (1024 a 1280px), la ruta queda cortada en “Dash” y el selector Light/Dark se superpone directamente sobre las letras.
          </div>
          <div class="qa-accordion">
            <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-def-03', this)">
              <span class="qa-accordion-title">Causa técnica</span>
              <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
            </div>
            <div id="cause-def-03" class="qa-accordion-content">
              El contenedor flexbox de la barra superior carece de <code>flex-wrap</code> y de un <code>min-width</code> asegurado para las migas de pan, provocando que los controles invadan el espacio del texto.
            </div>
          </div>
        </div>
        <div class="qa-col-right">
          <div class="qa-section-label">EVIDENCIA</div>
          <div class="qa-evidence-box" onclick="openModal('evidencias/DEF-03_colision_breadcrumbs_navbar.png','DEF-03: Truncamiento de Breadcrumbs')">
            <img class="qa-evidence-img" src="evidencias/DEF-03_colision_breadcrumbs_navbar.png" alt="DEF-03 Evidencia">
          </div>
        </div>
      </div>
    </div>

    <!-- OBS-01 -->
    <div class="qa-card">
      <div class="qa-card-header">
        <div class="qa-card-title-group">
          <span class="qa-id-badge badge-obs">OBS-01</span>
          <h2 class="qa-card-title">Bajo Contraste en Dark Mode</h2>
        </div>
        <div class="qa-card-meta-group">
          <span class="qa-meta-pill pill-obs">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><path d="M12 1v2M12 21v2M4.22 4.22l1.42 1.42M18.36 18.36l1.42 1.42M1 12h2M21 12h2M4.22 19.78l1.42-1.42M18.36 5.64l1.42-1.42"/></svg>
            Accesibilidad
          </span>
          <div class="qa-meta-divider"></div>
          <span class="qa-module-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>
            Dashboard
          </span>
        </div>
      </div>
      <div class="qa-card-body">
        <div class="qa-col-left">
          <div class="qa-section-label">QUÉ SUCEDE</div>
          <div class="qa-problem-statement">
            En Modo Oscuro, las etiquetas de los meses y los números del eje Y en Highcharts se vuelven casi invisibles contra el fondo negro de la tarjeta.
          </div>
          <div class="qa-accordion">
            <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-obs-01', this)">
              <span class="qa-accordion-title">Causa técnica</span>
              <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
            </div>
            <div id="cause-obs-01" class="qa-accordion-content">
              Highcharts tiene valores de color fijos oscuros (<code>#333333</code>) en lugar de adaptarse reactivamente a variables CSS de texto claro al aplicar la clase <code>.dark</code>.
            </div>
          </div>
        </div>
        <div class="qa-col-right">
          <div class="qa-section-label">EVIDENCIA</div>
          <div class="qa-evidence-box" onclick="openModal('evidencias/OBS-01_contraste_dark_mode.png','OBS-01: Falta de contraste en Dark Mode')">
            <img class="qa-evidence-img" src="evidencias/OBS-01_contraste_dark_mode.png" alt="OBS-01 Evidencia">
          </div>
        </div>
      </div>
    </div>

    <!-- OBS-02 -->
    <div class="qa-card">
      <div class="qa-card-header">
        <div class="qa-card-title-group">
          <span class="qa-id-badge badge-obs">OBS-02</span>
          <h2 class="qa-card-title">Sin Empty State en Búsqueda</h2>
        </div>
        <div class="qa-card-meta-group">
          <span class="qa-meta-pill pill-obs">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
            Usabilidad UX
          </span>
          <div class="qa-meta-divider"></div>
          <span class="qa-module-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg>
            Sucursales
          </span>
        </div>
      </div>
      <div class="qa-card-body">
        <div class="qa-col-left">
          <div class="qa-section-label">QUÉ SUCEDE</div>
          <div class="qa-problem-statement">
            Al buscar un texto inexistente (ej. “XYZ123”), la tabla queda completamente en blanco sin un mensaje que confirme la ausencia de registros.
          </div>
          <div class="qa-accordion">
            <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-obs-02', this)">
              <span class="qa-accordion-title">Causa técnica</span>
              <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
            </div>
            <div id="cause-obs-02" class="qa-accordion-content">
              Falta implementar una fila de estado vacío condicional cuando <code>resultados.length === 0</code> que indique <em>“No se encontraron sucursales para su búsqueda”</em>.
            </div>
          </div>
        </div>
        <div class="qa-col-right">
          <div class="qa-section-label">EVIDENCIA</div>
          <div class="qa-evidence-box" onclick="openModal('evidencias/SUCURSALES_1920x1080_COMPLETO.png','Sucursales - Estructura de tabla')">
            <img class="qa-evidence-img" src="evidencias/SUCURSALES_1920x1080_COMPLETO.png" alt="OBS-02 Evidencia">
          </div>
        </div>
      </div>
    </div>

    <!-- OBS-03 -->
    <div class="qa-card">
      <div class="qa-card-header">
        <div class="qa-card-title-group">
          <span class="qa-id-badge badge-info">OBS-03</span>
          <h2 class="qa-card-title">Límite de Cuota en Sucursales</h2>
        </div>
        <div class="qa-card-meta-group">
          <span class="qa-meta-pill pill-info">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="16" x2="12" y2="12"/><line x1="12" y1="8" x2="12.01" y2="8"/></svg>
            Regla de Negocio
          </span>
          <div class="qa-meta-divider"></div>
          <span class="qa-module-badge">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v2"/></svg>
            Sucursales
          </span>
        </div>
      </div>
      <div class="qa-card-body">
        <div class="qa-col-left">
          <div class="qa-section-label">QUÉ SUCEDE</div>
          <div class="qa-problem-statement">
            El botón “+ Nueva Sucursal” se renderiza inhabilitado (disabled), limitando la ejecución de pruebas de creación de sedes.
          </div>
          <div class="qa-accordion">
            <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-obs-03', this)">
              <span class="qa-accordion-title">Causa técnica</span>
              <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
            </div>
            <div id="cause-obs-03" class="qa-accordion-content">
              La empresa PLAEIS ENTERTAINMENT tiene contratada la cuota <strong>1 / 1 sucursales</strong>. Se requiere ampliar temporalmente el plan para habilitar la creación de nuevas sedes.
            </div>
          </div>
        </div>
        <div class="qa-col-right">
          <div class="qa-section-label">EVIDENCIA</div>
          <div class="qa-evidence-box" onclick="openModal('evidencias/OBS-03_sucursales_cuota_plan.png','OBS-03: Límite de cuota en plan de sucursales')">
            <img class="qa-evidence-img" src="evidencias/OBS-03_sucursales_cuota_plan.png" alt="OBS-03 Evidencia">
          </div>
        </div>
      </div>
    </div>

  </div>

  <!-- ══════════════════════════════════════════════════════════════ -->
  <!-- TAB 2: MATRIZ DE CASOS DE PRUEBA (ESTILO TABLA EXCEL) ── -->
  <!-- ══════════════════════════════════════════════════════════════ -->
  <div id="tab-matriz" class="pane">

    <div class="excel-container">
      
      <!-- Toolbar Excel -->
      <div class="excel-toolbar">
        <div class="excel-title-group">
          <div class="excel-sheet-icon">X</div>
          <div>
            <div class="excel-title">Matriz Completa de Pruebas QA (Libro de Validación)</div>
            <div class="excel-subtitle">11 casos auditados • Módulos Dashboard y Sucursales • Vista tabular tipo hoja de cálculo</div>
          </div>
        </div>

        <div class="excel-controls">
          <input type="text" id="excelSearch" class="excel-search-input" placeholder="🔍 Filtrar caso, resultado, módulo..." onkeyup="filterExcelTable()">
          <div class="excel-filters">
            <button class="excel-fpill active" onclick="filterExcelCategory('all', event)">Todos (11)</button>
            <button class="excel-fpill" onclick="filterExcelCategory('PASS', event)">PASS (8)</button>
            <button class="excel-fpill" onclick="filterExcelCategory('FAIL', event)">FAIL (3)</button>
            <button class="excel-fpill" onclick="filterExcelCategory('Dashboard', event)">Dashboard (6)</button>
            <button class="excel-fpill" onclick="filterExcelCategory('Sucursales', event)">Sucursales (5)</button>
          </div>
        </div>
      </div>

      <!-- Tabla Grid Excel -->
      <div class="excel-table-wrap">
        <table class="excel-table" id="excelMatrixTable">
          <thead>
            <tr>
              <th style="width: 105px;">ID Caso</th>
              <th style="width: 110px;">Módulo</th>
              <th style="width: 130px;">Tipo de Prueba</th>
              <th style="min-width: 260px;">Descripción del Caso</th>
              <th style="min-width: 250px;">Resultado Esperado</th>
              <th style="min-width: 260px;">Resultado Obtenido</th>
              <th style="width: 125px; text-align: center;">Estado</th>
              <th style="width: 95px; text-align: center;">Hallazgo</th>
              <th style="width: 120px; text-align: center;">Evidencia</th>
            </tr>
          </thead>
          <tbody>

            <!-- CP-DASH-01 -->
            <tr data-status="PASS" data-module="Dashboard">
              <td><span class="excel-id">CP-DASH-01</span></td>
              <td><strong>Dashboard</strong></td>
              <td><span class="excel-type-tag">Positivo</span></td>
              <td>Coherencia matemática de 4 KPIs superiores (Total, Activos, Inactivos, Sucursales, Roles).</td>
              <td>Total registrado = Activos + Inactivos; valores enteros válidos y no negativos.</td>
              <td><strong>1 Total = 1 Activo + 0 Inactivos</strong>. 1 Sucursal activa, 6 Roles configurados reflejados con exactitud.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-pass">✓ PASS</span>
              </td>
              <td style="text-align: center; color: #94A3B8;">—</td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/DASHBOARD_FULL_1920.png','CP-DASH-01: Coherencia matemática de KPIs')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-DASH-02 -->
            <tr data-status="FAIL" data-module="Dashboard">
              <td><span class="excel-id" style="color:#DC2626; background:#FEE8E1;">CP-DASH-02</span></td>
              <td><strong>Dashboard</strong></td>
              <td><span class="excel-type-tag">UI / Layout</span></td>
              <td>Delimitación y contención física de gráficos Highcharts en viewport de escritorio.</td>
              <td>Leyendas y series contenidas en el marco de cada tarjeta sin invadir elementos adyacentes.</td>
              <td><strong>Desbordamiento visual</strong>: las leyendas superiores solapan los títulos "Usuarios por Estado" y "Usuarios por Rol".</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-fail">✕ FAIL</span>
              </td>
              <td style="text-align: center;">
                <span class="excel-defect-link" onclick="switchTab('defectos')">DEF-01</span>
              </td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/DEF-01_solapamiento_leyendas_dashboard.png','CP-DASH-02: Solapamiento en Highcharts')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-DASH-03 -->
            <tr data-status="OBS" data-module="Dashboard">
              <td><span class="excel-id" style="color:#D97706; background:#FEF3C7;">CP-DASH-03</span></td>
              <td><strong>Dashboard</strong></td>
              <td><span class="excel-type-tag">Accesibilidad</span></td>
              <td>Conmutador de tema visual (Light / Dark) y contraste de textos analíticos.</td>
              <td>Contraste óptimo WCAG AA (4.5:1) en fondos oscuros y claros para todos los textos.</td>
              <td>Conmutación reactiva conforme. Las etiquetas de ejes en Highcharts usan color oscuro hardcoded (#333), perdiendo contraste en fondo negro.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-obs">⚠ PASS c/ OBS</span>
              </td>
              <td style="text-align: center;">
                <span class="excel-obs-link" onclick="switchTab('defectos')">OBS-01</span>
              </td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/OBS-01_contraste_dark_mode.png','CP-DASH-03: Falta de contraste en Dark Mode')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-DASH-04 -->
            <tr data-status="OBS" data-module="Dashboard">
              <td><span class="excel-id" style="color:#D97706; background:#FEF3C7;">CP-DASH-04</span></td>
              <td><strong>Dashboard</strong></td>
              <td><span class="excel-type-tag">Responsividad</span></td>
              <td>Toggle Sidebar (Colapso y expansión del menú lateral a 48px y 256px).</td>
              <td>Colapso fluido con reemplazo limpio de logo completo por isotipo vectorial.</td>
              <td>La rejilla y tarjetas se adaptan suavemente. Sin embargo, el espacio del isotipo queda en blanco por el recurso 404.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-obs">⚠ PASS c/ OBS</span>
              </td>
              <td style="text-align: center;">
                <span class="excel-defect-link" onclick="switchTab('defectos')">DEF-02</span>
              </td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/DEF-02_error_404_logo.png','CP-DASH-04: Recurso 404 en Logo')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-DASH-05 -->
            <tr data-status="PASS" data-module="Dashboard">
              <td><span class="excel-id">CP-DASH-05</span></td>
              <td><strong>Dashboard</strong></td>
              <td><span class="excel-type-tag">Navegación</span></td>
              <td>Menú desplegable de notificaciones y enlace a configuración de perfil.</td>
              <td>Popover accesible sin solapamiento y navegación operativa a /settings/profile.</td>
              <td>Popover muestra "Sin notificaciones nuevas" y redirección a perfil funciona conforme sin errores.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-pass">✓ PASS</span>
              </td>
              <td style="text-align: center; color: #94A3B8;">—</td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/DASHBOARD_FULL_1920.png','CP-DASH-05: Menú y Perfil')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-DASH-06 -->
            <tr data-status="FAIL" data-module="Dashboard">
              <td><span class="excel-id" style="color:#DC2626; background:#FEE8E1;">CP-DASH-06</span></td>
              <td><strong>Dashboard</strong></td>
              <td><span class="excel-type-tag">Técnico / Red</span></td>
              <td>Auditoría de peticiones HTTP en panel Network y excepciones en consola JS.</td>
              <td>Todas las peticiones resueltas con código 200/304; consola libre de errores.</td>
              <td>Petición <code>GET /assets/logo/company</code> retorna <strong>HTTP 404 Not Found</strong>. El archivo no existe en el servidor.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-fail">✕ FAIL</span>
              </td>
              <td style="text-align: center;">
                <span class="excel-defect-link" onclick="switchTab('defectos')">DEF-02</span>
              </td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/DEF-02_error_404_logo.png','CP-DASH-06: Error 404 en DevTools')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-BRAN-01 -->
            <tr data-status="PASS" data-module="Sucursales">
              <td><span class="excel-id">CP-BRAN-01</span></td>
              <td><strong>Sucursales</strong></td>
              <td><span class="excel-type-tag">Positivo</span></td>
              <td>Estructura de tabla de sucursales a pantalla completa (1920x1080).</td>
              <td>Todas las columnas visibles y bien proporcionadas sin scroll horizontal forzado.</td>
              <td>Tabla extendida conforme. Registro de Sede Principal con badge Activo en verde renderizado con nitidez.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-pass">✓ PASS</span>
              </td>
              <td style="text-align: center; color: #94A3B8;">—</td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/SUCURSALES_1920x1080_COMPLETO.png','CP-BRAN-01: Tabla de Sucursales')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-BRAN-02 -->
            <tr data-status="OBS" data-module="Sucursales">
              <td><span class="excel-id" style="color:#D97706; background:#FEF3C7;">CP-BRAN-02</span></td>
              <td><strong>Sucursales</strong></td>
              <td><span class="excel-type-tag">Filtros</span></td>
              <td>Búsqueda reactiva por texto y botón Limpiar en el listado de sucursales.</td>
              <td>Filtrar coincidencia en tiempo real; mostrar Empty State ante texto sin resultados.</td>
              <td>El filtro funciona correctamente. Sin embargo, ante términos inexistentes la tabla queda en blanco sin mensaje al usuario.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-obs">⚠ PASS c/ OBS</span>
              </td>
              <td style="text-align: center;">
                <span class="excel-obs-link" onclick="switchTab('defectos')">OBS-02</span>
              </td>
              <td style="text-align: center; color: #94A3B8;">—</td>
            </tr>

            <!-- CP-BRAN-03 -->
            <tr data-status="PASS" data-module="Sucursales">
              <td><span class="excel-id">CP-BRAN-03</span></td>
              <td><strong>Sucursales</strong></td>
              <td><span class="excel-type-tag">Validación Negativa</span></td>
              <td>Validación obligatoria de campo "Nombre *" en modal de sucursal.</td>
              <td>Bloqueo de formulario al enviar con Nombre * vacío; cero mutación de datos.</td>
              <td>Envío interceptado correctamente con tooltip <em>"Completa este campo"</em>. Integridad de base de datos preservada al 100%.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-pass">✓ PASS</span>
              </td>
              <td style="text-align: center; color: #94A3B8;">—</td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/CP-BRAN-03_validacion_formulario_exitosa.png','CP-BRAN-03: Validación Obligatoria Exitosa')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-BRAN-04 -->
            <tr data-status="PASS" data-module="Sucursales">
              <td><span class="excel-id">CP-BRAN-04</span></td>
              <td><strong>Sucursales</strong></td>
              <td><span class="excel-type-tag">Permisos / Modal</span></td>
              <td>Modal de Detalle de Sucursal ("Ver") y cierre con tecla Escape.</td>
              <td>Despliegue de datos de solo lectura estructurados y cierre limpio.</td>
              <td>Modal estructurado con datos completos de Sede Principal; botones de cierre y tecla Escape 100% operativos.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-pass">✓ PASS</span>
              </td>
              <td style="text-align: center; color: #94A3B8;">—</td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/SUCURSALES_1920x1080_COMPLETO.png','CP-BRAN-04: Detalle de Sucursal')">
                  Ver captura
                </button>
              </td>
            </tr>

            <!-- CP-BRAN-05 -->
            <tr data-status="FAIL" data-module="Sucursales">
              <td><span class="excel-id" style="color:#DC2626; background:#FEE8E1;">CP-BRAN-05</span></td>
              <td><strong>Sucursales</strong></td>
              <td><span class="excel-type-tag">Responsividad</span></td>
              <td>Truncamiento de Breadcrumbs en navbar superior en resoluciones 1024 a 1280px.</td>
              <td>Ruta de migas de pan legible completa junto a los controles de tema y perfil.</td>
              <td>Ruta se trunca a "Dash" y el conmutador de tema se superpone directamente encima del texto.</td>
              <td style="text-align: center;">
                <span class="excel-badge-status excel-status-fail">✕ FAIL</span>
              </td>
              <td style="text-align: center;">
                <span class="excel-defect-link" onclick="switchTab('defectos')">DEF-03</span>
              </td>
              <td style="text-align: center;">
                <button class="excel-btn-ev" onclick="openModal('evidencias/DEF-03_colision_breadcrumbs_navbar.png','CP-BRAN-05: Truncamiento de Breadcrumbs')">
                  Ver captura
                </button>
              </td>
            </tr>

          </tbody>
        </table>
      </div>

      <!-- Spreadsheet Status Bar Footer -->
      <div class="excel-statusbar">
        <div class="excel-statusbar-left">
          <span>✓ Hoja de pruebas cargada</span>
          <span>•</span>
          <span id="excelRowCount">11 casos mostrados de 11 totales</span>
          <span>•</span>
          <span>Criterio: Caja Negra No Destructiva</span>
        </div>
        <div class="excel-statusbar-right">
          <span style="color:#166534;">8 PASS (72.7%)</span>
          <span>|</span>
          <span style="color:#DC2626;">3 FAIL (27.3%)</span>
          <span>|</span>
          <span style="color:#1B59F8;">Integridad BD: 100%</span>
        </div>
      </div>

    </div>

  </div>

</main>

<!-- MODAL ZOOM -->
<div id="image-modal" class="modal-overlay" onclick="closeModal(event)">
  <div class="modal-card" onclick="event.stopPropagation()">
    <div class="modal-hd">
      <h3 id="modal-title">Evidencia de Calidad</h3>
      <button class="modal-close" onclick="closeModal()">&times;</button>
    </div>
    <div class="modal-body">
      <img id="modal-image" src="" alt="Evidencia">
    </div>
  </div>
</div>

<script>
  function switchTab(id, e) {
    document.querySelectorAll('.pane').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-tab').forEach(el => el.classList.remove('active'));
    document.getElementById('tab-' + id).classList.add('active');
    if (e && e.currentTarget) {
      e.currentTarget.classList.add('active');
    } else {
      const btn = document.querySelector(`.nav-tab[onclick*="${id}"]`);
      if (btn) btn.classList.add('active');
    }
  }

  function toggleAccordion(id, trigger) {
    const content = document.getElementById(id);
    const isOpen = content.classList.contains('open');
    if (isOpen) {
      content.classList.remove('open');
      trigger.classList.remove('open');
    } else {
      content.classList.add('open');
      trigger.classList.add('open');
    }
  }

  let currentCategory = 'all';

  function filterExcelCategory(category, e) {
    currentCategory = category;
    document.querySelectorAll('.excel-fpill').forEach(b => b.classList.remove('active'));
    if (e && e.target) e.target.classList.add('active');
    applyExcelFilters();
  }

  function filterExcelTable() {
    applyExcelFilters();
  }

  function applyExcelFilters() {
    const query = (document.getElementById('excelSearch').value || '').toLowerCase();
    const rows = document.querySelectorAll('#excelMatrixTable tbody tr');
    let visibleCount = 0;

    rows.forEach(row => {
      const status = row.getAttribute('data-status');
      const module = row.getAttribute('data-module');
      const text = row.innerText.toLowerCase();

      let matchesCategory = false;
      if (currentCategory === 'all') {
        matchesCategory = true;
      } else if (currentCategory === 'PASS') {
        matchesCategory = (status === 'PASS' || status === 'OBS');
      } else if (currentCategory === 'FAIL') {
        matchesCategory = (status === 'FAIL');
      } else if (currentCategory === 'Dashboard') {
        matchesCategory = (module === 'Dashboard');
      } else if (currentCategory === 'Sucursales') {
        matchesCategory = (module === 'Sucursales');
      }

      const matchesSearch = query === '' || text.includes(query);

      if (matchesCategory && matchesSearch) {
        row.style.display = '';
        visibleCount++;
      } else {
        row.style.display = 'none';
      }
    });

    const countElem = document.getElementById('excelRowCount');
    if (countElem) {
      countElem.textContent = `${visibleCount} casos mostrados de 11 totales`;
    }
  }

  function openModal(src, title) {
    document.getElementById('modal-image').src = src;
    document.getElementById('modal-title').textContent = title;
    document.getElementById('image-modal').classList.add('active');
  }

  function closeModal(e) {
    if (!e || e.target === document.getElementById('image-modal'))
      document.getElementById('image-modal').classList.remove('active');
  }

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') document.getElementById('image-modal').classList.remove('active');
  });
</script>
</body>
</html>"""

with open(r'd:\CONTROLA-2026\index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Generated portal successfully with Excel-style Matriz de Casos de Prueba!")
