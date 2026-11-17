# REGISTRO DIRECTO DE DEFECTOS Y OBSERVACIONES
**Proyecto:** Controla.pe (Plaeis Entertainment)  
**Destinatario:** Sandra Chabaneix  
**Auditor:** QA Tester Manual Profesional  
**Formato:** Directo (Problema + Razón Técnica)  

---

## 🐛 DEF-01: Solapamiento visual de leyendas Highcharts sobre tarjetas inferiores
* **Módulo:** MOD-01 Dashboard (`/dashboard`)
* **Severidad:** S3 - Media (Impacto en Maquetación / Layout)
* **Estado:** Abierto / Confirmado
* **🔴 Problema:** Las leyendas de los gráficos analíticos superiores se desbordan hacia abajo e invaden las tarjetas inferiores, solapándose directamente sobre los títulos `"Usuarios por Estado"` y `"Usuarios por Rol"`.
* **💡 Razón Técnica:** El contenedor de Highcharts carece de `overflow: hidden` y de un margen inferior (`padding-bottom`) adecuado para contener las etiquetas dinámicas generadas por las series de datos en resolución de escritorio.
* **Evidencia con Flechas:** [`../evidencias/DEF-01_solapamiento_leyendas_dashboard.png`](file:///d:/CONTROLA-2026/evidencias/DEF-01_solapamiento_leyendas_dashboard.png)

---

## 🐛 DEF-02: [DESCARTADO / CONFORME] Visualización de logotipo corporativo al retraer menú
* **Módulo:** MOD-01 Dashboard & Shell Global
* **Severidad:** N/A - Retirado
* **Estado:** Descartado / Conforme tras reevaluación técnica
* **🟢 Conclusión:** Se verificó que al retraer el menú lateral, la interfaz se adapta fluidamente y el logotipo/isotipo sí se muestra visible y centrado en la barra superior. El caso CP-DASH-04 se reclasificó como **PASS**.

---

## 🐛 DEF-03: Truncamiento de Breadcrumbs y solapamiento de selector de tema
* **Módulo:** Shell Global / MOD-02 Sucursales (`/branches`)
* **Severidad:** S3 - Media (Maquetación Responsiva Navbar)
* **Estado:** Abierto / Confirmado
* **🔴 Problema:** En resoluciones intermedias (1024 a 1280px), la ruta de migas de pan queda truncada a `"Dash"` y el selector de tema (*Light/Dark*) se monta visualmente encima de la palabra.
* **💡 Razón Técnica:** El contenedor flexbox de la barra superior no cuenta con `flex-wrap` ni define un `min-width` para el texto de la ruta, permitiendo que el contenedor derecho de controles invada el espacio de lectura.
* **Evidencia con Flechas:** [`../evidencias/DEF-03_colision_breadcrumbs_navbar.png`](file:///d:/CONTROLA-2026/evidencias/DEF-03_colision_breadcrumbs_navbar.png)

---

## 🐛 DEF-04: Desbordamiento horizontal y botones de acción ocultos en modal de detalle de Tarea
* **Módulo:** MOD-06 Tareas (`/tasks`)
* **Severidad:** S3 - Media (Maquetación CSS / Usabilidad Funcional)
* **Estado:** Abierto / Confirmado
* **🔴 Problema:** Al abrir el diálogo modal de detalle de una tarea existente (ej. `TASK-2026-00001`), el contenedor es excesivamente estrecho (512px). Los botones de acción de cabecera ("Editar" y "Cancelar") desbordan el marco derecho quedando completamente invisibles fuera de pantalla (offscreen). La pestaña "Historial" se visualiza cortada y se genera un scrollbar horizontal forzado en la base del modal.
* **💡 Razón Técnica:** Falta ampliar el contenedor modal a `max-w-2xl` o `max-w-3xl` e implementar `flex-wrap: wrap` en la fila de botones de acción para prevenir desbordamientos horizontales.
* **Evidencia:** [`../evidencias/DEF-04_modal_tarea_crop.png`](file:///d:/CONTROLA-2026/evidencias/DEF-04_modal_tarea_crop.png) y vista completa en [`../evidencias/DEF-04_desbordamiento_modal_detalle_tarea.png`](file:///d:/CONTROLA-2026/evidencias/DEF-04_desbordamiento_modal_detalle_tarea.png)

---

## 👁️ OBSERVACIONES Y CONDICIONES DE NEGOCIO

### OBS-01: Bajo contraste de etiquetas en Modo Oscuro (Highcharts)
* **Módulo:** MOD-01 Dashboard
* **Severidad:** S4 - Baja (Accesibilidad WCAG)
* **🟡 Problema:** Al activar el tema oscuro, los meses (Jun a Nov 2026) y los números del eje Y son casi invisibles contra el fondo negro de la tarjeta.
* **💡 Razón Técnica:** La configuración de Highcharts utiliza valores hexadecimales oscuros estáticos (`#333333`) en lugar de vincularse a variables CSS de color claro cuando se aplica la clase `.dark`.
* **Evidencia con Flecha:** [`../evidencias/OBS-01_contraste_dark_mode.png`](file:///d:/CONTROLA-2026/evidencias/OBS-01_contraste_dark_mode.png)

### OBS-02: Ausencia de Empty State descriptivo en buscador
* **Módulo:** MOD-02 Sucursales (`/branches`)
* **Severidad:** S4 - Baja (Usabilidad UX)
* **🟡 Problema:** Al ingresar un término de búsqueda sin coincidencia (ej. "XYZ123"), la tabla simplemente oculta las filas y queda en blanco sin mensaje al usuario.
* **💡 Razón Técnica:** Falta implementar un bloque condicional que renderice un mensaje amigable tipo *"No se encontraron sucursales para su búsqueda"* cuando la lista filtrada tenga longitud cero.

### OBS-03: Inhabilitación de botón "+ Nueva Sucursal" por cuota comercial
* **Módulo:** MOD-02 Sucursales (Entorno de Pruebas)
* **Severidad:** Informativa
* **🔵 Condición de Negocio:** El botón `+ Nueva Sucursal` se encuentra inhabilitado (`disabled`), impidiendo validar la creación de nuevas sedes en este momento.
* **💡 Razón Técnica:** La empresa PLAEIS ENTERTAINMENT tiene contratada la cuota comercial **1 / 1 sucursales**. Se requiere ampliar temporalmente el plan asignado para habilitar la creación de nuevas sedes en QA.
* **Evidencia:** [`../evidencias/OBS-03_sucursales_cuota_plan.png`](file:///d:/CONTROLA-2026/evidencias/OBS-03_sucursales_cuota_plan.png)
