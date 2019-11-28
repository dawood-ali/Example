##HELLO DAWOOD


def getInputfile(filename):
	file=False
	import os.path
	while file!=True:

		if os.path.isfile(filename)==True and filename[-4::]=='.txt':
			print("Thank you")
			file=True

		else:
			print("file DNE, try again")
			filename=input("filename: \n")

def cipher(filename):
	import string
	file= open(filename,'r')
	filecode= file.readlines()
	key= int(filecode[0])

	message=filecode[1]

	message=message.lower()
	message=message.replace("	"," ")
	message= message.replace("  "," ")
	print(message)
	numnew=0
	num=0
	decrypted=""

	for char in message:

		if ord(char)-key<97:
			num=123-(key-(ord(char)-97))
			decrypted+=chr(num)

		elif ord(char)-key>=97:
			numnew=ord(char)-key
			decrypted+=chr(numnew)

	decrypted= decrypted.replace('4'," ")


	return decrypted
	file.close()
if __name__=="__main__":

	#getInputfile(input("filename: \n"))
	print(cipher('secretMessage1.txt'))

