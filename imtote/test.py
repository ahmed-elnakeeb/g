
text="ahmed elnakeeb"
words=word_tokenize(text)
for word in words :
    spell = SpellChecker()
    print (spell.correction(word))
