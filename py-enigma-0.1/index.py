from flask import Flask
from flask import request
from flask import render_template
from enigma.machine import EnigmaMachine

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
    messageKey = request.form['messageKey']
    message = request.form['message']

    rotors = getRotor(rotor1, rotor2, rotor3)
    ringSettings = [ringSetting1, ringSetting2, ringSetting3]
    setDisplay = startingPosition1 + startingPosition2 + startingPosition3

    machine = EnigmaMachine.from_key_sheet(
        rotors,
        reflector,
        ringSettings
    )

    # set machine initial starting position
    machine.set_display(setDisplay)

    # decrypt the message key
    msg_key = machine.process_text(messageKey)

    # decrypt the cipher text with the unencrypted message key
    machine.set_display(msg_key)

    plaintext = machine.process_text(message)

    html = plaintext
    return html

def getRotor(rotor1, rotor2, rotor3):
    romNumRotors = ['0', 'I', 'II', 'III', 'IV', 'V']
    rotors = romNumRotors[rotor1] + " " + romNumRotors[rotor2] + " " + romNumRotors[rotor3]
    return rotors



@app.route("/encryptResult", methods=['POST'])
def encryptResult():
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
    messageKey = request.form['messageKey']
    message = request.form['message']

    rotors = getRotor(rotor1, rotor2, rotor3)
    ringSettings = [ringSetting1, ringSetting2, ringSetting3]
    setDisplay = startingPosition1 + startingPosition2 + startingPosition3

    machine = EnigmaMachine.from_key_sheet(
        rotors,
        reflector,
        ringSettings
    )
    # set machine initial starting position
    machine.set_display(setDisplay)

    #encrypt the key
    enc_key = machine.process_text('messageKey')

    cipherText = machine.process_text(message)

    html = "Cipher Text:" + cipherText
    html += "\n"
    html += "Key: " + enc_key
    return 1


if __name__ =="__main__":
    app.run()