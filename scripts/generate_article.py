#!/usr/bin/env python3
"""
Script para generar artículos automáticamente usando OpenAI API
y buscar productos relevantes en Amazon
"""

import os
import sys
from datetime import datetime
import random
from pathlib import Path
import json
import re

# Importaciones necesarias (instalar con: pip install openai python-dotenv)
try:
    from openai import OpenAI
    from dotenv import load_dotenv
except ImportError:
    print("❌ Error: Faltan dependencias. Ejecuta: pip install -r requirements.txt")
    sys.exit(1)

# Cargar variables de entorno
load_dotenv()

# Configuración
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
AMAZON_ASSOCIATE_ID = os.getenv('AMAZON_ASSOCIATE_ID', 'tu-affiliate-id-21')
BLOG_DIR = Path(__file__).parent.parent
POSTS_DIR = BLOG_DIR / '_posts'

# Crear directorio de posts si no existe
POSTS_DIR.mkdir(parents=True, exist_ok=True)

# Nichos y productos objetivo
NICHOS = {
    'gadgets_tech': {
        'nombre': 'Gadgets Tech',
        'keywords': ['auriculares bluetooth', 'power bank', 'webcam', 'ratón inalámbrico', 
                    'teclado mecánico', 'hub usb', 'soporte laptop', 'cable usb-c'],
        'comision': 3.0
    },
    'fitness': {
        'nombre': 'Fitness',
        'keywords': ['bandas de resistencia', 'esterilla yoga', 'pesas ajustables', 
                    'rodillo foam', 'cuerda saltar', 'mancuernas', 'pelota ejercicio'],
        'comision': 4.5
    },
    'cocina': {
        'nombre': 'Cocina',
        'keywords': ['freidora de aire', 'batidora', 'robot cocina', 'set cuchillos', 
                    'licuadora', 'cafetera', 'organizador cocina', 'báscula cocina'],
        'comision': 4.0
    },
    'mascotas': {
        'nombre': 'Mascotas',
        'keywords': ['comedero automático', 'juguetes perro', 'cama para gatos', 
                    'collar GPS', 'rascador gatos', 'correa extensible', 'fuente agua gatos'],
        'comision': 8.0
    }
}

# Tipos de artículos
TIPOS_ARTICULOS = [
    {
        'tipo': 'review',
        'template': 'Análisis Completo: {producto} - ¿Vale la Pena en 2026?'
    },
    {
        'tipo': 'comparativa',
        'template': '{producto1} vs {producto2}: ¿Cuál Comprar en 2026?'
    },
    {
        'tipo': 'guia',
        'template': 'Los {numero} Mejores {categoria} de 2026 - Guía de Compra'
    },
    {
        'tipo': 'tutorial',
        'template': 'Cómo Elegir {producto}: Guía Definitiva 2026'
    }
]


class GeneradorArticulos:
    def __init__(self):
        if not OPENAI_API_KEY:
            raise ValueError("❌ OPENAI_API_KEY no está configurada en el archivo .env")
        
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        print("✅ Cliente OpenAI inicializado")
    
    def generar_ideas_articulos(self, nicho, num_ideas=5):
        """Genera ideas de artículos para un nicho específico"""
        keywords = ', '.join(nicho['keywords'][:5])
        
        prompt = f"""Genera {num_ideas} ideas únicas de artículos para un blog de afiliados de Amazon 
sobre {nicho['nombre']}. Las keywords principales son: {keywords}

Cada idea debe:
1. Ser atractiva y clickeable
2. Incluir el año 2026
3. Resolver un problema real del usuario
4. Tener potencial SEO
5. Ser perfecta para incluir enlaces de afiliado

Formato de respuesta (JSON):
[
  {{
    "titulo": "Título del artículo",
    "tipo": "review|comparativa|guia|tutorial",
    "keyword_principal": "keyword principal",
    "productos_sugeridos": ["producto1", "producto2"]
  }}
]

Solo responde con el JSON, sin texto adicional."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un experto en marketing de contenidos y SEO para blogs de afiliados."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8
            )
            
            content = response.choices[0].message.content.strip()
            # Extraer JSON del contenido (por si viene con markdown)
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
            return json.loads(content)
            
        except Exception as e:
            print(f"❌ Error al generar ideas: {e}")
            return []
    
    def generar_articulo_completo(self, titulo, tipo, keyword, productos, nicho):
        """Genera un artículo completo optimizado para SEO y afiliados"""
        
        prompt = f"""Escribe un artículo COMPLETO y PROFESIONAL para un blog de afiliados de Amazon.

INFORMACIÓN DEL ARTÍCULO:
- Título: {titulo}
- Tipo: {tipo}
- Keyword principal: {keyword}
- Productos a mencionar: {', '.join(productos)}
- Nicho: {nicho['nombre']}
- Comisión promedio: {nicho['comision']}%

REQUISITOS ESTRICTOS:
1. Longitud mínima: 2000 palabras
2. Estructura clara con H2 y H3
3. Incluir tabla comparativa (si aplica)
4. Pros y contras para cada producto
5. Sección de preguntas frecuentes (FAQ) al final
6. Tono conversacional pero profesional
7. Incluir CTAs (Call to Action) naturales
8. Mencionar {len(productos)} productos con análisis detallado
9. SEO optimizado para la keyword: {keyword}
10. Incluir placeholders para enlaces de Amazon: [AMAZON_LINK:nombre-producto]

ESTRUCTURA REQUERIDA:
## Introducción
- Hook atractivo
- Problema que resuelve el artículo
- Breve resumen de lo que encontrarán

## [Secciones principales según el tipo de artículo]
- Análisis detallado de productos
- Comparaciones
- Características técnicas
- Experiencia de uso

## Tabla Comparativa (si aplica)
| Producto | Características | Precio | Valoración | Enlace |
|----------|----------------|--------|------------|--------|

## Pros y Contras
### Producto 1
**Pros:**
- Ventaja 1
- Ventaja 2

**Contras:**
- Desventaja 1

## Guía de Compra
- Qué buscar al comprar
- Consejos expertos

## Preguntas Frecuentes (FAQ)
### ¿Pregunta relevante?
Respuesta detallada.

## Conclusión
- Resumen
- Recomendación final
- CTA para comprar

IMPORTANTE: 
- Usa formato Markdown
- Los enlaces se agregarán después como: [Nombre Producto](amazon-url)
- Sé honesto y útil, no solo vendas
- Incluye datos reales y específicos cuando sea posible

Escribe SOLO el contenido del artículo en Markdown, sin introducción ni notas adicionales."""

        try:
            print(f"   🤖 Generando artículo con GPT-4...")
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",  # o "gpt-4" si tienes acceso
                messages=[
                    {"role": "system", "content": "Eres un redactor experto en contenido de afiliados, SEO y análisis de productos. Escribes artículos informativos, honestos y bien estructurados."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=4000
            )
            
            contenido = response.choices[0].message.content.strip()
            print(f"   ✅ Artículo generado ({len(contenido)} caracteres)")
            return contenido
            
        except Exception as e:
            print(f"   ❌ Error al generar artículo: {e}")
            return None
    
    def crear_front_matter(self, titulo, categoria, keywords, productos):
        """Crea el front matter de Jekyll para el post"""
        fecha = datetime.now()
        
        # Generar excerpt
        excerpt = f"Descubre todo sobre {', '.join(productos[:2])} y más. Análisis detallado, comparativas y guía de compra actualizada 2026."
        
        front_matter = f"""---
layout: post
title: "{titulo}"
date: {fecha.strftime('%Y-%m-%d %H:%M:%S')} +0000
category: {categoria}
tags: [{', '.join([f'"{k}"' for k in keywords[:5]])}]
excerpt: "{excerpt}"
image: https://via.placeholder.com/1200x630.png?text={titulo.replace(' ', '+')}
author: "Tech Deals Team"
reading_time: {random.randint(8, 15)}
---

"""
        return front_matter
    
    def agregar_enlaces_amazon(self, contenido, productos):
        """Agrega enlaces de afiliado de Amazon al contenido"""
        
        # Por ahora usamos placeholders genéricos
        # En producción, aquí usarías Amazon Product Advertising API
        for producto in productos:
            # Crear slug del producto
            slug = re.sub(r'[^a-z0-9]+', '-', producto.lower()).strip('-')
            
            # URL de afiliado de Amazon (formato ejemplo)
            amazon_url = f"https://www.amazon.es/dp/ASIN?tag={AMAZON_ASSOCIATE_ID}"
            
            # Reemplazar placeholder con enlace real
            contenido = contenido.replace(
                f"[AMAZON_LINK:{slug}]",
                f"[Ver {producto} en Amazon](amazon_url){{: .amazon-button}}"
            )
        
        return contenido
    
    def guardar_post(self, titulo, contenido, categoria, keywords, productos):
        """Guarda el post como archivo Markdown en _posts/"""
        
        # Crear filename compatible con Jekyll
        fecha = datetime.now()
        slug = re.sub(r'[^a-z0-9]+', '-', titulo.lower()).strip('-')[:60]
        filename = f"{fecha.strftime('%Y-%m-%d')}-{slug}.md"
        filepath = POSTS_DIR / filename
        
        # Crear front matter
        front_matter = self.crear_front_matter(titulo, categoria, keywords, productos)
        
        # Agregar enlaces de Amazon
        contenido_con_enlaces = self.agregar_enlaces_amazon(contenido, productos)
        
        # Contenido completo
        post_completo = front_matter + contenido_con_enlaces
        
        # Guardar archivo
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(post_completo)
        
        print(f"   💾 Post guardado: {filename}")
        return filepath
    
    def generar_post_aleatorio(self):
        """Genera un post aleatorio de un nicho aleatorio"""
        
        # Seleccionar nicho aleatorio
        nicho_key = random.choice(list(NICHOS.keys()))
        nicho = NICHOS[nicho_key]
        
        print(f"\n📝 Generando artículo para nicho: {nicho['nombre']}")
        
        # Generar ideas
        print("   💡 Generando ideas de artículos...")
        ideas = self.generar_ideas_articulos(nicho, num_ideas=1)
        
        if not ideas:
            print("   ❌ No se pudieron generar ideas")
            return None
        
        idea = ideas[0]
        print(f"   ✨ Idea seleccionada: {idea['titulo']}")
        
        # Generar artículo completo
        contenido = self.generar_articulo_completo(
            titulo=idea['titulo'],
            tipo=idea['tipo'],
            keyword=idea['keyword_principal'],
            productos=idea['productos_sugeridos'],
            nicho=nicho
        )
        
        if not contenido:
            return None
        
        # Guardar post
        filepath = self.guardar_post(
            titulo=idea['titulo'],
            contenido=contenido,
            categoria=nicho['nombre'],
            keywords=[idea['keyword_principal']] + random.sample(nicho['keywords'], 3),
            productos=idea['productos_sugeridos']
        )
        
        return filepath


def main():
    """Función principal"""
    print("🚀 Generador de Artículos para Blog de Afiliados Amazon\n")
    print("=" * 60)
    
    try:
        generador = GeneradorArticulos()
        
        # Generar un artículo
        filepath = generador.generar_post_aleatorio()
        
        if filepath:
            print("\n" + "=" * 60)
            print("✅ ¡Artículo generado exitosamente!")
            print(f"📄 Archivo: {filepath}")
            print("\n💡 Próximos pasos:")
            print("   1. Revisa el artículo generado")
            print("   2. Añade imágenes reales de productos")
            print("   3. Actualiza los enlaces de Amazon con ASINs reales")
            print("   4. Haz commit y push a GitHub")
            print("   5. GitHub Actions lo publicará automáticamente")
        else:
            print("\n❌ Error al generar el artículo")
            sys.exit(1)
            
    except Exception as e:
        print(f"\n❌ Error fatal: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
