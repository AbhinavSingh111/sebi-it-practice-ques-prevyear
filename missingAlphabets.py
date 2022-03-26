# Given a snippet of text containing alphabets, numbers and punctuation, you have to write a C/C++/JAVA programs to find out whether any of english alphabets are missing in the paragraph.  
# List of words separated by space/tab/newlines , Input is terminated as word “endpara”, 
# Note: Assume that endpara will never be the part of snippet.
#  Print the missing Alphabets in the paragraph in the ascending order in CAPITAL separated by space. 
# If none of the alphabet is missing, print “NONE”.

str = input()
s=[]
while("endpara" not in str):
    str=str+" "+input()
str = str.replace("endpara","")
str=str.upper()
pat = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
for i in pat:
    if i not in str:
        s.append(i)

if len(s)==0:
    print("NONE")
else:
    for j in s:
        print(j,end=" ")
