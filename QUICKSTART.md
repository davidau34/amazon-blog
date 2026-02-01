# 🎯 GUÍA RÁPIDA DE INICIO - 5 PASOS

## ✅ Checklist de Instalación

### Paso 1: Preparar el Repositorio
```bash
# Crear nuevo repositorio en GitHub
# https://github.com/new
# Nombre: amazon-affiliate-blog (o el que prefieras)
# Público o Privado (ambos funcionan)
# NO inicialices con README, .gitignore o licencia
```

### Paso 2: Clonar y Configurar
```bash
# Clonar este proyecto
git clone https://github.com/tu-usuario/amazon-affiliate-blog.git
cd amazon-affiliate-blog

# Copiar archivo de configuración
cp .env.example .env

# Editar .env con tus credenciales
nano .env  # o usa tu editor favorito
```

### Paso 3: Obtener API Keys

#### OpenAI API Key (REQUERIDO)
1. Ve a: https://platform.openai.com/api-keys
2. Crea una cuenta o inicia sesión
3. Crea una nueva API key
4. Copia la key (empieza con `sk-proj-...`)
5. Añádela a `.env`: `OPENAI_API_KEY=sk-proj-tu-key`

#### Amazon Associates ID (REQUERIDO)
1. Ve a: https://affiliate-program.amazon.com
2. Regístrate o inicia sesión
3. Completa tu perfil
4. Obtén tu Associate ID (termina en `-21` o similar)
5. Añádelo a `.env`: `AMAZON_ASSOCIATE_ID=tu-id-21`

#### Twitter API (OPCIONAL)
1. Ve a: https://developer.twitter.com/en/portal/dashboard
2. Crea una App
3. Obtén las 5 credenciales necesarias
4. Añádelas a `.env`

### Paso 4: Configurar GitHub Pages y Secrets

#### Habilitar GitHub Pages:
1. Ve a tu repositorio en GitHub
2. **Settings** → **Pages**
3. Source: **GitHub Actions**
4. Guarda

#### Configurar Secrets:
1. **Settings** → **Secrets and variables** → **Actions**
2. Click **New repository secret**
3. Añade estos secrets UNO POR UNO:

| Name | Value | Requerido |
|------|-------|-----------|
| `OPENAI_API_KEY` | Tu OpenAI API key | ✅ Sí |
| `AMAZON_ASSOCIATE_ID` | Tu Amazon ID | ✅ Sí |
| `BLOG_URL` | https://tu-usuario.github.io/repo-name | ✅ Sí |
| `TWITTER_API_KEY` | Tu Twitter API key | ⚠️ Opcional |
| `TWITTER_API_SECRET` | Tu Twitter secret | ⚠️ Opcional |
| `TWITTER_ACCESS_TOKEN` | Tu access token | ⚠️ Opcional |
| `TWITTER_ACCESS_SECRET` | Tu access secret | ⚠️ Opcional |
| `TWITTER_BEARER_TOKEN` | Tu bearer token | ⚠️ Opcional |

### Paso 5: Hacer Push y Activar

```bash
# Personaliza _config.yml
nano _config.yml
# Cambia: title, url, email, etc.

# Commit y push
git add .
git commit -m "Configure blog settings"
git push origin main

# Espera 2-3 minutos
# Tu blog estará en: https://tu-usuario.github.io/repo-name
```

## 🤖 Generar Primer Artículo

### Opción A: Automáticamente con GitHub Actions
1. Ve a **Actions** en tu repositorio
2. Selecciona **Auto-Generar y Publicar Artículos**
3. Click **Run workflow** → **Run workflow**
4. Espera 2-3 minutos
5. ¡Artículo publicado!

### Opción B: Manualmente en local
```bash
# Instalar dependencias
pip install -r requirements.txt

# Generar artículo
python scripts/generate_article.py

# Ver artículo generado
ls _posts/

# Push a GitHub
git add _posts/
git commit -m "Add new article"
git push
```

## 📅 Programación Automática

El workflow está configurado para ejecutarse **cada 2 días a las 10:00 AM UTC**.

**Para cambiar la frecuencia:**

Edita `.github/workflows/auto-publish.yml`:

```yaml
on:
  schedule:
    # Cada día:
    - cron: '0 10 * * *'
    
    # Cada 3 días:
    - cron: '0 10 */3 * *'
    
    # Cada lunes:
    - cron: '0 10 * * 1'
    
    # Dos veces por semana (lunes y jueves):
    - cron: '0 10 * * 1,4'
```

## 🧪 Probar Localmente (Opcional)

```bash
# Instalar Jekyll
gem install bundler
bundle install

# Ejecutar servidor local
bundle exec jekyll serve

# Abrir en navegador:
# http://localhost:4000
```

## ❗ Solución de Problemas Comunes

### Error: "Invalid workflow file"
- Verifica que los archivos en `.github/workflows/` tengan formato YAML correcto
- Asegúrate de que los secrets estén configurados

### Error: "OpenAI API key not found"
- Verifica que el secret `OPENAI_API_KEY` esté configurado en GitHub
- Verifica que la key sea válida en https://platform.openai.com/api-keys

### Error: "Jekyll build failed"
- Verifica que `_config.yml` tenga formato YAML válido
- Asegúrate de que `baseurl` y `url` estén correctos

### El sitio no se actualiza
- Espera 5 minutos (GitHub Pages tarda en deployar)
- Ve a Actions y verifica que el workflow se haya ejecutado correctamente
- Verifica que GitHub Pages esté habilitado

### No se generan artículos automáticamente
- Verifica que los secrets estén configurados
- Ve a Actions → Auto-Generar → Run workflow (manualmente)
- Revisa los logs de ejecución para ver errores

## 📞 Soporte

Si tienes problemas:

1. **Revisa los logs**: Actions → Último workflow → Ver logs
2. **Issues en GitHub**: [Crea un issue](https://github.com/tu-usuario/amazon-affiliate-blog/issues)
3. **README completo**: Lee `README.md` para más detalles

## 🎉 ¡Listo!

Tu blog de afiliados está configurado y funcionando. Los artículos se generarán automáticamente cada 2 días.

**Tiempo total de configuración**: 30-45 minutos  
**Mantenimiento requerido**: 1-2 horas/mes  
**Potencial de ingresos**: $500-2000/mes (después de 12 meses)

---

**Próximos pasos recomendados:**

1. ✅ Personaliza el diseño en `_layouts/`
2. ✅ Añade Google Analytics
3. ✅ Solicita acceso a Amazon Product Advertising API
4. ✅ Promociona tu blog en redes sociales
5. ✅ Monitorea rendimiento en Google Search Console

**¡Éxito con tu blog de afiliados! 🚀💰**
