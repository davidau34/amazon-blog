#!/bin/bash

# Script de instalación automática del blog de afiliados Amazon
# Autor: TechDeals Team
# Fecha: Febrero 2026

set -e  # Salir si hay algún error

echo "🚀 INSTALADOR AUTOMÁTICO - Blog de Afiliados Amazon"
echo "=================================================="
echo ""

# Colores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Función para imprimir con color
print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

# Verificar requisitos del sistema
echo "📋 Verificando requisitos del sistema..."
echo ""

# Verificar Git
if ! command -v git &> /dev/null; then
    print_error "Git no está instalado"
    echo "Instala Git desde: https://git-scm.com/downloads"
    exit 1
fi
print_success "Git instalado"

# Verificar Python
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 no está instalado"
    echo "Instala Python desde: https://www.python.org/downloads/"
    exit 1
fi
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
print_success "Python $PYTHON_VERSION instalado"

# Verificar Ruby (para Jekyll)
if ! command -v ruby &> /dev/null; then
    print_warning "Ruby no está instalado (necesario para Jekyll)"
    print_info "Instala Ruby desde: https://www.ruby-lang.org/en/downloads/"
    print_info "O continúa sin Jekyll (solo necesario para pruebas locales)"
else
    RUBY_VERSION=$(ruby --version | cut -d' ' -f2)
    print_success "Ruby $RUBY_VERSION instalado"
fi

echo ""
echo "=================================================="
echo "📝 CONFIGURACIÓN INICIAL"
echo "=================================================="
echo ""

# Solicitar información al usuario
print_info "Necesito algunos datos para configurar tu blog:"
echo ""

read -p "Tu nombre de usuario de GitHub: " GITHUB_USERNAME
read -p "Nombre del repositorio (ej: amazon-blog): " REPO_NAME
read -p "Título del blog: " BLOG_TITLE
read -p "Tu email: " USER_EMAIL

echo ""
print_info "Amazon Associates ID (lo puedes cambiar después en _config.yml)"
read -p "Amazon Associate ID: " AMAZON_ID

echo ""
print_warning "API Keys (puedes dejarlas vacías y configurarlas después en GitHub Secrets)"
read -p "OpenAI API Key (opcional ahora): " OPENAI_KEY

echo ""
echo "=================================================="
echo "🔨 CREANDO PROYECTO"
echo "=================================================="
echo ""

# Crear directorio del proyecto
PROJECT_DIR="$HOME/$REPO_NAME"

if [ -d "$PROJECT_DIR" ]; then
    print_warning "El directorio $PROJECT_DIR ya existe"
    read -p "¿Quieres sobrescribirlo? (y/n): " OVERWRITE
    if [ "$OVERWRITE" != "y" ]; then
        print_error "Instalación cancelada"
        exit 1
    fi
    rm -rf "$PROJECT_DIR"
fi

mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

print_success "Directorio creado: $PROJECT_DIR"

# Copiar archivos del proyecto (asume que estás en el directorio del template)
TEMPLATE_DIR="/tmp/amazon-affiliate-blog"

if [ -d "$TEMPLATE_DIR" ]; then
    print_info "Copiando archivos del template..."
    cp -r "$TEMPLATE_DIR/"* "$PROJECT_DIR/"
    print_success "Archivos copiados"
else
    print_error "Template no encontrado. Asegúrate de tener los archivos base."
    exit 1
fi

# Actualizar _config.yml con la información del usuario
print_info "Configurando _config.yml..."
sed -i.bak "s|title: \".*\"|title: \"$BLOG_TITLE\"|" _config.yml
sed -i.bak "s|url: \".*\"|url: \"https://$GITHUB_USERNAME.github.io/$REPO_NAME\"|" _config.yml
sed -i.bak "s|email: .*|email: $USER_EMAIL|" _config.yml
sed -i.bak "s|amazon_associate_id: \".*\"|amazon_associate_id: \"$AMAZON_ID\"|" _config.yml
rm _config.yml.bak
print_success "_config.yml configurado"

# Crear archivo .env
print_info "Creando archivo .env..."
cat > .env << EOF
# APIs
OPENAI_API_KEY=$OPENAI_KEY
AMAZON_ASSOCIATE_ID=$AMAZON_ID
AMAZON_REGION=es

# Blog
BLOG_URL=https://$GITHUB_USERNAME.github.io/$REPO_NAME

# Twitter (configurar después)
TWITTER_API_KEY=
TWITTER_API_SECRET=
TWITTER_ACCESS_TOKEN=
TWITTER_ACCESS_SECRET=
TWITTER_BEARER_TOKEN=
EOF
print_success "Archivo .env creado"

# Instalar dependencias Python
print_info "Instalando dependencias Python..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt > /dev/null 2>&1
    print_success "Dependencias Python instaladas"
else
    print_warning "pip3 no encontrado. Instala las dependencias manualmente con: pip3 install -r requirements.txt"
fi

# Instalar dependencias Ruby (Jekyll)
if command -v bundle &> /dev/null; then
    print_info "Instalando dependencias Ruby (Jekyll)..."
    bundle install > /dev/null 2>&1
    print_success "Jekyll instalado"
else
    print_warning "Bundler no encontrado. Para instalar Jekyll, ejecuta: gem install bundler && bundle install"
fi

# Inicializar repositorio Git
print_info "Inicializando repositorio Git..."
git init > /dev/null 2>&1
git add .
git commit -m "🎉 Initial commit: Automated Amazon Affiliate Blog" > /dev/null 2>&1
print_success "Repositorio Git inicializado"

echo ""
echo "=================================================="
echo "✅ ¡INSTALACIÓN COMPLETADA!"
echo "=================================================="
echo ""

print_success "Tu blog está listo en: $PROJECT_DIR"
echo ""
print_info "PRÓXIMOS PASOS:"
echo ""
echo "1️⃣  Crear repositorio en GitHub:"
echo "    https://github.com/new"
echo "    Nombre: $REPO_NAME"
echo ""
echo "2️⃣  Conectar y subir código:"
echo "    cd $PROJECT_DIR"
echo "    git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
echo "    git branch -M main"
echo "    git push -u origin main"
echo ""
echo "3️⃣  Habilitar GitHub Pages:"
echo "    Settings → Pages → Source: GitHub Actions"
echo ""
echo "4️⃣  Configurar Secrets en GitHub:"
echo "    Settings → Secrets and variables → Actions → New secret"
echo "    Añadir: OPENAI_API_KEY, AMAZON_ASSOCIATE_ID, etc."
echo ""
echo "5️⃣  Ejecutar primer artículo:"
echo "    Actions → Auto-Generar y Publicar Artículos → Run workflow"
echo ""
echo "📚 Lee el README.md completo para más detalles"
echo ""
print_success "Tu sitio estará en: https://$GITHUB_USERNAME.github.io/$REPO_NAME"
echo ""
print_warning "Recuerda configurar las API keys en GitHub Secrets para automatización completa"
echo ""
echo "🎉 ¡Buena suerte con tu blog de afiliados!"
