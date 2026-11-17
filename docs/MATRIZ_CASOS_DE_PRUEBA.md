# MATRIZ DE CASOS DE PRUEBA (QA MANUAL)
**Instancia:** `https://plaeis.controla.pe`  
**Cliente:** Sandra Chabaneix  
**Ambiente:** Producción / Web Desktop (1920 × 1080)  

---

## 1. Módulo 1: Dashboard y Navegación Global

| CP ID | Tipo | Caso de Prueba | Precondición | Pasos de Ejecución | Resultado Esperado | Resultado Obtenido | Estado | Defecto / Obs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-DASH-01** | Positivo | Coherencia matemática de KPIs superiores | Sesión activa en `/dashboard` | 1. Leer valores de Total Usuarios, Usuarios Activos, Sucursales y Roles.<br>2. Comparar con subtítulos. | Números enteros válidos, sin `NaN` ni contenedores rotos. Total = Activos + Inactivos. | Muestra: Total 1, Activos 1 (0 inactivos), Sucursales 1, Roles 6. Exacto. | **PASS** | - |
| **CP-DASH-02** | UI / Layout | Delimitación de gráficos y leyendas Highcharts | Resolución 1920x1080 | 1. Desplazarse a la sección analítica.<br>2. Observar la alineación entre la fila 1 y la fila 2 de tarjetas. | Las leyendas de cada gráfica deben estar contenidas dentro de su tarjeta. | Las leyendas superiores se desbordan e invaden los encabezados inferiores. | **FAIL** | **DEF-01** |
| **CP-DASH-03** | Usabilidad / Accesibilidad | Conmutador de tema visual (*Light/Dark*) | Selector de tema visible | 1. Clic en icono Luna (Dark).<br>2. Evaluar contraste de tarjetas y textos.<br>3. Volver a Light. | Cambio fluido sin romper legibilidad ni contraste WCAG. | Tema conmuta reactivamente. Los textos de los ejes quedan en gris oscuro sobre negro. | **PASS w/ OBS** | **OBS-01** |
| **CP-DASH-04** | UI / Responsividad | Colapso y expansión del menú lateral | Barra superior visible | 1. Clic en Toggle Sidebar.<br>2. Verificar reajuste de la rejilla.<br>3. Comprobar visualización del logo corporativo. | Menú colapsa suavemente y el logotipo/isotipo se visualiza correctamente en la esquina superior. | Expansión y colapso fluidos; el logo/isotipo sí se muestra visible y centrado. | **PASS** | - |
| **CP-DASH-05** | Funcional / Shell | Menú de notificaciones y perfil | Cabecera visible | 1. Clic en campana de notificaciones.<br>2. Clic en avatar de usuario y seleccionar "Configuración". | Notificaciones desplegadas; enlace navega a `/settings/profile`. | Popover abre ("Sin notificaciones"); `/settings/profile` 100% operativo. | **PASS** | - |
| **CP-DASH-06** | Técnico / Red | Integridad de peticiones HTTP en Dashboard | Consola DevTools abierta | 1. Cargar `/dashboard`.<br>2. Monitorear carga de recursos y scripts.<br>3. Revisar consola JS. | Carga estable sin bloqueos de renderizado ni interrupciones de sesión. | 0 excepciones JS fatales; interfaz operativa. | **PASS** | - |

---

## 2. Módulo 2: Sucursales (`/branches`)

| CP ID | Tipo | Caso de Prueba | Precondición | Pasos de Ejecución | Resultado Esperado | Resultado Obtenido | Estado | Defecto / Obs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-BRAN-01** | Positivo | Estructura de tabla y columnas a 1080p | Navegar a `/branches` | 1. Verificar encabezados de columna.<br>2. Comprobar badges y paginación. | Todas las columnas visibles sin scroll horizontal; badges "Principal" y "Activa" renderizados. | Tabla 100% visible a pantalla completa; 1 registro ("Sede Principal", MAIN). | **PASS** | - |
| **CP-BRAN-02** | Filtros | Búsqueda por texto y restauración | Tabla con registros | 1. Escribir "Principal" en buscador.<br>2. Escribir término sin coincidencia "XYZ123".<br>3. Clic en botón "Limpiar". | Filtra coincidencia; muestra Empty State ante valor inexistente; "Limpiar" restaura. | Filtra OK. Ante "XYZ123" la tabla queda en blanco sin mensaje. "Limpiar" restaura OK. | **PASS w/ OBS** | **OBS-02** |
| **CP-BRAN-03** | Validación Negativa | Campo obligatorio `Nombre *` en formulario | Modal Editar Sucursal abierto | 1. Vaciar el campo `Nombre *`.<br>2. Clic en "Guardar Cambios".<br>3. Clic en "Cancelar". | El formulario bloquea el envío y muestra tooltip de advertencia. Cero mutación en BD. | Envío bloqueado; tooltip nativo HTML5 `! Completa este campo` enfoca el input. BD intacta. | **PASS** | - |
| **CP-BRAN-04** | Permisos | Modal de Detalle ("Ver") | Menú `⋮` en fila | 1. Clic en opción "Ver".<br>2. Revisar campos estructurados.<br>3. Cerrar con Escape o botón Cerrar. | Despliegue de datos de solo lectura y cierre limpio del modal. | Modal abre con datos de "Sede Principal"; cierre por Escape y botón funcionales. | **PASS** | - |
| **CP-BRAN-05** | UI / Responsividad | Truncamiento de Breadcrumbs en navbar | Viewport intermedio (1024-1280px) | 1. Reducir viewport a 1024-1280px.<br>2. Observar barra superior con sidebar abierto. | Breadcrumbs y selector de tema deben coexistir sin solaparse. | La ruta se trunca a `"Dash"` y el switch de tema se superpone encima. | **FAIL** | **DEF-03** |

---

## 3. Módulo 6: Tareas (`/tasks`)

| CP ID | Tipo | Caso de Prueba | Precondición | Pasos de Ejecución | Resultado Esperado | Resultado Obtenido | Estado | Defecto / Obs |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **CP-TASK-01** | UI / Layout | Integridad de botones en Modal de Detalle de Tarea | Navegar a `/tasks` | 1. Ubicar tarea `TASK-2026-00001`.<br>2. Menú `[...]` > clic en "Ver".<br>3. Evaluar disposición de botones de acción y pestañas. | El diálogo debe mostrar todos los botones ("Editar", "Cancelar") y pestañas sin desbordamientos ni scroll horizontal. | Falla de maquetación: el modal de 512px desborda horizontalmente; botones "Editar" y "Cancelar" quedan fuera de pantalla (offscreen) y la pestaña "Historial" se corta. | **FAIL** | **DEF-04** |
