#!/usr/bin/env python3
"""
Script para compartir automáticamente en Twitter/X cuando se publica un nuevo artículo
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import random

try:
    from dotenv import load_dotenv
    import tweepy
except ImportError:
    print("❌ Error: Instala dependencias con: pip install -r requirements.txt")
    sys.exit(1)

load_dotenv()

# Configuración Twitter/X API v2
TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET = os.getenv('TWITTER_API_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN')

# URL base del blog
BLOG_URL = os.getenv('BLOG_URL', 'https://tu-usuario.github.io')


class TwitterBot:
    """
    Bot para publicar automáticamente en Twitter/X
    
    NOTA: Necesitas una cuenta de desarrollador de Twitter:
    1. Regístrate en: https://developer.twitter.com
    2. Crea una App
    3. Obtén las credenciales (API Key, Secret, etc.)
    4. Guárdalas en el archivo .env
    """
    
    def __init__(self):
        self.client = None
        self.inicializar_cliente()
    
    def inicializar_cliente(self):
        """Inicializa el cliente de Twitter API v2"""
        if not all([TWITTER_API_KEY, TWITTER_API_SECRET, 
                   TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET]):
            print("⚠️  Credenciales de Twitter no configuradas")
            print("   El script funcionará en modo simulación")
            return
        
        try:
            self.client = tweepy.Client(
                bearer_token=TWITTER_BEARER_TOKEN,
                consumer_key=TWITTER_API_KEY,
                consumer_secret=TWITTER_API_SECRET,
                access_token=TWITTER_ACCESS_TOKEN,
                access_token_secret=TWITTER_ACCESS_SECRET
            )
            print("✅ Cliente de Twitter inicializado")
        except Exception as e:
            print(f"⚠️  Error al inicializar Twitter: {e}")
            print("   Continuando en modo simulación")
    
    def generar_tweet(self, titulo, url, categoria):
        """
        Genera un tweet atractivo para el artículo
        
        Límite de caracteres en Twitter/X: 280
        Restamos ~25 caracteres para la URL (acortada automáticamente)
        """
        
        # Templates de tweets variados
        templates = [
            "🔥 {titulo}\n\n{url}\n\n#{hashtag1} #{hashtag2}",
            "💡 {titulo}\n\nAnálisis completo 👉 {url}\n\n#{hashtag1} #{hashtag2} #{hashtag3}",
            "¿Buscas {categoria}?\n\n{titulo}\n\n{url}\n\n#{hashtag1} #{hashtag2}",
            "✨ Nuevo artículo:\n\n{titulo}\n\n{url}\n\n#{hashtag1} #{hashtag2}",
            "📝 {titulo}\n\nReview completa aquí 👇\n{url}\n\n#{hashtag1} #{hashtag2}",
        ]
        
        # Hashtags según categoría
        hashtags_map = {
            'Gadgets Tech': ['TechDeals', 'Gadgets', 'Amazon', 'Tecnología'],
            'Fitness': ['Fitness', 'Deporte', 'EjercicioEnCasa', 'Amazon'],
            'Cocina': ['Cocina', 'Recetas', 'Electrodomésticos', 'Amazon'],
            'Mascotas': ['Mascotas', 'Perros', 'Gatos', 'Amazon'],
        }
        
        hashtags = hashtags_map.get(categoria, ['Amazon', 'Ofertas', 'Compras'])
        
        # Seleccionar template aleatorio
        template = random.choice(templates)
        
        # Acortar título si es muy largo
        titulo_corto = titulo[:100] + '...' if len(titulo) > 100 else titulo
        
        # Generar tweet
        tweet = template.format(
            titulo=titulo_corto,
            url=url,
            categoria=categoria.lower(),
            hashtag1=hashtags[0],
            hashtag2=hashtags[1],
            hashtag3=hashtags[2] if len(hashtags) > 2 else 'Ofertas'
        )
        
        # Asegurar que no exceda 280 caracteres
        if len(tweet) > 280:
            # Recortar título
            exceso = len(tweet) - 280
            titulo_corto = titulo_corto[:-exceso-3] + '...'
            tweet = template.format(
                titulo=titulo_corto,
                url=url,
                categoria=categoria.lower(),
                hashtag1=hashtags[0],
                hashtag2=hashtags[1],
                hashtag3=hashtags[2] if len(hashtags) > 2 else ''
            )
        
        return tweet[:280]  # Forzar límite
    
    def publicar_tweet(self, texto):
        """Publica un tweet"""
        if not self.client:
            print("⚠️  Modo simulación - Tweet que se publicaría:")
            print("-" * 60)
            print(texto)
            print("-" * 60)
            print(f"   Caracteres: {len(texto)}")
            return None
        
        try:
            response = self.client.create_tweet(text=texto)
            tweet_id = response.data['id']
            print(f"✅ Tweet publicado: https://twitter.com/user/status/{tweet_id}")
            return tweet_id
        except Exception as e:
            print(f"❌ Error al publicar tweet: {e}")
            return None
    
    def compartir_articulo(self, post_path):
        """Comparte un artículo en Twitter"""
        # Leer front matter del post
        with open(post_path, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Extraer información del front matter
        import re
        
        titulo_match = re.search(r'title:\s*"([^"]+)"', contenido)
        categoria_match = re.search(r'category:\s*([^\n]+)', contenido)
        
        if not titulo_match:
            print("❌ No se pudo extraer el título del post")
            return None
        
        titulo = titulo_match.group(1)
        categoria = categoria_match.group(1).strip() if categoria_match else "General"
        
        # Generar URL del artículo
        filename = post_path.stem
        # Formato: 2026-02-01-titulo-del-post.md -> /2026/02/01/titulo-del-post/
        partes = filename.split('-', 3)
        if len(partes) >= 4:
            year, month, day, slug = partes
            url_path = f"/{year}/{month}/{day}/{slug}/"
            url_completa = f"{BLOG_URL}{url_path}"
        else:
            url_completa = f"{BLOG_URL}/posts/{filename}/"
        
        # Generar y publicar tweet
        tweet_texto = self.generar_tweet(titulo, url_completa, categoria)
        tweet_id = self.publicar_tweet(tweet_texto)
        
        return tweet_id


def main():
    """Función principal"""
    print("🐦 Bot de Twitter/X para Blog de Afiliados\n")
    print("=" * 60)
    
    bot = TwitterBot()
    
    # Buscar el último post publicado
    posts_dir = Path(__file__).parent.parent / '_posts'
    
    if not posts_dir.exists() or not list(posts_dir.glob('*.md')):
        print("❌ No hay posts para compartir")
        sys.exit(1)
    
    # Obtener el post más reciente
    posts = sorted(posts_dir.glob('*.md'), reverse=True)
    ultimo_post = posts[0]
    
    print(f"📄 Post a compartir: {ultimo_post.name}")
    
    # Compartir en Twitter
    tweet_id = bot.compartir_articulo(ultimo_post)
    
    if tweet_id:
        print("\n✅ ¡Artículo compartido en Twitter!")
    else:
        print("\n✅ Tweet generado (modo simulación)")
    
    print("\n💡 Próximos pasos:")
    print("   1. Configura las credenciales de Twitter en .env")
    print("   2. El script se ejecutará automáticamente con GitHub Actions")
    print("   3. Cada nuevo post se compartirá automáticamente")


if __name__ == "__main__":
    main()
