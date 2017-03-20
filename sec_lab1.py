#Andrei Botnari C13383341
#lab1 part 1
def caesar(s, k, decrypt=False):
    if decrypt: k = 26 - k
 
    r = ""
 
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90):
            r += chr((ord(i) - 65 + k) % 26 +65)
			
        elif (ord(i) >= 97 and ord(i) <= 122):
            r += chr((ord(i) - 97 + k) % 26 + 97)
			
        else:
            r += i
 
    return r
 
def encrypt(p, k):
    return caesar(p, k)
 
def decrypt(c, k):
    return caesar(c, k, True)
	
p = "This is a test"
k = 4

print( "text = ", p, " encrypted = ",encrypt(p, k),
"decrypted = ", decrypt(encrypt(p, k), k), "key=",k)
