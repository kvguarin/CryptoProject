from enigma.machine import EnigmaMachine

# setup machine according to specs from a daily key sheet:

machine = EnigmaMachine.from_key_sheet(
       rotors='II IV V',
       reflector='B',
       ring_settings=[1, 20, 11],
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

# set machine initial starting position
machine.set_display('WXC')

# decrypt the message key
msg_key = machine.process_text('KCH')
# decrypt the cipher text with the unencrypted message key
machine.set_display(msg_key)


ciphertext = 'NIBLFMYMLLUFWCASCSSNVHAZ'
plaintext = machine.process_text(ciphertext)

print(plaintext)


print("DECRYPT THE MESSAGE")
machine2 = EnigmaMachine.from_key_sheet(
       rotors='II IV V',
       reflector='B',
       ring_settings=[1, 20, 11],
       plugboard_settings='AV BS CG DL FU HZ IN KM OW RX')

# set machine initial starting position
machine2.set_display('WXC')

# encrypt message key
enc_key = machine2.process_text('BLA')
# use message key BLA
machine2.set_display('BLA')
ciphertext = machine2.process_text('THEXRUSSIANSXAREXCOMINGX')
print(ciphertext)
