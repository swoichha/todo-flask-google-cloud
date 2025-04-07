from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)
API_URL = "http://35.184.31.83:5000/api"  # Backend API base URL

@app.route("/")
def show_list():
    resp = requests.get(f"{API_URL}/items")
    return render_template('index.html', todolist=resp.json())

@app.route("/add", methods=['POST'])
def add_entry():
    requests.post(f"{API_URL}/add", json={
        'what_to_do': request.form['what_to_do'],
        'due_date': request.form['due_date']
    })
    return redirect(url_for('show_list'))

@app.route("/delete/<item>")
def delete_entry(item):
    requests.delete(f"{API_URL}/delete/{item}")
    return redirect(url_for('show_list'))

@app.route("/mark/<item>")
def mark_as_done(item):
    requests.put(f"{API_URL}/mark/{item}")
    return redirect(url_for('show_list'))

if __name__ == "__main__":
    app.run("0.0.0.0", port=5001)  # Different port than backend