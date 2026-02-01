# 🖼️ Cómo Añadir Imágenes Reales a los Artículos

## Método 1: Editar directamente en GitHub

1. Ve a: https://github.com/davidau34/amazon-blog/tree/main/_posts
2. Click en el artículo que quieres editar
3. Click en el icono del lápiz ✏️ (Edit this file)
4. Busca la línea `image:` en el front matter (arriba)
5. Reemplaza con una URL real
6. Scroll abajo → "Commit changes"

## Método 2: URLs de Amazon

### Cómo obtener URL de imagen de Amazon:

1. Ve al producto en Amazon.es
2. Click derecho en la imagen principal
3. "Copiar dirección de imagen"
4. Pégala en el campo `image:` del artículo

Ejemplo:
```yaml
image: https://m.media-amazon.com/images/I/71ABC123DEF.jpg
```

## Método 3: Unsplash (imágenes gratis de alta calidad)

1. Busca en: https://unsplash.com
2. Busca: "air fryer", "kitchen", "cooking", etc.
3. Click en una imagen
4. Click derecho → "Copiar dirección de imagen"
5. Añade parámetros de tamaño: `?w=1200&h=630`

Ejemplo:
```yaml
image: https://images.unsplash.com/photo-1234567890?w=1200&h=630
```

## Método 4: Subir tus propias imágenes

```bash
# Crear carpeta
mkdir -p assets/images

# Poner tus imágenes ahí (jpg, png)
# Por ejemplo: freidora-aire.jpg

# Subir a GitHub
git add assets/images/
git commit -m "Add product images"
git push
```

En el artículo:
```yaml
image: /assets/images/freidora-aire.jpg
```

## 🎯 RECOMENDACIÓN

Para empezar: **Usa Unsplash** (gratis, legal, alta calidad)

Para profesional: **Fotos reales de productos de Amazon**

## Tamaños recomendados:

- **Imagen principal del post**: 1200x630px (para redes sociales)
- **Imágenes dentro del artículo**: 800x600px
- **Thumbnails**: 400x300px

## ⚠️ IMPORTANTE

- No uses imágenes con copyright
- Las de Amazon son OK para afiliados
- Unsplash es gratis y legal
- Atribución en Unsplash es opcional pero recomendada
