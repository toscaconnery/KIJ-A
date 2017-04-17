#Tosca Yoel Connery
#5114100061
#KIJ A
from operator import xor

def encrypt(atext, asecr):
    hasil = [None] * len(atext)
    charhasil = [None] * len(atext)

    #Menentukan Leftmost secret key dan Rightmost secret key
    lsecret = [None] * 4
    rsecret = [None] * 4
    for i in range(0,4):
        lsecret[i] = asecr[i]
        rsecret[i] = asecr[i+4]

    #Melakukan proses xor antara p dan k0
    idx = 0
    jumlahblok = len(atext) / 4
    for i in range(0, jumlahblok):
        for j in range(0, 4):
            hasil[idx] = xor(atext[idx],lsecret[j])
            idx += 1

    #Melakukan proses add antara hasil proses sebelumnya dengan k1, kemudian di modulo
    idx = 0
    for i in range(0, jumlahblok):
        for j in range(0, 4):
            hasil[idx] = hasil[idx] + rsecret[j]
            #Modulo terhadap 32 bit oleh 64 bit tidak akan mengubah nilai
            hasil[idx] = hasil[idx] % 256
            idx += 1

    #Mengubah ke karakter
    hasilencrypt = ''
    for i in range(0,len(atext)):
        charhasil[i] = chr(hasil[i])
        hasilencrypt += str(charhasil[i])

    hasilsemua = [None] * 2
    hasilsemua[0] = hasil
    hasilsemua[1] = hasilencrypt
    hasil2 = decrypt(hasil, asecr)
    print "Hasil2", hasil2

    file = open("hasilencrypt.txt","w")
    file.write("Hasil encrypt : ")
    file.write(hasilencrypt)
    file.write("\r\nASCII : ")
    for i in range(0, len(hasil)):
        file.write(str(hasil[i]))
        file.write(" ")
    file.close()

    return hasilsemua

def decrypt(atext, asecr):
    # Menentukan Leftmost secret key dan Rightmost secret key
    lsecret = [None] * 4
    rsecret = [None] * 4
    for i in range(0, 4):
        lsecret[i] = asecr[i]
        rsecret[i] = asecr[i + 4]

    jumlahblok = len(atext) / 4
    #Mengubah dari string ke array
    hasil = [None] * len(atext)
    for i in range(0, len(atext)):
        hasil[i] = atext[i]

    #Proses mengembalikan add dan modulo 2^64,
    """2^64 jauh lebih panjang dari 8 bit karakter sehingga
    hasil modulo tidak akan mempengaruhi nilai dari 32 bit
    data yg akan diproses"""
    idx = 0
    for i in range(0,jumlahblok):
        for j in range(0, 4):
            hasil[idx] = hasil[idx] - rsecret[j]
            idx += 1

    #Proses mengembalikan dari xor
    idx = 0
    for i in range(0,jumlahblok):
        for j in range(0, 4):
            hasil[idx] = xor(hasil[idx], lsecret[j])
            idx += 1

    #Mengembalikan ke bentuk string
    hasildecrypt = ''
    hasilchar = [None] * len(atext)
    print "DEBUG : ", hasil
    for i in range(0, len(atext)):
        if hasil[i] >= 0:
            hasilchar[i] = chr(hasil[i])
            hasildecrypt += str(hasilchar[i])

    hasilsemua = [None] * 2
    hasilsemua[0] = hasil
    hasilsemua[1] = hasildecrypt

    file = open("hasildecrypt.txt","w")
    file.write("Hasil decrypt : ")
    file.write(hasildecrypt)
    file.write("\r\nASCII : ")
    for i in range(0, len(hasil)):
        file.write(str(hasil[i]))
        file.write(" ")
    file.close()

    return hasilsemua


"""MAIN PROGRAM"""

#Secret key
print "Enter the 64 bits secret key (8 letters): "
secret = raw_input("Secret key: ")
panjangsecret = len(secret)
#Mengonversikan secret key ke ascii
asciisecret = [None] * panjangsecret
for i in range(0, panjangsecret):
    asciisecret[i] = ord(secret[i])

#Text
print "Enter the text: "
text = raw_input("Text: ")
panjang = len(text)
panjangdata = panjang

print "1) Encrypt"
print "2) Decrypt"
pilihan = raw_input("Choose: " )

#Menentukan panjang karakter yang akan diproses, membuatnya sesuai dengan 32 bit block
if panjang % 4 > 0:
    sisa = 4 - (panjang % 4)
    panjangdata = panjang + sisa
textdata = [None] * panjangdata
for i in range(0, panjangdata):
    if i < panjang:
        textdata[i] = text[i]
    else:
        textdata[i] = " "

#Mengonversikan string ke ascii
asciitext = [None] * panjangdata
for i in range(0, panjangdata):
    asciitext[i] = ord(textdata[i])

if pilihan == '1':
    hasil = encrypt(asciitext, asciisecret)
    print "ASCII: ", hasil[0]
    print "Cypher: ", hasil[1]
elif pilihan == '2':
    hasil = decrypt(asciitext, asciisecret)
    print "ASCII: ", hasil[0]
    print "Plaintext: ", hasil[1]

#Testing Auto Decrypt
#asciihasil = [None] * len(hasil)
#for i in range(0, len(asciihasil)):
#    asciihasil[i] = ord(hasil[i])
#hasil2 = decrypt(asciihasil, asciisecret)
#print hasil2

























#secretkey = "lima"

#print "Plaintext:", plaintext
#print "Secret key:", secretkey

#bplaintext = map(bin,bytearray(plaintext))
#bsecretkey = map(bin,bytearray(secretkey))

#print "Binary Plaintext:", bplaintext
#print "Binary Secretkey:", bsecretkey

#a = ord(plaintext[0])
#b = ord(plaintext[1])
#c = ord(plaintext[2])
#d = ord(plaintext[3])

#print "a b c d", a, b, c, d

#ba = a ^ b
#ba = xorvalue(a,b)
#print ba

#binplaintext = map(bin,bytearray(plaintext))
#print "Ini output ", binplaintext




