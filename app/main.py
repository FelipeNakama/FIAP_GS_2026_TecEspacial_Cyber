import os
from flask import Flask, jsonify
 
app = Flask(__name__)
 
# Credencial injetada via variável de ambiente (NUNCA hardcoded)
# NASA_API_KEY = os.environ.get("NASA_API_KEY", "")

# Credencial Hardcoded para simular o erro: 
NASA_API_KEY = "nasa-secret-token-abc123XYZ"

@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "Space Debris Monitor"})
 
@app.route("/debris/count")
def debris_count():
    # Simulação — em prod, chamaria a API real com NASA_API_KEY
    return jsonify({"tracked_objects": 27000, "source": "Space-Track.org"})
 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

