from spellchecker import SpellChecker
from tqdm import tqdm
from tqdm import trange

class engin:
    def __init__(self,studentanswer:str,modelanswers:list,keywords:list,trng:int):
        self.student_Answer=studentanswer
        self.model_Answers=modelanswers
        self.Keywords=keywords
        self.trng=trng

    def correct(self)->str:
        spell=SpellChecker()
        corrected_text=""
        #toknize
        words=spell._tokenizer(self.student_Answer)
        # get keywords ready 
        spell.word_frequency.load_dictionary("mydic.json")
        spell.word_frequency._update_dictionary()
        

        
        for word in tqdm(words):
            corrected_text+=spell.correction(word)+" "
        return corrected_text
    
