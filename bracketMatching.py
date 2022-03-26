""" Brackets are tall punctuation marks used in matched pairs within text, to set apart or interject other text. Brackets refer to different types of brackets in different parts of the world and in different contexts.
Write a program which reads a String, which consists of alphabets [a-z, A-Z] and 3 types of brackets listed below:
Parentheses - ()
Square brackets - []
Braces or Curly brackets - {}
And determine whether every open bracket has a matching close bracket. If any open/close bracket doesn’t have a matching close/open bracket or any extra open/close bracket then it is to be treated as invalid string.
Following are 3 examples of valid string:
(the[is]{valid})
{the(is[valid])}
(this)(is)(valid)
Following are 4 examples of invalid string:
(the[is]{invalid))
(the[is]{invalid}}
(this](is}{invalid)
[this]{is}(invalid))
 """
openl=["(","{","["]
closel=[")","}","]"]
n=int(input())
for i in range(n):
    str = input()
    stack=[]
    for i in str:
        if i in openl:
            stack.append(i)
        elif i in closel:
            pos = closel.index(i)
            if ((len(stack)>0) and openl[pos]==stack[len(stack)-1]):
                stack.pop()
            else:
                stack.append(i)
    if len(stack)==0:
        print("VALID")
    else:
        openb=0
        closeb=0
        for i in stack:
            if i in openl:
                openb+=1
            if i in closel:
                closeb+=1
        if openb>closeb:
            print("TOO MANY OPENING")
        elif openb==closeb:
            print("MISSMATCH")
        else:
            print("TOO MANY CLOSING")
