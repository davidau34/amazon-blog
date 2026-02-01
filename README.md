# 🤖 Sistema Automatizado de Blog de Afiliados Amazon

![Status](https://img.shields.io/badge/status-ready-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![Jekyll](https://img.shields.io/badge/jekyll-4.3+-red)

Sistema 100% automatizado para generar y publicar contenido de afiliados de Amazon con:
- ✨ Generación automática de artículos con IA (ChatGPT)
- 📦 Búsqueda de productos trending en Amazon
- 🚀 Publicación automática cada 2 días
- 🐦 Compartir en Twitter/X automáticamente
- 💰 Enlaces de afiliado optimizados
- 📊 SEO optimizado para máxima visibilidad

## 🎯 Características

- **100% Gratis**: Usa GitHub Pages (hosting gratis) + APIs con tier gratuito
- **Totalmente Automatizado**: GitHub Actions ejecuta todo automáticamente
- **SEO Optimizado**: Artículos optimizados para búsquedas de Google
- **Responsive**: Funciona perfecto en móvil y desktop
- **Múltiples Nichos**: Gadgets Tech, Fitness, Cocina, Mascotas
- **Sin Mantenimiento**: Configura una vez y olvídate

## 📋 Requisitos Previos

1. **Cuenta GitHub** (gratis)
2. **API Key de OpenAI** ($5 gratis inicial) - [Obtener aquí](https://platform.openai.com/api-keys)
3. **Cuenta Amazon Associates** (gratis) - [Registrarse aquí](https://affiliate-program.amazon.com)
4. **Cuenta Twitter Developer** (gratis, opcional) - [Registrarse aquí](https://developer.twitter.com)

## 🚀 Instalación y Configuración

### Paso 1: Fork o Clone este repositorio

```bash
# Opción 1: Fork desde GitHub (recomendado)
# Click en "Fork" arriba a la derecha

# Opción 2: Clonar directamente
git clone https://github.com/tu-usuario/amazon-affiliate-blog.git
cd amazon-affiliate-blog
```

### Paso 2: Configurar GitHub Pages

1. Ve a **Settings** → **Pages** en tu repositorio
2. En **Source**, selecciona **GitHub Actions**
3. Tu sitio estará en: `https://tu-usuario.github.io/amazon-affiliate-blog/`

### Paso 3: Configurar Secrets en GitHub

Ve a **Settings** → **Secrets and variables** → **Actions** → **New repository secret**

Añade estos secrets (¡IMPORTANTE!):

```
OPENAI_API_KEY=tu-api-key-de-openai
AMAZON_ASSOCIATE_ID=tu-affiliate-id-21
BLOG_URL=https://tu-usuario.github.io/amazon-affiliate-blog

# Opcionales (para Twitter):
TWITTER_API_KEY=tu-twitter-api-key
TWITTER_API_SECRET=tu-twitter-api-secret
TWITTER_ACCESS_TOKEN=tu-twitter-access-token
TWITTER_ACCESS_SECRET=tu-twitter-access-secret
TWITTER_BEARER_TOKEN=tu-twitter-bearer-token
```

### Paso 4: Personalizar el blog

Edita el archivo `_config.yml`:

```yaml
title: "Tu Nombre del Blog"
description: "Tu descripción"
url: "https://tu-usuario.github.io/amazon-affiliate-blog"
amazon_associate_id: "tu-affiliate-id-21"
twitter_username: tu_usuario
```

### Paso 5: Activar GitHub Actions

1. Ve a **Actions** en tu repositorio
2. Si está deshabilitado, haz click en "I understand, enable them"
3. El workflow `auto-publish.yml` se ejecutará cada 2 días automáticamente

### Paso 6: Generar primer artículo manualmente (opcional)

Puedes probar el sistema localmente:

```bash
# Instalar dependencias Python
pip install -r requirements.txt

# Copiar archivo de configuración
cp .env.example .env

# Editar .env con tus credenciales
nano .env

# Generar un artículo de prueba
python scripts/generate_article.py

# Ver el artículo generado en _posts/
```

## 📁 Estructura del Proyecto

```
amazon-affiliate-blog/
├── _config.yml              # Configuración de Jekyll
├── _layouts/
│   ├── default.html         # Layout principal
│   └── post.html            # Layout de artículos
├── _posts/                  # Artículos generados (auto)
│   └── 2026-02-01-ejemplo.md
├── scripts/
│   ├── generate_article.py  # Genera artículos con IA
│   ├── amazon_products.py   # Busca productos Amazon
│   └── twitter_share.py     # Comparte en Twitter/X
├── .github/workflows/
│   ├── auto-publish.yml     # Automatización principal
│   └── deploy.yml           # Deploy a GitHub Pages
├── index.html               # Página principal
├── requirements.txt         # Dependencias Python
├── Gemfile                  # Dependencias Ruby/Jekyll
└── README.md               # Este archivo
```

## 🤖 Funcionamiento Automático

### Cada 2 días automáticamente:

1. **10:00 AM UTC**: GitHub Actions se activa
2. **Genera artículo**: Script usa ChatGPT para crear contenido único
3. **Busca productos**: Obtiene productos relevantes de Amazon
4. **Publica artículo**: Commit y push al repositorio
5. **Deploy**: GitHub Pages actualiza el sitio (2-3 min)
6. **Comparte**: Tweet automático con el nuevo artículo
7. **Repite**: Cada 2 días sin intervención

### También puedes ejecutar manualmente:

1. Ve a **Actions** → **Auto-Generar y Publicar Artículos**
2. Click en **Run workflow** → **Run workflow**
3. Espera 2-3 minutos
4. ¡Nuevo artículo publicado!

## 📊 Nichos Incluidos

El sistema genera automáticamente contenido para estos nichos rentables:

| Nicho | Comisión | Productos Ejemplo |
|-------|----------|-------------------|
| 🔌 Gadgets Tech | 3-4% | Auriculares, power banks, webcams |
| 💪 Fitness | 4-4.5% | Bandas resistencia, esterillas, pesas |
| 🍳 Cocina | 4-4.5% | Freidoras aire, batidoras, cuchillos |
| 🐕 Mascotas | 5-8% | Comederos automáticos, juguetes, camas |

## 🎨 Personalización

### Cambiar nichos:

Edita `scripts/generate_article.py`:

```python
NICHOS = {
    'tu_nicho': {
        'nombre': 'Tu Nicho',
        'keywords': ['keyword1', 'keyword2'],
        'comision': 5.0
    }
}
```

### Cambiar frecuencia de publicación:

Edita `.github/workflows/auto-publish.yml`:

```yaml
on:
  schedule:
    # Cada día a las 10 AM:
    - cron: '0 10 * * *'
    
    # Cada semana (lunes):
    - cron: '0 10 * * 1'
```

### Personalizar diseño:

Edita archivos en `_layouts/` y añade tus estilos CSS.

## 💰 Monetización

### 1. Amazon Associates

- Comisiones del 1-10% según categoría
- Ganas por cualquier compra en 24h después del click
- Sin costos para el comprador

### 2. Google AdSense (opcional)

Añade tu código en `_layouts/default.html`:

```html
<!-- Google AdSense -->
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-XXXXXXX"
     crossorigin="anonymous"></script>
```

### 3. Sponsored Posts (futuro)

Una vez tengas tráfico, puedes vender artículos patrocinados.

## 📈 Crecimiento y SEO

### Estrategias incluidas:

- ✅ URLs optimizadas
- ✅ Meta descripciones únicas
- ✅ Schema markup para rich snippets
- ✅ Sitemap XML automático
- ✅ Internal linking
- ✅ Mobile-friendly
- ✅ Fast loading
- ✅ Social sharing buttons

### Para mejorar ranking:

1. **Paciencia**: SEO toma 3-6 meses
2. **Consistencia**: El sistema publica automáticamente
3. **Quality**: Revisa artículos ocasionalmente
4. **Backlinks**: Comparte en redes, forums, etc.
5. **Google Search Console**: Monitorea rendimiento

## 🔧 Mantenimiento

### Mínimo requerido:

- ⏰ **Tiempo**: 1-2 horas/mes
- 🔍 **Revisar**: Artículos generados (opcional)
- 🔗 **Actualizar**: Enlaces rotos (cada 3 meses)
- 📊 **Monitorear**: Analytics (mensual)

### Comandos útiles:

```bash
# Probar localmente
bundle exec jekyll serve

# Generar artículo manual
python scripts/generate_article.py

# Actualizar productos
python scripts/amazon_products.py

# Test Twitter
python scripts/twitter_share.py
```

## 🐛 Troubleshooting

### El workflow falla:

1. Verifica que todos los secrets estén configurados
2. Revisa los logs en Actions
3. Asegúrate de tener créditos de OpenAI API

### No se genera el sitio:

1. Ve a Actions → Deploy Jekyll
2. Verifica que GitHub Pages esté habilitado
3. Espera 5 minutos después del push

### Los enlaces de Amazon no funcionan:

1. Verifica tu AMAZON_ASSOCIATE_ID
2. Asegúrate de estar aprobado en Amazon Associates
3. Necesitas 3 ventas en 180 días para mantener la cuenta

## 📊 Ingresos Esperados

### Proyección conservadora:

| Mes | Artículos | Visitas/mes | Clicks | Conversión | Ingresos |
|-----|-----------|-------------|--------|------------|----------|
| 1-3 | 45 | 100-500 | 10-50 | 5% | $5-25 |
| 4-6 | 90 | 500-2000 | 50-200 | 7% | $25-150 |
| 7-12 | 180 | 2000-5000 | 200-500 | 10% | $150-500 |
| 12+ | 360+ | 5000+ | 500+ | 10%+ | $500-2000+ |

**Factores clave:**
- Calidad del contenido
- Selección de productos
- SEO y keywords
- Tráfico orgánico
- Tasa de conversión

## 📝 Requisitos Legales

### IMPORTANTE: Disclaimer obligatorio

El blog ya incluye disclaimers legales en:
- Footer (todas las páginas)
- Cada artículo individual
- Página de política de privacidad

**Amazon exige:**
> "Como Asociado de Amazon, ganamos por compras cualificadas"

Esto está incluido automáticamente en todos los posts.

## 🤝 Contribuir

¿Mejoras? ¡Pull requests bienvenidos!

1. Fork el proyecto
2. Crea tu branch (`git checkout -b feature/mejora`)
3. Commit cambios (`git commit -m 'Add: nueva feature'`)
4. Push al branch (`git push origin feature/mejora`)
5. Abre un Pull Request

## 📄 Licencia

MIT License - Usa libremente, modifica y monetiza.

## ❓ FAQ

### ¿Es realmente gratis?

Sí, con limitaciones:
- GitHub Pages: Gratis (100GB bandwidth/mes)
- OpenAI API: $5 gratis inicial, luego ~$10-20/mes
- Amazon Associates: Gratis
- Twitter API: Gratis (tier básico)

### ¿Necesito saber programar?

No. Solo necesitas:
1. Copiar configuraciones
2. Pegar API keys
3. El sistema hace todo lo demás

### ¿Cuánto tiempo hasta ganar dinero?

- Primer pago Amazon: 3-6 meses (realistic)
- Ingresos consistentes: 6-12 meses
- Ingresos significativos ($500+): 12-24 meses

### ¿Puedo usar múltiples nichos?

Sí, el sistema ya alterna entre 4 nichos automáticamente.

### ¿Funciona en [mi país]?

Sí, si Amazon Associates opera allí:
- España: amazon.es
- USA: amazon.com
- UK: amazon.co.uk
- Alemania: amazon.de
- Francia: amazon.fr
- Y más...

## 📞 Soporte

- 🐛 **Issues**: [GitHub Issues](https://github.com/tu-usuario/amazon-affiliate-blog/issues)
- 📧 **Email**: tu-email@example.com
- 🐦 **Twitter**: [@tu_usuario](https://twitter.com/tu_usuario)

## 🌟 Créditos

Desarrollado con ❤️ usando:
- Jekyll (generador de sitios estáticos)
- OpenAI GPT-4 (generación de contenido)
- GitHub Actions (automatización)
- Amazon Associates (monetización)

---

**⭐ Si este proyecto te ayuda, dale una estrella en GitHub!**

**💰 ¡Empieza a generar ingresos pasivos hoy mismo!**

```bash
git clone https://github.com/tu-usuario/amazon-affiliate-blog.git
cd amazon-affiliate-blog
# Sigue los pasos arriba y estarás online en 30 minutos
```

---

Última actualización: Febrero 2026
