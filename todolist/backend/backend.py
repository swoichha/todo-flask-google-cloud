from flask import Flask, jsonify, request, g
import sqlite3

DATABASE = 'todolist.db'
app = Flask(__name__)
app.config.from_object(__name__)

# Database helpers (same as original)
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(app.config['DATABASE'])
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# API Endpoints
@app.route("/api/items", methods=['GET'])
def get_items():
    db = get_db()
    cur = db.execute('SELECT what_to_do, due_date, status FROM entries')
    entries = cur.fetchall()
    return jsonify([dict(what_to_do=row[0], due_date=row[1], status=row[2]) for row in entries])

@app.route("/api/add", methods=['POST'])
def add_item():
    db = get_db()
    data = request.get_json()
    db.execute('INSERT INTO entries (what_to_do, due_date) VALUES (?, ?)', 
               [data['what_to_do'], data['due_date']])
    db.commit()
    return jsonify({"status": "success"}), 201

@app.route("/api/delete/<item>", methods=['DELETE'])
def delete_item(item):
    db = get_db()
    db.execute("DELETE FROM entries WHERE what_to_do=?", (item,))
    db.commit()
    return jsonify({"status": "deleted"})

@app.route("/api/mark/<item>", methods=['PUT'])
def mark_item(item):
    db = get_db()
    db.execute("UPDATE entries SET status='done' WHERE what_to_do=?", (item,))
    db.commit()
    return jsonify({"status": "marked as done"})

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)  # Different port than frontend