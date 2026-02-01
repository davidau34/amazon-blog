# 🔧 Solución de Problemas

## ❌ Workflow de GitHub Actions falla

### Verificar logs del workflow

1. Ve a: https://github.com/davidau34/amazon-blog/actions
2. Haz clic en el workflow fallido (con ❌)
3. Haz clic en "generate-and-publish"
4. Expande cada paso para ver el error específico

### Errores comunes y soluciones

#### Error: "OPENAI_API_KEY not found"
**Causa:** El secreto OPENAI_API_KEY no está configurado correctamente en GitHub

**Solución:**
1. Ve a: https://github.com/davidau34/amazon-blog/settings/secrets/actions
2. Verifica que existe el secreto `OPENAI_API_KEY`
3. Si no existe o es incorrecto:
   - Haz clic en "New repository secret"
   - Name: `OPENAI_API_KEY`
   - Secret: Tu clave API de OpenAI (sk-proj-...)
   - Click "Add secret"

#### Error: "insufficient_quota" o "rate_limit_exceeded"
**Causa:** Tu cuenta de OpenAI se ha quedado sin créditos

**Solución:**
1. Ve a: https://platform.openai.com/account/billing
2. Añade créditos a tu cuenta (mínimo $5)
3. Vuelve a ejecutar el workflow

#### Error: "Permission denied" al hacer push
**Causa:** El token de GitHub no tiene permisos suficientes

**Solución:**
1. El workflow ya tiene `permissions: contents: write`
2. Si sigue fallando, ve a Settings → Actions → General
3. En "Workflow permissions", selecciona "Read and write permissions"
4. Click "Save"

#### El workflow se ejecuta pero no genera artículos nuevos
**Causa:** Ya existe un artículo para el día de hoy

**Solución:**
- El script automáticamente salta la generación si ya existe un artículo del día
- Esto es normal y evita duplicados
- El próximo artículo se generará en 2 días (según el cron schedule)

### Ejecutar workflow manualmente

Para probar el workflow sin esperar al cron:

1. Ve a: https://github.com/davidau34/amazon-blog/actions/workflows/auto-publish.yml
2. Click "Run workflow" → "Run workflow"
3. Espera ~1 minuto
4. Revisa los logs si falla

### Probar localmente

Para probar el script localmente antes de GitHub Actions:

```bash
cd /tmp/amazon-affiliate-blog

# Asegurarte de que .env tiene las credenciales
cat .env

# Probar generación de artículo
python3 scripts/generate_article.py

# Probar actualización de productos (opcional)
python3 scripts/amazon_products.py

# Probar compartir en Twitter (opcional)
python3 scripts/twitter_share.py
```

### Verificar secretos configurados

Secretos necesarios en GitHub:
- ✅ `OPENAI_API_KEY` - **OBLIGATORIO**
- ✅ `AMAZON_ASSOCIATE_ID` - **OBLIGATORIO**
- ✅ `BLOG_URL` - **OBLIGATORIO**
- ⚠️ `TWITTER_API_KEY` - Opcional
- ⚠️ `TWITTER_API_SECRET` - Opcional
- ⚠️ `TWITTER_ACCESS_TOKEN` - Opcional
- ⚠️ `TWITTER_ACCESS_SECRET` - Opcional
- ⚠️ `TWITTER_BEARER_TOKEN` - Opcional
- ⚠️ `AMAZON_ACCESS_KEY` - Opcional
- ⚠️ `AMAZON_SECRET_KEY` - Opcional

Los secretos marcados como "Opcional" no son necesarios para que el blog funcione.

### Logs detallados

Si necesitas más información sobre un error:

1. Ve a la run fallida en Actions
2. Haz clic en el paso que falló
3. Lee el mensaje de error completo
4. Busca líneas que contengan "Error" o "Failed"

### Contacto

Si el problema persiste:
1. Copia el mensaje de error completo de GitHub Actions
2. Verifica que todos los secretos obligatorios están configurados
3. Revisa que tu cuenta de OpenAI tiene créditos disponibles
