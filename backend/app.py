from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Enterprise DevSecOps Platform"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/users")
def users():
    conn = psycopg2.connect(
        host="postgres",
        database="enterprise",
        user="admin",
        password="admin123"
    )

    cur = conn.cursor()

    cur.execute("SELECT * FROM users")

    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify(rows)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)