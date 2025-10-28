# Guía Completa: Vibe Coding - Desarrollo Asistido por IA

**Documento Definitivo - Clase 02**
**Curso:** Inteligencia Artificial para Negocios
**Universidad Externado de Colombia (Compensar)**
**Profesor:** Julián Zuluaga - Orbital Lab
**Fecha de Clase:** 23 de octubre de 2025
**Versión Documento:** 2.0 Expandida

---

## 📖 Índice

1. [Fundamentos Conceptuales](#fundamentos-conceptuales)
2. [Historia y Contexto](#historia-y-contexto)
3. [Ecosistema de Herramientas](#ecosistema-de-herramientas)
4. [Análisis Comparativo Profundo](#análisis-comparativo-profundo)
5. [Metodología y Mejores Prácticas](#metodología-y-mejores-prácticas)
6. [Casos de Uso por Industria](#casos-de-uso-por-industria)
7. [Patrones de Prompting Avanzados](#patrones-de-prompting-avanzados)
8. [Arquitectura Técnica (Overview)](#arquitectura-técnica-overview)
9. [Seguridad, Privacidad y Compliance](#seguridad-privacidad-y-compliance)
10. [Troubleshooting y Errores Comunes](#troubleshooting-y-errores-comunes)
11. [Roadmap de Aprendizaje](#roadmap-de-aprendizaje)
12. [Recursos y Bibliografía](#recursos-y-bibliografía)

---

## 1. Fundamentos Conceptuales

### 1.1 Definición y Taxonomía

**Vibe Coding** es una práctica emergente de desarrollo de software que utiliza inteligencia artificial generativa para crear código funcional a partir de instrucciones en lenguaje natural, permitiendo que personas sin conocimientos técnicos previos desarrollen aplicaciones completas.

#### Taxonomía del Concepto

```
AI-Assisted Development (Paraguas)
├── No-Code Platforms (Visual builders, no código expuesto)
├── Low-Code Platforms (Código generado pero editable)
├── Vibe Coding (Conversacional, generación mediante prompts)
└── AI-Augmented IDEs (Para desarrolladores, autocompletado)
```

**Términos relacionados:**
- **Byte Coding**: Variante del término (menos usada)
- **Prompt Coding**: Enfatiza el rol de los prompts
- **Conversational Development**: Enfoque en diálogo iterativo
- **Natural Language Programming**: Término académico

### 1.2 Origen del Término

**Acuñado por:** Andrew Ng
**Contexto:** Cofundador de OpenAI, ex-jefe de IA en Google Brain, fundador de DeepLearning.AI
**Año:** ~2023-2024
**Motivación:** Observó que el desarrollo de software estaba cambiando de "escribir código" a "dirigir la creación de código"

**Cita original:**
> "We're entering an era where the ability to 'vibe' with AI—to convey intent, emotion, and context—is becoming as important as traditional coding skills."

### 1.3 Expansión del Concepto "Vibe"

El término se ha expandido más allá del código:

| Disciplina | Término | Descripción |
|------------|---------|-------------|
| **Diseño** | Vibe Designing | Generación de diseños mediante IA (Figma AI, Midjourney) |
| **Escritura** | Vibe Writing | Creación de contenido con asistentes de escritura |
| **Música** | Vibe Music | Composición algorítmica (Suno, Udio) |
| **Video** | Vibe Editing | Edición de video asistida por IA |
| **3D** | Vibe Modeling | Generación de modelos 3D desde texto |

### 1.4 Filosofía del Estado de Flujo

**Concepto central:** El desarrollador entra en un estado de flujo creativo donde:

1. **Visualiza** la aplicación completa (colores, estructura, interacciones)
2. **Siente** la experiencia del usuario
3. **Transmite** esa visión a la IA mediante lenguaje natural
4. **Itera** en colaboración con la IA como co-creador

**Diferencia clave con programación tradicional:**

| Programación Tradicional | Vibe Coding |
|--------------------------|-------------|
| Pensar en **cómo** implementar | Pensar en **qué** construir |
| Sintaxis y estructura | Intención y objetivo |
| Debugging de código | Refinamiento de prompts |
| Compilador como juez | IA como colaborador |

---

## 2. Historia y Contexto

### 2.1 Evolución Histórica

#### Era 1: Programación Manual (1950s-2000s)
- Código escrito línea por línea
- IDEs básicos (Vim, Emacs, Eclipse)
- Foco: sintaxis, algoritmos, estructuras de datos

#### Era 2: Frameworks y Abstracción (2000s-2020)
- Frameworks que abstraen complejidad (Rails, Django, React)
- Stack Overflow como "IA" rudimentaria
- Copy-paste como workflow común

#### Era 3: AI-Assisted Coding (2020-2023)
- **GitHub Copilot** (Jun 2021): Autocompletado inteligente
- **ChatGPT** (Nov 2022): Generación de código conversacional
- **Replit Ghostwriter** (2022): IDE con IA integrada

#### Era 4: Vibe Coding (2023-Presente)
- **Lovable** (2023): No-code puro conversacional
- **v0.dev** (2023): Componentes React desde prompts
- **Claude Artifacts** (Mar 2024): Código ejecutable en chat
- **ChatGPT Canvas** (Oct 2024): Edición colaborativa
- **Cursor** (2024): IDE completo AI-first

### 2.2 Datos de Adopción (2025)

#### Mercado Global

**Tamaño del mercado:**
- **2023:** $5,000M
- **2025:** ~$12,000M (estimado)
- **2030:** $26,000M-$100,000M (proyecciones)
- **CAGR:** 20-30% anual

**Penetración por sector:**
- **Startups:** 60% usan herramientas de AI coding
- **Empresas tech (FAANG):** 85% han adoptado internamente
- **Corporativos tradicionales:** 25% en fase piloto
- **Educación:** 40% lo enseñan en cursos de CS

#### Estadísticas de Uso

**Código generado por IA:**
- **41%** del código global en GitHub tiene trazas de IA (2024)
- **25%** de startups Y Combinator (W2025) tienen código 95% IA-generado
- **44%** de desarrolladores profesionales usan herramientas IA diariamente

**Productividad:**
- **55%** de aumento en velocidad de desarrollo (GitHub study)
- **40%** de reducción en bugs (para desarrolladores con IA)
- **10x** más rápido para prototipos vs desarrollo tradicional

### 2.3 Drivers de Adopción

**Factores tecnológicos:**
1. Modelos de lenguaje más potentes (GPT-4, Claude 3.5)
2. Context windows más largos (200K tokens)
3. Velocidad de inferencia mejorada (<1s respuesta)

**Factores económicos:**
1. Costo de desarrollo reducido 70-90% para MVPs
2. Time-to-market de meses a días/horas
3. Democratización: no necesitas contratar developers

**Factores sociales:**
1. Generación Z más cómoda con IA que con código
2. "Citizenship developers" en empresas
3. Movimiento no-code/low-code mainstream

---

## 3. Ecosistema de Herramientas

### 3.1 Mapa Completo del Ecosistema

```
VIBE CODING LANDSCAPE 2025
├── Tier 1: No-Code Conversational
│   ├── Lovable (Prototipos rápidos)
│   ├── Replit Agent (Apps fullstack)
│   ├── Hostinger AI (Websites)
│   └── Framer AI (Landing pages)
├── Tier 2: Low-Code Visual
│   ├── v0.dev (Componentes React)
│   ├── Bolt.new (Apps editables)
│   ├── Claude Artifacts (Prototipos)
│   └── ChatGPT Canvas (Código + docs)
├── Tier 3: Developer-First
│   ├── Cursor (IDE completo)
│   ├── Windsurf (Colaborativo)
│   ├── GitHub Copilot (Autocompletado)
│   └── Codeium (Open alternative)
├── Tier 4: Especializados
│   ├── Supabase (Backend as a Service)
│   ├── Firebase (Google BaaS)
│   ├── Vercel AI SDK (Streaming AI apps)
│   └── LangChain (AI orchestration)
└── Tier 5: Mobile/Native
    ├── FlutterFlow AI (Apps móviles)
    ├── Draftbit AI (React Native)
    └── Glide AI (Apps desde spreadsheets)
```

### 3.2 Análisis Detallado por Herramienta

---

#### 🔷 **Lovable** (lovable.dev)

**Categoría:** No-Code Conversational
**Modelo:** Freemium (tokens diarios gratis, luego pago)
**Fundación:** 2023, Alemania/India
**Status:** Salió a bolsa Q3 2023

**Características:**
- ✅ Chat conversacional puro (cero código expuesto)
- ✅ Genera apps fullstack (frontend + backend + DB)
- ✅ Preview en tiempo real
- ✅ Deploy automático a URL pública
- ✅ Responsive por defecto

**Stack técnico generado:**
- Frontend: React + TailwindCSS
- Backend: Node.js (opcional)
- Database: PostgreSQL / Firebase
- Hosting: Propio infrastructure

**Casos de uso ideales:**
- MVPs de validación de ideas (1-4 horas)
- Prototipos para pitch a inversores
- Landing pages interactivas
- Herramientas internas de equipos

**Limitaciones:**
- ⚠️ Tokens limitados en plan gratuito (~10-15 apps/mes)
- ⚠️ Código no es fácilmente exportable
- ⚠️ Depende de su infraestructura (vendor lock-in)
- ⚠️ No ideal para apps complejas (>20 vistas)

**Ejemplo de prompt efectivo:**
```
Crea una app de gestión de tareas para equipos.

Funcionalidades:
- Dashboard con lista de tareas (tabla)
- Filtros: estado (pendiente/completada), prioridad, asignado
- Crear nueva tarea (modal): título, descripción, prioridad, asignado, fecha límite
- Marcar como completada con un click
- Contador de tareas por estado (cards superiores)

Diseño:
- Paleta: azul (#3B82F6) primario, gris neutro fondo
- Tipografía: Inter, moderna y limpia
- Iconos: Lucide icons
- Layout: sidebar izquierdo con navegación, contenido principal a la derecha

Datos:
- Mock data de 15 tareas para demo
```

**Pricing (2025):**
- Free: 100 tokens/mes (~10 apps simples)
- Pro: $20/mes - 1000 tokens + features avanzados
- Team: $50/mes - ilimitado + colaboración

**Alternativas similares:**
- **Builder.io AI**: Similar pero más orientado a e-commerce
- **Brancher.ai**: Foco en automatizaciones workflow

---

#### 🔷 **Replit Agent** (replit.com/ai)

**Categoría:** No-Code Conversational + Code Exposure
**Modelo:** Freemium ($7/mes Pro, $20/mes Teams)
**Fundación:** Replit 2016, Agent 2023

**Características:**
- ✅ IDE completo en la nube
- ✅ Agent mode: conversacional puro
- ✅ Ghostwriter mode: autocompletado en código
- ✅ Deploy con un click
- ✅ Colaboración en tiempo real
- ✅ 50+ lenguajes soportados

**Stack técnico generado:**
- Flexible: Python, Node.js, Go, Rust, etc.
- Frameworks: React, Vue, Flask, FastAPI, etc.
- Databases: PostgreSQL, MongoDB, Redis
- Hosting: Replit infrastructure

**Casos de uso ideales:**
- Apps fullstack con backend complejo
- APIs REST/GraphQL
- Bots de Discord/Telegram
- Juegos simples (web games)
- Herramientas de scraping/automatización

**Limitaciones:**
- ⚠️ Performance limitada en plan gratuito
- ⚠️ Cold starts al despertar (si inactivo >1h)
- ⚠️ Límites de RAM/CPU en free tier

**Ejemplo de prompt efectivo:**
```
Crea un bot de Discord que responda preguntas usando OpenAI API.

Requisitos técnicos:
- Python con discord.py
- Integración con OpenAI GPT-4
- Variables de entorno para API keys
- Comando: !ask <pregunta>
- Logging de uso

Funcionalidades:
- Responder en hilos para no saturar canal
- Límite de 100 tokens por respuesta
- Cooldown de 5s entre comandos por usuario
- Comando !help con instrucciones

Deploy:
- Mantener bot activo 24/7
- Health check endpoint
```

**Pricing (2025):**
- Free: Limitado, cold starts, 500MB storage
- Hacker: $7/mes - Always-on, 1GB RAM, 5GB storage
- Pro: $20/mes - 4GB RAM, colaboración, analytics

---

#### 🔷 **v0.dev** (v0.dev)

**Categoría:** Low-Code Visual (Componentes)
**Modelo:** Freemium (Vercel)
**Fundación:** 2023, Vercel (empresa de Next.js)

**Características:**
- ✅ Genera componentes React individuales
- ✅ Código visible y editable desde el inicio
- ✅ Stack moderno: Next.js + TailwindCSS + shadcn/ui
- ✅ Preview interactivo
- ✅ Export a código local

**Stack técnico generado:**
- Framework: Next.js 14 (App Router)
- Styling: TailwindCSS
- Componentes: shadcn/ui (Radix UI)
- TypeScript por defecto

**Casos de uso ideales:**
- Componentes UI individuales (botones, modals, forms)
- Dashboards con gráficos (Recharts integration)
- Landing pages modernas
- Sections de marketing

**Limitaciones:**
- ⚠️ No genera backend (solo frontend)
- ⚠️ Requiere conocimiento básico de React para editar
- ⚠️ Tokens limitados en plan gratuito

**Ejemplo de prompt efectivo:**
```
Genera un componente de pricing table con 3 tiers.

Estructura:
- 3 columnas: Free, Pro, Enterprise
- Cada tier tiene:
  - Nombre del plan
  - Precio (destacado)
  - Lista de features (con checkmarks)
  - Botón CTA

Diseño:
- Tier central (Pro) destacado: más grande, shadow
- Animación hover: lift effect
- Gradiente sutil en fondo de cards
- Badges para "Most Popular" en Pro

Features por tier:
Free: 10 projects, 1 user, Community support
Pro: Unlimited projects, 5 users, Priority support, Analytics
Enterprise: Everything in Pro + Custom domain + SLA
```

**Pricing (2025):**
- Free: 200 créditos/mes (~10-15 componentes)
- Pro: Integrado con Vercel Pro ($20/mes)

---

#### 🔷 **Claude Artifacts** (claude.ai)

**Categoría:** Low-Code Conversational
**Modelo:** Claude Pro ($20/mes) o Free limitado
**Fundación:** Anthropic, feature lanzado Mar 2024

**Características:**
- ✅ Genera HTML/React/SVG/Mermaid en "artifacts"
- ✅ Preview inmediato al lado del chat
- ✅ Edición iterativa conversacional
- ✅ Export a HTML standalone
- ✅ Share vía URL pública

**Stack técnico generado:**
- HTML puro + JavaScript
- React (en algunos casos)
- SVG para visualizaciones
- Mermaid para diagramas

**Casos de uso ideales:**
- Prototipos visuales rápidos
- Visualizaciones de datos (gráficos interactivos)
- Infografías interactivas
- Diagramas explicativos

**Limitaciones:**
- ⚠️ No genera backend
- ⚠️ No persiste datos (reinicia al recargar)
- ⚠️ Limitado a single-page apps

**Ejemplo de prompt efectivo:**
```
Crea una visualización interactiva del ciclo CRISP-DM.

Estructura:
- 6 fases en círculo: Business Understanding → Data Understanding → Data Preparation → Modeling → Evaluation → Deployment
- Flechas bidireccionales entre fases
- Al hacer hover en cada fase: tooltip con descripción + entregables clave
- Click en fase: panel lateral con detalles expandidos

Diseño:
- Colores diferenciados por fase (gradiente azul-verde)
- Animación: pulso sutil en fases activas
- Centro del círculo: logo CRISP-DM
- Fondo: grid sutil

Datos:
- Descripción de cada fase (2-3 líneas)
- 3-4 entregables clave por fase
```

---

#### 🔷 **Cursor** (cursor.sh)

**Categoría:** Developer-First IDE
**Modelo:** Pago ($20/mes)
**Fundación:** 2023, fork de VS Code

**Características:**
- ✅ IDE completo (fork de VS Code)
- ✅ Cmd+K: edición inline con IA
- ✅ Chat contextual con codebase
- ✅ Multi-file editing
- ✅ Composer: arquitecto de código

**Stack técnico:**
- Cualquier lenguaje (hereda de VS Code)
- Contexto: 200K tokens (Claude 3.5 Sonnet)
- Modelos: GPT-4, Claude, Gemini (configurable)

**Casos de uso ideales:**
- Desarrollo profesional fullstack
- Refactoring de código legacy
- Migración entre frameworks
- Generación de tests automáticos

**Limitaciones:**
- ⚠️ Requiere conocimiento de programación
- ⚠️ Costo mensual significativo ($20/mes)
- ⚠️ Curva de aprendizaje para aprovechar al máximo

**Workflow típico:**
1. Cmd+K en archivo: "Refactor this component to use hooks"
2. Cmd+L: Chat con contexto de todo el codebase
3. Composer: "Add authentication to this app"

---

### 3.3 Matriz de Decisión: ¿Qué Herramienta Usar?

| Criterio | Lovable | Replit | v0.dev | Claude Artifacts | Cursor |
|----------|---------|--------|--------|------------------|--------|
| **Curva aprendizaje** | Muy baja | Baja | Media | Baja | Alta |
| **Complejidad apps** | Simple-Media | Media-Alta | Simple | Simple | Muy Alta |
| **Backend incluido** | ✅ Sí | ✅ Sí | ❌ No | ❌ No | Manual |
| **Edición código** | ❌ No | ✅ Sí | ✅ Sí | Limitado | ✅ Sí |
| **Deploy fácil** | ✅ Automático | ✅ 1-click | Manual | Share URL | Manual |
| **Costo mensual** | $0-$20 | $0-$20 | $0-$20 | $0-$20 | $20 |
| **Ideal para** | MVPs | APIs/Bots | UI Components | Prototipos | Producción |

**Regla de oro:**
- **Si NO sabes programar:** Lovable o Replit Agent
- **Si sabes HTML básico:** v0.dev o Claude Artifacts
- **Si eres developer:** Cursor o GitHub Copilot

---

## 4. Análisis Comparativo Profundo

### 4.1 Comparación Multi-Dimensional

#### Dimensión 1: Facilidad de Uso

```
┌─────────────────────────────────────────────┐
│ Escala: 1 (difícil) → 10 (muy fácil)       │
├─────────────────────────────────────────────┤
│ Lovable          ████████████████████ 10/10 │
│ Claude Artifacts ██████████████████   9/10  │
│ ChatGPT Canvas   ██████████████████   9/10  │
│ Replit Agent     ████████████████     8/10  │
│ v0.dev           ██████████████       7/10  │
│ Bolt.new         ██████████████       7/10  │
│ Windsurf         ████████████         6/10  │
│ Cursor           ██████████           5/10  │
│ GitHub Copilot   ████████             4/10  │
└─────────────────────────────────────────────┘
```

#### Dimensión 2: Control sobre Código

```
┌─────────────────────────────────────────────┐
│ Escala: 1 (sin control) → 10 (total)       │
├─────────────────────────────────────────────┤
│ Cursor           ████████████████████ 10/10 │
│ GitHub Copilot   ████████████████████ 10/10 │
│ Windsurf         ██████████████████   9/10  │
│ Replit Agent     ████████████████     8/10  │
│ Bolt.new         ██████████████       7/10  │
│ v0.dev           ██████████████       7/10  │
│ ChatGPT Canvas   ████████████         6/10  │
│ Claude Artifacts ██████████           5/10  │
│ Lovable          ████                 2/10  │
└─────────────────────────────────────────────┘
```

#### Dimensión 3: Velocidad de Prototipado

```
┌─────────────────────────────────────────────┐
│ Tiempo para MVP funcional (horas)          │
├─────────────────────────────────────────────┤
│ Lovable          █ 0.5-2h                   │
│ Claude Artifacts █ 0.5-1h                   │
│ v0.dev           ██ 1-3h                    │
│ Replit Agent     ██ 2-4h                    │
│ ChatGPT Canvas   ██ 1-3h                    │
│ Bolt.new         ███ 2-5h                   │
│ Windsurf         ████ 4-8h                  │
│ Cursor           █████ 6-12h                │
│ Código manual    ████████████ 20-40h        │
└─────────────────────────────────────────────┘
```

### 4.2 Ventajas y Desventajas por Herramienta

#### Lovable

**✅ Ventajas:**
- Cero conocimiento técnico requerido
- Más rápido para MVPs simples
- Deploy automático incluido
- Responsive por defecto

**❌ Desventajas:**
- Vendor lock-in severo (código no exportable fácilmente)
- Limitado a apps relativamente simples
- Tokens limitados en plan gratuito
- No ideal para producción enterprise

**Mejor para:** Emprendedores no técnicos validando ideas

---

#### Replit Agent

**✅ Ventajas:**
- Flexibilidad de lenguajes (50+)
- Backend completo incluido
- Colaboración en tiempo real
- IDE completo si necesitas editar código

**❌ Desventajas:**
- Performance limitada en free tier
- Cold starts frecuentes
- Interfaz puede ser abrumadora para no técnicos

**Mejor para:** Apps con backend complejo (APIs, bots)

---

#### v0.dev

**✅ Ventajas:**
- Stack moderno y mantenible (Next.js + shadcn/ui)
- Código limpio y exportable
- Componentes reutilizables
- Documentación excelente del stack

**❌ Desventajas:**
- Solo frontend (no backend)
- Requiere conocimiento de React para aprovechar
- Tokens limitados rápidamente

**Mejor para:** Frontend developers creando UI moderna

---

#### Claude Artifacts

**✅ Ventajas:**
- Gratis (con límites)
- Preview inmediato
- Iteración rápida conversacional
- Share fácil vía URL

**❌ Desventajas:**
- No persiste datos
- Single-page apps únicamente
- No backend

**Mejor para:** Prototipos visuales, infografías, demos

---

#### Cursor

**✅ Ventajas:**
- Control total sobre código
- Multi-file editing
- Contexto de codebase completo
- Producción-ready

**❌ Desventajas:**
- Requiere expertise en programación
- Costo mensual
- Curva de aprendizaje

**Mejor para:** Desarrolladores profesionales en producción

---

### 4.3 Casos de Uso por Perfil

#### Perfil 1: Emprendedor No Técnico

**Objetivo:** Validar idea de negocio con MVP funcional

**Stack recomendado:**
1. **Lovable** (primera opción)
   - Crear MVP en 2-4 horas
   - Deploy automático
   - Compartir con early adopters

2. **Claude Artifacts** (complemento)
   - Landing page explicativa
   - Infografías de valor
   - Presentaciones pitch

**Workflow típico:**
```
1. Boceto en papel (30 min)
2. Lovable: crear app funcional (2-3h)
3. Claude: crear landing page (30 min)
4. Share y validar con 10-20 usuarios
5. Iterar basado en feedback
```

**Ejemplo real:** Kathleen (estudiante de clase)
- Contexto: Trabaja en área de tesorería
- Problema: Gestionar flujos de caja manualmente
- Solución: App de gestión de tesorería con Lovable
- Tiempo: 30 minutos en clase (prototipo inicial)

---

#### Perfil 2: Diseñador con HTML Básico

**Objetivo:** Componentes UI modernos para portfolio

**Stack recomendado:**
1. **v0.dev** (primera opción)
   - Componentes React profesionales
   - Stack moderno (Next.js + Tailwind)
   - Código limpio para estudiar

2. **Bolt.new** (complemento)
   - Apps completas editables
   - Integración con Figma diseños

**Workflow típico:**
```
1. Diseño en Figma
2. v0.dev: convertir secciones a componentes
3. Export código a proyecto local
4. Editar detalles en VS Code
5. Deploy a Vercel
```

---

#### Perfil 3: Analista de Datos (Python)

**Objetivo:** Dashboards interactivos de KPIs

**Stack recomendado:**
1. **Replit Agent** (primera opción)
   - Python + Streamlit
   - Conexión a bases de datos
   - APIs de data sources

2. **Claude Artifacts** (complemento)
   - Visualizaciones standalone
   - Infografías de reportes

**Workflow típico:**
```
1. Replit: crear app Streamlit con conexión a DB
2. Prompts: "Crea dashboard con gráficos de X, Y, Z"
3. Iteración: ajustar cálculos y visualizaciones
4. Deploy interno en Replit
5. Share URL con stakeholders
```

**Ejemplo real:** Dashboard Netflix (demo en clase)
- Input: CSV de títulos Netflix
- Output: Dashboard interactivo con filtros
- Tiempo: 15 minutos durante la clase

---

#### Perfil 4: Developer Profesional

**Objetivo:** Producción-ready apps con tests

**Stack recomendado:**
1. **Cursor** (primera opción)
   - Control total de codebase
   - Multi-file editing
   - Tests automáticos

2. **GitHub Copilot** (complemento)
   - Autocompletado en código existente
   - Integración con GitHub

**Workflow típico:**
```
1. Cursor Composer: arquitectura inicial
2. Cmd+K inline: implementar features
3. Chat: refactoring y optimizaciones
4. Copilot: autocompletar detalles
5. Tests con IA: generar test suites
6. CI/CD tradicional
```

---

## 5. Metodología y Mejores Prácticas

### 5.1 Principios Fundamentales

#### Principio 1: "Menos es Más" (Incremental)

**Concepto:** Empezar con lo mínimo viable e iterar incrementalmente.

**Anti-patrón:**
```
❌ MALO:
"Crea una app como Uber con:
- Registro de usuarios (riders y drivers)
- Geolocalización en tiempo real
- Sistema de pagos (Stripe)
- Ratings bidireccionales
- Chat en vivo
- Notificaciones push
- Dashboard de analytics
- Panel de administración"
```

**Patrón correcto:**
```
✅ BUENO - Iteración 1:
"Crea una app simple de solicitud de transporte.
- Formulario: origen, destino, tipo de vehículo
- Mostrar precio estimado
- Botón 'Solicitar viaje'
- Lista de viajes solicitados"

✅ Iteración 2 (después de validar 1):
"Agrega mapa interactivo con:
- Marcadores de origen y destino
- Ruta sugerida entre ambos puntos"

✅ Iteración 3:
"Integra geolocalización:
- Botón 'Usar mi ubicación actual'
- Actualizar mapa automáticamente"
```

**Por qué funciona:**
- IA genera mejor con scope limitado
- Menos oportunidad de errores
- Feedback temprano
- Pivot rápido si algo no funciona

---

#### Principio 2: "Vibra, No Especifiques" (Vibe over Spec)

**Concepto:** Transmitir la emoción/intención antes que detalles técnicos.

**Anti-patrón:**
```
❌ MALO (muy técnico):
"Implementa un React functional component con useState para counter,
useEffect para side effects, memoización con useMemo,
y estilizado con Tailwind usando clases flex, justify-center, items-center,
bg-gradient-to-r from-blue-500 to-purple-600"
```

**Patrón correcto:**
```
✅ BUENO (vibracional):
"Crea un contador moderno y vibrante.
Colores: gradiente azul-morado energético
Sensación: dinámico, con animaciones sutiles al hacer click
Botones: grandes, táctiles, con feedback visual
Tipografía: números grandes y bold, fáciles de leer"
```

**Por qué funciona:**
- IA es experta en tomar decisiones técnicas
- Tu expertise es UX/visión, no implementación
- Resultados más creativos e inesperados

---

#### Principio 3: "Contexto es Rey" (Context-First)

**Concepto:** Dar contexto rico antes de pedir implementación.

**Anti-patrón:**
```
❌ MALO (sin contexto):
"Crea un formulario de contacto"
```

**Patrón correcto:**
```
✅ BUENO (con contexto):
"Contexto: Soy un dentista freelance en Bogotá.
Necesito un formulario en mi web para que pacientes potenciales
soliciten citas.

Campos necesarios:
- Nombre completo
- Teléfono (validar formato Colombia)
- Email
- Tipo de servicio (dropdown): Limpieza, Ortodoncia, Urgencia
- Fecha preferida (date picker)
- Comentarios (opcional)

Restricciones:
- Horario de atención: Lunes-Viernes 8am-6pm
- No agendar fines de semana
- Máximo 1 mes de anticipación

Después de enviar:
- Mensaje de confirmación
- Email automático a mi correo
- WhatsApp al paciente (si es posible)"
```

**Por qué funciona:**
- IA entiende el dominio
- Toma decisiones contextuales correctas
- Menos iteraciones necesarias

---

### 5.2 Patrones de Prompting Avanzados

#### Patrón 1: Especificación por Ejemplos

**Técnica:** Mostrar ejemplos visuales/textuales en lugar de describir.

**Ejemplo:**
```
"Crea un pricing table como este [adjuntar screenshot de Stripe pricing]

Cambia:
- Colores a nuestra paleta (azul #3B82F6, verde #10B981)
- 3 tiers: Starter ($9), Pro ($29), Enterprise (custom)
- Features [lista]"
```

**Herramientas que lo soportan:**
- ChatGPT (imágenes)
- Claude (imágenes + PDFs)
- Lovable (imágenes de diseño)

---

#### Patrón 2: Role-Playing

**Técnica:** Asignar un rol experto a la IA.

**Ejemplo:**
```
"Eres un senior product designer con 10 años en SaaS B2B.

Diseña un onboarding flow para nuestra app de CRM que:
- Minimice fricción (no más de 3 pasos)
- Capture info esencial: nombre empresa, rol, tamaño equipo
- Incluya tooltips contextuales
- Tenga opción 'Skip' para usuarios expertos

Aplica las mejores prácticas de UX que conoces."
```

---

#### Patrón 3: Chain of Thought (Cadena de Pensamiento)

**Técnica:** Pedir que la IA piense paso a paso antes de implementar.

**Ejemplo:**
```
"Antes de crear el código, analiza:
1. ¿Cuál es la mejor estructura de datos para este problema?
2. ¿Qué edge cases debo considerar?
3. ¿Cómo optimizo para performance?

Luego, implementa la solución basada en tu análisis."
```

---

#### Patrón 4: Constraints-Driven

**Técnica:** Definir restricciones claras guía mejor que libertad total.

**Ejemplo:**
```
"Restricciones estrictas:
- Máximo 3 colores (primario, secundario, neutral)
- Sin librerías externas (solo stdlib)
- Performance: < 100ms carga inicial
- Accesibilidad: WCAG 2.1 AA compliance
- Mobile-first: diseñar para 360px primero"
```

---

### 5.3 Workflow Recomendado (7 Etapas)

#### Etapa 1: Ideación (5-10 min)

**Objetivo:** Clarificar qué construir y por qué.

**Preguntas clave:**
- ¿Qué problema resuelve?
- ¿Quién es el usuario final?
- ¿Cuál es el MVP mínimo mínimo?
- ¿Cómo se mide el éxito?

**Herramientas:**
- Papel y lápiz
- Excalidraw (digital whiteboard)
- FigJam / Miro

**Output:** Boceto de 1-2 pantallas principales

---

#### Etapa 2: Selección de Stack (2 min)

**Decisión 1:** ¿Necesito backend?
- **Sí:** Replit Agent, Lovable
- **No:** v0.dev, Claude Artifacts

**Decisión 2:** ¿Qué nivel de control necesito?
- **Cero código:** Lovable
- **Ver código:** Claude Artifacts, v0.dev
- **Editar código:** Replit, Bolt.new
- **Control total:** Cursor

---

#### Etapa 3: Primer Prompt (Contexto) (1 min)

**Template básico:**
```
Contexto: [quién eres, qué problema]

Crea un/a [tipo de app] que [objetivo principal]

Funcionalidades:
- [Feature 1]
- [Feature 2]
- [Feature 3]

Estilo:
- Colores: [paleta]
- Sensación: [adjetivos]
- Referencias: [inspiración]

Datos:
- [Mock data si aplica]
```

---

#### Etapa 4: Iteración 1 - Estructura (10-15 min)

**Objetivo:** Validar layout y navegación.

**Prompts comunes:**
- "Mueve la sidebar a la derecha"
- "Agranda los botones principales"
- "Cambia el header a sticky"

**Validación:**
- [ ] Layout general correcto
- [ ] Navegación intuitiva
- [ ] Jerarquía visual clara

---

#### Etapa 5: Iteración 2 - Funcionalidad (15-20 min)

**Objetivo:** Implementar lógica interactiva.

**Prompts comunes:**
- "Al hacer click en X, mostrar modal Y"
- "Filtrar tabla por columna Z"
- "Validar formulario: email debe ser válido"

**Validación:**
- [ ] Interacciones funcionan
- [ ] Estados se actualizan
- [ ] Validaciones correctas

---

#### Etapa 6: Iteración 3 - Polish (10-15 min)

**Objetivo:** Detalles finales de UX.

**Prompts comunes:**
- "Agrega animaciones sutiles al hover"
- "Loading spinners cuando carga data"
- "Toast notifications de éxito/error"

**Validación:**
- [ ] Responsive (mobile/desktop)
- [ ] Estados loading/empty/error
- [ ] Micro-interacciones

---

#### Etapa 7: Deploy (5 min)

**Por plataforma:**
- **Lovable:** Automático (URL única)
- **Replit:** Click en "Deploy"
- **Claude:** Share button (URL pública)
- **v0.dev:** Export → Vercel

**Validación final:**
- [ ] URL pública funciona
- [ ] Compartible con stakeholders
- [ ] Performance aceptable

---

### 5.4 Errores Comunes y Soluciones

#### Error 1: "IA se va muy lejos"

**Síntoma:** IA agrega 20 features no solicitadas.

**Solución:**
```
"ALTO. Descarta todo lo que agregaste.
Vuelve a la versión anterior.
SOLO implementa [feature específica], nada más."
```

---

#### Error 2: "No entiende mi visión"

**Síntoma:** Output no se parece a lo imaginado.

**Solución:**
- Adjuntar screenshot de referencia
- Dibujar boceto y compartir imagen
- Usar analogías: "Como Stripe, pero más colorido"

---

#### Error 3: "Código no funciona"

**Síntoma:** Errores de runtime, bugs.

**Solución:**
```
"Hay un error: [copiar mensaje de error]

Analiza el problema y arréglalo.
Explica qué causó el error."
```

---

#### Error 4: "IA olvida contexto anterior"

**Síntoma:** En iteración 5, pierde features de iteración 1.

**Solución:**
- Usar herramientas con artifacts (Claude, ChatGPT Canvas)
- Cada 3-4 iteraciones, reset y consolidar estado
- Guardar versiones intermedias

---

## 6. Casos de Uso por Industria

### 6.1 Salud (Healthcare)

#### Caso 1: Triaje Automatizado

**Problema:** Clínica con sobrecarga de llamadas para citas.

**Solución con Vibe Coding:**
```
Herramienta: Lovable
Tiempo: 3 horas
Complejidad: Media

App:
- Formulario de síntomas (checkboxes)
- Clasificación automática: Urgente / Normal / Puede esperar
- Sugerencia de especialidad
- Agenda cita según clasificación
- Integración WhatsApp para confirmación
```

**Impacto:**
- 60% reducción en llamadas
- Triaje más consistente
- Pacientes urgentes priorizados

---

#### Caso 2: Dashboard de Métricas Clínicas

**Problema:** Médicos quieren ver KPIs de pacientes.

**Solución:**
```
Herramienta: Replit Agent + Streamlit
Tiempo: 4 horas
Complejidad: Media

Dashboard:
- Conexión a DB de registros médicos
- Gráficos: Pacientes/mes, Diagnósticos top, Readmisiones
- Filtros: Rango fechas, Doctor, Especialidad
- Export a PDF para reportes
```

---

### 6.2 E-Commerce

#### Caso 1: Landing Page de Producto

**Problema:** Startup lanza producto nuevo, necesita landing rápido.

**Solución:**
```
Herramienta: v0.dev
Tiempo: 1.5 horas
Complejidad: Baja

Landing:
- Hero con video demo producto
- Sección features (3 cards)
- Pricing table (2 tiers)
- FAQ accordion
- Form de early access
- Footer con redes sociales
```

---

#### Caso 2: Generador de Descripciones de Producto

**Problema:** 500 productos sin descripciones SEO-friendly.

**Solución:**
```
Herramienta: Replit Agent + OpenAI API
Tiempo: 2 horas
Complejidad: Baja

App:
- Cargar CSV con productos (nombre, categoría, specs)
- Botón "Generar descripciones"
- IA crea descripción 50-100 palabras por producto
- Export CSV con descripciones
- Bulk upload a Shopify
```

---

### 6.3 Educación

#### Caso 1: Quiz Interactivo

**Problema:** Profesor quiere quiz personalizado por tema.

**Solución:**
```
Herramienta: Claude Artifacts
Tiempo: 30 minutos
Complejidad: Baja

Quiz:
- 10 preguntas con opciones múltiples
- Timer de 15 minutos
- Feedback inmediato (correcto/incorrecto)
- Puntaje final con % acierto
- Explicaciones de respuestas
```

**Caso real de clase:** Infografía CRISP-DM
- Visualización interactiva de metodología
- Tooltips explicativos
- Navegación entre fases

---

### 6.4 Finanzas

#### Caso 1: Calculadora de ROI

**Problema:** Sales team necesita calcular ROI para demos.

**Solución:**
```
Herramienta: Claude Artifacts
Tiempo: 20 minutos
Complejidad: Baja

Calculator:
- Inputs: Inversión inicial, Ingresos mensuales, Costos
- Cálculo automático: ROI %, Payback period, NPV
- Gráfico de proyección 12 meses
- Botón "Generar PDF" para enviar a cliente
```

**Caso real de clase:** App "Orbital Finance"
- Tracking de acciones
- Gráficos de cotización
- Portafolio personal

---

### 6.5 Recursos Humanos

#### Caso 1: Portal de Onboarding

**Problema:** 20 nuevos empleados/mes, onboarding manual caótico.

**Solución:**
```
Herramienta: Lovable
Tiempo: 4 horas
Complejidad: Media

Portal:
- Checklist de tareas (firmar contratos, completar perfil, etc.)
- Videos de introducción a empresa
- Directorio de equipo con fotos y roles
- Chat para preguntas frecuentes (FAQ bot)
- Progreso visual del onboarding (barra %)
```

---

## 7. Patrones de Prompting Avanzados

### 7.1 Taxonomía de Patrones

```
Patrones de Prompting
├── Estructurales
│   ├── Template-Based
│   ├── Especificación por Ejemplos
│   └── Constraints-Driven
├── Cognitivos
│   ├── Chain of Thought
│   ├── Role-Playing
│   └── Self-Correction
├── Iterativos
│   ├── Refinamiento Progresivo
│   ├── A/B Comparison
│   └── Error-Driven Development
└── Contextuales
    ├── Context-First
    ├── User Story Format
    └── Domain-Specific Language
```

### 7.2 Patrones Estructurales

#### Patrón: Template-Based

**Cuándo usar:** Primera iteración, app desde cero.

**Template genérico:**
```markdown
# Contexto
[Quién eres, cuál es el problema]

# Objetivo
Crear [tipo de app] que [propósito]

# Funcionalidades Core
- [Feature 1]
- [Feature 2]
- [Feature 3]

# Diseño Visual
- Colores: [paleta específica]
- Tipografía: [fonts]
- Estilo: [adjetivos: minimalista, vibrante, corporativo]
- Referencias: [apps similares o screenshots]

# Datos
[Mock data, estructura de objetos, o fuente de datos]

# Restricciones
- [Técnicas: performance, tamaño]
- [Negocio: regulaciones, compliance]
- [UX: accesibilidad, idiomas]
```

**Ejemplo aplicado:**
```markdown
# Contexto
Soy gerente de ventas de una distribuidora de alimentos.
Necesito trackear visitas de vendedores a clientes.

# Objetivo
Crear app móvil-friendly para registrar visitas de campo

# Funcionalidades Core
- Formulario de visita: Cliente (dropdown), Fecha, Productos mostrados, Orden capturada (sí/no), Notas
- Lista de visitas del día (ordenadas por hora)
- Mapa con ubicaciones de clientes visitados
- Estadísticas diarias: Total visitas, % conversión, Top productos

# Diseño Visual
- Colores: Verde #10B981 (primario), Gris #6B7280 (secundario)
- Tipografía: Inter (moderna, legible en móvil)
- Estilo: Limpio, profesional, fácil de usar con una mano
- Referencias: Google Maps + Notion (simplicidad)

# Datos
Clientes mock:
- Nombre: "Supermercado El Éxito", "Tienda D1", "Carulla"
- Dirección + coordenadas
Productos: ["Leche", "Pan", "Huevos", "Queso"]

# Restricciones
- Móvil-first (360px width)
- Offline-capable (guardar localmente si no hay internet)
- Accesibilidad: contraste AA, botones grandes
```

---

#### Patrón: Especificación por Ejemplos

**Cuándo usar:** Tienes referencia visual de lo que quieres.

**Formato:**
```
Crea [componente] inspirado en [referencia]

[Adjuntar screenshot o link]

Diferencias con la referencia:
- Cambiar [aspecto 1] por [nuevo valor]
- Agregar [feature nueva]
- Remover [feature innecesaria]
```

**Ejemplo:**
```
Crea un hero section inspirado en https://stripe.com

[O adjuntar screenshot del hero de Stripe]

Diferencias:
- Headline: "Automatiza tu nómina en minutos"
- Subheadline: Nuestro producto, no Stripe
- CTA primario: "Probar gratis" (no "Sign up")
- Colores: Azul #3B82F6 (no Stripe purple)
- Mantener: Animación de gradiente, layout general
```

---

### 7.3 Patrones Cognitivos

#### Patrón: Chain of Thought (Cadena de Pensamiento)

**Cuándo usar:** Problemas complejos que requieren razonamiento.

**Formato:**
```
Antes de implementar, piensa paso a paso:

1. [Pregunta de diseño]
2. [Pregunta de arquitectura]
3. [Pregunta de edge cases]

Documenta tu razonamiento, luego implementa.
```

**Ejemplo:**
```
Voy a crear un sistema de reservas de restaurante.

Antes de implementar, piensa paso a paso:

1. ¿Cómo represento horarios disponibles (slots)?
   - ¿Array de objetos {hora, disponible}?
   - ¿Cómo manejar múltiples mesas?

2. ¿Qué pasa si dos usuarios reservan al mismo tiempo?
   - ¿Necesito locking optimista?
   - ¿O simplemente primero en llegar?

3. ¿Cómo cancelo reservas?
   - ¿Cuánto tiempo antes se puede cancelar?
   - ¿Libero el slot inmediatamente?

Después de razonar, implementa la mejor solución.
```

---

#### Patrón: Role-Playing

**Cuándo usar:** Necesitas expertise específica.

**Roles efectivos:**
- "Senior UX designer con 10 años en SaaS"
- "Backend architect especializado en sistemas de pagos"
- "Security engineer con certificación CISSP"
- "Accessibility advocate (WCAG expert)"

**Formato:**
```
Eres [rol experto].

[Descripción de problema]

Aplica tu experiencia de [dominio] para resolver esto.
```

**Ejemplo:**
```
Eres una senior UX researcher especializada en onboarding de apps fintech.

Diseña un flow de KYC (Know Your Customer) que:
- Cumpla regulaciones colombianas (Superfinanciera)
- Minimice fricción (no más de 5 minutos)
- Tenga fallbacks si cédula no se lee correctamente

Aplica las mejores prácticas de UX fintech que conoces.
Prioriza conversión sobre seguridad (pero mantén mínimos legales).
```

---

### 7.4 Patrones Iterativos

#### Patrón: Refinamiento Progresivo

**Cuándo usar:** Iterar sobre versión existente.

**Vocabulario efectivo:**
```
Nivel 1 (Estructura):
- "Reorganiza el layout..."
- "Mueve X al lado de Y"
- "Agrupa estos elementos relacionados"

Nivel 2 (Estilo):
- "Haz los colores más vibrantes"
- "Aumenta el contraste del texto"
- "Espaciado más generoso entre secciones"

Nivel 3 (Funcionalidad):
- "Agrega validación al formulario"
- "Implementa búsqueda en tabla"
- "Filtros por categoría"

Nivel 4 (Polish):
- "Animaciones sutiles al hover"
- "Loading states"
- "Empty states con ilustraciones"
```

---

#### Patrón: A/B Comparison

**Cuándo usar:** No estás seguro de qué opción es mejor.

**Formato:**
```
Genera 2 versiones de [componente]:

Versión A: [Descripción opción 1]
Versión B: [Descripción opción 2]

Muéstralas lado a lado para que yo elija.
```

**Ejemplo:**
```
Genera 2 versiones del pricing table:

Versión A: Layout vertical (tiers uno debajo de otro)
- Mejor para móvil
- Enfatiza comparación secuencial

Versión B: Layout horizontal (tiers lado a lado)
- Mejor para desktop
- Comparación visual directa

Implementa ambas y muéstralas para que yo elija.
```

---

### 7.5 Anti-Patrones (Qué NO Hacer)

#### Anti-Patrón 1: Sobre-Especificación Técnica

**❌ MALO:**
```
Crea un React functional component usando useState hook
para manejar el estado del contador. Usa useCallback
para memoizar el handler de click. Estiliza con
Tailwind usando clases flex justify-center items-center
bg-gradient-to-r from-blue-500 to-purple-600 rounded-lg
shadow-xl hover:shadow-2xl transition-all duration-300.
```

**✅ BUENO:**
```
Crea un contador moderno.
- Colores: gradiente azul-morado energético
- Botones grandes y táctiles
- Animación suave al click
```

**Por qué:** IA es mejor decidiendo detalles técnicos. Tu rol es visión.

---

#### Anti-Patrón 2: Ambigüedad Extrema

**❌ MALO:**
```
Crea algo cool para mi negocio.
```

**✅ BUENO:**
```
Contexto: Vendo repostería artesanal por Instagram.
Necesito landing page para capturar pedidos.

Objetivo: Mostrar catálogo de productos con precios,
formulario de pedido con delivery, y WhatsApp directo.

Estilo: Femenino, colores pasteles (rosa, lila),
tipografía elegante, fotos de postres destacadas.
```

**Por qué:** IA no puede leer tu mente. Contexto > Todo.

---

#### Anti-Patrón 3: Prompts Contradictorios

**❌ MALO:**
```
"Crea un dashboard minimalista con muchos colores vibrantes
y animaciones complejas pero que sea super simple."
```

**✅ BUENO:**
```
Versión 1: "Dashboard minimalista (paleta monocromática,
espacios amplios, animaciones sutiles)"

O

Versión 2: "Dashboard vibrante (colores saturados,
animaciones dinámicas, información densa)"
```

**Por qué:** Contradicciones confunden a la IA. Define prioridades claras.

---

## 8. Arquitectura Técnica (Overview)

### 8.1 ¿Qué Pasa "Por Detrás"?

Cuando usas Vibe Coding, hay una cadena de procesamiento:

```
Tu Prompt → LLM (GPT-4/Claude) → Código Generado → Runtime → Preview
```

#### Paso 1: Procesamiento del Prompt

```python
# Pseudocódigo simplificado
def process_prompt(user_prompt, context):
    # 1. Agregar contexto del sistema
    system_context = """
    Eres un experto desarrollador fullstack.
    Genera código funcional, limpio, y con buenas prácticas.
    Stack: React + TailwindCSS
    """

    # 2. Agregar historial de conversación
    conversation_history = get_previous_messages(user_id)

    # 3. Agregar ejemplos (few-shot learning)
    examples = """
    Ejemplo 1: Prompt "botón azul" → <button className="bg-blue-500">Click</button>
    Ejemplo 2: Prompt "formulario de login" → [código de form]
    """

    # 4. Construir prompt completo
    full_prompt = system_context + examples + conversation_history + user_prompt

    # 5. Enviar a LLM
    response = llm_api.complete(full_prompt)

    return response
```

#### Paso 2: Generación de Código

El LLM genera código en formato estructurado:

```json
{
  "language": "tsx",
  "framework": "react",
  "code": "import React from 'react'...",
  "dependencies": ["react", "tailwindcss"],
  "explanation": "Este componente crea un botón..."
}
```

#### Paso 3: Compilación y Ejecución

```javascript
// Lovable, v0.dev, etc. hacen esto internamente
const code = generated_response.code;

// Transpilar TypeScript → JavaScript
const js_code = typescript.transpile(code);

// Bundlear con dependencias
const bundle = webpack.bundle(js_code, dependencies);

// Inyectar en iframe para preview
iframe.contentWindow.eval(bundle);
```

### 8.2 Stacks Técnicos Comunes

#### Lovable / v0.dev

```yaml
Frontend:
  - React (UI library)
  - TailwindCSS (Styling)
  - TypeScript (Type safety)

Backend (si aplica):
  - Node.js + Express
  - PostgreSQL (Database)
  - Prisma (ORM)

Hosting:
  - Vercel / Netlify (Static)
  - Railway / Fly.io (Fullstack)
```

#### Replit Agent

```yaml
Flexible (50+ lenguajes):
  - Python: Flask, FastAPI, Django
  - JavaScript: Express, Next.js
  - Go: Gin, Echo
  - Rust: Actix, Rocket

Database:
  - PostgreSQL (managed)
  - MongoDB
  - Redis (caching)

Hosting:
  - Replit infrastructure (containers)
```

### 8.3 Limitaciones Técnicas

#### Limitación 1: Context Window

**Problema:** LLMs tienen límite de tokens de contexto.

| Modelo | Context Window | Equivalente |
|--------|----------------|-------------|
| GPT-4 | 8K-32K tokens | ~6K-24K líneas código |
| Claude 3.5 | 200K tokens | ~150K líneas código |
| Gemini 1.5 | 1M tokens | ~750K líneas código |

**Implicación:**
- Apps muy grandes (>10K líneas) pierden contexto
- IA "olvida" código de archivos lejanos
- Necesitas arquitectura modular

**Solución:**
- Divide app en módulos pequeños
- Usa herramientas como Cursor (contexto de codebase)

---

#### Limitación 2: Alucinaciones

**Problema:** IA inventa APIs/funciones que no existen.

**Ejemplo:**
```javascript
// IA genera esto (pero no existe):
import { magicSort } from 'react-utils';

const sorted = magicSort(data, 'name');
```

**Solución:**
- Especificar librerías exactas a usar
- Validar código generado en runtime
- Iterar corrigiendo errores

---

#### Limitación 3: Estado y Persistencia

**Problema:** Apps generadas no persisten datos por defecto.

**¿Por qué?**
- Requiere backend + base de datos
- IA no puede configurar infraestructura externa

**Solución:**
- LocalStorage para datos simples
- Backend-as-a-Service (Supabase, Firebase)
- Especificar explícitamente en prompt

---

## 9. Seguridad, Privacidad y Compliance

### 9.1 Riesgos de Seguridad

#### Riesgo 1: Exposición de Datos Sensibles

**Escenario:**
```
Usuario: "Crea dashboard con datos de clientes"
[Adjunta CSV con nombres, emails, cédulas]
```

**Qué ocurre:**
- IA procesa datos en servidores del proveedor (OpenAI, Anthropic)
- Datos se usan para entrenamiento (si está habilitado)
- Terceros potencialmente acceden

**Mitigación:**
1. **Anonimizar datos** antes de subir
```python
import pandas as pd
df = pd.read_csv('clientes.csv')
df['cedula'] = df['cedula'].apply(lambda x: 'XXX-' + str(x)[-4:])
df['email'] = df['email'].apply(lambda x: 'user' + str(hash(x))[:6] + '@example.com')
```

2. **Usar datos sintéticos** para prototipo
```
Genera datos mock de 50 clientes:
- Nombre: nombres colombianos comunes
- Email: firstname.lastname@example.com
- Cédula: formato válido pero ficticio
```

3. **Desactivar entrenamiento**
- ChatGPT: Settings > Data Controls > desactivar "Improve model"
- Claude: Settings > Privacy > desactivar "Train on data"

---

#### Riesgo 2: Código Vulnerable

**Problema:** IA puede generar código con vulnerabilidades.

**Vulnerabilidades comunes:**
```javascript
// ❌ SQL Injection
const query = `SELECT * FROM users WHERE id = ${userId}`;

// ❌ XSS (Cross-Site Scripting)
innerHTML = userInput;

// ❌ Hardcoded credentials
const API_KEY = "sk-1234567890abcdef";
```

**Mitigación:**
```
Prompt de seguridad:

"Genera código siguiendo OWASP Top 10:
- Usa prepared statements (NO string concatenation en SQL)
- Sanitiza todos los inputs de usuario
- NO hardcodear secrets (usa variables de entorno)
- Implementa rate limiting en APIs
- Valida y escapa outputs"
```

---

#### Riesgo 3: Vendor Lock-In

**Problema:** Dependencia de plataforma dificulta migración.

**Severidad por herramienta:**

| Herramienta | Lock-In | Mitigación |
|-------------|---------|------------|
| Lovable | 🔴 Alto | ❌ Código no exportable fácilmente |
| Replit | 🟡 Medio | ⚠️ Exportar via Git, rebuild infra |
| v0.dev | 🟢 Bajo | ✅ Código exportable estándar |
| Claude/ChatGPT | 🟢 Bajo | ✅ Código copiable, framework estándar |
| Cursor | 🟢 Bajo | ✅ Código local en tu máquina |

**Best practice:** Usar herramientas con código exportable para proyectos críticos.

---

### 9.2 Compliance y Regulaciones

#### GDPR (Europa) / LGPD (Brasil) / Ley 1581 (Colombia)

**Principios clave:**
1. **Minimización de datos**: Solo pedir datos necesarios
2. **Derecho al olvido**: Permitir eliminar datos
3. **Consentimiento explícito**: Checkbox de términos

**Checklist para apps con datos personales:**
```
- [ ] Política de privacidad visible y comprensible
- [ ] Checkbox de consentimiento (NO pre-checked)
- [ ] Opción de eliminar cuenta y datos
- [ ] Encriptar datos sensibles en tránsito y reposo
- [ ] Logging de acceso a datos personales
- [ ] DPO (Data Protection Officer) si aplica
```

**Prompt de compliance:**
```
"Crea formulario de registro cumpliendo GDPR:

- Checkbox de aceptación de términos (explícito, NO default checked)
- Link a política de privacidad
- Checkbox separado para newsletter (opcional)
- Mensaje de qué datos se recolectan y por qué
- Opción de solicitar eliminación de datos

Diseño: claro, no abrumador, pero legal."
```

---

#### WCAG (Web Content Accessibility Guidelines)

**Nivel AA (mínimo recomendado):**

**Criterios principales:**
1. **Contraste:** Mínimo 4.5:1 para texto
2. **Navegación por teclado:** Todo accesible con Tab/Enter
3. **Alt text:** Descripciones de imágenes
4. **Labels:** Todos los inputs con label asociado

**Prompt de accesibilidad:**
```
"Genera formulario accesible (WCAG 2.1 AA):

- Contraste mínimo 4.5:1 entre texto y fondo
- Todos los inputs con <label> asociado (for/id)
- Imágenes decorativas con alt=""
- Focus visible en navegación por teclado
- Mensajes de error descriptivos y asociados con aria-describedby

Test: debe ser usable solo con teclado."
```

---

### 9.3 Best Practices Empresariales

#### Para Empleados

**🚫 NO HACER:**
- ❌ Subir código de la empresa a IAs públicas
- ❌ Compartir credenciales en prompts
- ❌ Generar apps con datos de clientes reales
- ❌ Usar planes gratuitos para proyectos críticos

**✅ SÍ HACER:**
- ✅ Usar cuenta corporativa (si empresa tiene)
- ✅ Pedir permiso antes de usar IAs con data sensible
- ✅ Prototipo con datos sintéticos/mock
- ✅ Revisar código generado antes de producción

---

#### Para Empresas

**Políticas recomendadas:**

```yaml
Política de Uso de IA Generativa

Permitido:
  - Prototipos con datos ficticios
  - Generación de docs públicas
  - Refactoring de código open-source interno
  - Aprendizaje y experimentación

Requiere Aprobación:
  - Apps con datos de clientes
  - Integración con sistemas críticos
  - Deploy a producción

Prohibido:
  - Secretos/credenciales en prompts
  - Código de algoritmos propietarios
  - PII (Personally Identifiable Information)
  - Propiedad intelectual estratégica
```

---

## 10. Troubleshooting y Errores Comunes

### 10.1 Errores de IA

#### Error 1: "No puedo generar eso"

**Síntoma:** IA se niega a generar código.

**Causas comunes:**
- Prompt incluye lenguaje ofensivo
- Solicitud de código malicioso (hacking)
- Violación de términos de servicio

**Solución:**
```
Reformular prompt sin palabras sensibles:

❌ "Crea hack para..."
✅ "Crea script de testing de seguridad para..."
```

---

#### Error 2: "IA genera código que no funciona"

**Síntoma:** Código tiene errores de sintaxis o runtime.

**Debug workflow:**
```
1. Copiar mensaje de error exacto
2. Prompt: "Hay este error: [pegar error]. Analiza y arregla."
3. Si persiste: "Explica paso a paso qué hace el código"
4. Si aún falla: "Reescribe desde cero usando [alternativa]"
```

**Ejemplo:**
```
IA generó:
const data = response.json();

Error: TypeError: response.json is not a function

Prompt de fix:
"Error: response.json is not a function
Analiza el problema. ¿Es fetch? ¿Axios?
Corrige usando la API correcta."
```

---

#### Error 3: "IA olvida contexto anterior"

**Síntoma:** En iteración 5, features de iteración 1 desaparecen.

**Solución:**
```
Opción 1: Reset con contexto consolidado
"Resumen de lo que tenemos hasta ahora:
- Feature A: [descripción]
- Feature B: [descripción]
- Estilos: [paleta]

Ahora agrega Feature C sin modificar A ni B."

Opción 2: Usar herramientas con artifacts
- Claude Artifacts (mantiene versión)
- ChatGPT Canvas (editable)
- Lovable (historial de versiones)
```

---

### 10.2 Errores de Plataforma

#### Error 1: "Rate limit exceeded"

**Síntoma:** "Too many requests, try again later"

**Causas:**
- Demasiadas requests en poco tiempo
- Plan gratuito con límites estrictos

**Solución:**
- Esperar 1-5 minutos
- Upgrade a plan pago
- Usar alternativa temporalmente

---

#### Error 2: "Token limit exceeded"

**Síntoma:** Prompt muy largo no se procesa.

**Solución:**
```
Dividir en chunks:

Prompt 1: "Crea estructura base del dashboard"
[Esperar respuesta]

Prompt 2: "Agrega gráficos de línea para ventas"
[Esperar respuesta]

Prompt 3: "Agrega tabla de productos top"
```

---

### 10.3 Errores de Usuario

#### Error 1: "No sé cómo describir lo que quiero"

**Solución:** Usar referencias visuales.

```
Opción 1: Adjuntar screenshot
"Crea algo como esto [adjuntar imagen]"

Opción 2: Analogías
"Crea dashboard estilo Stripe, pero para finanzas personales"

Opción 3: Dibujar boceto
[Dibujar en papel, foto, adjuntar]
"Implementa este diseño"
```

---

#### Error 2: "Resultado no es lo que esperaba"

**Workflow de refinamiento:**
```
Iteración 1: Intento inicial
→ Output: 60% de lo esperado

Iteración 2: "Cambia X, Y, Z"
→ Output: 75% de lo esperado

Iteración 3: "Casi perfecto, ajusta solo [detalle]"
→ Output: 90% de lo esperado

Si después de 3-4 iteraciones no mejora:
→ Reset: "Descarta todo, empecemos de nuevo con este approach..."
```

---

## 11. Roadmap de Aprendizaje

### 11.1 Nivel 1: Fundamentos (Semana 1-2)

**Objetivo:** Crear primer app funcional sin código.

#### Día 1-2: Conceptos

- [ ] Leer esta guía (secciones 1-3)
- [ ] Ver videos introductorios:
  - "What is Vibe Coding?" (YouTube)
  - "Lovable tutorial" (10 min)
- [ ] Crear cuentas:
  - ChatGPT (free)
  - Claude (free)
  - Lovable (free trial)

#### Día 3-5: Primera App

- [ ] Ejercicio: Landing page personal
  - Herramienta: Claude Artifacts o Lovable
  - Secciones: Hero, About, Skills, Contact
  - Tiempo objetivo: 2 horas

**Checklist de éxito:**
- [ ] App funcional y publicada
- [ ] Al menos 3 iteraciones de mejora
- [ ] Compartida con 2-3 personas para feedback

#### Día 6-7: Segunda App

- [ ] Ejercicio: Calculadora especializada
  - Ejemplos: ROI calculator, BMI calculator, Tip calculator
  - Herramienta: Claude Artifacts
  - Tiempo objetivo: 1 hora

---

### 11.2 Nivel 2: Intermedio (Semana 3-4)

**Objetivo:** Apps con lógica de negocio y datos.

#### Semana 3: App con Estado

- [ ] Ejercicio: Todo list con filtros
  - Funcionalidades: Crear, completar, filtrar, contar
  - Herramienta: Lovable o v0.dev
  - Persistencia: LocalStorage

**Checklist:**
- [ ] Maneja estado complejo (lista + filtros)
- [ ] Persiste datos (no se pierde al recargar)
- [ ] Validaciones de input

#### Semana 4: App con API

- [ ] Ejercicio: Weather app
  - API: OpenWeather (free tier)
  - Herramienta: Replit Agent
  - Features: Búsqueda ciudad, forecast 5 días, geolocalización

**Checklist:**
- [ ] Integra API externa
- [ ] Maneja estados: loading, error, success
- [ ] UI responsive

---

### 11.3 Nivel 3: Avanzado (Mes 2)

**Objetivo:** Apps completas fullstack.

#### Proyecto 1: CRUD App

- [ ] Ejercicio: Sistema de gestión (elegir dominio)
  - Ejemplos: Inventario, CRM, Gestión de proyectos
  - Backend: Replit + PostgreSQL
  - Auth: Login simple
  - Tiempo: 8-12 horas (distribuir en semana)

**Features mínimas:**
- [ ] CRUD completo (Create, Read, Update, Delete)
- [ ] Autenticación básica
- [ ] Filtros y búsqueda
- [ ] Validaciones server-side

#### Proyecto 2: App con Integraciones

- [ ] Ejercicio: Dashboard de métricas
  - Integraciones: Google Sheets / Airtable + API externa
  - Visualizaciones: Gráficos interactivos
  - Herramienta: Replit Agent + Chart library

---

### 11.4 Nivel 4: Expert (Mes 3+)

**Objetivo:** Producción-ready apps, arquitectura escalable.

#### Transición a Herramientas Pro

- [ ] Aprender Cursor
  - Multi-file editing
  - Refactoring de codebase grande
  - Test generation

- [ ] Best practices avanzadas
  - TypeScript estricto
  - Testing (Jest, Playwright)
  - CI/CD pipelines

#### Proyecto Final: Startup MVP

- [ ] Elegir idea real de negocio
- [ ] Diseñar arquitectura completa
- [ ] Implementar con Vibe Coding + edición manual
- [ ] Deploy a producción
- [ ] Métricas de uso (Analytics)

**Objetivo:** App usable por clientes reales, 90%+ generada por IA.

---

## 12. Recursos y Bibliografía

### 12.1 Documentación Oficial

**Herramientas:**
- [Lovable Docs](https://docs.lovable.dev)
- [Replit AI Guide](https://docs.replit.com/replitai)
- [v0.dev Examples](https://v0.dev/chat)
- [Claude Artifacts](https://www.anthropic.com/news/artifacts)
- [Cursor Documentation](https://docs.cursor.com)

**APIs y Frameworks:**
- [React Docs](https://react.dev)
- [TailwindCSS](https://tailwindcss.com/docs)
- [Next.js](https://nextjs.org/docs)
- [Supabase](https://supabase.com/docs)

---

### 12.2 Cursos y Tutoriales

**Video Tutoriales (YouTube):**
- "Build a SaaS with AI in 24 hours" - Fireship
- "v0.dev Complete Tutorial" - Vercel
- "Lovable Tutorial for Beginners" - No Code MBA
- "Cursor IDE Masterclass" - Code with Antonio

**Cursos Estructurados:**
- "AI-Assisted Development" - Frontend Masters
- "No-Code Development Bootcamp" - Udemy
- "Prompt Engineering for Developers" - DeepLearning.AI

---

### 12.3 Comunidades

**Discord:**
- [Lovable Community](https://discord.gg/lovable)
- [Replit Community](https://discord.gg/replit)
- [Cursor Community](https://discord.gg/cursor)

**Reddit:**
- [r/aicoding](https://reddit.com/r/aicoding)
- [r/nocode](https://reddit.com/r/nocode)
- [r/SideProject](https://reddit.com/r/SideProject)

**Twitter/X (Influencers):**
- @AndrewYNg (Fundador concepto Vibe Coding)
- @OpenAI (Noticias GPT)
- @AnthropicAI (Noticias Claude)
- @vercel (v0.dev updates)

---

### 12.4 Artículos y Papers

**Artículos Clave:**
- "The Future of Programming with AI" - Andrew Ng (2024)
- "AI Coding Tools: 2025 Survey" - Y Combinator Research
- "Democratizing Software Development" - MIT Technology Review
- "GitHub Copilot Impact Study" - GitHub Research (2024)

**Papers Académicos:**
- "Large Language Models for Code Generation" - arXiv
- "Evaluating LLM-Generated Code Quality" - ACM
- "Human-AI Collaboration in Software Engineering" - IEEE

---

### 12.5 Herramientas Complementarias

**Diseño:**
- [Figma](https://figma.com) - Diseño de interfaces
- [Excalidraw](https://excalidraw.com) - Bocetos rápidos
- [Coolors](https://coolors.co) - Paletas de colores

**Iconos e Imágenes:**
- [Lucide Icons](https://lucide.dev) - Iconos React
- [Unsplash](https://unsplash.com) - Fotos stock
- [Illustrations](https://undraw.co) - Ilustraciones SVG

**Deployment:**
- [Vercel](https://vercel.com) - Frontend hosting
- [Railway](https://railway.app) - Fullstack apps
- [Netlify](https://netlify.com) - Static sites

---

## 🎯 Conclusión

Vibe Coding representa un cambio paradigmático en cómo creamos software. Ya no se trata de **escribir código**, sino de **dirigir la creación de software** mediante conversación natural con inteligencia artificial.

### Puntos Clave para Recordar

1. **Es una habilidad, no conocimiento teórico** - Se aprende practicando, no leyendo
2. **Democratización tecnológica** - Cualquiera puede crear apps, sin ser programador
3. **Ideal para prototipos** - 10x más rápido que desarrollo tradicional
4. **Limitaciones claras** - No para todo (producción crítica, sistemas complejos)
5. **Seguridad es crítica** - No usar con datos sensibles sin validación

### El Futuro

En 5-10 años, Vibe Coding será tan fundamental como usar Excel hoy. Los profesionales que lo dominen tendrán ventaja competitiva crucial en el mercado laboral.

**Tu siguiente paso:** Crear tu primera app. Ahora mismo. No en una semana. **Hoy**.

---

**Documento creado por:** Julián Zuluaga (Orbital Lab) + Claude (Anthropic)
**Última actualización:** 28 de octubre de 2025
**Versión:** 2.0 Expandida
**Licencia:** Creative Commons BY-NC-SA 4.0

Para preguntas o feedback: julian@orbitallab.co
