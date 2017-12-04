from flask import Flask
from flask import render_template

app = Flask(__name__)
app.debug = True


@app.route("/")
def landingPage():
    return render_template('index.html')

@app.route('/simulator', methods=['POST'])
def simulator():
    html = ""
    html += "<html>\n"
    html += "<body>\n"
    html += '<form method = "POST" action="form_input">\n'
    html += 'Enter name of movie: <input type="text" name="userInput" />\n'
    html += '<input type="submit" value="submit" />\n'
    html += "</form>\n"
    html += "</body>\n"
    html += "</html>\n"
    return html

@app.route("/decryptResult")
def decryptResult():
    return 1

@app.route("/encryptResult")
def encryptResult():
    return 1


if __name__ =="__main__":
    app.run()