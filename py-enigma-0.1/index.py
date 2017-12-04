from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def landingPage():
    return render_template('index.html')

@app.route('/simulator', methods=['POST'])
def simulator():
    html = "hello"
    # html += "<html>\n"
    # html += "<body>\n"
    # html += '<form method = "POST" action="form_input">\n'
    # html += 'Enter name of movie: <input type="text" name="userInput" />\n'
    # html += '<input type="submit" value="submit" />\n'
    # html += "</form>\n"
    # html += "</body>\n"
    # html += "</html>\n"
    return html

@app.route("/decryptResult", methods=['POST'])
def decryptResult():
    rotor1 = request.form['rotor1']


    return 1

@app.route("/encryptResult", methods=['POST'])
def encryptResult():
    return 1


if __name__ =="__main__":
    app.run()