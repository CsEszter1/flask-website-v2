from flask import Flask, render_template, jsonify  # from flask modul import Flask class 
from database import load_jobs_from_db


app = Flask(__name__)   # app is the object of the class flask, import flask functionality



@app.route("/")
def hello_science():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs)


@app.route("/api/jobs")
def list_jobs():
  jobs = load_jobs_from_db()
  return jsonify(jobs)
  

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
