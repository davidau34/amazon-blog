#!/bin/bash

# 🚀 Script de Configuración Automática para davidau34
# Este script contiene TODOS los comandos que necesitas ejecutar

echo "======================================================================"
echo "🚀 CONFIGURACIÓN AUTOMÁTICA - Blog de Afiliados Amazon"
echo "======================================================================"
echo ""
echo "Usuario: davidau34"
echo "Email: dcoletb@hotmail.com"
echo "Amazon ID: davidau342123-21"
echo ""

# ============================================================================
# PARTE 1: LO QUE YA ESTÁ HECHO ✅
# ============================================================================
echo "✅ Archivos configurados con tu información"
echo "✅ Git inicializado y commit creado"
echo "✅ Archivo .env creado"
echo ""

# ============================================================================
# PARTE 2: LO QUE NECESITAS HACER TÚ
# ============================================================================
echo "======================================================================"
echo "📝 PASOS QUE DEBES SEGUIR (copiar y pegar comandos)"
echo "======================================================================"
echo ""

# ----------------------------------------------------------------------------
# PASO 1: OpenAI API Key
# ----------------------------------------------------------------------------
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 PASO 1: Obtener OpenAI API Key"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Abre en tu navegador:"
echo "   👉 https://platform.openai.com/api-keys"
echo ""
echo "2. Crea cuenta o inicia sesión"
echo ""
echo "3. Click en 'Create new secret key'"
echo ""
echo "4. Copia la key (empieza con sk-proj-...)"
echo ""
echo "5. Ejecuta este comando (reemplaza TU-KEY-AQUI con tu key real):"
echo ""
echo "   cd /tmp/amazon-affiliate-blog"
echo "   echo 'OPENAI_API_KEY=sk-proj-TU-KEY-AQUI' >> .env"
echo ""
read -p "Presiona ENTER cuando hayas añadido tu OpenAI API key..."
echo ""

# ----------------------------------------------------------------------------
# PASO 2: Crear repositorio en GitHub
# ----------------------------------------------------------------------------
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 PASO 2: Crear repositorio en GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Abre en tu navegador:"
echo "   👉 https://github.com/new"
echo ""
echo "2. Configuración del repositorio:"
echo "   - Repository name: amazon-blog"
echo "   - Description: Blog automatizado de afiliados Amazon"
echo "   - Public (recomendado para GitHub Pages gratis)"
echo "   - ❌ NO marques 'Add a README file'"
echo "   - ❌ NO añadas .gitignore"
echo "   - ❌ NO añadas license"
echo ""
echo "3. Click 'Create repository'"
echo ""
read -p "Presiona ENTER cuando hayas creado el repositorio..."
echo ""

# ----------------------------------------------------------------------------
# PASO 3: Push a GitHub
# ----------------------------------------------------------------------------
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 PASO 3: Subir código a GitHub"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "Copia y pega estos comandos UNO POR UNO:"
echo ""
echo "cd /tmp/amazon-affiliate-blog"
echo ""
echo "git remote add origin https://github.com/davidau34/amazon-blog.git"
echo ""
echo "git branch -M main"
echo ""
echo "git push -u origin main"
echo ""
echo "NOTA: Si pide usuario/contraseña:"
echo "  - Username: davidau34"
echo "  - Password: Necesitas un Personal Access Token (NO tu contraseña normal)"
echo "    👉 Generarlo en: https://github.com/settings/tokens"
echo "    👉 New token (classic) → Marcar 'repo' → Generate"
echo ""
read -p "Presiona ENTER cuando hayas hecho el push..."
echo ""

# ----------------------------------------------------------------------------
# PASO 4: Habilitar GitHub Pages
# ----------------------------------------------------------------------------
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 PASO 4: Habilitar GitHub Pages"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Ve a tu repositorio:"
echo "   👉 https://github.com/davidau34/amazon-blog"
echo ""
echo "2. Click en 'Settings' (arriba derecha)"
echo ""
echo "3. En el menú izquierdo → 'Pages'"
echo ""
echo "4. En 'Source': Selecciona 'GitHub Actions'"
echo ""
echo "5. Save"
echo ""
echo "Tu blog estará en: https://davidau34.github.io/amazon-blog/"
echo ""
read -p "Presiona ENTER cuando hayas habilitado GitHub Pages..."
echo ""

# ----------------------------------------------------------------------------
# PASO 5: Configurar Secrets
# ----------------------------------------------------------------------------
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 PASO 5: Configurar Secrets en GitHub (IMPORTANTE)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Ve a tu repositorio → Settings"
echo ""
echo "2. Menú izquierdo → 'Secrets and variables' → 'Actions'"
echo ""
echo "3. Click 'New repository secret' y añade estos 3 secrets:"
echo ""
echo "   SECRET 1:"
echo "   Name:  OPENAI_API_KEY"
echo "   Value: sk-proj-tu-key-de-openai"
echo ""
echo "   SECRET 2:"
echo "   Name:  AMAZON_ASSOCIATE_ID"
echo "   Value: davidau342123-21"
echo ""
echo "   SECRET 3:"
echo "   Name:  BLOG_URL"
echo "   Value: https://davidau34.github.io/amazon-blog"
echo ""
read -p "Presiona ENTER cuando hayas añadido los 3 secrets..."
echo ""

# ----------------------------------------------------------------------------
# PASO 6: Generar primer artículo
# ----------------------------------------------------------------------------
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "📌 PASO 6: Generar primer artículo"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "1. Ve a tu repositorio → 'Actions' (menú superior)"
echo ""
echo "2. Verás 'Auto-Generar y Publicar Artículos'"
echo ""
echo "3. Click en el workflow"
echo ""
echo "4. Click 'Run workflow' → 'Run workflow'"
echo ""
echo "5. Espera 2-3 minutos"
echo ""
echo "¡Se generará tu primer artículo automáticamente! 🎉"
echo ""
read -p "Presiona ENTER cuando hayas ejecutado el workflow..."
echo ""

# ----------------------------------------------------------------------------
# COMPLETADO
# ----------------------------------------------------------------------------
echo "======================================================================"
echo "✅ ¡CONFIGURACIÓN COMPLETADA!"
echo "======================================================================"
echo ""
echo "Tu blog está en: https://davidau34.github.io/amazon-blog/"
echo ""
echo "El sistema ahora trabajará automáticamente:"
echo "  ✅ Genera artículo cada 2 días"
echo "  ✅ Publica en el sitio"
echo "  ✅ Todo sin tu intervención"
echo ""
echo "📊 Monitorea tus ventas en: https://afiliados.amazon.es"
echo ""
echo "💰 Objetivo: 3 ventas en 180 días"
echo ""
echo "======================================================================"
echo "🎉 ¡FELICIDADES! Tu sistema de ingresos pasivos está activo"
echo "======================================================================"
