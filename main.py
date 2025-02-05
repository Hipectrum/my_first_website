from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/twitter')
def twitter():
    return redirect("https://twitter.com/kullaniciadi")

@app.route('/facebook')
def facebook():
    return redirect("https://www.facebook.com/")

@app.route('/instagram')
def instagram():
    return redirect("https://www.instagram.com/")

@app.route('/linkedin')
def linkedin():
    return redirect("https://www.linkedin.com/")

@app.route('/dribbble')
def dribbble():
    return redirect("https://dribbble.com/")

@app.route('/pinterest')
def pinterest():
    return redirect("https://www.pinterest.com/kullaniciadi")

if __name__ == "__main__":
    app.run(debug=True)