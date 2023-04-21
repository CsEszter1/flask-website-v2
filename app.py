from flask import Flask, render_template, jsonify  # from flask modul import Flask class 

app = Flask(__name__)   # app is the object of the class flask, import flask functionality

JOBS = [
  {
    'id': 1,
    'title': 'Research Assistant',
    'location': 'Frankfurt, Germany',
    'salary': '1000 euro'
  },
  {
    'id': 2,
    'title': 'Group Leader',
    'location': 'Oslo, Norway',
    
  },
  {
    'id': 3,
    'title': 'Research Fellow',
    'location': 'Berlin., Germany',
    'salary': '2200 euro'
  }
]
@app.route("/")
def hello_science():
  return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
