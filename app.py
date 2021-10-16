from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", defaults={"id": None})
@app.route("/<id>")
def Content(id):

    with open("file1.txt", "r") as f1, open("file1.txt", "r") as f2:
        text = f1.readlines()
        full_text = f2.read()
        if id != None:

            for text in text:
                if id in text[0:4]:
                    print(True)
                    text = text
                    return render_template("content.html", text=text)
                    break
        else:
            return render_template("content.html", text=full_text)


@app.route("/file2", defaults={"id": None})
@app.route("/file2/<id>")
def Content2(id):
    with open("file2.txt", "r") as f1, open("file2.txt", "r") as f2:
        text = f1.readlines()
        full_text = f2.read()
        if id != None:
   

            for text in text:

                if id in text[0:4]:
                    print(text[0:4])
                    print("id:", id)
                    print(True)
                    text = text

                    return render_template("content.html", text=text)
                    print("break")

        else:
            return render_template("content.html", text=full_text)


@app.route("/file3")
def Content3():
    with open("file3.txt", "r") as f:
        text = f.read()

        return render_template("content.html", text=text)


@app.route("/file4")
def Content4(id):
    with open("file4.txt", errors="ignore") as f:
        text = f.read()

        return render_template("content.html", text=text)


app.run(debug=True)
