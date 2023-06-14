##python.txt
s='Python is a very useful programming language.'

x=s.replace("useful","IMPORTANT")

print(x)

count=0

for i in range(0,len(s)):
    if s[i] == " ":
        count += 1
        
print(count)

f= open('text.txt')
text= f.read()
the_letters=[]
for i in range(125):
    the_letters.append(0)

print(the_letters)
print(len(text))    
 
for x in text:
    num= ord(x.lower())
    if num > 65 and num < 123:
        the_letters[num]+=1

for i in range (len(the_letters)):
    if the_letters[i] > 0:
        print(chr(i),the_letters[i])
        
        
        
        
f = open( (text. txt')
text = f. read()
the_letters =[]
 d = len(text)
 print ("\nEnglish text - total number of letters in the text is " + str(d) +'\n')
 for i in range(125):
    the_letters.append(0)
 for x in text:
     num 1 = ord(x. .lower())
     if num > 65 and num < 123:
         the_letters[ [num] += 1
print("%6s %5s %10s" %( 'letter', 'amount', 'frequency' ) )
 for i in range(len( (the letters)):
     if the_letters[i] > 0:
         print("3s %7d %9.1f" %( chr(i), the_letters[i],