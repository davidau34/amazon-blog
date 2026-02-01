#!/bin/bash
echo "🧪 Probando workflow localmente..."
echo ""
echo "1️⃣ Generando artículo..."
python3 scripts/generate_article.py
echo ""
echo "2️⃣ Actualizando productos..."
python3 scripts/amazon_products.py || echo "⚠️ Paso opcional - continuando..."
echo ""
echo "3️⃣ Compartiendo en Twitter..."
python3 scripts/twitter_share.py || echo "⚠️ Paso opcional - continuando..."
echo ""
echo "✅ Test completado - todos los pasos ejecutados"
