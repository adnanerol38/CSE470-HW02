import string

#Kullanicidan sifrelenecek metinin alinmasi
plainText = raw_input("What is your plaintext? ")

#Kullanicidan sifrelenecek metinin kac harf ileri shift edileceginin alinmasi
shift = int(raw_input("What is your shift? "))

#Sifreleme fonksiyonu, verlen stringin karakterlerini 
#shift miktarinca ilerleterek degistirir. 
def caesar(plaintext, shift):
	alphabet = string.ascii_lowercase
	shifted_alphabet = alphabet[shift:] + alphabet[:shift]
	table = string.maketrans(alphabet, shifted_alphabet)
	return plaintext.translate(table)

print caesar(plainText, shift)	#sifreleme
print caesar(caesar(plainText, shift), -shift)	#desifreleme
