# name = input ("Enter your name :")

# print(f"Good nighht {name} broo")

letter = '''hi my name is <|Name|>
                 i am all good 
                 my dob is <|date|>'''
print(letter.replace("<|Name|>","KARTIK").replace("<|date|>","29/08/2006"))
print (letter.find("good"))