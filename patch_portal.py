import re

with open(r'd:\CONTROLA-2026\build_full_excel_portal.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update modules_list count dynamically
old_sidebar_prep = '''sidebar_html = ""
current_group = None
for m in modules_list:'''

new_sidebar_prep = '''from collections import Counter
mod_counts = Counter(c["module"] for c in cases_data)
mod_fails = Counter(c["module"] for c in cases_data if "FAIL" in c.get("status", ""))

for m in modules_list:
    if m["id"] == "all":
        m["count"] = len(cases_data)
        m["badge"] = f"{len(cases_data)} casos"
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
for m in modules_list:'''

if old_sidebar_prep in content:
    content = content.replace(old_sidebar_prep, new_sidebar_prep, 1)
    print('Updated dynamic sidebar!')
else:
    print('Could not find old_sidebar_prep')

# 2. Update hero stats
old_hero = '''    <div class="hero-stats">
      <div class="hero-stat">
        <div class="hero-stat-val">12</div>
        <div class="hero-stat-label">Casos de prueba</div>
      </div>
      <div class="hero-stat-divider"></div>
      <div class="hero-stat">
        <div class="hero-stat-val" style="color:#6EE7B7;">9</div>
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
    </div>'''

new_hero = '''    <div class="hero-stats">
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
    </div>'''

if old_hero in content:
    content = content.replace(old_hero, new_hero, 1)
    print('Updated hero stats!')
else:
    print('Could not find old_hero')

# 3. Update subtitle and filter pills
old_toolbar = '''          <div class="excel-title-group">
            <div class="excel-sheet-icon">X</div>
            <div>
              <div class="excel-title" id="excelHeaderTitle">Matriz Completa de Pruebas QA (Libro de Validación)</div>
              <div class="excel-subtitle" id="excelHeaderSubtitle">12 casos auditados • Módulos Dashboard, Sucursales y Tareas • Vista tabular tipo hoja de cálculo</div>
            </div>
          </div>

          <div class="excel-controls">
            <button class="btn-export-csv" onclick="exportMatrixToCSV()" title="Descargar como archivo CSV para Excel">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
              Exportar Excel (.csv)
            </button>
            <input type="text" id="excelSearch" class="excel-search-input" placeholder="🔍 Buscar por ID, componente, falla..." onkeyup="filterExcelTable()">
            <div class="excel-filters">
              <button class="excel-fpill active" onclick="filterExcelCategory('all', event)">Todos (12)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('PASS', event)">✓ PASS (9)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('FAIL', event)">✕ FAIL (3)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Dashboard', event)">Dashboard (6)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Sucursales', event)">Sucursales (5)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Tareas', event)">Tareas (1)</button>
            </div>
          </div>'''

new_toolbar = '''          <div class="excel-title-group">
            <div class="excel-sheet-icon">X</div>
            <div>
              <div class="excel-title" id="excelHeaderTitle">Matriz Completa de Pruebas QA (Libro de Validación)</div>
              <div class="excel-subtitle" id="excelHeaderSubtitle">25 casos auditados • 16 Módulos y 5 Fases del Negocio • Vista tabular tipo hoja de cálculo</div>
            </div>
          </div>

          <div class="excel-controls">
            <button class="btn-export-csv" onclick="exportMatrixToCSV()" title="Descargar como archivo CSV para Excel">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
              Exportar Excel (.csv)
            </button>
            <input type="text" id="excelSearch" class="excel-search-input" placeholder="🔍 Buscar por ID, componente, falla..." onkeyup="filterExcelTable()">
            <div class="excel-filters">
              <button class="excel-fpill active" onclick="filterExcelCategory('all', event)">Todos (25)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('PASS', event)">✓ PASS (22)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('FAIL', event)">✕ FAIL (3)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Fase 1', event)">Fase 1: Configurar (8)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Fase 2', event)">Fase 2: Planificar (2)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Fase 3', event)">Fase 3: Ejecutar (4)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Fase 4', event)">Fase 4: Evidencias (4)</button>
              <button class="excel-fpill" onclick="filterExcelCategory('Fase 5', event)">Fase 5: Evaluar (7)</button>
            </div>
          </div>'''

if old_toolbar in content:
    content = content.replace(old_toolbar, new_toolbar, 1)
    print('Updated toolbar and pills!')
else:
    print('Could not find old_toolbar')

# 4. Update JS strings
content = content.replace("'12 casos mostrados de 12 totales'", "'25 casos mostrados de 25 totales'")
content = content.replace("'12 casos auditados • Módulos Dashboard, Sucursales y Tareas • Vista tabular tipo hoja de cálculo'", "'25 casos auditados • 16 Módulos y 5 Fases del Negocio • Vista tabular tipo hoja de cálculo'")

# 5. Update filterExcelCategory in JS
old_filter_js = '''  function filterExcelCategory(cat, evt) {{
    document.querySelectorAll('.excel-fpill').forEach(p => p.classList.remove('active'));
    if (evt) evt.currentTarget.classList.add('active');

    const dataRows = document.querySelectorAll('.excel-data-row');
    let count = 0;
    dataRows.forEach(row => {{
      const rowMod = row.getAttribute('data-module');
      const rowStatus = row.getAttribute('data-status');
      const detailId = 'detail-' + row.id.replace('row-', '');
      const detailRow = document.getElementById(detailId);

      let matches = false;
      if (cat === 'all') {{
        matches = true;
      }} else if (cat === 'PASS' || cat === 'FAIL') {{
        matches = (rowStatus === cat);
      }} else {{
        matches = (rowMod === cat);
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
    if (cEl) cEl.textContent = count + ' casos mostrados';
  }}'''

new_filter_js = '''  function filterExcelCategory(cat, evt) {{
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
  }}'''

if old_filter_js in content:
    content = content.replace(old_filter_js, new_filter_js, 1)
    print('Updated filterExcelCategory JS!')
else:
    print('Could not find old_filter_js')

with open(r'd:\CONTROLA-2026\build_full_excel_portal.py', 'w', encoding='utf-8') as f:
    f.write(content)

print('Finished patching build_full_excel_portal.py')
