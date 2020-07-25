
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



#db=my_JSON()
#x=db.load_json_from_file("clarify.json")


c=engin("the light is faster than lightneng ",["i like red . i do not like blue","i hate blue but not red"],["red","blue"],10)
print(c.correct())