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
    rotor2 = request.form['rotor2']
    rotor3 = request.form['rotor3']
    reflector = request.form['reflector']
    ringSetting1 = request.form['ringSetting1']
    ringSetting2 = request.form['ringSetting2']
    ringSetting3 = request.form['ringSetting3']
    startingPosition1 = request.form['startingPosition1']
    startingPosition2 = request.form['startingPosition2']
    startingPosition3 = request.form['startingPosition3']



    return 1

@app.route("/encryptResult", methods=['POST'])
def encryptResult():
    return 1


if __name__ =="__main__":
    app.run()