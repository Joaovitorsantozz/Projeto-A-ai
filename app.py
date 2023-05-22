// para rodar digite  flask run
from flask import Flask, render_template, request,redirect

app = Flask(__name__)

REGISTRANTS={}
MODELS = [
   "Modelo 1",
   "Modelo 2",
   "Modelo 3",

]


#@app.route("/")
#def index():
 #  return render_template("index.html", models=MODELS)


#@app.route("/register", methods=["POST"])
#def register():

    #if not request.form.get("name") or request.form.get("model") not in MODELS:
     #   return render_template("failure.html")

    #return render_template("sucess.html")
    #

@app.route("/")
def index():
   return render_template("index.html", models=MODELS)

@app.route("/register", methods=["POST"])
def register():
   name = request.form.get("name")
   if not name:
      return render_template("error.html", message="Missing name")

   model = request.form.get("model")
   if not model:
      return render_template("error.html", message="Missing sport")
   if model not in MODELS:
      return render_template("error.html", message="Invalid sport")

   REGISTRANTS[name] = model

   return redirect("/registrants")


@app.route("/registrants")
def registrants():
   return render_template("registrants.html", registrants=REGISTRANTS)