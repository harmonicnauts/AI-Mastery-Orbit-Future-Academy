# =[Modules dan Packages]========================

from flask import Flask,render_template
from flask_ngrok import run_with_ngrok

# =[Variabel Global]=============================

app   = Flask(__name__)

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('cv.html')

@app.route("/Muzero_Rachmat")
def ea():
    return "Ea Ea Ea Ea"


# =[Main]========================================

if __name__ == '__main__':
    # Run Flask di localhost 
    run_with_ngrok(app)
    app.run()


