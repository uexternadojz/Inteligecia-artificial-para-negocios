<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

## Claude Skills: La Nueva Funcionalidad de Anthropic - Guía Técnica Profunda

Claude Skills es la innovación más reciente de Anthropic lanzada el **16 de octubre de 2025**, representando un cambio fundamental en cómo especializar agentes de IA con expertise reutilizable. Mientras que los sub-agentes se enfocan en paralelismo y aislamiento de tareas, las Skills resuelven un problema diferente: cómo cargar expertise especializada de manera eficiente sin sobrecargar la ventana de contexto.[^1][^2]

## ¿Qué Son las Claude Skills?

Las Skills son **carpetas organizadas de instrucciones, scripts y recursos** que Claude carga dinámicamente cuando son relevantes para una tarea. Se diferencian fundamentalmente de los sub-agentes porque:[^1][^3]

- **Sub-Agentes**: Son asistentes independientes con contexto aislado que manejan tareas complejas en paralelo
- **Skills**: Son "paquetes de expertise" que se cargan en el contexto del agente principal de forma progresiva[^4]

La metáfora oficial de Anthropic es clara: "Crear una Skill es como preparar un manual de onboarding para un nuevo empleado". No es un agente separado; es expertise empaquetada que Claude aprende a usar automáticamente.[^2][^5]

![Claude Skills vs Sub-Agents vs Traditional Prompts: Technical Comparison and Use Cases](https://ppl-ai-code-interpreter-files.s3.amazonaws.com/web/direct-files/bd97dd16882099750b87a8e36c91f527/2d2c88cf-6299-4dfb-923c-efdf52a4f25c/dcde6011.png)

Claude Skills vs Sub-Agents vs Traditional Prompts: Technical Comparison and Use Cases

## Arquitectura Técnica: Progressive Disclosure

El concepto central que hace a las Skills revolucionarias es **progressive disclosure** (divulgación progresiva), un mecanismo de tres niveles que resuelve la sobrecarga de contexto:[^3][^6]

### Nivel 1: Metadata (Siempre Cargado)

Al iniciar sesión, Claude carga **solo** los metadatos YAML de cada Skill disponible:

```yaml
---
name: "pdf-processing"
description: "Extract text and tables from PDFs, fill forms, merge documents. Use when working with PDF files or user mentions PDFs, forms, or document extraction."
---
```

**Costo de Token**: ~100 tokens por Skill, sin importar cuántas Skills tengas instaladas. Con 20 Skills instaladas = ~2000 tokens en startup. Comparado con cargar todos los prompts completos, esto es revolucionario.[^2][^3][^7]

**Cómo funciona**: Claude escanea esta descripción y decide automáticamente si la Skill es relevante para tu solicitud. Es exactamente lo que Meta hace internamente con su sistema de routing de agentes, pero de forma descentralizada.[^8]

### Nivel 2: Instrucciones (Cargadas al Activarse)

Si Claude detecta que una Skill es relevante, Lee la carpeta SKILL.md completa **desde el filesystem**:

```bash
# Claude ejecuta internamente:
bash: read pdf-skill/SKILL.md
```

El contenido entra al contexto solo entonces. **Costo**: < 5,000 tokens típicamente.[^3][^7]

**Ejemplo práctico**: Dices "extrae texto de este PDF". Claude:

1. Ve que "pdf" + "extract" coincide con la descripción de pdf-processing
2. Lee SKILL.md desde el filesystem
3. Procede con la tarea usando las instrucciones

### Nivel 3+: Recursos (Bajo Demanda)

Las Skills pueden incluir archivos adicionales referenciados **contextualmente** desde SKILL.md:

```
pdf-skill/
├── SKILL.md (core, ~2K tokens)
├── FORMS.md (form-filling guide, ~3K tokens - SOLO si necesario)
├── REFERENCE.md (API reference, ~5K tokens - SOLO si necesario)
└── scripts/
    └── fill_form.py (código ejecutable - NO entra a contexto)
```

Si la tarea NO requiere llenar formularios, FORMS.md nunca se carga. La ventaja: puedes bundlear documentación ilimitada sin penalidad de contexto.[^3][^5]

**Datos clave**:[^3]

- Metadata (Nivel 1): ~100 tokens per skill
- Instructions (Nivel 2): Under 5k tokens
- Resources/Scripts (Nivel 3): Effectively unlimited (ejecutados via bash sin cargar código)


## Integración con Claude Code: Cómo Funciona

Las Skills en Claude Code son **completamente nativas** y funcionan a través del filesystem local, NO requieren uploads a API:[^9][^10]

### Estructura de Carpetas en Claude Code

```
.claude/skills/              # Project-specific (prioridad alta)
├── authentication-setup/
│   ├── SKILL.md
│   ├── scripts/
│   │   ├── create_auth.py
│   │   └── validate_jwt.py
│   └── resources/
│       ├── security-patterns.md
│       └── templates/
└── database-migration/

~/.claude/skills/           # User-level (prioridad baja, disponible globalmente)
└── custom-reporter/
```


### Cómo Se Descubren y Usan Automáticamente

Cuando inicias Claude Code en un proyecto:

1. Claude escanea `.claude/skills/` (proyecto) y `~/.claude/skills/` (usuario)
2. Carga metadata de cada SKILL.md en su system prompt
3. A medida que trabajas, detecta automáticamente cuándo son relevantes
4. Invoca explícitamente: `> Usa el authentication-setup skill para crear JWT`

**Diferencia crítica con sub-agentes**: Las Skills se activan automáticamente sin necesidad de Task/delegación explícita. No necesitas escribir código especial para invocarlas.[^9][^10]

## Casos de Uso Real: Skills vs Sub-Agentes vs Prompts

### Cuándo Usar Skills

**Mejor para**: Workflows repetitivos con forma consistente que quieres que Claude identifique automáticamente:[^11]


| Caso | Por Qué Skills | Ejemplo |
| :-- | :-- | :-- |
| Revisión de código | Detección automática basada en descripción | "Revisa este PR" → loads code-reviewer skill |
| Reportes financieros | Plantillas reutilizables, formato consistente | Monthly sales reports, Q3 summaries |
| Brand guidelines | Aplicar automáticamente a documentos/presentaciones | Asegura colores, fonts, logo en cada output |
| Data cleaning pipelines | Scripts determinísticos, reproducibles | CSV → validated → report (mismo resultado siempre) |

**Industrias adoptando**:[^12][^11]

- **Legal Tech**: Revisión de contratos con políticas de empresa empaquetadas
- **FinTech**: Generación de reportes con formato regulatorio predefinido
- **E-commerce**: Automatización de descripciones de productos con brand voice


### Cuándo Usar Sub-Agentes

**Mejor para**: Investigación paralela, análisis complejos con estado isolado:


| Caso | Por Qué Sub-Agentes |
| :-- | :-- |
| Code review + refactoring paralelos | Dos agentes trabajando en paralelo sin contaminar contexto |
| Debugging + testing paralelos | El debugger descubre issues, validator verifica fixes simultáneamente |
| Análisis de múltiples fuentes | Investigador A busca en docs, Investigador B analiza código base |

### Cuándo Usar Prompts Tradicionales

**Mejor para**: Exploración, iteración rápida, tareas únicas:


| Caso | Por Qué |
| :-- | :-- |
| "Help me brainstorm this feature" | No es repetitivo, contexto mínimo |
| Prototipado de nuevo workflow | Todavía no sabe si es recurrente |

## Arquitectura Técnica: Code Execution Tool y Filesystem

Las Skills requieren **obligatoriamente** el Code Execution Tool beta (no es opcional). Aquí's por qué:[^3][^13]

### El Modelo de Ejecución de Skills

```
┌─────────────────────────────────────────┐
│         Claude Code Session              │
│  (terminal/IDE en tu máquina local)     │
└─────────────────────────────────────────┘
                    ↓
     ┌──────────────────────────┐
     │  .claude/skills/auth/    │
     │  ├── SKILL.md            │
     │  ├── scripts/            │
     │  │   └── create_jwt.py   │
     │  └── resources/          │
     │      └── security.md     │
     └──────────────────────────┘
                    ↓
     ┌──────────────────────────┐
     │  Code Execution Container │
     │  (VM sandbox)            │
     │  - Filesystem access     │
     │  - Bash commands         │
     │  - Python/Node execution │
     │  - NO network access     │
     │  - NO package installs   │
     └──────────────────────────┘
```

**Limitaciones clave del contenedor de ejecución**:[^3]

- ✅ Acceso filesystem para leer archivos de Skill
- ✅ Ejecución de bash para invocar scripts
- ✅ Pre-installed packages only (pandas, numpy, requests, etc.)
- ❌ NO network access (no pueden hacer API calls externas)
- ❌ NO runtime package installation
- ❌ NO persistent state entre sesiones


### Por Qué Code Execution Es Requerido

Los scripts ejecutables en Skills ofrecen **eficiencia de tokens y determinismo** imposible de lograr con generación:

```python
# En SKILL.md/scripts/validate_form.py
# Este script NUNCA entra al contexto (solo su output)
import pdfplumber
import json

def extract_form_fields(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Procesa PDF directamente
        fields = pdf.forms
    return json.dumps({"fields": fields})

# Claude ejecuta:
bash: python scripts/validate_form.py input.pdf
# → Recibe: {"fields": [...]}
# → Costo: 100 tokens (output) vs 5000+ (si Claude lo escribiera)
```

**Comparación de Costo**:[^5]

- Generar código para procesar PDF: ~5,000 tokens
- Ejecutar script preescrito + recibir output: ~100 tokens
- **Ahorro**: 50x más eficiente[^7]


## SKILL.md: Estructura y Mejores Prácticas

### Anatomía Completa de SKILL.md

```markdown
---
name: "contract-reviewer"
description: "Analyze contracts for risk using Acme Corp policies. Use when reviewing legal documents, NDAs, or vendor agreements."
version: "1.0.0"
dependencies: "python>=3.8"
---

# Contract Reviewer Skill

## Quick Start
For basic reviews, follow the 5-point checklist in resources/checklist.txt.

## How to Use
When reviewing a contract:
1. Identify document type (NDA, Service Agreement, License)
2. Check against our policies - see resources/policies.md
3. Flag high-risk clauses per resources/risk-framework.md
4. Generate report using templates/report-template.md

## Examples
Example analysis: See resources/example-redlines.md

[Continue with detailed instructions...]

## Advanced: Custom Risk Analysis
For non-standard clauses, refer to resources/advanced-patterns.md.
```


### Campos Requeridos vs Opcionales[^14][^10]

| Campo | Requerido | Máx. Caracteres | Notas |
| :-- | :-- | :-- | :-- |
| `name` | ✅ | 64 | Lowercase, hyphenated, no XML tags, no "anthropic" or "claude" |
| `description` | ✅ | 1024 | **Crítico**: Claude usa esto para routing. Incluir "Use when..." |
| `version` | ❌ | — | Recomienda semver (1.0.0) para tracking |
| `dependencies` | ❌ | — | Python packages pre-installed: pandas, requests, etc. |

### Mejores Prácticas de Descripción[^6][^7]

**❌ Malo**:

```yaml
description: "PDF processing"
```

**✅ Bueno**:

```yaml
description: "Extract text and structured data from PDF files, fill out PDF forms with provided values, and merge multiple PDFs. Use when the user needs to read, modify, or combine PDF documents."
```

La descripción es tu **hook de activación**. Claude usa semantic matching contra las palabras clave del usuario.

## API Skills: El Nuevo Endpoint `/v1/skills`

Las Skills también funcionan en la API Claude con versionamiento organizacional:

### Crear Skills Programáticamente

```bash
curl https://api.anthropic.com/v1/skills \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-beta: skills-2025-10-02" \
  -F "skill_folder=@my-skill.zip"
```


### Headers Requeridos para API[^15]

```
anthropic-beta: skills-2025-10-02      # Habilita funcionalidad de Skills
anthropic-beta: code-execution-2025-08-25  # Requiere Code Execution Tool
anthropic-beta: files-api-2025-04-14   # Para upload/download de archivos
```

**Scope de Compartición**:[^3]

- **Claude.ai**: Individual user (cada miembro debe uploadear por separado)
- **API/Claude Developer Platform**: Workspace-wide (todos los miembros acceden a Skills compartidas)
- **Claude Code**: Filesystem-based (`.claude/skills/` por proyecto, `~/.claude/skills/` global)


## Skills vs MCP: El Gran Debate de Octubre 2025

Anthropic posicionó Skills como **potencialmente mayor que MCP**, lo cual generó discusión en la comunidad:[^2]


| Aspecto | Skills | MCP |
| :-- | :-- | :-- |
| **Propósito** | Expertise y procedimientos reutilizables | Conexión a herramientas y datos externos |
| **Token Cost** | 30-50 tokens (metadata) hasta estar activa | Requiere descripción en system prompt ~500+ |
| **Composabilidad** | Skills pueden stacking automáticamente | MCPs son puntos de conexión discretos |
| **Network Access** | ❌ NO (sandbox) | ✅ SÍ (conexión a APIs externas) |
| **Determinism** | ✅ Scripts ejecutables para ops confiables | Parcial (depende del servidor MCP) |
| **Setup** | Carpeta ZIP, upload local | Servidor MCP standalone |
| **Governance** | Versionado, auditado, organizacional | Menos central |

**Cuándo Usar Cada Uno**:[^16][^17]

- **Skills + MCP juntos**: Una Skill puede invocar MCP para herramientas específicas
- **Skills alone**: Workflows internos, templates, brand guidelines, data processing
- **MCP alone**: Integración con Salesforce, Slack, Linear (sistemas externos)

Simon Willison (fundador de Datasette) argumentó que **Skills resuelven el problema de contexto mejor que MCP** porque:

1. No requieren servidor externo
2. Token efficiency es 10x mejor (30 vs 500+ tokens iniciales)
3. Composición automática sin orquestación manual[^2]

## Community \& Adoption: Primeras Dos Semanas (Oct 16-27)

### Skills Populares Emergentes

**Reddit/GitHub muestran estos patrones**:[^18][^19][^20]

1. **AI Project Architect Skill** (287 upvotes)
    - Genera arquitecturas event-driven de 43 tareas
    - Identifica riesgos, backtesting
    - Crea WebSocket handlers automáticamente
2. **Report Generation Skill**
    - Parsea Git logs, commits, stats
    - Genera Markdown o Word docs
    - Incluye links a PRs automáticamente
3. **Financial Dashboard Skill**
    - Template con Excel formulas pre-set
    - Validación de datos
    - Charts automáticos
4. **Full-Stack Starter Skills Pack**
    - Auth setup (JWT, OTP, rate limiting, CSRF)
    - Multi-tenant (orgs, memberships, invitations)
    - Dashboard shell (sidebar resizable, responsive)

### Adoption Stats (Octubre 2025)

- **awesome-claude-skills**: 1,300+ stars en 2 semanas
- **claude-code-plugins-plus**: 227 Skills production-ready
- **Marketplace oficial**: Anthropic Skills + comunidad Skills comenzando


### Challenges Tempranos Reportados

1. **Overloading SKILL.md**: Algunos desarrolladores metieron 20K tokens en un único archivo (debería ser < 5K, rest en resources/)[^6]
2. **Falta de composición**: Esperar que Skills se invoquen mutuamente (requiere explicit delegation aún)
3. **Network restrictions**: Querer hacer API calls (Skills no tienen acceso a red)[^3]

## Configuración en Claude Code: Paso a Paso

### Instalación de Skills Prebuilt

```bash
claude
/plugins
# Selecciona "Anthropic Agent Skills"
# Elige "document-skills" o "example-skills"
# Click "Install Now"
```


### Crear Tu Primer Skill

```bash
cd mi-proyecto
mkdir -p .claude/skills/mi-skill
cat > .claude/skills/mi-skill/SKILL.md << 'EOF'
---
name: "code-formatter"
description: "Format code files to company standards with prettier config. Use when formatting JavaScript, TypeScript, or React code."
---

# Code Formatter Skill

## Instructions
1. Apply prettier config from resources/prettier.config.js
2. Format all .js, .ts, .tsx files
3. Verify no syntax errors post-formatting

## When to Use
User asks: "format this code", "fix indentation", "apply prettier"
EOF

# Crear resources
mkdir -p .claude/skills/mi-skill/resources
cp ~/prettier.config.js .claude/skills/mi-skill/resources/

# Usar en Claude Code
claude
# Automáticamente detecta y carga la Skill
```


### Reload Cuando Cambies una Skill

```bash
/reload-skills
# O reinicia la sesión de Claude Code
```


## Limitaciones Conocidas y Roadmap 2025-2026

### Limitaciones Actuales

1. **Sin Recursión**: Las Skills no pueden invocar otras Skills (por diseño, para evitar infinite loops)[^3]
2. **Sin Network**: Code execution container NO tiene internet (solo file system local)[^3]
3. **Sin Package Install Runtime**: No puedes `pip install` nuevos paquetes durante ejecución[^3]
4. **No Cross-Surface Sync**: Skills en Claude.ai no se sincronizan automáticamente a API o Claude Code[^3]
5. **Single VM per Session**: No hay persistencia de estado entre sesiones

### Roadmap Esperado (Q4 2025 - Q1 2026)

- Marketplace oficial con discovery mejorado
- Skill composition frameworks para orquestación automática
- Skills autogeneradas (Claude genera Skills de sus propios patrones)
- Integración profunda con sistema de memoria (context stored outside window)
- Auditing y compliance tools para enterprise


## El Futuro: Visión de Anthropic

Anthropic ve Skills como el puente entre **prompts estáticos** y **agentes fully agentic**:[^5]

> "En el futuro, esperamos que los agentes creen, editen y evalúen Skills por sí mismos, codificando sus propios patrones de comportamiento en capacidades reutilizables."

Esto sugiere que en 2026 podrías:

1. Decir "optimiza tu workflow" a Claude
2. Claude automáticamente crea una Skill capturando tu proceso
3. Esa Skill se aplica a todas las tareas futuras similares

## Conclusión: Skills vs Tasks/Sub-Agentes

**Las Skills y Sub-Agentes No Son Competidoras—Son Complementarias**:

- **Sub-Agentes (Tasks)**: Para **paralelismo y aislamiento**. Cuándo: investigación compleja, debugging + testing paralelos, análisis multifuente
- **Skills**: Para **automatización y especialización**. Cuándo: workflows repetitivos (3+ veces/semana), plantillas, consistency organizacional

**Stack Recomendado en Claude Code**:[^21]

1. **Prompts Tradicionales**: Exploración inicial, brainstorming
2. **Skills**: Workflows descubiertos como recurrentes
3. **Sub-Agentes**: Cuando necesitas paralelismo o contexto completamente isolado
4. **MCP**: Integraciones externas (Salesforce, APIs)
5. **Plugins**: Empaquetamiento completo de comandos + sub-agents + MCP

Las Skills son el componente que **cierra la brecha entre prompt engineering estáticos y agentes autónomos verdaderamente especializados**. Su belleza radica en la simplicidad: solo carpetas con Markdown e instrucciones, pero con el diseño de progressive disclosure que las hace escalables a decenas de skills sin penalidad de contexto.[^2][^7][^5]
<span style="display:none">[^22][^23][^24][^25][^26][^27][^28][^29][^30][^31][^32][^33][^34][^35][^36][^37][^38][^39][^40][^41][^42][^43]</span>

<div align="center">⁂</div>

[^1]: https://www.anthropic.com/news/skills

[^2]: https://simonwillison.net/2025/Oct/16/claude-skills/

[^3]: https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview

[^4]: https://www.reddit.com/r/ClaudeAI/comments/1obq6wq/understanding_claude_skills_vs_subagents_its_not/

[^5]: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills

[^6]: https://skywork.ai/blog/ai-agent/claude-skills-skill-md-resources-runtime-loading/

[^7]: https://tylerfolkman.substack.com/p/the-complete-guide-to-claude-skills

[^8]: https://skywork.ai/blog/llm/claude-skills-the-beginning-of-a-smarter/

[^9]: https://apidog.com/blog/claude-skills/

[^10]: https://www.cometapi.com/how-to-create-and-use-claudes-skills/

[^11]: https://www.cursor-ide.com/blog/claude-code-skills

[^12]: https://www.datastudios.org/post/claude-in-the-enterprise-case-studies-of-ai-deployments-and-real-world-results-1

[^13]: https://devops.com/claude-introduces-agent-skills-for-custom-ai-workflows/

[^14]: https://support.claude.com/en/articles/12512198-how-to-create-custom-skills

[^15]: https://docs.claude.com/en/release-notes/api

[^16]: https://departmentofproduct.substack.com/p/what-are-claude-skills-and-how-can

[^17]: https://www.eesel.ai/blog/claude-skills

[^18]: https://www.reddit.com/r/ClaudeAI/comments/1ofltdr/i_spent_way_too_long_cataloguing_claude_code/

[^19]: https://www.reddit.com/r/ClaudeAI/comments/1og6r3v/two_realworld_examples_of_claude_skills/

[^20]: https://www.reddit.com/r/ClaudeAI/comments/1og1gdx/now_that_were_one_week_into_the_claude_skills/

[^21]: https://www.linkedin.com/posts/unwind-ai_claude-projects-vs-subagents-vs-skills-activity-7385498679157346305-4Xgs

[^22]: https://www.cometapi.com/claude-skills-what-it-is-and-how-to-use/

[^23]: https://skywork.ai/blog/ai-agent/claude-skills-vs-system-prompts-2025-comparison/

[^24]: https://support.claude.com/en/articles/12512176-what-are-skills

[^25]: https://www.infoq.com/news/2025/10/anthropic-claude-skills/

[^26]: https://www.reddit.com/r/ClaudeAI/comments/1oalv0o/what_are_claude_skills_really/

[^27]: https://github.com/alirezarezvani/claude-skills

[^28]: https://www.eesel.ai/blog/skills-vs-subagent

[^29]: https://www.nathanonn.com/claude-skills-your-i-know-kung-fu-moment-has-arrived-part-1-of-3/

[^30]: https://www.reddit.com/r/ClaudeAI/comments/1o9ph4u/ive_been_tracking_what_people_are_building_with/

[^31]: https://www.lennysnewsletter.com/p/claude-skills-explained

[^32]: https://www.reddit.com/r/ClaudeAI/comments/1oaseqh/i_built_a_claude_code_skill_that_turns_claude/

[^33]: https://www.reddit.com/r/ClaudeAI/comments/1o8af9q/claude_can_now_use_skills/

[^34]: https://www.youngleaders.tech/p/claude-skills-commands-subagents-plugins

[^35]: https://www.youtube.com/watch?v=7_SL0FaY8MM

[^36]: https://www.youtube.com/watch?v=421T2iWTQio

[^37]: https://github.com/travisvn/awesome-claude-skills

[^38]: https://shipyard.build/blog/claude-code-skills/

[^39]: https://www.youtube.com/watch?v=v1y5EUSQ8WA

[^40]: https://www.youtube.com/watch?v=FOqbS_llAms

[^41]: https://skywork.ai/blog/ai-agent/claude-skills-plan-comparison-2025/

[^42]: https://www.ai-supremacy.com/p/claude-code-skills-just-changed-everything-agents-anthropic

[^43]: https://support.claude.com/en/articles/12512180-using-skills-in-claude

