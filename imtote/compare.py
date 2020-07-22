from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet, stopwords
from nltk.stem import PorterStemmer
class compare:
    def __init__(self):
        pass
    #Function To Fillter The Words
    def fillter_Words(self,my_List):
        stopWords = set(stopwords.words("English"))
        filtered_List = []
        
        for w in my_List:
            if w not in stopWords:
                filtered_List.append(w)
        return filtered_List


    #Function To Get The Synonyms For The Anonymous Word
    def get_Synonyms_For_Word(self,word):
        synonyms = []
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
        return synonyms


    #Function To Check If The Synonyms Of The Anonymous Word Existing In The Right Answer
    def check_The_Anonymous_Word_In_The_Right_Answer(self,word, right_Answer_list):
        Synonyms_List = self.get_Synonyms_For_Word(word)
        for w in Synonyms_List:
            if w in right_Answer_list:
                return True
        return False
    
    def compare(self,student_answer:str,mentor_answer_path:str):
        # To Open The File That Contain The Question Answer And Read It
        read_The_Stu_Answer = student_answer
        file_Right_Answer = open(mentor_answer_path,"r")
        read_The_Right_Answer = file_Right_Answer.read()
        #Split The Answer To Words
        words_Of_Stu_Answer = word_tokenize(read_The_Stu_Answer)
        words_Of_Right_Answer = word_tokenize(read_The_Right_Answer)
        #Fillter The Answer
        words_Of_Stu_Answer = self.fillter_Words(words_Of_Stu_Answer)
        words_Of_Right_Answer = self.fillter_Words(words_Of_Right_Answer)
        num_Of_Correct_Words = 0
        num_Of_Words_In_Right_Answer = len(words_Of_Right_Answer)
        list_For_correct_Words = []
        #Check How Many Correct Words In The Answer
        for element in words_Of_Stu_Answer:
            if element in words_Of_Right_Answer:
                num_Of_Correct_Words = num_Of_Correct_Words + 1
                list_For_correct_Words.append(element)
            else:
                #Search In Dictionary For Synonyms
                check = self.check_The_Anonymous_Word_In_The_Right_Answer(element, words_Of_Right_Answer)
                if check == True:
                    num_Of_Correct_Words = num_Of_Correct_Words + 1
                    list_For_correct_Words.append(element)
        degree_Of_Question = (num_Of_Correct_Words / num_Of_Words_In_Right_Answer) * 100
        print("Degree Of Question", degree_Of_Question)
        print("List For correct Words", list_For_correct_Words)
        print("Words Of Student Answer", words_Of_Stu_Answer)
        print("Words Of Right Answer", words_Of_Right_Answer)

        return degree_Of_Question




        
