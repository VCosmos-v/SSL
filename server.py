from flask import Flask, render_template,url_for
import os

app = Flask(__name__)

@app.route("/")
@app.route("/SSL")
def SSL():
    return render_template("main.html",
                           cs="/static/css/style.css",
                           nv="/static/main/nv.png",
                           bg="/static/main/background.jpg",
                           bg2="/static/main/background_2.png",
                           bg3="/static/main/background_3.png",
                           ssl="/static/main/SSL.png",
                           astrob="/static/main/astroobject_1.jpg",
                           astrob2="/static/main/astroobject_2.jpg",
                           astrob3="/static/main/astroobject_3.jpg",
                           astrob4="/static/main/astroobject_4.jpg",
                           astrob5="/static/main/astroobject_5.jpg",
                           astrob6="/static/main/astroobject_6.jpg",
                           bottom="static/main/nv_bottom.jpg",
                           milky=url_for("Milkyway")
                           )

@app.route("/Milkyway")
def Milkyway():
    return render_template("about.html",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           back=url_for("SSL")
                           )

@app.route("/Nothing")
def Nothing():
    return render_template("about.html",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           back=url_for("SSL")
                           )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)