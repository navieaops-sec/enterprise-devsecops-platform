from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

# PostgreSQL connection (Docker service name = db)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'postgresql://postgres:postgres@db:5432/devsecops'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model (table)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

# Health check
@app.route('/')
def home():
    return {"message": "Backend connected to PostgreSQL"}

# CREATE
@app.route('/add', methods=['POST'])
def add_user():
    data = request.json
    user = User(name=data['name'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User added"})

# READ
@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name} for u in users])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=5000)