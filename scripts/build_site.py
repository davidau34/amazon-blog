#!/usr/bin/env python3
"""
Construye el sitio HTML estático a partir de los posts en Markdown
"""

import os
import re
from pathlib import Path
from datetime import datetime
import markdown

BASE_DIR = Path(__file__).parent.parent
POSTS_DIR = BASE_DIR / '_posts'
PUBLIC_DIR = BASE_DIR / 'public'
POSTS_PUBLIC_DIR = PUBLIC_DIR / 'posts'

# Configuración del sitio
SITE_CONFIG = {
    'title': 'TechDeals - Las Mejores Ofertas de Amazon',
    'description': 'Descubre los mejores productos de tecnología, gadgets y más en Amazon',
    'url': 'https://davidau34.github.io/amazon-blog',
    'amazon_id': 'davidau342123-21'
}

def create_html_template(title, content, is_home=False):
    """Crea el template HTML completo"""
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | {SITE_CONFIG['title']}</title>
    <meta name="description" content="{SITE_CONFIG['description']}">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f7fa;
        }}
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }}
        header {{
            background: white;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }}
        .header-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #667eea;
            text-decoration: none;
        }}
        nav ul {{
            list-style: none;
            display: flex;
            gap: 30px;
        }}
        nav a {{
            text-decoration: none;
            color: #333;
            font-weight: 500;
            transition: color 0.3s;
        }}
        nav a:hover {{
            color: #667eea;
        }}
        .hero {{
            text-align: center;
            padding: 60px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border-radius: 10px;
            margin: 40px 0;
        }}
        .hero h1 {{
            font-size: 48px;
            margin-bottom: 20px;
        }}
        .post-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 30px;
            margin: 40px 0;
        }}
        .post-card {{
            background: white;
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }}
        .post-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }}
        .post-image {{
            width: 100%;
            height: 200px;
            object-fit: cover;
        }}
        .post-content {{
            padding: 20px;
        }}
        .post-content h2 {{
            margin-bottom: 10px;
        }}
        .post-content h2 a {{
            color: #333;
            text-decoration: none;
        }}
        .post-content h2 a:hover {{
            color: #667eea;
        }}
        .post-meta {{
            color: #666;
            font-size: 14px;
            margin: 10px 0;
        }}
        .post-category {{
            background: #667eea;
            color: white;
            padding: 4px 12px;
            border-radius: 15px;
            font-size: 12px;
            margin-left: 10px;
        }}
        .read-more {{
            display: inline-block;
            margin-top: 15px;
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }}
        .amazon-link {{
            display: inline-block;
            background: linear-gradient(135deg, #ff9900, #ff6600);
            color: white !important;
            padding: 10px 20px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            margin: 10px 5px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .amazon-link:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 8px rgba(255,153,0,0.3);
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        table th, table td {{
            padding: 12px;
            text-align: left;
            border-bottom: 1px solid #ddd;
        }}
        table th {{
            background: #667eea;
            color: white;
        }}
        .read-more:hover {{
            text-decoration: underline;
        }}
        article img {{
            max-width: 100%;
            height: auto;
            border-radius: 8px;
            margin: 20px 0;
        }}
        article h2, article h3 {{
            margin-top: 30px;
            margin-bottom: 15px;
            color: #333;
        }}
        article p {{
            margin-bottom: 15px;
        }}
        article a {{
            color: #667eea;
            text-decoration: none;
        }}
        article a:hover {{
            text-decoration: underline;
        }}
        .amazon-button {{
            display: inline-block;
            background: #ff9900;
            color: white;
            padding: 12px 24px;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            margin: 10px 5px;
        }}
        .amazon-button:hover {{
            background: #e88900;
        }}
        footer {{
            background: #2d3748;
            color: white;
            padding: 40px 0;
            margin-top: 60px;
        }}
        .footer-content {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 30px;
        }}
        .disclaimer {{
            background: #fff3cd;
            border: 1px solid #ffc107;
            border-radius: 5px;
            padding: 15px;
            margin: 30px 0;
        }}
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="header-content">
                <a href="{SITE_CONFIG['url']}" class="logo">{SITE_CONFIG['title']}</a>
                <nav>
                    <ul>
                        <li><a href="{SITE_CONFIG['url']}">Inicio</a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </header>

    <main class="container">
        {content}
    </main>

    <footer>
        <div class="container">
            <div class="footer-content">
                <div>
                    <h3>{SITE_CONFIG['title']}</h3>
                    <p>{SITE_CONFIG['description']}</p>
                </div>
                <div>
                    <p><small>⚠️ Como Asociado de Amazon, ganamos por compras cualificadas.</small></p>
                    <p><small>© 2026 {SITE_CONFIG['title']}. Todos los derechos reservados.</small></p>
                </div>
            </div>
        </div>
    </footer>
</body>
</html>"""

def parse_post(filepath):
    """Lee y parsea un post en Markdown"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extraer front matter
    front_matter = {}
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            front_matter_text = parts[1]
            for line in front_matter_text.strip().split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    front_matter[key.strip()] = value.strip().strip('"')
            content = parts[2]
    
    # Convertir markdown a HTML
    md = markdown.Markdown(extensions=['extra', 'codehilite'])
    html_content = md.convert(content)
    
    return front_matter, html_content

def replace_amazon_links(content, amazon_id):
    """Reemplaza placeholders [AMAZON_LINK:...] con enlaces de afiliado reales"""
    def create_amazon_link(match):
        product_key = match.group(1)
        # Convertir el key en un término de búsqueda
        search_term = product_key.replace('_', '+')
        return f'<a href="https://www.amazon.es/s?k={search_term}&tag={amazon_id}" target="_blank" rel="nofollow noopener" class="amazon-link">Ver en Amazon 🛒</a>'
    
    return re.sub(r'\[AMAZON_LINK:([^\]]+)\]', create_amazon_link, content)

def build_post_page(post_file):
    """Construye una página individual de post"""
    front_matter, content = parse_post(POSTS_DIR / post_file)
    
    title = front_matter.get('title', 'Post')
    date = front_matter.get('date', '')
    category = front_matter.get('category', '')
    image = front_matter.get('image', '')
    
    # Reemplazar enlaces de Amazon
    content = replace_amazon_links(content, SITE_CONFIG['amazon_id'])
    
    # Crear slug del filename
    slug = post_file.replace('.md', '')
    
    post_html = f"""
    <article>
        <div class="hero">
            <h1>{title}</h1>
            <p class="post-meta">{date} {f'<span class="post-category">{category}</span>' if category else ''}</p>
        </div>
        
        {f'<img src="{image}" alt="{title}" style="width:100%; max-height:400px; object-fit:cover; border-radius:10px;">' if image else ''}
        
        <div style="background:white; padding:40px; border-radius:10px; margin-top:30px;">
            {content}
        </div>
        
        <div class="disclaimer">
            <p><small>⚠️ <strong>Aviso:</strong> Este sitio contiene enlaces de afiliado de Amazon. Podemos ganar una comisión si realizas una compra a través de nuestros enlaces.</small></p>
        </div>
    </article>
    """
    
    full_html = create_html_template(title, post_html)
    
    # Guardar
    output_file = POSTS_PUBLIC_DIR / f"{slug}.html"
    output_file.write_text(full_html, encoding='utf-8')
    
    return {
        'slug': slug,
        'title': title,
        'date': date,
        'category': category,
        'image': image,
        'excerpt': front_matter.get('excerpt', '')
    }

def build_home_page(posts):
    """Construye la página de inicio"""
    posts_html = '<div class="post-grid">'
    
    for post in sorted(posts, key=lambda x: x['date'], reverse=True):
        posts_html += f"""
        <div class="post-card">
            {f'<img src="{post["image"]}" alt="{post["title"]}" class="post-image">' if post['image'] else ''}
            <div class="post-content">
                <h2><a href="{SITE_CONFIG['url']}/posts/{post['slug']}.html">{post['title']}</a></h2>
                <div class="post-meta">
                    <span>{post['date'][:10]}</span>
                    {f'<span class="post-category">{post["category"]}</span>' if post['category'] else ''}
                </div>
                <p>{post['excerpt'][:150]}...</p>
                <a href="{SITE_CONFIG['url']}/posts/{post['slug']}.html" class="read-more">Leer más →</a>
            </div>
        </div>
        """
    
    posts_html += '</div>'
    
    home_content = f"""
    <div class="hero">
        <h1>🔥 Las Mejores Ofertas de Amazon 2026</h1>
        <p style="font-size:20px; margin-top:20px;">Análisis expertos, reviews honestas y las mejores ofertas en tecnología</p>
    </div>
    
    <h2 style="margin-bottom:30px;">📝 Últimos Artículos</h2>
    {posts_html}
    
    <div class="disclaimer">
        <p><small>⚠️ <strong>Aviso:</strong> Este sitio contiene enlaces de afiliado de Amazon. Podemos ganar una comisión si realizas una compra a través de nuestros enlaces, sin costo adicional para ti.</small></p>
    </div>
    """
    
    full_html = create_html_template('Inicio', home_content, is_home=True)
    (PUBLIC_DIR / 'index.html').write_text(full_html, encoding='utf-8')

def main():
    """Construye todo el sitio"""
    print("🔨 Construyendo sitio HTML estático...\n")
    
    # Crear directorios
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    POSTS_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    
    # Procesar todos los posts
    posts = []
    post_files = list(POSTS_DIR.glob('*.md'))
    
    if not post_files:
        print("❌ No se encontraron posts en _posts/")
        return
    
    for post_file in post_files:
        print(f"📄 Procesando: {post_file.name}")
        post_info = build_post_page(post_file.name)
        posts.append(post_info)
    
    # Construir home page
    print(f"\n🏠 Construyendo página de inicio...")
    build_home_page(posts)
    
    print(f"\n✅ Sitio construido exitosamente!")
    print(f"   📁 Archivos en: {PUBLIC_DIR}")
    print(f"   📝 {len(posts)} artículos procesados")
    print(f"\n🌐 Para probar localmente:")
    print(f"   cd {PUBLIC_DIR} && python3 -m http.server 8000")

if __name__ == '__main__':
    main()
