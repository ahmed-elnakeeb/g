import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
import nltk
class NLPMax:
    def __init__(self):
        print("hi")

    def tokenize_words(self,sentence:str)->list:
       """Return a tokenized copy of *text*, using NLTK's recommended word tokenizer (currently an improved .TreebankWordTokenizer along with .PunktSentenceTokenizer for english).\n:param text: text to split into words\n:type text: str"""        
       return word_tokenize(sentence)

    def tokenize_sents(self,sentence:str)->list:
        """Return a sentence-tokenized copy of *text*, using NLTK's recommended sentence tokenizer (currently .PunktSentenceTokenizer for the english).\n:param text: text to split into sentences"""
        return sent_tokenize(sentence)

    def tokenize_custom(self,sentence:str) ->list:
        custom_sent_tokenizer = PunktSentenceTokenizer()
        tokenized = custom_sent_tokenizer.tokenize(sentence)
        return tokenized

    def filter_stop_words(self,sentence:str) ->list:
        stop_words=set(stopwords.words("english"))
        words=self.tokenize(sentence)
        filtered =[word for word in words if not word in stop_words]
        return filtered


    def stem(self,sentence:str) ->list:
        words=word_tokenize(sentence)
        stemed=[]
        ps=PorterStemmer()
        for word in words:
            stemed.append(ps.stem(word))
        return stemed

    def lemmatize(self,sentence:str) ->list:
        words=word_tokenize(sentence)
        lemmatized=[]
        lemmatizer = WordNetLemmatizer()
        for word in words:
            lemmatized.append(lemmatizer.lemmatize(word))
        return lemmatized
    

    def tag(self,sentence:str) ->list:
        custom_sent_tokenizer = PunktSentenceTokenizer()
        tokenized = custom_sent_tokenizer.tokenize(sentence)
        tag_list=[]
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                tag_list.append(tagged)
                

        except Exception as e:
            print(str(e))
        return tag_list

    def chunk (self,sentence:str) ->list:
        custom_sent_tokenizer = PunktSentenceTokenizer()
        tokenized = custom_sent_tokenizer.tokenize(sentence)
        chunk_list=[]
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                chunkgram=r"""chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} """
                chunkparser=nltk.RegexpParser(chunkgram)
                chunked=chunkparser.parse(tagged)
                chunk_list.append(chunked)
        except Exception as e:
            print(str(e))
        return chunk_list

    def chunkgram (self,sentence:str,chunkgramer) ->list:
        custom_sent_tokenizer = PunktSentenceTokenizer()
        tokenized = custom_sent_tokenizer.tokenize(sentence)
        chunk_list=[]
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                chunkgram=chunkgramer
                chunkparser=nltk.RegexpParser(chunkgram)
                chunked=chunkparser.parse(tagged)
                chunk_list.append(chunked)
        except Exception as e:
            print(str(e))
        return chunk_list

    def namedEntity (self,sentence:str) ->list:
        custom_sent_tokenizer = PunktSentenceTokenizer()
        tokenized = custom_sent_tokenizer.tokenize(sentence)
        chunk_list=[]
        try:
            for i in tokenized:
                words = nltk.word_tokenize(i)
                tagged = nltk.pos_tag(words)
                namedent=nltk.ne_chunk(tagged)
                chunk_list.append(namedent)
        except Exception as e:
            print(str(e))
        return chunk_list

    def senset(self,word:str):
        return wordnet.synsets(word)[0]

    def wup_similarity(self,w1:nltk.corpus.reader.wordnet.Synset,w2:nltk.corpus.reader.wordnet.Synset):
        return w1.wup_similarity(w2)
        
    def senset_names(self,word:str):
        names=[]
        set=wordnet.synsets(word)
        for zz in set:
            names.append(set[zz].lemmas()[0].name())
        return names
        
