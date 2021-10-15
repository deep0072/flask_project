from flask import Flask, render_template


app = Flask(__name__)


@app.route(f"/<id>")
def Content(id):

    with open("file1.txt", "r") as f1, open("file1.txt", "r") as f2:

        text = f1.readlines()
        full_text = f2.read()

        # for text in text:
        #     if id in text[0:2]:
        #         print(text[0:2])
        #         print(True)
        #         text = text
        #
        #
        final_text = ""
        print(id[0], id[len(id) - 1])
        for line_number, text in enumerate(text):

            if line_number == int(id[0]):
                final_text.append(text)

            if line_number == int(id[len(id) - 1]):
                final_text.append(text)

        text = final_text

    return render_template("content.html", text=text)


@app.route("/file2")
def Content2():
    with open("file2.txt", "r") as f:
        text = f.read()

        return render_template("content.html", text=text)


@app.route("/file3")
def Content3():
    with open("file3.txt", "r") as f:
        text = f.read()

        return render_template("content.html", text=text)


@app.route("/file4")
def Content4():
    with open("file4.txt", errors="ignore") as f:
        text = f.read()

        return render_template("content.html", text=text)


app.run(debug=False)
