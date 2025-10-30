# 🚀 Guía de Deployment a GitHub Pages

Este documento describe cómo deployar el sitio de **IA para Negocios** a GitHub Pages.

---

## 📋 Pre-requisitos

- Repositorio git inicializado
- Cuenta de GitHub
- Node.js 20+ instalado localmente

---

## 🔧 Configuración del Repositorio

### 1. Crear/Verificar Repositorio en GitHub

Si aún no tienes el repositorio en GitHub:

```bash
# Desde la raíz del proyecto docencia
cd /home/jzuluaga/code/education-research/externado/docencia

# Inicializar git (si no está inicializado)
git init

# Agregar remote (reemplaza con tu URL real)
git remote add origin https://github.com/jzuluaga/externado-docencia.git

# O si prefieres SSH
git remote add origin git@github.com:jzuluaga/externado-docencia.git
```

**⚠️ IMPORTANTE:** Reemplaza `jzuluaga` con tu usuario real de GitHub.

### 2. Verificar Configuración de Astro

El archivo `astro.config.mjs` está configurado para GitHub Pages con:

```javascript
const site = process.env.SITE_URL || "https://jzuluaga.github.io";
const base = process.env.BASE_PATH || "/ia-negocios";
```

**Si tu repo tiene otro nombre**, actualiza el `base`:

```javascript
// Ejemplo si tu repo se llama "docencia-externado"
const base = process.env.BASE_PATH || "/docencia-externado/ia-negocios";
```

---

## 🚀 Deployment Automático (Recomendado)

### 1. Activar GitHub Pages en tu Repositorio

1. Ve a tu repositorio en GitHub
2. Navega a **Settings** → **Pages**
3. En **Source**, selecciona **GitHub Actions**

### 2. Push del Código

```bash
# Asegúrate de estar en la rama main
git checkout main

# Agrega todos los cambios
git add .

# Commit
git commit -m "feat: Setup GitHub Pages deployment for IA Negocios site"

# Push
git push origin main
```

### 3. Monitorear el Deployment

1. Ve a la pestaña **Actions** en tu repositorio
2. Verás el workflow "Deploy IA Negocios Site to GitHub Pages" ejecutándose
3. Una vez completado (✅), tu sitio estará disponible en:

```
https://[tu-usuario].github.io/[nombre-repo]/ia-negocios
```

**Ejemplo:** `https://jzuluaga.github.io/externado-docencia/ia-negocios`

---

## 🧪 Testing Local del Build de Producción

Antes de deployar, puedes probar el build localmente:

```bash
# Desde el directorio del sitio
cd materias/inteligencia-artificial-para-negocios/site

# Build de producción
npm run build

# Preview del build
npm run preview
```

El preview estará disponible en `http://localhost:4321/ia-negocios/`

---

## 🔄 Re-deployment

Cada vez que hagas push a `main` con cambios en el directorio del sitio, el workflow se ejecutará automáticamente:

```bash
# Haz tus cambios...

git add .
git commit -m "feat: Add new content to Clase 4"
git push origin main

# GitHub Actions se encarga del resto
```

---

## 🛠️ Deployment Manual (Alternativa)

Si prefieres no usar GitHub Actions:

### 1. Build Local

```bash
cd materias/inteligencia-artificial-para-negocios/site
npm run build
```

### 2. Deploy con GitHub Pages CLI

```bash
# Instalar gh-pages
npm install -D gh-pages

# Deploy
npx gh-pages -d dist -b gh-pages
```

### 3. Configurar GitHub Pages

En **Settings** → **Pages**, selecciona:
- **Source:** Deploy from a branch
- **Branch:** `gh-pages` / `root`

---

## 🐛 Troubleshooting

### Error: 404 en assets

**Problema:** Los assets (imágenes, CSS, JS) no cargan.

**Solución:** Verifica que el `base` en `astro.config.mjs` coincida con tu URL de GitHub Pages.

```javascript
// Debe ser exactamente el path después de tu dominio
const base = "/ia-negocios"; // ✅ Correcto
const base = "/"; // ❌ Solo si tu repo se llama username.github.io
```

### Error: Workflow no se ejecuta

**Problema:** El workflow de GitHub Actions no se dispara.

**Soluciones:**
1. Verifica que el archivo esté en `.github/workflows/`
2. Confirma que GitHub Actions esté habilitado en tu repo (Settings → Actions)
3. Verifica que hiciste push a la rama `main`

### Error: 403 en deployment

**Problema:** Permisos insuficientes para GitHub Pages.

**Solución:**
1. Ve a **Settings** → **Actions** → **General**
2. En **Workflow permissions**, selecciona **Read and write permissions**
3. Marca **Allow GitHub Actions to create and approve pull requests**

---

## 📁 Estructura de Archivos Importantes

```
docencia/
├── .github/
│   └── workflows/
│       └── deploy-ia-negocios.yml    # Workflow de deployment
├── materias/
│   └── inteligencia-artificial-para-negocios/
│       └── site/
│           ├── astro.config.mjs      # Configuración de Astro
│           ├── package.json          # Scripts de build
│           ├── dist/                 # Output del build (gitignored)
│           └── DEPLOY.md            # Esta guía
```

---

## ✅ Checklist de Deployment

Antes de hacer tu primer deployment:

- [ ] Repositorio creado en GitHub
- [ ] Remote configurado (`git remote -v`)
- [ ] `astro.config.mjs` con la URL correcta
- [ ] GitHub Pages activado en Settings
- [ ] Workflow en `.github/workflows/`
- [ ] Build local exitoso (`npm run build`)
- [ ] Commit y push a `main`
- [ ] Workflow ejecutado exitosamente en Actions
- [ ] Sitio accesible en la URL de GitHub Pages

---

## 🔗 URLs de Referencia

- **GitHub Pages Docs:** https://docs.github.com/en/pages
- **Astro Deployment:** https://docs.astro.build/en/guides/deploy/github/
- **GitHub Actions:** https://docs.github.com/en/actions

---

**Última actualización:** 30 Octubre 2025
**Sitio:** Inteligencia Artificial para Negocios - Universidad Externado
