from flask import Flask, render_template 

    
app = Flask(__name__) 
    
@app.route('/') 
def Content(): 
    with open('file1.txt', 'r') as f: 
        text = f.read()
       
        return render_template('content.html', text=text)



@app.route('/file2') 
def Content2(): 
    with open('file2.txt', 'r') as f: 
        text = f.read()
       
        return render_template('content.html', text=text)



@app.route('/file3') 
def Content3(): 
    with open('file3.txt', 'r') as f: 
        text = f.read()
       
        return render_template('content.html', text=text)

@app.route('/file4') 
def Content4(): 
    with open('file4.txt', errors="ignore") as f: 
        text = f.read()
       
        return render_template('content.html', text=text)

app.run(debug = False)