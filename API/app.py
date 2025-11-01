from flask import Flask, jsonify
from flask_cors import CORS
from routes.item_routes import item_bp
from routes.unidade_routes import unidade_bp
from routes.departamento_routes import departamento_bp
from routes.sala_routes import sala_bp
from routes.vistoria_routes import vistoria_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(vistoria_bp)
app.register_blueprint(item_bp)
app.register_blueprint(unidade_bp)
app.register_blueprint(departamento_bp)
app.register_blueprint(sala_bp)

@app.route("/")
def index():
    return jsonify({"status": "API de Inventário rodando 🚀"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
