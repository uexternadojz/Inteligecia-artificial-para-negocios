# ✅ Checklist de Deployment a GitHub Pages

## 📦 Archivos Configurados

### ✅ Configuración de Astro
- **Archivo:** `materias/inteligencia-artificial-para-negocios/site/astro.config.mjs`
- **Configuración:** GitHub Pages con base path `/ia-negocios`
- **Output:** Static Site Generation (SSG)

### ✅ GitHub Actions Workflow
- **Archivo:** `.github/workflows/deploy-ia-negocios.yml`
- **Trigger:** Push a `main` con cambios en el sitio
- **Build:** Automático en cada push
- **Deploy:** Directo a GitHub Pages

### ✅ Archivos Adicionales
- **`.gitignore`:** Actualizado para permitir `package-lock.json`
- **`public/.nojekyll`:** Creado para evitar procesamiento Jekyll
- **`DEPLOY.md`:** Guía completa de deployment

---

## 🚀 Pasos para el Primer Deploy

### 1. Configurar Repositorio GitHub (Una sola vez)

```bash
# Si no tienes remote configurado
cd /home/jzuluaga/code/education-research/externado/docencia
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git

# Verificar
git remote -v
```

**⚠️ IMPORTANTE:** Reemplaza `TU_USUARIO` y `TU_REPO` con tus valores reales.

### 2. Verificar Configuración

```bash
# Revisar qué archivos se van a commitear
git status

# Revisar archivos nuevos creados
git status --untracked-files
```

### 3. Activar GitHub Pages en tu Repositorio

1. Ve a tu repositorio en GitHub
2. **Settings** → **Pages**
3. En **Source**, selecciona **GitHub Actions**

### 4. Hacer el Push

```bash
# Agregar archivos nuevos
git add .

# Commit con mensaje descriptivo
git commit -m "feat: Setup GitHub Pages deployment for IA Negocios site

- Configure Astro for GitHub Pages
- Add GitHub Actions workflow
- Create deployment documentation
- Update .gitignore for production builds"

# Push a main
git push origin main
```

### 5. Monitorear el Deployment

1. Ve a **Actions** en tu repositorio GitHub
2. Verás el workflow "Deploy IA Negocios Site to GitHub Pages" ejecutándose
3. Espera a que termine (toma 2-3 minutos)
4. Tu sitio estará en: `https://TU_USUARIO.github.io/TU_REPO/ia-negocios`

---

## 🔍 Verificación Post-Deployment

Una vez deployado, verifica:

- [ ] Homepage carga correctamente
- [ ] Navegación funciona (Clase 02, Clase 03)
- [ ] Imágenes se muestran correctamente
- [ ] Videos embebidos funcionan
- [ ] Links externos funcionan
- [ ] Responsive design funciona en mobile

---

## 📊 Archivos Nuevos Creados

```
docencia/
├── .github/
│   └── workflows/
│       └── deploy-ia-negocios.yml      ✅ NUEVO - Workflow de CI/CD
│
├── materias/inteligencia-artificial-para-negocios/site/
│   ├── astro.config.mjs                ✅ MODIFICADO - GitHub Pages config
│   ├── public/
│   │   └── .nojekyll                   ✅ NUEVO - Evitar Jekyll
│   ├── DEPLOY.md                       ✅ NUEVO - Guía completa
│   └── dist/                           ✅ GENERADO - Build de producción
│
├── .gitignore                           ✅ MODIFICADO - Permitir package-lock.json
└── DEPLOY_CHECKLIST.md                 ✅ NUEVO - Este archivo
```

---

## 🧪 Comandos Útiles

### Build y Preview Local

```bash
cd materias/inteligencia-artificial-para-negocios/site

# Build de producción
npm run build

# Preview del build (simula GitHub Pages)
npm run preview
# Visita: http://localhost:4321/ia-negocios/
```

### Verificar Estado de Git

```bash
# Ver archivos modificados
git status

# Ver diferencias
git diff

# Ver log de commits
git log --oneline -5
```

### Troubleshooting Build

```bash
# Limpiar cache y rebuild
rm -rf dist .astro
npm run build
```

---

## 🔄 Workflow de Desarrollo

Para futuras actualizaciones:

1. **Desarrolla localmente** con `npm run dev`
2. **Verifica el build** con `npm run build && npm run preview`
3. **Commit y push** a `main`
4. **GitHub Actions** se encarga del deploy automáticamente
5. **Verifica el sitio** en GitHub Pages

---

## ⚠️ Notas Importantes

### Base Path
La configuración actual usa `/ia-negocios` como base path. Si tu repo tiene otro nombre o estructura:

```javascript
// En astro.config.mjs
const base = process.env.BASE_PATH || "/TU_PATH_AQUI";
```

### Logos Faltantes
Hay algunos logos que generan 404 (no bloquean el sitio):
- perplexity.png
- gamma.png
- canva.png
- nano-banana.png
- gemini.png
- cursor.png
- copilot.png

**Solución:** Agregar estos logos a `public/assets/logos/` o usar placeholders.

### Package Lock
El `package-lock.json` DEBE estar versionado para builds reproducibles. Ya está configurado en `.gitignore`.

---

## 📞 Soporte

Si encuentras problemas:

1. Revisa la pestaña **Actions** en GitHub para ver logs de error
2. Consulta `DEPLOY.md` para troubleshooting detallado
3. Verifica que el base path en `astro.config.mjs` sea correcto

---

**Fecha de configuración:** 30 Octubre 2025
**Configurado por:** Claude Code
**Estado:** ✅ Listo para deploy
