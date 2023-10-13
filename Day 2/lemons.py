'''
7 lemons to 3 gods then 21 needed 
if less say how many need if more than 21 then say extra if other than int say enter
correct value
'''
i=int(input())
print( ("enough") if i==21 else (i-21,"extra") if i>21 else (21-i,"less") else ("enter valid input") if(is_integer("i")!=True))                

