
encryptionKey = {"a": 1, "b": 3, "c": 5, "d": 7,"e": 9, "f": 11,"g": 13,
"h": 15, "i": 17, "j": 19,"k": 21, "l": 23, "m": 25, "n": 27, "o": 29,
"p": 31, "q": 33, "r": 35, "s": 37, "t": 39, "u": 41,"v": 43,"w": 45,
"x": 47, "y": 49, "z": 51, " ":"@", ":":"#", ".":"$"}

readFile = open("info_security.txt","r")

writeFile = open("Encrypted_info_security.txt","w")

for character in readFile.read():
    writeFile.write(str(encryptionKey[character.lower()]))

writeFile.close()

readFile.close()
