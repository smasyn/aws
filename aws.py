from flask import Flask,render_template,redirect,url_for
app = Flask(__name__)

# test
@app.route('/')
def hello_world():
   return render_template("index_navbar.html")
   #return "Hello, World!"

@app.route('/change-language/<lang>')
def change_language(lang):
    print(f"language selected: {lang}")

    return redirect(url_for('index_navbar'))   

if __name__ == "__main__":
   app.run(host='0.0.0.0')