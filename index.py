from flask import Flask, render_template, request, jsonify, send_from_directory
import json
import os
from datetime import datetime

app = Flask(__name__)

# Perfume data (you can expand this)
PERFUMES = {
    "1": {
        "name": "Luxe Noir",
        "price": "$89.99",
        "description": "A seductive blend of black vanilla, amber, and musk. Perfect for evening allure.",
        "image": "luxe_noir.jpg",
        "notes": ["Black Vanilla", "Amber", "Musk", "Sandalwood"],
        "rating": 4.8
    },
    "2": {
        "name": "Ocean Breeze",
        "price": "$69.99",
        "description": "Fresh aquatic notes with citrus and marine accords. Ideal for daytime freshness.",
        "image": "ocean_breeze.jpg",
        "notes": ["Bergamot", "Marine Accord", "Jasmine", "Cedarwood"],
        "rating": 4.6
    },
    "3": {
        "name": "Rose Eternal",
        "price": "$79.99",
        "description": "Timeless rose bouquet with fruity and woody undertones. Romantic and elegant.",
        "image": "rose_eternal.jpg",
        "notes": ["Damask Rose", "Peach", "Patchouli", "Vetiver"],
        "rating": 4.9
    }
}

@app.route('/')
def home():
    return render_template('index.html', perfumes=PERFUMES)

@app.route('/perfume/<perfume_id>')
def perfume_detail(perfume_id):
    perfume = PERFUMES.get(perfume_id)
    if not perfume:
        return "Perfume not found", 404
    return render_template('perfume.html', perfume=perfume, perfume_id=perfume_id)

@app.route('/generate-link')
def generate_link():
    perfume_id = request.args.get('id')
    if perfume_id:
        link = f"https://{request.host}/{perfume_id}"
        return jsonify({
            "success": True,
            "shareable_link": link,
            "message": f"Share this link for {PERFUMES[perfume_id]['name']}"
        })
    return jsonify({"success": False, "message": "No perfume ID provided"})

@app.route('/api/perfumes')
def api_perfumes():
    return jsonify(PERFUMES)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)