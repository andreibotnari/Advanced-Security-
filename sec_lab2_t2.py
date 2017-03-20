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
	
c = "Vg jbhyq frrz gung, nf ur rknzvarq gur frireny cbffvovyvgvrf, n fhfcvpvba pebffrq uvf zvaq: gur"
"zrzbel bs ubj ur uvzfrys unq orunirq va rneyvre qnlf znqr uvz nfx jurgure fbzrbar zvtug or"
"uvqvat ure sebz gur jbeyq"

#This loop goes through key 0-20 to check whik key would be acceptable to 
#decrypt its inneficient but it find the unknown key
for k in range (10, 14):

	print( k ,"text = ", c, " encrypted = ",decrypt(c, k),
	"decrypted = ", "key=",k ,"/n")
