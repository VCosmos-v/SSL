from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
@app.route("/SSL")
def SSL():
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title>SSL</title>
    </head>
    <body class="bg-black">
    <div class="wrapper">
        <div style="display:grid; background-color:white; width:1440px; height:2000px; margin-left:auto; margin-right:auto; position:relative">
            <div class="overflow-hidden" style="position:absolute; z-index:10;"><img src="/static/main/nv.png" style="width:100%; height:100%;"></div>
            <div class="overflow-hidden" style="margin-top:-155px ;position:absolute; z-index:9; top:-155px;"><img src="/static/main/background.jpg" style="width:100%; height:100%;"></div>
            <div class="overflow-hidden" style="position:absolute; z-index:9; top:19%; left:11.5%"><img src="/static/main/background_2.png" style="width:100%; height:100%;"></div>
            <div class="overflow-hidden" style="margin-left:11%; margin-right:0%; margin-top:26%; position:absolute; z-index:7;"><img src="/static/main/background_3.png" style="width:100%; height:100%;"></div>
            <div class="overflow-hidden" style="margin-left:25%; margin-right:25%; position:absolute; z-index:10; top:4%;"><img src="/static/main/SSL.png" style="width:100% height:100%" style=""></div>
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(port="8080")