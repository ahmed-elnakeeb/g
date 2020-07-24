
#v0.02
"""
in:
student aswer
model answer(s)
key words

out:
degree based on smilarity

proc:
parse
find annomlies
nomait corrections
compare 

libraries: 
nltk 
pyspellchecker
problems:
nlp not effcient neither am i
how to collect the degree 
uncertinty
"""

from my_JSON import my_JSON
from Engine import engin


db=my_JSON()
x=db.load_json_from_file("clarify.json")

with open("keywords.txt", 'w') as json_file:
    for key in x:
        words=x[key][1]
        for word in words:
            json_file.write(word+"\n")

c=engin("i like red . i do not like blue",["i like red . i do not like blue","i hate blue but not red"],["like_red","hate_blue"])