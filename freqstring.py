a=raw_input("Enter a String:").lower()
a=a.replace(" ","")

freq={}

for x in a:
	freq[x]=0

for x in a:
	freq[x]+=1
print freq
