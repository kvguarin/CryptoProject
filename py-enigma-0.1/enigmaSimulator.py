from flask import Flask
from flask import request
from flask import render_template
from enigma.machine import EnigmaMachine

app = Flask(__name__)
app.debug = True


@app.route("/")
def landingPage():
    return render_template('index.html')


@app.route("/decryptSimulator", methods=['POST'])
def decryptSimulator():
    return render_template('decryptSimulator.html')


@app.route("/encryptSimulator", methods=['POST'])
def encryptSimulator():
    return render_template('encryptSimulator.html')


@app.route("/decryptResult", methods=['POST'])
def decryptResult():
    message = request.form['message']
    reflector = request.form['reflector'].upper()
    rotor1 = int(request.form['rotor1'])
    rotor2 = int(request.form['rotor2'])
    rotor3 = int(request.form['rotor3'])
    ringSetting1 = int(request.form['ringSetting1'])
    ringSetting2 = int(request.form['ringSetting2'])
    ringSetting3 = int(request.form['ringSetting3'])
    startingPosition1 = request.form['startingPosition1']
    startingPosition2 = request.form['startingPosition2']
    startingPosition3 = request.form['startingPosition3']
    messageKey = request.form['messageKey1'] + request.form['messageKey2'] + request.form['messageKey3']

    setDisplay = startingPosition1 + startingPosition2 + startingPosition3

    machine = EnigmaMachine.from_key_sheet(
        rotors=getRotor(rotor1, rotor2, rotor3),
        reflector=request.form['reflector'].upper(),
        ring_settings=[ringSetting1, ringSetting2, ringSetting3]
    )


    # set machine initial starting position
    machine.set_display(setDisplay)

    # decrypt the message key
    msg_key = machine.process_text(messageKey)

    # decrypt the cipher text with the unencrypted message key
    machine.set_display(msg_key)

    plaintext = machine.process_text(message)

    html = plaintext
    html = "<!DOCTYPE html>\n"
    html += "<html lang='en'>\n"
    html += "<head>\n"
    html += "<meta charset='UTF-8'>\n"
    html += "<title>Encrypted</title>\n"
    html += "</head>\n"
    html += "<body style='background-color:powderblue;'>\n"
    html += "<div>\n"
    html += "<p style='font-family: Courier;'>Plain Text: " + plaintext + "</p>\n"
    html += "</div>\n"
    html += "<div>\n"
    html += "<form method='POST' action='encryptSimulator'>\n"
    html += "<input style='width:150px; height:150px; font-size:100px;' type='submit' value='Encrypt'/>\n"
    html += "</form>\n"
    html += "<br/>\n"
    html += "<form method='POST' action='decryptSimulator'>\n"
    html += "<input style='width:150px; height:150px; font-size:100px;' type='submit' value='Decrypt'/>\n"
    html += "</form>\n"
    html += "</div>\n"
    html += "</body>"
    html += "</html>"
    return html


@app.route('/simulator', methods=['POST', 'GET'])
def simulator():
    return render_template('simulator.html')


def getRotor(rotor1, rotor2, rotor3):
    romNumRotors = ['0', 'I', 'II', 'III', 'IV', 'V']
    rotors = romNumRotors[rotor1] + " " + romNumRotors[rotor2] + " " + romNumRotors[rotor3]
    return rotors



@app.route("/encryptResult", methods=['POST'])
def encryptResult():
    message = request.form['message']
    reflector = request.form['reflector'].upper()
    rotor1 = int(request.form['rotor1'])
    rotor2 = int(request.form['rotor2'])
    rotor3 = int(request.form['rotor3'])
    ringSetting1 = int(request.form['ringSetting1'])
    ringSetting2 = int(request.form['ringSetting2'])
    ringSetting3 = int(request.form['ringSetting3'])
    startingPosition1 = request.form['startingPosition1']
    startingPosition2 = request.form['startingPosition2']
    startingPosition3 = request.form['startingPosition3']
    messageKey = request.form['messageKey1'] + request.form['messageKey2'] + request.form['messageKey3']

    setDisplay = startingPosition1 + startingPosition2 + startingPosition3

    machine = EnigmaMachine.from_key_sheet(
        rotors=getRotor(rotor1, rotor2, rotor3),
        reflector=request.form['reflector'].upper(),
        ring_settings=[ringSetting1, ringSetting2, ringSetting3]
    )


    # set machine initial starting position of rotors
    machine.set_display(setDisplay)

    #encrypt the key
    enc_key = machine.process_text(messageKey)

    # use message key
    machine.set_display(messageKey)

    cipherText = machine.process_text(message)

    html = "<!DOCTYPE html>\n"
    html += "<html lang='en'>\n"
    html += "<head>\n"
    html += "<meta charset='UTF-8'>\n"
    html += "<title>Encrypted</title>\n"
    html += "</head>\n"
    html += "<body style='background-color:powderblue;'>\n"
    html += "<div>\n"
    html+= "<p style='font-family: Courier;'>Cipher Text: " + cipherText + "</p>"
    html += "</div>\n"
    html += "<div>\n"
    html+= "<p style='font-family: Courier;'>Message Key: " + enc_key + "</p>"
    html += "</div>\n"
    html += "<div>\n"
    html += "<form method='POST' action='encryptSimulator'>\n"
    html += "<input style='width:150px; height:150px; font-size:100px;' type='submit' value='Encrypt'/>\n"
    html += "</form>\n"
    html += "<br/>\n"
    html += "<form method='POST' action='decryptSimulator'>\n"
    html += "<input style='width:150px; height:150px; font-size:100px;' type='submit' value='Decrypt'/>\n"
    html += "</form>\n"
    html += "</div>\n"
    html += "</body>"
    html += "</html>"
    return html


if __name__ =="__main__":
    app.run()