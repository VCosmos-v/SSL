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
                           milky=url_for("Milkyway"),
                           nothing=url_for("Nothing"),
                           earth=url_for("Earth")
                           )

@app.route("/Milkyway")
def Milkyway():
    f = [i.rstrip() for i in open("static/Milkyway/text.csv", encoding="utf8").readlines()]
    return render_template("Milkyway.html",
                           cs="/static/css/style.css",
                           title="Млечный путь",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Cтатью подготовила Лузгина Елизавета",
                           image1="/static/Milkyway/images/1.png",
                           image2="/static/Milkyway/images/2.png",
                           image3="/static/Milkyway/images/3.png",
                           image4="/static/Milkyway/images/4.png",
                           image5="/static/Milkyway/images/5.png",
                           image6="/static/Milkyway/images/6.png",
                           back=url_for("SSL")
                           )

@app.route("/Nothing")
def Nothing():
    f = [i.rstrip() for i in open("static/nothing/text.csv", encoding="utf8").readlines()]
    return render_template("nothing.html",
                           cs="/static/css/style.css",
                           title="Ничего нет",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Константин Циолковский\n 1932 г.",
                           back=url_for("SSL")
                           )

@app.route("/Earth")
def Earth():
    f = [i.rstrip() for i in open("static/Earth/text.csv", encoding="utf8").readlines()]
    return render_template("earth.html",
                           cs="/static/css/style.css",
                           title="Земля",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Cтатью подготовила Осташова Полина",
                           image1="/static/Earth/images/1.png",
                           image2="/static/Earth/images/2.png",
                           image3="/static/Earth/images/3.png",
                           image4="/static/Earth/images/4.png",
                           image5="/static/Earth/images/5.png",
                           image6="/static/Earth/images/6.png",
                           back=url_for("SSL")
                           )


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)