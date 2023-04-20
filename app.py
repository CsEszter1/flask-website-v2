from flask import Flask  # from flask modul import Flask class 

app = Flask(__name__)   # app is the object of the class flask, import flask functionality
@app.route("/")
def hello_world():
  return "Hello, world"

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
