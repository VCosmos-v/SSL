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
                           earth=url_for("Earth"),
                           mars=url_for("Mars"),
                           mercury=url_for("Mercury"),
                           neptun=url_for("Neptun"),
                           # uran=url_for("Uran"),
                           jupiter=url_for("Jupiter"),
                           halley=url_for("Halley"),
                           neutron=url_for("Neutron"),
                           blackhole=url_for("Blackhole")
                           )

@app.route("/Milkyway")
def Milkyway():
    f = [i.rstrip() for i in open("static/Milkyway/text.csv", encoding="utf8").readlines()]
    return render_template("Milkyway.html",
                           cs="/static/css/style.css",
                           height=2886,
                           width=1440,
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
                           height=2886,
                           width=1440,
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
                           height=2800,
                           width=1440,
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

@app.route("/Mars")
def Mars():
    f = [i.rstrip() for i in open("static/Mars/text.csv", encoding="utf8").readlines()]
    return render_template("mars.html",
                           cs="/static/css/style.css",
                           height=2350,
                           width=1440,
                           title="Марс",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовил Кустов Кирилл",
                           image1="/static/Mars/images/1.jpg",
                           image2="/static/Mars/images/2.jpg",
                           image3="/static/Mars/images/3.jpg",
                           image4="/static/Mars/images/4.jpg",
                           image5="/static/Mars/images/5.jpg",
                           back=url_for("SSL")
                           )

@app.route("/Mercury")
def Mercury():
    f = [i.rstrip() for i in open("static/Mercury/text.csv", encoding="utf8").readlines()]
    return render_template("mercury.html",
                           cs="/static/css/style.css",
                           height=1600,
                           width=1440,
                           title="Меркурий",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовил Пальцев Елисей",
                           image1="/static/Mercury/images/1.jpeg",
                           image2="/static/Mercury/images/2.jpg",
                           back=url_for("SSL")
                           )

@app.route("/Neptun")
def Neptun():
    f = [i.rstrip() for i in open("static/Neptun/text.csv", encoding="utf8").readlines()]
    return render_template("neptun.html",
                           cs="/static/css/style.css",
                           height=3700,
                           width=1440,
                           title="Нептун",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовил Чернов Тимофей",
                           image1="/static/Neptun/images/1.png",
                           image2="/static/Neptun/images/2.png",
                           image3="/static/Neptun/images/3.png",
                           image4="/static/Neptun/images/4.png",
                           image5="/static/Neptun/images/5.png",
                           image6="/static/Neptun/images/6.png",
                           back=url_for("SSL")
                           )

@app.route("/Neutron")
def Neutron():
    f = [i.rstrip() for i in open("static/Neutron/text.csv", encoding="utf8").readlines()]
    return render_template("neutron.html",
                           cs="/static/css/style.css",
                           height=3300,
                           width=1440,
                           title="Нейтронные звезды (Пульсары)",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовила Барабанова Юлия",
                           image1="/static/Neutron/images/1.jpeg",
                           image2="/static/Neutron/images/2.jpeg",
                           image3="/static/Neutron/images/3.jpeg",
                           back=url_for("SSL")
                           )

@app.route("/Jupiter")
def Jupiter():
    f = [i.rstrip() for i in open("static/Jupiter/text.csv", encoding="utf8").readlines()]
    return render_template("jupiter.html",
                           cs="/static/css/style.css",
                           height=4200,
                           width=1440,
                           title="Юпитер",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовил Мехоношин Алексей",
                           image1="/static/Jupiter/images/1.png",
                           image2="/static/Jupiter/images/2.jpg",
                           back=url_for("SSL")
                           )

@app.route("/Halley")
def Halley():
    f = [i.rstrip() for i in open("static/Halley/text.csv", encoding="utf8").readlines()]
    return render_template("halley.html",
                           cs="/static/css/style.css",
                           height=2200,
                           width=1440,
                           title="Комета Галлея",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовила Михеева Елизавета",
                           image1="/static/Halley/images/1.jpg",
                           back=url_for("SSL")
                           )

@app.route("/Blackhole")
def Blackhole():
    f = [i.rstrip() for i in open("static/Blackhole/text.csv", encoding="utf8").readlines()]
    return render_template("blackhole.html",
                           cs="/static/css/style.css",
                           height=2000,
                           width=1440,
                           title="Чёрная дыра",
                           nv="/static/about/nv.png",
                           bt="/static/about/bt.jpg",
                           text=f,
                           creator="Статью подготовила Плюснина Юлия",
                           image1="/static/Blackhole/images/1.jpg",
                           image2="/static/Blackhole/images/2.jpg",
                           back=url_for("SSL")
                           )

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)