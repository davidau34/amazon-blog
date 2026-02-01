#!/usr/bin/env python3
"""
Script para buscar productos trending en Amazon usando Product Advertising API
Alternativa: scraping básico o búsqueda manual para empezar
"""

import os
import sys
import json
import time
from datetime import datetime
from pathlib import Path

try:
    from dotenv import load_dotenv
    import requests
except ImportError:
    print("❌ Error: Instala dependencias con: pip install -r requirements.txt")
    sys.exit(1)

load_dotenv()

# Configuración
AMAZON_ACCESS_KEY = os.getenv('AMAZON_ACCESS_KEY')
AMAZON_SECRET_KEY = os.getenv('AMAZON_SECRET_KEY')
AMAZON_ASSOCIATE_ID = os.getenv('AMAZON_ASSOCIATE_ID')
AMAZON_REGION = os.getenv('AMAZON_REGION', 'es')  # España por defecto

# Cache de productos
CACHE_DIR = Path(__file__).parent.parent / '.cache'
CACHE_DIR.mkdir(exist_ok=True)
PRODUCTS_CACHE = CACHE_DIR / 'amazon_products.json'


class AmazonProductFinder:
    """
    Clase para buscar productos en Amazon
    
    NOTA: Para usar Amazon Product Advertising API necesitas:
    1. Registrarte en: https://affiliate-program.amazon.com/assoc_credentials/home
    2. Solicitar acceso a Product Advertising API
    3. Obtener Access Key y Secret Key
    
    Mientras tanto, este script usa una lista curada manualmente de productos populares
    """
    
    def __init__(self):
        self.cache = self.cargar_cache()
        print("✅ Finder de productos Amazon inicializado")
    
    def cargar_cache(self):
        """Carga productos desde cache"""
        if PRODUCTS_CACHE.exists():
            with open(PRODUCTS_CACHE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {}
    
    def guardar_cache(self):
        """Guarda productos en cache"""
        with open(PRODUCTS_CACHE, 'w', encoding='utf-8') as f:
            json.dump(self.cache, f, indent=2, ensure_ascii=False)
    
    def obtener_productos_nicho(self, nicho):
        """
        Obtiene productos populares de un nicho específico
        
        IMPORTANTE: Esta es una implementación básica con productos de ejemplo.
        Para producción, integra la Amazon Product Advertising API real.
        """
        
        # Base de datos de productos de ejemplo (actualizar con productos reales)
        productos_db = {
            'gadgets_tech': [
                {
                    'titulo': 'Auriculares Inalámbricos Bluetooth 5.3',
                    'asin': 'B0EXAMPLE1',
                    'precio': 29.99,
                    'rating': 4.5,
                    'reviews': 2547,
                    'categoria': 'Electrónica',
                    'keywords': ['auriculares', 'bluetooth', 'inalámbricos'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Auriculares'
                },
                {
                    'titulo': 'Power Bank 20000mAh Carga Rápida',
                    'asin': 'B0EXAMPLE2',
                    'precio': 24.99,
                    'rating': 4.6,
                    'reviews': 1823,
                    'categoria': 'Electrónica',
                    'keywords': ['power bank', 'batería externa', 'carga rápida'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=PowerBank'
                },
                {
                    'titulo': 'Webcam Full HD 1080p con Micrófono',
                    'asin': 'B0EXAMPLE3',
                    'precio': 39.99,
                    'rating': 4.4,
                    'reviews': 956,
                    'categoria': 'Informática',
                    'keywords': ['webcam', 'cámara web', '1080p'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Webcam'
                }
            ],
            'fitness': [
                {
                    'titulo': 'Set Bandas de Resistencia 5 Niveles',
                    'asin': 'B0EXAMPLE4',
                    'precio': 19.99,
                    'rating': 4.7,
                    'reviews': 3421,
                    'categoria': 'Deportes',
                    'keywords': ['bandas resistencia', 'fitness', 'ejercicio'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Bandas'
                },
                {
                    'titulo': 'Esterilla Yoga Antideslizante Premium',
                    'asin': 'B0EXAMPLE5',
                    'precio': 27.99,
                    'rating': 4.6,
                    'reviews': 1567,
                    'categoria': 'Deportes',
                    'keywords': ['esterilla', 'yoga', 'pilates'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Esterilla'
                },
                {
                    'titulo': 'Pesas Ajustables 20kg Set Completo',
                    'asin': 'B0EXAMPLE6',
                    'precio': 89.99,
                    'rating': 4.5,
                    'reviews': 892,
                    'categoria': 'Deportes',
                    'keywords': ['pesas', 'mancuernas', 'gimnasio casa'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Pesas'
                }
            ],
            'cocina': [
                {
                    'titulo': 'Freidora de Aire 5L Digital',
                    'asin': 'B0EXAMPLE7',
                    'precio': 79.99,
                    'rating': 4.8,
                    'reviews': 4521,
                    'categoria': 'Hogar y Cocina',
                    'keywords': ['freidora aire', 'airfryer', 'cocina'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Freidora'
                },
                {
                    'titulo': 'Batidora Amasadora 1000W Profesional',
                    'asin': 'B0EXAMPLE8',
                    'precio': 129.99,
                    'rating': 4.7,
                    'reviews': 2156,
                    'categoria': 'Hogar y Cocina',
                    'keywords': ['batidora', 'amasadora', 'repostería'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Batidora'
                },
                {
                    'titulo': 'Set Cuchillos Profesionales 8 Piezas',
                    'asin': 'B0EXAMPLE9',
                    'precio': 49.99,
                    'rating': 4.6,
                    'reviews': 1234,
                    'categoria': 'Hogar y Cocina',
                    'keywords': ['cuchillos', 'set cuchillos', 'cocina'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Cuchillos'
                }
            ],
            'mascotas': [
                {
                    'titulo': 'Comedero Automático Programable Mascotas',
                    'asin': 'B0EXAMPLE10',
                    'precio': 54.99,
                    'rating': 4.5,
                    'reviews': 1876,
                    'categoria': 'Mascotas',
                    'keywords': ['comedero automático', 'mascotas', 'gatos perros'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Comedero'
                },
                {
                    'titulo': 'Rascador para Gatos 3 Niveles',
                    'asin': 'B0EXAMPLE11',
                    'precio': 39.99,
                    'rating': 4.7,
                    'reviews': 2341,
                    'categoria': 'Mascotas',
                    'keywords': ['rascador', 'gatos', 'árbol gatos'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Rascador'
                },
                {
                    'titulo': 'Fuente Agua para Gatos Filtrada',
                    'asin': 'B0EXAMPLE12',
                    'precio': 32.99,
                    'rating': 4.6,
                    'reviews': 1654,
                    'categoria': 'Mascotas',
                    'keywords': ['fuente agua', 'bebedero gatos', 'mascotas'],
                    'imagen': 'https://via.placeholder.com/500x500.png?text=Fuente'
                }
            ]
        }
        
        return productos_db.get(nicho, [])
    
    def generar_url_afiliado(self, asin):
        """Genera URL de afiliado de Amazon"""
        base_urls = {
            'es': 'https://www.amazon.es/dp/',
            'com': 'https://www.amazon.com/dp/',
            'uk': 'https://www.amazon.co.uk/dp/',
            'de': 'https://www.amazon.de/dp/',
            'fr': 'https://www.amazon.fr/dp/',
        }
        
        base_url = base_urls.get(AMAZON_REGION, base_urls['es'])
        return f"{base_url}{asin}?tag={AMAZON_ASSOCIATE_ID}"
    
    def buscar_productos_trending(self, categoria, limit=10):
        """
        Busca productos trending en una categoría
        
        TODO: Implementar búsqueda real con Amazon Product Advertising API
        Por ahora retorna productos de ejemplo
        """
        print(f"🔍 Buscando productos trending en: {categoria}")
        
        productos = self.obtener_productos_nicho(categoria)
        
        # Simular delay de API
        time.sleep(0.5)
        
        # Agregar URLs de afiliado
        for producto in productos[:limit]:
            producto['url_afiliado'] = self.generar_url_afiliado(producto['asin'])
            producto['ultima_actualizacion'] = datetime.now().isoformat()
        
        # Guardar en cache
        self.cache[categoria] = {
            'productos': productos[:limit],
            'fecha_actualizacion': datetime.now().isoformat()
        }
        self.guardar_cache()
        
        print(f"✅ Encontrados {len(productos[:limit])} productos")
        return productos[:limit]
    
    def obtener_detalles_producto(self, asin):
        """
        Obtiene detalles de un producto específico
        
        TODO: Implementar con Amazon Product Advertising API
        """
        # Por ahora busca en todos los nichos
        for nicho_key, nicho_data in self.cache.items():
            if 'productos' in nicho_data:
                for producto in nicho_data['productos']:
                    if producto['asin'] == asin:
                        return producto
        
        return None
    
    def exportar_productos_json(self, output_file='productos_amazon.json'):
        """Exporta todos los productos a JSON"""
        output_path = Path(__file__).parent.parent / output_file
        
        todos_productos = []
        for nicho_data in self.cache.values():
            if 'productos' in nicho_data:
                todos_productos.extend(nicho_data['productos'])
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(todos_productos, f, indent=2, ensure_ascii=False)
        
        print(f"📄 Productos exportados a: {output_path}")
        return output_path


def main():
    """Función principal"""
    print("🛍️  Buscador de Productos Amazon\n")
    print("=" * 60)
    
    finder = AmazonProductFinder()
    
    # Buscar productos en todos los nichos
    nichos = ['gadgets_tech', 'fitness', 'cocina', 'mascotas']
    
    for nicho in nichos:
        productos = finder.buscar_productos_trending(nicho, limit=5)
        print(f"\n📦 {nicho.upper()}:")
        for i, prod in enumerate(productos, 1):
            print(f"   {i}. {prod['titulo']} - €{prod['precio']}")
            print(f"      ⭐ {prod['rating']} ({prod['reviews']} reviews)")
            print(f"      🔗 {prod['url_afiliado'][:60]}...")
    
    # Exportar a JSON
    print("\n" + "=" * 60)
    finder.exportar_productos_json()
    
    print("\n✅ Proceso completado")
    print("\n💡 Próximos pasos:")
    print("   1. Actualiza los ASINs con productos reales de Amazon")
    print("   2. Solicita acceso a Amazon Product Advertising API")
    print("   3. Implementa búsqueda real de productos")


if __name__ == "__main__":
    main()
