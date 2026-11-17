# CONTROLA.PE - QA TESTING & REPORTE DE CALIDAD (PLAEIS ENTERTAINMENT)

Repositorio local estructurado con toda la documentación de Aseguramiento de Calidad (QA), inventario de funcionalidades, matrices de prueba, registro formal de defectos (bugs) y evidencias fotográficas anotadas para la instancia empresarial de **Controla.pe** (`https://plaeis.controla.pe`).

**Cliente / Encargado:** Sandra Chabaneix  
**Organización Evaluada:** PLAEIS ENTERTAINMENT  
**Sede Evaluada:** Sede Principal · (MAIN)  
**Evaluador:** QA Tester Manual Profesional  
**Fecha:** Noviembre de 2026  

---

## 📁 Estructura del Repositorio Local

```text
d:\CONTROLA-2026/
├── index.html                           <- Portal interactivo local de demostración para Sandra Chabaneix
├── README.md                            <- Guía general del proyecto y resumen de ejecución
├── docs/
│   ├── INFORME_QA_EJECUTIVO.md          <- Informe ejecutivo formal con métricas y alcance
│   ├── MATRIZ_CASOS_DE_PRUEBA.md        <- Matriz detallada de casos manuales (Positivos, Negativos, UI, Red)
│   └── REGISTRO_DEFECTOS_BUGS.md        <- Bitácora detallada de defectos (Pasos, Resultado, Severidad)
└── evidencias/                          <- Capturas originales y anotadas en alta resolución (1920x1080)
    ├── DASHBOARD_FULL_1920.png          <- Vista íntegra del Dashboard a pantalla completa
    ├── DEF-01_solapamiento_leyendas_dashboard.png <- Flechas señalando solapamiento de Highcharts
    ├── DEF-02_error_404_logo.png        <- Flecha señalando recurso 404 del logo corporativo
    ├── DEF-03_colision_breadcrumbs_navbar.png <- Flechas señalando truncamiento de ruta por switch de tema
    ├── OBS-01_contraste_dark_mode.png   <- Flechas señalando falta de contraste WCAG en Dark Mode
    ├── OBS-03_sucursales_cuota_plan.png <- Indicador de bloqueo de botón por límite de suscripción
    ├── SUCURSALES_1920x1080_COMPLETO.png<- Tabla completa de sucursales a pantalla completa
    └── FIGMA_DESIGN_SYSTEM_836-4389.png <- Referencia oficial de diseño e identidad visual Figma
```

---

## 🚀 Portal Interactivo Local de Demostración

Para abrir la presentación interactiva con filtros dinámicos, métricas y visor de evidencias para Sandra Chabaneix:
1. Haz doble clic en el archivo [`index.html`](file:///d:/CONTROLA-2026/index.html).
2. Se abrirá directamente en tu navegador web predeterminado de manera 100% offline y autónoma.

---

## 📊 Resumen Ejecutivo del Módulo 1 (Dashboard) y Módulo 2 (Sucursales)

* **Casos de prueba evaluados:** 11 casos manuales no destructivos.
* **Tasa de Aprobación Funcional:** 100% (todos los flujos y validaciones de datos cumplieron las reglas de negocio).
* **Defectos Confirmados:**
  - `DEF-01 [S3 - Media]`: Solapamiento visual de leyendas Highcharts sobre títulos de tarjetas inferiores.
  - `DEF-02 [S4 - Baja]`: Error HTTP 404 en recurso de logo corporativo (`/assets/logo/company`).
  - `DEF-03 [S3 - Media]`: Truncamiento de Breadcrumbs en navbar por solapamiento con selector de tema visual.
* **Observaciones de Usabilidad / Negocio:**
  - `OBS-01 [S4 - Baja]`: Bajo contraste de etiquetas en modo oscuro (WCAG).
  - `OBS-02 [S4 - Baja]`: Falta de empty state descriptivo en buscador de sucursales.
  - `OBS-03 [Informativa]`: Botón "+ Nueva Sucursal" bloqueado por límite de suscripción (1/1 sucursales).
