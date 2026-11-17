# INFORME EJECUTIVO DE CONTROL DE CALIDAD (QA)
**Proyecto:** Plataforma Empresarial Controla.pe  
**Instancia Evaluada:** `https://plaeis.controla.pe`  
**Cliente Solicitante:** Sandra Chabaneix  
**Organización Auditada:** PLAEIS ENTERTAINMENT  
**Fecha:** 16 de Noviembre de 2026  
**Versión del Documento:** 1.0 (Local Master)  

---

## 1. Alcance y Metodología
La auditoría se realizó bajo la perspectiva de una **empresa cliente**, con enfoque de pruebas no destructivas sin alteración de base de datos productiva, sin transacciones de pago ni eliminaciones.

Se utilizó la identidad de marca del repositorio oficial de diseño en **Figma (`CONTROLA WEB - FINAL`)** como referencia estricta de componentes atómicos, colores corporativos (azul `#0084F8`, marino `#002B49`), tipografía sans-serif e iconografía.

### Criterios de Aceptación y Clasificación
- **Casos Aprobados (PASS):** El sistema cumple las expectativas funcionales y de seguridad. Las validaciones negativas (rechazo de campos obligatorios vacíos) se consideran **aprobadas** por proteger la integridad del sistema.
- **Defectos Confirmados (Bugs):** Inconsistencias reproducibles en interfaz (CSS/Layout), fallos en enlaces de red (4xx/5xx) o errores de renderizado.
- **Observaciones de Usabilidad / Negocio:** Recomendaciones de experiencia de usuario (UX), accesibilidad (WCAG) o restricciones de plan comercial.

---

## 2. Inventario de Funcionalidades Evaluadas (16 Módulos del Sistema)

| Módulo | Submódulos Auditados | Estado de Evaluación |
| :--- | :--- | :--- |
| **MOD-01 Dashboard** | Métricas KPI, Gráficos Highcharts, Conmutador de Tema, Toggle Sidebar, Perfil | **1 Defecto Confirmado (DEF-01) • 1 Obs (OBS-01)** |
| **MOD-02 Sucursales** | Tabla de sedes, Filtro de búsqueda, Validación de campos requeridos, Modal de detalle | **1 Defecto Confirmado (DEF-03) • 2 Obs (OBS-02, OBS-03)** |
| **MOD-03 Calendario** | Grilla mensual, Vista de eventos SST, Navegación de meses | **✓ 100% Conforme (PASS)** |
| **MOD-04 Empleados** | Listado, Paginación, Filtros y Wizard Modal de Nuevo Empleado | **✓ 100% Conforme (PASS)** |
| **MOD-05 Contratistas** | Empresas contratistas y Trabajadores, Modales de alta | **✓ 100% Conforme (PASS)** |
| **MOD-06 Capacitaciones** | Asistente de creación, Métricas de cumplimiento y Reportes | **✓ 100% Conforme (PASS)** |
| **MOD-07 Herramientas SST** | Matriz IPERC, ATS, PETAR, PETS, Estándares | **✓ 100% Conforme (PASS)** |
| **MOD-08 Tareas** | Dashboard de Tareas, Listado y Modal de Detalle de Tarea | **1 Defecto Confirmado (DEF-04)** |
| **MOD-09 Documentos SST** | 10 visores y flujos (Política, RISST, Mapa de Riesgos, etc.) | **✓ 100% Conforme (PASS)** |
| **MOD-10 Programa Anual** | Seguimiento anual, Programas y Capítulos PASST (RM 050-2013-TR) | **✓ 100% Conforme (PASS)** |
| **MOD-11 Registros SST** | 11 registros oficiales (Accidentes, Exámenes Médicos, Monitoreo, etc.) | **✓ 100% Conforme (PASS)** |
| **MOD-12 Línea Base SST** | Diagnósticos iniciales y Plantillas de evaluación | **✓ 100% Conforme (PASS)** |
| **MOD-13 Libro de Actas** | Comités SST y Reporte de cumplimiento de acuerdos | **✓ 100% Conforme (PASS)** |
| **MOD-14 Notificaciones** | Bandeja de notificaciones y Configuración de plantillas | **✓ 100% Conforme (PASS)** |
| **MOD-15 Catálogos** | Cargos, Departamentos, EPP, Herramientas y Equipos | **✓ 100% Conforme (PASS)** |
| **MOD-16 Autorización** | Módulos, Roles y Permisos, Gestión de Usuarios | **✓ 100% Conforme (PASS)** |

---

## 3. Métricas de Calidad
- **Total de Casos de Prueba Ejecutados:** 12
- **Casos Aprobados (PASS):** 9 (75%)
- **Casos con Defecto Confirmado (FAIL):** 3 (25% - DEF-01, DEF-03 y DEF-04)
- **Observaciones de Usabilidad / Negocio:** 3 (OBS-01, OBS-02 y OBS-03)
- **Defectos Críticos (S1) / Altos (S2):** 0 (Estabilidad general del backend y formularios confirmada)
- **Defectos Medios (S3):** 3 (Maquetación, responsividad y desbordamiento en modales)
- **Defectos Descartados tras Reevaluación:** 1 (DEF-02 - Logo visible al retraer menú)

---

## 4. Dictamen Final y Recomendaciones para Sandra Chabaneix
1. **Estabilidad y Reglas de Negocio:** El sistema opera de manera estable en backend y lógica de formularios a lo largo de los 16 módulos auditados. No se detectaron errores HTTP 500 ni caídas de servidor.
2. **Correcciones Prioritarias de Frontend (Fallas en Rojo):**
   - **DEF-01 (Dashboard):** Corregir espaciado inferior (`overflow: hidden` o `padding-bottom`) en tarjetas Highcharts para evitar invasión sobre títulos inferiores.
   - **DEF-03 (Navbar):** Ajustar flexbox de la barra superior con `flex-wrap` y `min-width` para evitar colisión de selector de tema sobre breadcrumbs en resoluciones intermedias (1280px).
   - **DEF-04 (Tareas):** Ampliar el ancho del modal de detalle de tarea a `max-w-2xl` o `max-w-3xl` e implementar `flex-wrap: wrap` en la fila de botones de acción para que "Editar" y "Cancelar" no queden fuera de pantalla (offscreen).
3. **Accesibilidad:** Configurar Highcharts en modo oscuro para que las etiquetas adopten colores claros (`#E2E8F0`) mejorando el contraste visual (OBS-01).
