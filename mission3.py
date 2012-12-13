
import hashlib

encrypted = raw_input('Enter Encrypted String: ')
		
elist = []
elist = encrypted.split(' ')

characters = [ 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9' ]
hex_chars = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9' ]
	
def Sum(hex):
	hex_list = list(hex)
	sum = 0
	for element in hex_list:
		sum += int(element,16)
	return sum
	
def MD5_Hash(string1):
	m = hashlib.md5()
	m.update(str(string1))
	return m.hexdigest()

def SpecialChar(location): #These characters are the same for each serial
	if(location%20 == 19):
		return "\n"
	elif((location%20 == 3) or (location%20 == 7) or (location%20 == 11) or (location%20 == 15)):
		return "-"
	elif(location%20 == 8):
		return "O"
	elif(location%20==9):
		return "E"
	elif(location%20==10):
		return "M"
	elif((location%20 == 18) or (location%20==16)):
		return "1"
	elif(location%20==17):
		return "."
	else:
		return "0"
	
#passhash_guess is pass_guess array
#elist is an array of the nums in encrypted string
#times_run is the intMD5Total for the times_run'th character in the serial
def Total(str_guess, passhash_guess, previous, times_run):
	if(times_run == 0):
		intTotal = ord(str(str_guess)[0:1]) - int(elist[times_run]) + int(passhash_guess,16)
		return intTotal
	else:
		return Sum(str(MD5_Hash(str_guess[:(times_run+1)]))[0:16] + str(MD5_Hash(previous))[0:16])
		


def Find_Possible():
	for j in range(len(hex_chars)):
		for i in range(len(characters)):
			if(((ord(characters[i]) + int(hex_chars[j],16) - Total(characters[i], hex_chars[j],0, 0)) == int(elist[0]))):
				intTotal = Total(characters[i], hex_chars[j],Total(characters[i], hex_chars[j],0, 0), 1)
				if(HashCalculate(characters[i],1, str(hex_chars[j]),intTotal) != "0"):
					return 1
										
	return 0

def HashCalculate(char_guess,depth,hash_string,total):
	if(depth > 99):
		print "Found!" + str(char_guess)
		return str(char_guess)
	elif(depth > 31): #Once we get to the 32nd loop, we have the MD5 hash of the password and only need to bruteforce the unencrypted string
		if(SpecialChar(depth) != "0"):
				intTotal = Total(char_guess+SpecialChar(depth), hash_string[0:1],total, depth+1)
				strDone = HashCalculate(char_guess+SpecialChar(depth),depth+1,hash_string,intTotal)
				return strDone
		else:	
			for i in range(len(characters)):
				if((ord(characters[i]) + int(hash_string[(depth%32):(depth%32+1)],16) - total) == int(elist[depth])):
					intTotal = Total(char_guess+characters[i], hash_string[0:1],total, depth+1)
					strDone = HashCalculate(char_guess+characters[i],depth+1,hash_string,intTotal)
					if(strDone != "0"):
						return strDone
		return "0"
		
	else:
		for j in range(len(hex_chars)):
			if(SpecialChar(depth) != "0"):
				if((ord(SpecialChar(depth)) + int(hex_chars[j],16) - total) == int(elist[depth])):
					intTotal = Total(char_guess+SpecialChar(depth), hash_string[0:1],total, depth+1)
					strDone = HashCalculate(char_guess+SpecialChar(depth),depth+1,hash_string+hex_chars[j],intTotal)
					if(strDone != "0"):
						return strDone
			else:	
				for i in range(len(characters)):
					if((ord(characters[i]) + int(hex_chars[j],16) - total) == int(elist[depth])):
						intTotal = Total(char_guess+characters[i], hash_string[0:1],total, depth+1)
						strDone = HashCalculate(char_guess+characters[i],depth+1,hash_string+hex_chars[j],intTotal)
						if(strDone != "0"):
							return strDone
		
	return "0"
Find_Possible()


					



