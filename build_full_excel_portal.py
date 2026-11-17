import os
import json
from generate_rows import rows_html, cases_data

cases_json = json.dumps(cases_data, ensure_ascii=False)

modules_list = [
    {"id": "all", "name": "Todos los Módulos", "group": "GENERAL", "icon": "grid", "count": 12, "badge": ""},
    {"id": "Dashboard", "name": "Dashboard", "group": "PLATAFORMA", "icon": "dashboard", "count": 6, "badge": "6 casos • 1 ✕"},
    {"id": "Calendario", "name": "Calendario", "group": "PLATAFORMA", "icon": "calendar", "count": 0, "badge": "0"},
    {"id": "Sucursales", "name": "Sucursales", "group": "PLATAFORMA", "icon": "building", "count": 5, "badge": "5 casos • 1 ✕"},
    {"id": "Empleados", "name": "Empleados", "group": "PLATAFORMA", "icon": "users", "count": 0, "badge": "0"},
    {"id": "Contratistas", "name": "Contratistas", "group": "PLATAFORMA", "icon": "briefcase", "count": 0, "badge": "0"},
    {"id": "Capacitaciones", "name": "Capacitaciones", "group": "PLATAFORMA", "icon": "award", "count": 0, "badge": "0"},
    {"id": "Herramientas SST", "name": "Herramientas SST", "group": "PLATAFORMA", "icon": "shield-alert", "count": 0, "badge": "0"},
    {"id": "Tareas", "name": "Tareas", "group": "PLATAFORMA", "icon": "check-square", "count": 1, "badge": "1 caso • 1 ✕"},
    {"id": "Documentos SST", "name": "Documentos SST", "group": "PLATAFORMA", "icon": "file-text", "count": 0, "badge": "0"},
    {"id": "Programa Anual", "name": "Programa Anual", "group": "PLATAFORMA", "icon": "calendar-days", "count": 0, "badge": "0"},
    {"id": "Registros SST", "name": "Registros SST", "group": "PLATAFORMA", "icon": "clipboard-list", "count": 0, "badge": "0"},
    {"id": "Línea Base SST", "name": "Línea Base SST", "group": "PLATAFORMA", "icon": "target", "count": 0, "badge": "0"},
    {"id": "Libro de Actas", "name": "Libro de Actas", "group": "PLATAFORMA", "icon": "book-open", "count": 0, "badge": "0"},
    {"id": "Notificaciones", "name": "Notificaciones", "group": "PLATAFORMA", "icon": "bell", "count": 0, "badge": "0"},
    {"id": "Catálogos", "name": "Catálogos", "group": "PLATAFORMA", "icon": "folder", "count": 0, "badge": "0"},
    {"id": "Autorización", "name": "Autorización", "group": "AUTORIZACIÓN", "icon": "key", "count": 0, "badge": "0"},
]

icons_svg = {
    "grid": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>',
    "dashboard": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>',
    "calendar": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "building": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M8 10h.01M16 10h.01M8 14h.01M16 14h.01"/></svg>',
    "users": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "briefcase": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "award": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
    "shield-alert": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>',
    "check-square": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    "file-text": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>',
    "calendar-days": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/><path d="M8 14h.01M12 14h.01M16 14h.01M8 18h.01M12 18h.01M16 18h.01"/></svg>',
    "clipboard-list": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1"/><line x1="12" y1="11" x2="16" y2="11"/><line x1="12" y1="16" x2="16" y2="16"/><circle cx="9" cy="11" r="1"/><circle cx="9" cy="16" r="1"/></svg>',
    "target": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
    "book-open": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>',
    "bell": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>',
    "folder": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>',
    "key": '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 2l-2 2m-1.5 1.5L16 4l-3 3-4-4-5 5 1.5 1.5M7 11l-5 5v5h5l5-5"/></svg>'
}

from collections import Counter
mod_counts = Counter(c["module"] for c in cases_data)
mod_fails = Counter(c["module"] for c in cases_data if "FAIL" in c.get("status", ""))

for m in modules_list:
    if m["id"] == "all":
        m["count"] = len(cases_data)
        m["badge"] = ""
    else:
        cnt = mod_counts.get(m["name"], 0)
        fails = mod_fails.get(m["name"], 0)
        m["count"] = cnt
        suffix = 's' if cnt > 1 else ''
        if fails > 0:
            m["badge"] = f"{cnt} caso{suffix} • {fails} ✕"
        elif cnt > 0:
            m["badge"] = f"{cnt} caso{suffix} • ✓"
        else:
            m["badge"] = "0"

sidebar_html = ""
current_group = None
for m in modules_list:
    if m["group"] != current_group:
        current_group = m["group"]
        if current_group != "GENERAL":
            sidebar_html += f'<div class="sidebar-group-title">{current_group}</div>'
    
    is_active = "active" if m["id"] == "all" else ""
    badge_html = ""
    if m.get("badge"):
        badge_cls = "sidebar-count count-fail" if "✕" in m["badge"] else ("sidebar-count count-empty" if m["count"] == 0 else "sidebar-count")
        badge_html = f'<span class="{badge_cls}">{m["badge"]}</span>'
    
    sidebar_html += f'''
    <div class="sidebar-item {is_active}" data-mod-id="{m["id"]}" onclick="selectSidebarModule('{m["id"]}', this)">
      <div class="sidebar-item-left">
        <span class="sidebar-icon">{icons_svg.get(m["icon"], "")}</span>
        <span class="sidebar-name">{m["name"]}</span>
      </div>
      {badge_html}
    </div>
    '''

html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Controla.pe • Informe QA Profesional | Plaeis Entertainment</title>
  
  <style>
    /* ── E-UKRAINE FONTS ── */
    @font-face {{
      font-family: 'e-Ukraine';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-Ukraine-Regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'e-Ukraine';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-Ukraine-Medium.woff2') format('woff2');
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'e-Ukraine';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-Ukraine-Bold.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'e-UkraineHead';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-UkraineHead-Regular.woff2') format('woff2');
      font-weight: 400;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'e-UkraineHead';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-UkraineHead-Medium.woff2') format('woff2');
      font-weight: 500;
      font-style: normal;
      font-display: swap;
    }}
    @font-face {{
      font-family: 'e-UkraineHead';
      src: url('./assets/resources/font/e-Ukraine_font/web/e-UkraineHead-Bold.woff2') format('woff2');
      font-weight: 700;
      font-style: normal;
      font-display: swap;
    }}

    :root {{
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
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: var(--bg);
      color: var(--text);
      font-family: 'e-Ukraine', -apple-system, BlinkMacSystemFont, sans-serif;
      line-height: 1.5;
      -webkit-font-smoothing: antialiased;
      padding-bottom: 80px;
    }}

    /* ── TOPBAR ── */
    .topbar {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 36px;
      position: sticky;
      top: 0;
      z-index: 100;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }}
    .topbar-inner {{
      max-width: 1560px;
      margin: 0 auto;
      height: 64px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
    }}
    .topbar-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .brand-logo-img {{ height: 28px; width: auto; }}
    .brand-divider {{ width: 1px; height: 20px; background: var(--border); }}
    .brand-badge {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      background: var(--primary-light);
      color: var(--primary);
      padding: 4px 10px;
      border-radius: 6px;
    }}
    .topbar-right {{
      display: flex;
      align-items: center;
      gap: 16px;
      font-size: 12px;
      color: var(--text-muted);
    }}
    .topbar-team-tag {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: #F1F5F9;
      padding: 5px 12px;
      border-radius: 999px;
      font-weight: 600;
      color: #334155;
    }}

    /* ── HERO BANNER ── */
    .hero {{
      background: linear-gradient(135deg, #1B59F8 0%, #0D3DB0 100%);
      padding: 36px 36px 32px;
    }}
    .hero-inner {{ max-width: 1560px; margin: 0 auto; }}
    .hero-eyebrow {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11.5px;
      font-weight: 700;
      letter-spacing: 1.2px;
      color: rgba(255,255,255,0.75);
      text-transform: uppercase;
      margin-bottom: 6px;
    }}
    .hero h1 {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 30px;
      font-weight: 700;
      color: #fff;
      letter-spacing: -0.5px;
      line-height: 1.2;
    }}
    .hero-stats {{
      display: flex;
      gap: 32px;
      margin-top: 22px;
      flex-wrap: wrap;
    }}
    .hero-stat-val {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 32px;
      font-weight: 700;
      color: #fff;
      line-height: 1;
    }}
    .hero-stat-label {{
      font-size: 11.5px;
      color: rgba(255,255,255,0.75);
      margin-top: 4px;
    }}
    .hero-stat-divider {{ width: 1px; background: rgba(255,255,255,0.2); }}

    /* ── NAV TABS ── */
    .nav-wrap {{
      background: var(--surface);
      border-bottom: 1px solid var(--border);
      padding: 0 36px;
      transition: padding 0.2s ease;
    }}
    .nav-wrap.no-sidebar-nav {{
      padding: 0 24px;
    }}
    .nav-bar {{
      max-width: 1560px;
      margin: 0 auto;
      display: flex;
      gap: 8px;
      transition: max-width 0.2s ease;
    }}
    .nav-wrap.no-sidebar-nav .nav-bar {{
      max-width: 100%;
      margin: 0;
    }}
    .nav-tab {{
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
    }}
    .nav-tab:hover {{ color: var(--primary); }}
    .nav-tab.active {{ color: var(--primary); border-bottom-color: var(--primary); }}

    /* ── LAYOUT CON SIDEBAR DE 16 MÓDULOS ── */
    .app-layout {{
      max-width: 1560px;
      margin: 0 auto;
      padding: 28px 36px;
      display: flex;
      gap: 28px;
      align-items: flex-start;
      transition: all 0.2s ease;
    }}
    /* En la vista de matriz de casos de prueba se elimina el menú de módulos (sidebar) y solo va el Excel a ancho completo */
    .app-layout.no-sidebar {{
      display: block;
      max-width: 100% !important;
      width: 100% !important;
      margin: 0 !important;
      padding: 20px 24px !important;
      box-sizing: border-box;
    }}
    .app-layout.no-sidebar .app-sidebar {{
      display: none !important;
    }}
    .app-layout.no-sidebar .app-main {{
      width: 100% !important;
      max-width: 100% !important;
    }}
    @media (max-width: 1024px) {{
      .app-layout {{ flex-direction: column; padding: 20px; }}
    }}

    /* SIDEBAR */
    .app-sidebar {{
      width: 290px;
      flex-shrink: 0;
      background: var(--surface);
      border: 1px solid #ECEFF3;
      border-radius: 24px;
      box-shadow: var(--shadow-card);
      padding: 20px 16px;
      position: sticky;
      top: 84px;
      max-height: calc(100vh - 104px);
      overflow-y: auto;
    }}
    @media (max-width: 1024px) {{
      .app-sidebar {{ width: 100%; position: static; max-height: none; }}
    }}
    .app-sidebar-header {{
      padding: 4px 10px 14px;
      border-bottom: 1px solid #F1F5F9;
      margin-bottom: 10px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}
    .app-sidebar-title {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: #64748B;
    }}
    .app-sidebar-badge {{
      background: #EFF6FF;
      color: #1B59F8;
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      padding: 3px 8px;
      border-radius: 999px;
    }}
    .sidebar-group-title {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 10px;
      font-weight: 700;
      letter-spacing: 0.9px;
      color: #94A3B8;
      text-transform: uppercase;
      padding: 12px 10px 6px;
    }}
    .sidebar-item {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 9px 12px;
      border-radius: 12px;
      color: #334155;
      font-size: 13px;
      font-weight: 500;
      cursor: pointer;
      transition: all 0.15s;
      user-select: none;
      margin-bottom: 2px;
    }}
    .sidebar-item:hover {{
      background: #F8FAFC;
      color: #1B59F8;
    }}
    .sidebar-item.active {{
      background: #1B59F8;
      color: #FFFFFF;
      font-weight: 700;
      box-shadow: 0 4px 12px rgba(27,89,248,0.22);
    }}
    .sidebar-item-left {{
      display: flex;
      align-items: center;
      gap: 10px;
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }}
    .sidebar-icon {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 18px;
      height: 18px;
      opacity: 0.85;
    }}
    .sidebar-item.active .sidebar-icon {{ opacity: 1; }}
    .sidebar-name {{
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }}
    .sidebar-count {{
      font-size: 11px;
      font-weight: 700;
      padding: 2px 7px;
      border-radius: 999px;
      background: #F1F5F9;
      color: #475569;
      white-space: nowrap;
    }}
    .sidebar-item.active .sidebar-count {{
      background: rgba(255,255,255,0.25);
      color: #FFFFFF;
    }}
    .sidebar-count.count-fail {{
      background: #FEE8E1;
      color: #991B1B;
    }}
    .sidebar-item.active .sidebar-count.count-fail {{
      background: rgba(255,255,255,0.3);
      color: #FFFFFF;
    }}
    .sidebar-count.count-empty {{
      font-size: 10px;
      color: #94A3B8;
      background: transparent;
      font-weight: 500;
    }}
    .sidebar-item.active .sidebar-count.count-empty {{
      color: rgba(255,255,255,0.7);
    }}

    /* MAIN CONTENT */
    .app-main {{
      flex: 1;
      min-width: 0;
    }}
    .pane {{ display: none; }}
    .pane.active {{ display: block; animation: fadeIn 0.18s ease-out; }}
    @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(6px); }} to {{ opacity: 1; transform: translateY(0); }} }}

    /* ── DIIA DEFECT CARD DESIGN ── */
    .qa-card {{
      background: var(--surface);
      border: 1px solid #ECEFF3;
      border-radius: var(--radius-card);
      box-shadow: var(--shadow-card);
      padding: 36px 40px;
      margin-bottom: 28px;
      transition: transform 0.2s, box-shadow 0.2s;
    }}
    .qa-card:hover {{
      box-shadow: var(--shadow-hover);
    }}
    .qa-card-header {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid #EFEFEF;
      padding-bottom: 24px;
      margin-bottom: 28px;
      flex-wrap: wrap;
      gap: 16px;
    }}
    .qa-card-title-group {{
      display: flex;
      align-items: center;
      gap: 18px;
      flex-wrap: wrap;
    }}
    .qa-id-badge {{
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
    }}
    .qa-id-badge.badge-obs {{ background: #FEF3C7; color: #92400E; }}
    .qa-id-badge.badge-info {{ background: #E0F2FE; color: #075985; }}

    .qa-card-title {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #000000;
      letter-spacing: -0.3px;
    }}

    .qa-card-meta-group {{
      display: flex;
      align-items: center;
      gap: 14px;
    }}
    .qa-meta-pill {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 14px;
      font-weight: 500;
      color: #475569;
      background: #F1F5F9;
      padding: 6px 14px;
      border-radius: var(--radius-pill);
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}
    .qa-meta-pill.pill-warn {{ background: #FEF3C7; color: #92400E; }}
    .qa-meta-pill.pill-info {{ background: #E0F2FE; color: #075985; }}

    .qa-meta-divider {{
      width: 1px;
      height: 16px;
      background: #D1D5DB;
    }}
    .qa-module-badge {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 14px;
      font-weight: 500;
      color: #475569;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .qa-card-body {{
      display: grid;
      grid-template-columns: 1fr 1.15fr;
      gap: 48px;
      align-items: start;
    }}
    @media (max-width: 900px) {{
      .qa-card-body {{ grid-template-columns: 1fr; gap: 28px; }}
    }}

    .qa-section-label {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 12px;
      font-weight: 700;
      letter-spacing: 0.8px;
      text-transform: uppercase;
      color: #94A3B8;
      margin-bottom: 12px;
    }}

    .qa-problem-statement {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #0F172A;
      line-height: 1.45;
      margin-bottom: 24px;
    }}

    .qa-accordion {{
      border-top: 1px solid #EFEFEF;
      padding-top: 18px;
    }}
    .qa-accordion-trigger {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      cursor: pointer;
      user-select: none;
    }}
    .qa-accordion-title {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #0F172A;
    }}
    .qa-accordion-icon {{
      transition: transform 0.2s ease;
      color: #475569;
    }}
    .qa-accordion-trigger.open .qa-accordion-icon {{
      transform: rotate(180deg);
    }}
    .qa-accordion-content {{
      display: none;
      font-size: 14px;
      color: #334155;
      line-height: 1.6;
      margin-top: 12px;
      background: #F8FAFC;
      border: 1px solid #E2E8F0;
      border-radius: 12px;
      padding: 16px 20px;
    }}
    .qa-accordion-content.open {{
      display: block;
      animation: fadeIn 0.15s ease-out;
    }}

    /* Evidence container */
    .qa-evidence-box {{
      position: relative;
      border-radius: 20px;
      overflow: hidden;
      border: 1px solid #E2E8F0;
      background: #F8FAFC;
      cursor: pointer;
      aspect-ratio: 16/9;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: box-shadow 0.2s;
    }}
    .qa-evidence-box:hover {{
      box-shadow: 0 8px 24px rgba(0,0,0,0.1);
    }}
    .qa-evidence-img {{
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: top center;
      display: block;
    }}
    .qa-evidence-overlay-btn {{
      position: absolute;
      bottom: 14px;
      right: 14px;
      background: rgba(15,23,42,0.85);
      backdrop-filter: blur(4px);
      color: #FFFFFF;
      font-family: 'e-Ukraine', sans-serif;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 14px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      pointer-events: none;
    }}

    /* ── SPREADSHEET (TABLA EXCEL) ── */
    .excel-container {{
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      border-radius: 20px;
      box-shadow: 0 4px 20px rgba(0,0,0,0.04);
      overflow: hidden;
      margin-bottom: 40px;
    }}

    /* Spreadsheet Toolbar */
    .excel-toolbar {{
      background: #F8FAFC;
      border-bottom: 1px solid #E2E8F0;
      padding: 18px 24px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 16px;
      flex-wrap: wrap;
    }}
    .excel-title-group {{
      display: flex;
      align-items: center;
      gap: 12px;
    }}
    .excel-sheet-icon {{
      width: 34px;
      height: 34px;
      background: #107C41; /* Excel green */
      border-radius: 8px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: #FFFFFF;
      font-family: 'e-UkraineHead', sans-serif;
      font-weight: 700;
      font-size: 17px;
      box-shadow: 0 2px 6px rgba(16,124,65,0.25);
    }}
    .excel-title {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 17px;
      font-weight: 700;
      color: #0F172A;
    }}
    .excel-subtitle {{
      font-size: 12px;
      color: #64748B;
    }}

    .excel-controls {{
      display: flex;
      align-items: center;
      gap: 10px;
      flex-wrap: wrap;
    }}
    .excel-search-input {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 13px;
      padding: 8px 16px;
      border: 1px solid #CBD5E1;
      border-radius: 8px;
      outline: none;
      width: 250px;
      background: #FFFFFF;
      transition: border-color 0.15s, box-shadow 0.15s;
    }}
    .excel-search-input:focus {{
      border-color: #1B59F8;
      box-shadow: 0 0 0 3px rgba(27,89,248,0.12);
    }}

    .excel-filters {{
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    .excel-fpill {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 12px;
      font-weight: 600;
      padding: 6px 12px;
      border-radius: 8px;
      border: 1px solid #CBD5E1;
      background: #FFFFFF;
      color: #475569;
      cursor: pointer;
      transition: all 0.15s;
    }}
    .excel-fpill:hover {{
      background: #F1F5F9;
      color: #0F172A;
    }}
    .excel-fpill.active {{
      background: #0F172A;
      color: #FFFFFF;
      border-color: #0F172A;
    }}

    .btn-export-csv {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 12px;
      font-weight: 700;
      background: #107C41;
      color: #FFFFFF;
      border: none;
      padding: 8px 16px;
      border-radius: 8px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 6px;
      transition: background 0.15s;
      box-shadow: 0 2px 6px rgba(16,124,65,0.2);
    }}
    .btn-export-csv:hover {{
      background: #0D6535;
    }}

    /* Spreadsheet Table Grid */
    .excel-table-wrap {{
      overflow-x: auto;
      max-width: 100%;
    }}
    .excel-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 12.5px;
      text-align: left;
    }}
    .excel-table th {{
      background: #F1F5F9;
      color: #334155;
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.5px;
      text-transform: uppercase;
      padding: 12px 12px;
      border-right: 1px solid #CBD5E1;
      border-bottom: 2px solid #CBD5E1;
      white-space: nowrap;
      user-select: none;
    }}
    .excel-table th:last-child {{
      border-right: none;
    }}
    .excel-table td {{
      padding: 12px 12px;
      border-right: 1px solid #E2E8F0;
      border-bottom: 1px solid #E2E8F0;
      vertical-align: top;
      line-height: 1.45;
    }}
    .excel-table td:last-child {{
      border-right: none;
    }}
    .excel-table tbody tr.excel-data-row:nth-child(4n+1) {{
      background: #FAFBFD;
    }}
    .excel-table tbody tr.excel-data-row:hover {{
      background: #EFF6FF !important;
    }}

    /* Toggle Row Button */
    .btn-toggle-row {{
      background: #F1F5F9;
      border: 1px solid #CBD5E1;
      width: 24px;
      height: 24px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      color: #475569;
      transition: all 0.15s;
    }}
    .btn-toggle-row:hover {{
      background: #1B59F8;
      color: #FFFFFF;
      border-color: #1B59F8;
    }}
    .btn-toggle-row.open svg {{
      transform: rotate(180deg);
    }}

    /* Spreadsheet Cell Badges */
    .excel-id {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 8px;
      border-radius: 6px;
      display: inline-block;
      white-space: nowrap;
    }}
    .excel-badge-status {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 9px;
      border-radius: 999px;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      white-space: nowrap;
    }}
    .excel-status-pass {{
      background: #DCFCE7;
      color: #166534;
      border: 1px solid #BBF7D0;
    }}
    .excel-status-fail {{
      background: #FEE8E1;
      color: #991B1B;
      border: 1px solid #FECACA;
    }}
    .excel-status-obs {{
      background: #FEF3C7;
      color: #92400E;
      border: 1px solid #FDE68A;
    }}

    .excel-defect-link {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      color: #991B1B;
      background: #FEE8E1;
      border: 1px solid #FECACA;
      padding: 3px 8px;
      border-radius: 6px;
      cursor: pointer;
      transition: background 0.15s;
    }}
    .excel-defect-link:hover {{
      background: #FCA5A5;
      color: #7F1D1D;
    }}
    .excel-obs-link {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      color: #92400E;
      background: #FEF3C7;
      border: 1px solid #FDE68A;
      padding: 3px 8px;
      border-radius: 6px;
      cursor: pointer;
    }}

    .excel-btn-ev {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 11px;
      font-weight: 600;
      padding: 4px 10px;
      border: 1px solid #CBD5E1;
      background: #FFFFFF;
      color: #1E293B;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 4px;
      transition: all 0.15s;
    }}
    .excel-btn-ev:hover {{
      background: #1B59F8;
      color: #FFFFFF;
      border-color: #1B59F8;
    }}

    /* Row Detail Drawer (Ficha Completa IEEE 829) */
    .row-detail-card {{
      padding: 24px 30px;
      border-bottom: 2px solid #CBD5E1;
      background: #F8FAFC;
      width: 100%;
      box-sizing: border-box;
    }}
    .row-detail-grid {{
      display: grid;
      grid-template-columns: 1fr;
      gap: 20px;
    }}
    @media (max-width: 960px) {{
      .row-detail-grid {{ grid-template-columns: 1fr; }}
    }}
    .detail-label {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.6px;
      text-transform: uppercase;
      color: #475569;
      margin-bottom: 8px;
    }}
    .detail-steps {{
      font-family: 'e-Ukraine', sans-serif;
      font-size: 13px;
      line-height: 1.6;
      color: #1E293B;
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 12px 16px;
    }}
    .detail-tag {{
      display: inline-block;
      background: #FFFFFF;
      border: 1px solid #CBD5E1;
      padding: 5px 12px;
      border-radius: 6px;
      font-size: 12px;
      color: #334155;
    }}
    .detail-meta-list {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 10px;
      padding: 14px 18px;
      display: flex;
      flex-direction: column;
      gap: 10px;
      font-size: 13px;
    }}
    .detail-meta-item {{
      display: flex;
      align-items: baseline;
      gap: 16px;
      border-bottom: 1px dashed #E2E8F0;
      padding-bottom: 8px;
    }}
    .detail-meta-item:last-child {{
      border-bottom: none;
      padding-bottom: 0;
    }}
    .detail-meta-item span {{
      color: #64748B;
      min-width: 140px;
      flex-shrink: 0;
    }}
    .detail-meta-item strong {{
      color: #0F172A;
      font-weight: 700;
    }}

    /* Spreadsheet Footer / Status Bar */
    .excel-statusbar {{
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
    }}
    .excel-statusbar-left {{
      display: flex;
      align-items: center;
      gap: 16px;
    }}
    .excel-statusbar-right {{
      display: flex;
      align-items: center;
      gap: 16px;
      font-family: 'e-UkraineHead', sans-serif;
      font-weight: 600;
    }}

    /* Empty Module Placeholder */
    .empty-module-card {{
      background: #FFFFFF;
      border: 1px solid #E2E8F0;
      border-radius: 20px;
      padding: 50px 32px;
      text-align: center;
      margin: 16px 0 32px;
    }}
    .empty-module-icon {{
      width: 56px;
      height: 56px;
      border-radius: 50%;
      background: #EFF6FF;
      color: #1B59F8;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 16px;
    }}
    .empty-module-title {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 20px;
      font-weight: 700;
      color: #0F172A;
      margin-bottom: 8px;
    }}
    .empty-module-badge {{
      display: inline-block;
      background: #FEF3C7;
      color: #92400E;
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 11px;
      font-weight: 700;
      padding: 4px 12px;
      border-radius: 999px;
      margin-bottom: 16px;
    }}
    .empty-module-desc {{
      color: #64748B;
      font-size: 14px;
      max-width: 600px;
      margin: 0 auto 20px;
      line-height: 1.6;
    }}
    .btn-empty-reset {{
      background: #1B59F8;
      color: #FFFFFF;
      border: none;
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 13px;
      font-weight: 700;
      padding: 10px 22px;
      border-radius: 8px;
      cursor: pointer;
      transition: background 0.15s;
    }}
    .btn-empty-reset:hover {{
      background: #1040C0;
    }}

    /* ── MODAL ── */
    .modal-overlay {{
      display: none;
      position: fixed;
      inset: 0;
      background: rgba(15,23,42,0.8);
      backdrop-filter: blur(8px);
      z-index: 1000;
      justify-content: center;
      align-items: center;
      padding: 24px;
    }}
    .modal-overlay.active {{ display: flex; }}
    .modal-card {{
      background: #FFFFFF;
      border-radius: 20px;
      max-width: 1100px;
      width: 100%;
      max-height: 90vh;
      overflow: hidden;
      display: flex;
      flex-direction: column;
      box-shadow: 0 24px 48px rgba(0,0,0,0.3);
    }}
    .modal-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 24px;
      border-bottom: 1px solid var(--border);
    }}
    .modal-header h3 {{
      font-family: 'e-UkraineHead', sans-serif;
      font-size: 16px;
      font-weight: 700;
      color: #0F172A;
    }}
    .modal-close {{
      background: #F1F5F9;
      border: none;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      font-size: 18px;
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--text-muted);
    }}
    .modal-close:hover {{ background: #FEE2E2; color: #DC2626; }}
    .modal-body {{ padding: 24px 28px; overflow: auto; text-align: center; }}
    .modal-body img {{ max-width: 100%; max-height: 74vh; border-radius: 12px; }}

    /* ── MOBILE TABLE SCROLL HINT ── */
    .mobile-table-hint {{
      display: none;
    }}

    /* ══════════════════════════════════════════════════════════════ */
    /* ── RESPONSIVE DESIGN (TABLETS & SMARTPHONES) ── */
    /* ══════════════════════════════════════════════════════════════ */

    @media (max-width: 1024px) {{
      .app-layout {{
        flex-direction: column;
        padding: 20px 18px;
        gap: 20px;
      }}
      .app-sidebar {{
        width: 100%;
        position: static;
        max-height: none;
      }}
    }}

    @media (max-width: 900px) {{
      /* Topbar */
      .topbar {{
        padding: 0 16px;
      }}
      .topbar-inner {{
        height: 56px;
      }}
      .brand-logo-img {{
        height: 24px;
      }}
      .topbar-team-tag {{
        font-size: 11px;
        padding: 4px 10px;
      }}

      /* Hero Section */
      .hero {{
        padding: 24px 16px 20px;
      }}
      .hero-eyebrow {{
        font-size: 10.5px;
        letter-spacing: 1px;
      }}
      .hero h1 {{
        font-size: 21px;
        letter-spacing: -0.3px;
        line-height: 1.25;
      }}
      .hero-stats {{
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 12px 14px;
        margin-top: 16px;
      }}
      .hero-stat-divider {{
        display: none;
      }}
      .hero-stat-val {{
        font-size: 24px;
      }}
      .hero-stat-label {{
        font-size: 11px;
      }}

      /* Navigation Tabs */
      .nav-wrap,
      .nav-wrap.no-sidebar-nav {{
        padding: 0 12px;
      }}
      .nav-bar {{
        overflow-x: auto;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
        gap: 6px;
      }}
      .nav-bar::-webkit-scrollbar {{
        display: none;
      }}
      .nav-tab {{
        padding: 12px 14px;
        font-size: 12.5px;
        flex-shrink: 0;
        gap: 6px;
      }}
      .nav-tab svg {{
        width: 14px;
        height: 14px;
      }}

      /* App Layout */
      .app-layout {{
        padding: 14px 10px !important;
        gap: 14px;
      }}
      .app-layout.no-sidebar {{
        padding: 12px 6px !important;
      }}

      /* Sidebar as Horizontal Swipeable Chips */
      .app-sidebar {{
        width: 100%;
        padding: 10px 10px 6px;
        border-radius: 14px;
        background: var(--surface);
        box-shadow: 0 2px 8px rgba(0,0,0,0.03);
      }}
      .app-sidebar-header {{
        padding: 0 2px 6px;
        margin-bottom: 6px;
      }}
      .app-sidebar-title {{
        font-size: 10.5px;
      }}
      .sidebar-list {{
        display: flex;
        overflow-x: auto;
        gap: 6px;
        padding-bottom: 6px;
        -webkit-overflow-scrolling: touch;
        scrollbar-width: none;
      }}
      .sidebar-list::-webkit-scrollbar {{
        display: none;
      }}
      .sidebar-group-title {{
        display: none;
      }}
      .sidebar-item {{
        flex-shrink: 0;
        padding: 7px 11px;
        font-size: 12px;
        margin-bottom: 0;
        border: 1px solid #E2E8F0;
        background: #F8FAFC;
        border-radius: 999px;
        gap: 6px;
      }}
      .sidebar-item.active {{
        background: #1B59F8;
        border-color: #1B59F8;
        box-shadow: 0 2px 8px rgba(27,89,248,0.25);
      }}
      .sidebar-icon {{
        width: 14px;
        height: 14px;
      }}
      .sidebar-icon svg {{
        width: 13px;
        height: 13px;
      }}
      .sidebar-count {{
        font-size: 10px;
        padding: 1px 6px;
      }}

      /* QA Defect Cards */
      .qa-card {{
        padding: 18px 14px;
        border-radius: 16px;
        margin-bottom: 16px;
      }}
      .qa-card-header {{
        padding-bottom: 12px;
        margin-bottom: 14px;
        gap: 10px;
      }}
      .qa-card-title-group {{
        gap: 8px;
        width: 100%;
      }}
      .qa-id-badge {{
        font-size: 13px;
        padding: 4px 10px;
        border-radius: 8px;
      }}
      .qa-card-title {{
        font-size: 16.5px;
        line-height: 1.3;
        width: 100%;
      }}
      .qa-card-meta-group {{
        flex-wrap: wrap;
        gap: 6px;
        width: 100%;
      }}
      .qa-meta-pill {{
        font-size: 11.5px;
        padding: 4px 8px;
      }}
      .qa-meta-divider {{
        display: none;
      }}
      .qa-module-badge {{
        font-size: 11.5px;
      }}
      .qa-card-body {{
        grid-template-columns: 1fr;
        gap: 16px;
      }}
      .qa-problem-statement {{
        font-size: 13.5px;
        line-height: 1.5;
        margin-bottom: 14px;
      }}
      .qa-accordion {{
        padding-top: 12px;
      }}
      .qa-accordion-title {{
        font-size: 13.5px;
      }}
      .qa-accordion-content {{
        font-size: 12px;
        padding: 10px 12px;
        border-radius: 10px;
      }}
      .qa-evidence-box {{
        border-radius: 12px;
        max-height: 220px;
      }}
      .qa-evidence-overlay-btn {{
        font-size: 10.5px;
        padding: 4px 10px;
        bottom: 8px;
        right: 8px;
      }}

      /* Excel Container & Table */
      .excel-container {{
        border-radius: 14px;
        margin-bottom: 20px;
        border-color: #E2E8F0;
      }}
      .mobile-table-hint {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 6px;
        font-size: 11px;
        font-weight: 600;
        color: #475569;
        background: #F1F5F9;
        padding: 8px 12px;
        border-bottom: 1px solid #CBD5E1;
        text-align: center;
      }}
      .excel-table-wrap {{
        -webkit-overflow-scrolling: touch;
      }}
      .excel-table th,
      .excel-table td {{
        padding: 9px 8px;
        font-size: 11px;
      }}
      .excel-id {{
        font-size: 11px;
        padding: 2px 6px;
      }}
      .excel-badge-status {{
        font-size: 10px;
        padding: 3px 6px;
      }}
      .excel-btn-ev {{
        font-size: 10px;
        padding: 3px 6px;
        gap: 3px;
      }}
      .btn-toggle-row {{
        width: 22px;
        height: 22px;
      }}
      .row-detail-card {{
        padding: 12px 10px;
      }}
      .detail-steps {{
        font-size: 11.5px;
        padding: 8px 10px;
        line-height: 1.5;
      }}
      .detail-tag {{
        font-size: 10px;
        padding: 3px 6px;
      }}
      .excel-statusbar {{
        padding: 8px 10px;
        font-size: 10.5px;
        flex-direction: column;
        align-items: flex-start;
        gap: 4px;
      }}

      /* Modal Dialog */
      .modal-overlay {{
        padding: 10px;
      }}
      .modal-card {{
        border-radius: 14px;
        max-height: 94vh;
      }}
      .modal-header {{
        padding: 10px 14px;
      }}
      .modal-header h3 {{
        font-size: 13.5px;
      }}
      .modal-body {{
        padding: 10px 12px;
      }}
      .modal-body img {{
        max-height: 70vh;
        border-radius: 8px;
      }}

      /* Empty State */
      .empty-module-card {{
        padding: 24px 14px;
        border-radius: 14px;
      }}
      .empty-module-icon {{
        width: 40px;
        height: 40px;
      }}
      .empty-module-title {{
        font-size: 16px;
      }}
      .empty-module-desc {{
        font-size: 12.5px;
      }}
      .btn-empty-reset {{
        font-size: 12px;
        padding: 8px 16px;
      }}
    }}

    @media (max-width: 480px) {{
      .topbar-team-tag {{
        display: none;
      }}
      .hero h1 {{
        font-size: 18px;
      }}
      .hero-stat-val {{
        font-size: 20px;
      }}
      .qa-card-title {{
        font-size: 15px;
      }}
      .nav-tab {{
        padding: 10px 12px;
        font-size: 11.5px;
      }}
    }}
  </style>
</head>
<body>

<!-- TOPBAR -->
<header class="topbar">
  <div class="topbar-inner">
    <div class="topbar-left">
      <img src="assets/logo_controla.png" alt="Controla" class="brand-logo-img">
    </div>
  </div>
</header>

<!-- HERO -->
<section class="hero">
  <div class="hero-inner">
    <h1>Informe de Calidad Funcional &amp; Defectos</h1>
    
    <div class="hero-stats">
      <div class="hero-stat">
        <div class="hero-stat-val">25</div>
        <div class="hero-stat-label">Casos de prueba</div>
      </div>
      <div class="hero-stat-divider"></div>
      <div class="hero-stat">
        <div class="hero-stat-val" style="color:#6EE7B7;">22</div>
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

    <!-- Prominente barra de fechas y responsabilidades eliminada -->
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

<!-- ══════════════════════════════════════════════════════════════ -->
<!-- APP LAYOUT CON SIDEBAR DE 16 MÓDULOS                          -->
<!-- ══════════════════════════════════════════════════════════════ -->
<div class="app-layout">

  <!-- SIDEBAR IZQUIERDO: 16 MÓDULOS DE CONTROLA.PE -->
  <aside class="app-sidebar">
    <div class="app-sidebar-header">
      <span class="app-sidebar-title">Módulos del Sistema</span>
    </div>
    
    <div class="sidebar-list">
      {sidebar_html}
    </div>
  </aside>

  <!-- CONTENIDO PRINCIPAL (TAB 1 Y TAB 2) -->
  <main class="app-main">

    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- TAB 1: REGISTRO DE DEFECTOS (DISEÑO DIIA EXACTO A LA IMAGEN) -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <div id="tab-defectos" class="pane active">

      <!-- DEF-01 -->
      <div class="qa-card" data-module="Dashboard">
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
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>
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
              <span class="qa-evidence-overlay-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Ver evidencia
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- OBS-01 -->
      <div class="qa-card" data-module="Dashboard">
        <div class="qa-card-header">
          <div class="qa-card-title-group">
            <span class="qa-id-badge badge-obs">OBS-01</span>
            <h2 class="qa-card-title">Pérdida de Contraste en Modo Oscuro</h2>
          </div>
          <div class="qa-card-meta-group">
            <span class="qa-meta-pill pill-warn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
              Observación UX
            </span>
            <div class="qa-meta-divider"></div>
            <span class="qa-module-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="9"/><rect x="14" y="3" width="7" height="5"/><rect x="14" y="12" width="7" height="9"/><rect x="3" y="16" width="7" height="5"/></svg>
              Dashboard
            </span>
          </div>
        </div>
        <div class="qa-card-body">
          <div class="qa-col-left">
            <div class="qa-section-label">QUÉ SUCEDE</div>
            <div class="qa-problem-statement">
              Al activar el modo oscuro, las etiquetas y meses en los gráficos Highcharts conservan color gris oscuro fijo (#333333) dificultando su lectura.
            </div>
            <div class="qa-accordion">
              <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-obs-01', this)">
                <span class="qa-accordion-title">Causa técnica</span>
                <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
              </div>
              <div id="cause-obs-01" class="qa-accordion-content">
                Las opciones de Highcharts tienen estilos en línea estáticos en lugar de clases CSS o variables dinámicas adaptadas al tema oscuro.
              </div>
            </div>
          </div>
          <div class="qa-col-right">
            <div class="qa-section-label">EVIDENCIA</div>
            <div class="qa-evidence-box" onclick="openModal('evidencias/OBS-01_contraste_dark_mode.png','OBS-01: Contraste deficiente en modo oscuro')">
              <img class="qa-evidence-img" src="evidencias/OBS-01_contraste_dark_mode.png" alt="OBS-01 Evidencia">
              <span class="qa-evidence-overlay-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Ver evidencia
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- DEF-03 -->
      <div class="qa-card" data-module="Sucursales">
        <div class="qa-card-header">
          <div class="qa-card-title-group">
            <span class="qa-id-badge">DEF-03</span>
            <h2 class="qa-card-title">Colisión en Breadcrumbs de Barra Superior</h2>
          </div>
          <div class="qa-card-meta-group">
            <span class="qa-meta-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
              S3 • Media
            </span>
            <div class="qa-meta-divider"></div>
            <span class="qa-module-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M8 10h.01M16 10h.01M8 14h.01M16 14h.01"/></svg>
              Sucursales
            </span>
          </div>
        </div>
        <div class="qa-card-body">
          <div class="qa-col-left">
            <div class="qa-section-label">QUÉ SUCEDE</div>
            <div class="qa-problem-statement">
              En resoluciones de laptops (1024 a 1280px), la ruta de migas de pan se trunca a “Dash” y el botón de tema se superpone directamente encima.
            </div>
            <div class="qa-accordion">
              <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-def-03', this)">
                <span class="qa-accordion-title">Causa técnica</span>
                <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
              </div>
              <div id="cause-def-03" class="qa-accordion-content">
                El contenedor flexible de la barra superior carece de <code>flex-wrap: wrap</code> y no tiene un ancho mínimo (<code>min-width</code>) para salvaguardar el bloque de breadcrumbs.
              </div>
            </div>
          </div>
          <div class="qa-col-right">
            <div class="qa-section-label">EVIDENCIA</div>
            <div class="qa-evidence-box" onclick="openModal('evidencias/DEF-03_colision_breadcrumbs_navbar.png','DEF-03: Truncamiento y colisión en breadcrumbs')">
              <img class="qa-evidence-img" src="evidencias/DEF-03_colision_breadcrumbs_navbar.png" alt="DEF-03 Evidencia">
              <span class="qa-evidence-overlay-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Ver evidencia
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- OBS-02 -->
      <div class="qa-card" data-module="Sucursales">
        <div class="qa-card-header">
          <div class="qa-card-title-group">
            <span class="qa-id-badge badge-obs">OBS-02</span>
            <h2 class="qa-card-title">Falta de Estado Vacío en Búsqueda</h2>
          </div>
          <div class="qa-card-meta-group">
            <span class="qa-meta-pill pill-warn">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
              Observación UX
            </span>
            <div class="qa-meta-divider"></div>
            <span class="qa-module-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M8 10h.01M16 10h.01M8 14h.01M16 14h.01"/></svg>
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
              <span class="qa-evidence-overlay-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Ver evidencia
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- OBS-03 -->
      <div class="qa-card" data-module="Sucursales">
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
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M8 10h.01M16 10h.01M8 14h.01M16 14h.01"/></svg>
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
              <span class="qa-evidence-overlay-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Ver evidencia
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- DEF-04 -->
      <div class="qa-card" data-module="Tareas">
        <div class="qa-card-header">
          <div class="qa-card-title-group">
            <span class="qa-id-badge">DEF-04</span>
            <h2 class="qa-card-title">Desbordamiento y Botones Ocultos en Detalle de Tarea</h2>
          </div>
          <div class="qa-card-meta-group">
            <span class="qa-meta-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 20V10M12 20V4M6 20v-6"/></svg>
              S3 • Media
            </span>
            <div class="qa-meta-divider"></div>
            <span class="qa-module-badge">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>
              Tareas
            </span>
          </div>
        </div>
        <div class="qa-card-body">
          <div class="qa-col-left">
            <div class="qa-section-label">QUÉ SUCEDE</div>
            <div class="qa-problem-statement">
              Al abrir el modal "Ver Tarea", el cuadro de diálogo es demasiado estrecho (512px) y se desborda horizontalmente: los botones "Editar" y "Cancelar" quedan cortados fuera de la pantalla (offscreen) y la pestaña "Historial" queda cercenada, forzando una barra de scroll horizontal en la base del diálogo.
            </div>
            <div class="qa-accordion">
              <div class="qa-accordion-trigger" onclick="toggleAccordion('cause-def-04', this)">
                <span class="qa-accordion-title">Causa técnica</span>
                <svg class="qa-accordion-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m6 9 6 6 6-6"/></svg>
              </div>
              <div id="cause-def-04" class="qa-accordion-content">
                El contenedor modal utiliza una clase fija restrictiva (<code>max-w-lg</code> = 512px) que no soporta el ancho del conjunto de botones de acción en la cabecera (ancho acumulado superior a 470px) con <code>flex-wrap: nowrap</code>. Se requiere ampliar a <code>max-w-2xl</code> o <code>max-w-3xl</code> y añadir <code>flex-wrap: wrap</code> al contenedor de botones.
              </div>
            </div>
          </div>
          <div class="qa-col-right">
            <div class="qa-section-label">EVIDENCIA</div>
            <div class="qa-evidence-box" onclick="openModal('evidencias/DEF-04_modal_tarea_crop.png','DEF-04: Botones offscreen y desbordamiento en modal de detalle de Tarea')">
              <img class="qa-evidence-img" src="evidencias/DEF-04_modal_tarea_crop.png" alt="DEF-04 Evidencia">
              <span class="qa-evidence-overlay-btn">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                Ver evidencia
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- Placeholder cuando un módulo sin defectos es seleccionado en Tab 1 -->
      <div id="defectsEmptyModule" class="empty-module-card" style="display: none;">
        <div class="empty-module-icon">
          <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        </div>
        <h3 id="defectsEmptyTitle" class="empty-module-title">Módulo: Calendario</h3>
        <div class="empty-module-badge" style="background:#DCFCE7; color:#166534;">SIN DEFECTOS REPORTADOS</div>
        <p class="empty-module-desc">
          Este módulo no registra defectos activos en el ciclo de pruebas del <strong>16/11/2026</strong>.
        </p>
        <button class="btn-empty-reset" onclick="selectSidebarModule('all', event)">Ver todos los hallazgos (6)</button>
      </div>

    </div>

    <!-- ══════════════════════════════════════════════════════════════ -->
    <!-- TAB 2: MATRIZ DE CASOS DE PRUEBA (TABLA EXCEL PROFESIONAL)  -->
    <!-- ══════════════════════════════════════════════════════════════ -->
    <div id="tab-matriz" class="pane">

      <div class="excel-container">
        
        <div class="mobile-table-hint">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8L22 12L18 16"/><path d="M6 8L2 12L6 16"/><path d="M2 12H22"/></svg>
          Desliza la tabla hacia los lados para ver todas las columnas
        </div>

        <!-- Tabla Grid Excel con 13 Columnas Principales + Ficha Desplegable -->
        <div class="excel-table-wrap">
          <table class="excel-table" id="excelMatrixTable">
            <thead>
              <tr>
                <th style="width: 40px; text-align: center;">Ficha</th>
                <th style="width: 95px;">ID Caso</th>
                <th style="width: 105px;">
                  <span style="display:inline-flex; align-items:center; gap:4px;">
                    <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
                    Fecha Detección
                  </span>
                </th>
                <th style="width: 110px;">Perfil / Rol</th>
                <th style="width: 160px;">Módulo / Componente</th>
                <th style="min-width: 220px;">¿Qué se prueba? (Descripción)</th>
                <th style="min-width: 200px;">¿Qué debería pasar? (Esperado)</th>
                <th style="min-width: 220px;">Resultado Obtenido</th>
                <th style="width: 85px;">Severidad</th>
                <th style="width: 85px;">Prioridad</th>
                <th style="width: 110px; text-align: center;">Estado</th>
                <th style="width: 80px; text-align: center;">Hallazgo</th>
                <th style="width: 100px; text-align: center;">Evidencia</th>
              </tr>
            </thead>
            <tbody id="excelTableBody">
              {rows_html}
            </tbody>
          </table>
        </div>

        <!-- Placeholder para módulos en cola sin casos de prueba -->
        <div id="excelEmptyModule" class="empty-module-card" style="display: none;">
          <div class="empty-module-icon">
            <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          </div>
          <h3 id="emptyModuleTitle" class="empty-module-title">Módulo: Calendario</h3>
          <div class="empty-module-badge">EN COLA DE AUDITORÍA</div>
          <p class="empty-module-desc">
            Este módulo forma parte de la arquitectura de 16 módulos de <strong>plaeis.controla.pe</strong>. En el ciclo de pruebas actual del <strong>16/11/2026</strong>, no registra defectos ni casos reportados.
          </p>
          <button class="btn-empty-reset" onclick="selectSidebarModule('all', event)">Ver todos los casos auditados (11)</button>
        </div>

      </div>

    </div>

  </main>
</div>

<!-- ══════════════════════════════════════════════════════════════ -->
<!-- MODAL DE EVIDENCIA EN ALTA RESOLUCIÓN                         -->
<!-- ══════════════════════════════════════════════════════════════ -->
<div id="image-modal" class="modal-overlay" onclick="closeModal(event)">
  <div class="modal-card">
    <div class="modal-header">
      <h3 id="modal-title">Evidencia de Auditoría QA</h3>
      <button class="modal-close" onclick="closeModal()">✕</button>
    </div>
    <div class="modal-body">
      <img id="modal-image" src="" alt="Evidencia ampliada">
    </div>
  </div>
</div>

<script>
  let currentActiveTab = 'defectos';
  let currentSelectedModule = 'all';
  const allCases = {cases_json};

  function switchTab(tabName, evt) {{
    currentActiveTab = tabName;
    const layout = document.querySelector('.app-layout');
    const navWrap = document.querySelector('.nav-wrap');
    document.querySelectorAll('.pane').forEach(p => p.classList.remove('active'));
    document.querySelectorAll('.nav-tab').forEach(t => t.classList.remove('active'));
    
    if (tabName === 'defectos') {{
      if (layout) layout.classList.remove('no-sidebar');
      if (navWrap) navWrap.classList.remove('no-sidebar-nav');
      document.getElementById('tab-defectos').classList.add('active');
      if (evt) evt.currentTarget.classList.add('active');
      else document.querySelectorAll('.nav-tab')[0].classList.add('active');
      applyModuleFilter();
    }} else {{
      if (layout) layout.classList.add('no-sidebar');
      if (navWrap) navWrap.classList.add('no-sidebar-nav');
      document.getElementById('tab-matriz').classList.add('active');
      if (evt) evt.currentTarget.classList.add('active');
      else document.querySelectorAll('.nav-tab')[1].classList.add('active');

      // En la matriz de casos de prueba solo va el Excel a pantalla completa
      const tableWrap = document.querySelector('.excel-table-wrap');
      const emptyBox = document.getElementById('excelEmptyModule');
      if (tableWrap) tableWrap.style.display = '';
      if (emptyBox) emptyBox.style.display = 'none';

      // Resetear filtros del toolbar de Excel a "Todos"
      document.querySelectorAll('.excel-fpill').forEach(p => p.classList.remove('active'));
      const firstPill = document.querySelector('.excel-fpill');
      if (firstPill) firstPill.classList.add('active');

      const dataRows = document.querySelectorAll('.excel-data-row');
      dataRows.forEach(row => row.style.display = '');

      const countEl = document.getElementById('excelRowCount');
      if (countEl) countEl.textContent = '25 casos mostrados de 25 totales';
      const headerTitle = document.getElementById('excelHeaderTitle');
      if (headerTitle) headerTitle.textContent = 'Matriz Completa de Pruebas QA (Libro de Validación)';
      const headerSubtitle = document.getElementById('excelHeaderSubtitle');
      if (headerSubtitle) headerSubtitle.textContent = '25 casos auditados • 16 Módulos y 5 Fases del Negocio • Vista tabular tipo hoja de cálculo';
    }}
  }}

  function toggleAccordion(id, el) {{
    const content = document.getElementById(id);
    const isOpen = content.classList.contains('open');
    if (isOpen) {{
      content.classList.remove('open');
      el.classList.remove('open');
    }} else {{
      content.classList.add('open');
      el.classList.add('open');
    }}
  }}

  function toggleRowDetail(detailId, btn) {{
    const row = document.getElementById(detailId);
    if (!row) return;
    const isHidden = row.style.display === 'none' || row.style.display === '';
    if (isHidden) {{
      row.style.display = 'table-row';
      btn.classList.add('open');
    }} else {{
      row.style.display = 'none';
      btn.classList.remove('open');
    }}
  }}

  /* ── SIDEBAR SELECTION (16 MÓDULOS) ── */
  function selectSidebarModule(modId, el) {{
    currentSelectedModule = modId;
    
    // Update sidebar active classes
    document.querySelectorAll('.sidebar-item').forEach(item => item.classList.remove('active'));
    if (el) {{
      el.classList.add('active');
    }} else {{
      const match = document.querySelector(`.sidebar-item[data-mod-id="${{modId}}"]`);
      if (match) match.classList.add('active');
    }}

    applyModuleFilter();
  }}

  function applyModuleFilter() {{
    const modId = currentSelectedModule;
    
    // 1. Filtrar Tab 1 (Defectos)
    const defectCards = document.querySelectorAll('.qa-card');
    let visibleDefects = 0;
    defectCards.forEach(card => {{
      const cardMod = card.getAttribute('data-module');
      if (modId === 'all' || cardMod === modId) {{
        card.style.display = '';
        visibleDefects++;
      }} else {{
        card.style.display = 'none';
      }}
    }});

    const defectsEmpty = document.getElementById('defectsEmptyModule');
    if (visibleDefects === 0 && modId !== 'all') {{
      defectsEmpty.style.display = 'block';
      document.getElementById('defectsEmptyTitle').textContent = 'Módulo: ' + modId;
    }} else {{
      defectsEmpty.style.display = 'none';
    }}

    // 2. Filtrar Tab 2 (Tabla Excel)
    const dataRows = document.querySelectorAll('.excel-data-row');
    const tableWrap = document.querySelector('.excel-table-wrap');
    const emptyBox = document.getElementById('excelEmptyModule');
    let visibleRows = 0;

    dataRows.forEach(row => {{
      const rowMod = row.getAttribute('data-module');
      const detailId = 'detail-' + row.id.replace('row-', '');
      const detailRow = document.getElementById(detailId);

      if (modId === 'all' || rowMod === modId) {{
        row.style.display = '';
        visibleRows++;
      }} else {{
        row.style.display = 'none';
        if (detailRow) detailRow.style.display = 'none';
      }}
    }});

    const countEl = document.getElementById('excelRowCount');
    const headerTitle = document.getElementById('excelHeaderTitle');
    const headerSubtitle = document.getElementById('excelHeaderSubtitle');

    if (visibleRows === 0 && modId !== 'all') {{
      tableWrap.style.display = 'none';
      emptyBox.style.display = 'block';
      document.getElementById('emptyModuleTitle').textContent = 'Módulo: ' + modId;
      if (countEl) countEl.textContent = '0 casos en el módulo ' + modId;
      if (headerTitle) headerTitle.textContent = 'Módulo: ' + modId + ' (En cola de evaluación)';
      if (headerSubtitle) headerSubtitle.textContent = 'Sin casos ni defectos ejecutados en el ciclo de pruebas del 16/11/2026';
    }} else {{
      tableWrap.style.display = '';
      emptyBox.style.display = 'none';
      if (modId === 'all') {{
        if (countEl) countEl.textContent = '25 casos mostrados de 25 totales';
        if (headerTitle) headerTitle.textContent = 'Matriz Completa de Pruebas QA (Libro de Validación)';
        if (headerSubtitle) headerSubtitle.textContent = '25 casos auditados • 16 Módulos y 5 Fases del Negocio • Vista tabular tipo hoja de cálculo';
      }} else {{
        if (countEl) countEl.textContent = visibleRows + ' casos mostrados en ' + modId;
        if (headerTitle) headerTitle.textContent = 'Matriz de Pruebas • Módulo ' + modId;
        if (headerSubtitle) headerSubtitle.textContent = visibleRows + ' casos ejecutados en ' + modId + ' • Fecha: 16/11/2026';
      }}
    }}
  }}

  function filterExcelCategory(cat, evt) {{
    document.querySelectorAll('.excel-fpill').forEach(p => p.classList.remove('active'));
    if (evt) evt.currentTarget.classList.add('active');

    const dataRows = document.querySelectorAll('.excel-data-row');
    let count = 0;
    dataRows.forEach(row => {{
      const rowMod = row.getAttribute('data-module') || '';
      const rowStatus = row.getAttribute('data-status') || '';
      const rowStage = row.getAttribute('data-stage') || '';
      const detailId = 'detail-' + row.id.replace('row-', '');
      const detailRow = document.getElementById(detailId);

      let matches = false;
      if (cat === 'all') {{
        matches = true;
      }} else if (cat === 'PASS') {{
        matches = rowStatus.includes('PASS');
      }} else if (cat === 'FAIL') {{
        matches = (rowStatus === 'FAIL');
      }} else if (cat.startsWith('Fase')) {{
        matches = rowStage.toLowerCase().includes(cat.toLowerCase());
      }} else {{
        matches = (rowMod === cat || rowStage.includes(cat));
      }}

      if (matches) {{
        row.style.display = '';
        count++;
      }} else {{
        row.style.display = 'none';
        if (detailRow) detailRow.style.display = 'none';
      }}
    }});
    const cEl = document.getElementById('excelRowCount');
    if (cEl) cEl.textContent = count + ' casos mostrados de 25 totales';
  }}

  function filterExcelTable() {{
    const searchEl = document.getElementById('excelSearch');
    if (!searchEl) return;
    const query = searchEl.value.toLowerCase();
    const dataRows = document.querySelectorAll('.excel-data-row');
    let count = 0;

    dataRows.forEach(row => {{
      const text = row.textContent.toLowerCase();
      const detailId = 'detail-' + row.id.replace('row-', '');
      const detailRow = document.getElementById(detailId);

      const matchesQuery = text.includes(query);

      if (matchesQuery) {{
        row.style.display = '';
        count++;
      }} else {{
        row.style.display = 'none';
        if (detailRow) detailRow.style.display = 'none';
      }}
    }});
    const cEl = document.getElementById('excelRowCount');
    if (cEl) cEl.textContent = count + ' casos encontrados';
  }}

  function exportMatrixToCSV() {{
    const headers = [
      "ID Caso", "Fecha Deteccion", "Perfil / Rol", "Modulo / Componente",
      "Descripcion de la Falla", "Pasos para Reproducir", "Resultado Esperado", "Resultado Obtenido",
      "Severidad", "Prioridad", "Estado", "Ambiente", "Reportado por", "Supervisado por", "Asignado a",
      "Evidencia", "Observaciones", "Fecha de Cierre"
    ];

    let csvContent = "\\uFEFF" + headers.map(h => `"${{h}}"`).join(",") + "\\n";

    allCases.forEach(c => {{
      const cleanSteps = c.steps.replace(/<br>/g, " | ");
      const row = [
        c.id, c.date, c.role, c.component,
        c.description, cleanSteps, c.expected, c.obtained,
        c.severity, c.priority, c.status, c.environment, c.reporter, c.supervisor || "Sandra Chabaneix (Jefa de QA)", c.assignee,
        c.evidence || "—", c.notes || "—", c.closeDate
      ];
      csvContent += row.map(v => `"${{String(v).replace(/"/g, '""')}}"`).join(",") + "\\n";
    }});

    const blob = new Blob([csvContent], {{ type: 'text/csv;charset=utf-8;' }});
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.setAttribute("href", url);
    link.setAttribute("download", "Matriz_Casos_Prueba_Controla_16_Modulos.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }}

  function openModal(src, title) {{
    document.getElementById('modal-image').src = src;
    document.getElementById('modal-title').textContent = title;
    document.getElementById('image-modal').classList.add('active');
  }}

  function closeModal(e) {{
    if (!e || e.target === document.getElementById('image-modal'))
      document.getElementById('image-modal').classList.remove('active');
  }}

  document.addEventListener('keydown', e => {{
    if (e.key === 'Escape') document.getElementById('image-modal').classList.remove('active');
  }});
</script>
</body>
</html>
"""

with open(r'd:\CONTROLA-2026\index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print("Full Portal with 16 Modules Sidebar built successfully!")
