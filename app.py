from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./src/view")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form ["num2"] != ""):
            return str(int(request.form["num1"]) + int(request.form ["num2"]))
        else:
            return "Informe um valor válido! ou preencha todos campos" 

@app.route("/<int:id>")
def Home_id(id):
    return str(id + 1)
    
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")


app.run(port=8081, debug=True)