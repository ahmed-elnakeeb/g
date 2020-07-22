import re
from spellchecker import SpellChecker
from nltk_tool_kit import nltkToolKit
import pattern

class newToolKit:
    def __init__(self,nltktools):
        print ("newToolKit instance")
        self.mynlp=nltktools
        self.spell=SpellChecker()

    def reduce_lengthening(self,text:str) ->str:
        pattern = re.compile(r"(.)\1{2,}")
        return pattern.sub(r"\1\1", text)
    
    def type_1_WordAutoFix(self,word:str) -> str:
        word=self.reduce_lengthening(word)
        return self.spell.correction(word)

    def type_1_textAutoFix(self,text:str) ->str:
        tokens=self.mynlp.tokenize_words(text)
        text=""
        for i in tokens:

            text=text+self.type_1_WordAutoFix(i)+" "
            

        return text

    def type_1_textCandidates(self,text:str) ->list:
        
        word=self.mynlp.tokenize_words(text)[0]
        return self.spell.candidates(word)
            
      

    def unknown(self,text):
        tokens=self.mynlp.tokenize_words(text)
        return self.spell.unknown(tokens)

    def fixemall(self,text:str):
        x=self.mynlp.tokenize_words(text)
        text=""
        for i in x:
            g=self.reduce_lengthening(i);
            g=self.type_1_WordAutoFix(g)
            text+=g
            text+=" "
        return text

        