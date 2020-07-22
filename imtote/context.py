from new_tool_kit import newToolKit
from nltk_tool_kit import nltkToolKit
class context:
    def __init__(self):
        self.nlp=nltkToolKit()
        self.new=newToolKit(self.nlp)

    def simi(self,w1:str,w2:str)->float:
        try:
            senw1=self.nlp.senset(w1)
            senw2=self.nlp.senset(w2)
            return self.nlp.wup_similarity(senw1,senw2)
        except:
            return 0.0
    def simiforall(self,word:str,text:str)->float:
        word=self.nlp.tokenize_words(word)[0]
        text=self.nlp.tokenize_words(text)
        sum=0
        for i in text:
            try:
                sum+=self.simi(i,word)
            except:
                pass
        return sum

    def select_corr(self, word:str,conext:str)->str:
        word=self.nlp.tokenize_words(word)[0]
        cands=self.new.type_1_textCandidates(word)
        cands=list(cands)
        bestchoise=cands[0]
        likelihood=0
        for i in cands:
            temp= self.simiforall(i,conext)
            if temp > likelihood:
                bestchoise=i
        return bestchoise

    def corr(self,word:str)->str:
        word=self.nlp.tokenize_words(word)[0]
        cands=self.new.type_1_textCandidates(word)
        cands=list(cands)
        return cands[0] 


    def Context_sensitive_spellchecker(self,text:str)->str:
        wordlist=self.nlp.tokenize_words(text)
        correctedtext=""
        for i in wordlist:
            correctedtext+=self.select_corr(i,text)
            correctedtext+=" "

        return correctedtext
    def non_context(self,text:str)->str:
        wordlist=self.nlp.tokenize_words(text)
        for i in wordlist:
            correctedtext+=self.corr(i)
            correctedtext+=" "

        return correctedtext



            