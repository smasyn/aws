from flask import Flask,render_template
app = Flask(__name__)

# test
@app.route('/')
def hello_world():
   return render_template("index_navbar.html")
   #return "Hello, World!"

if __name__ == "__main__":
   app.run(host='0.0.0.0')