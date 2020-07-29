
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
import os
import sys
import getopt
import io
import platform


system = platform.system()
version = platform.python_version()
if version[0] != '3':
    print("sorry! this only works for python3")
    sys.exit()

def err():
    if system == "Windows":
        print('python cptc.py -h')
    else:
        print('cptc -h')
    sys.exit()

def main(argv):
    ###---        main        ---###
    outfile_path=os.path.join( os.getcwd(),'report.txt')
    student_answer=""
    model_answer=""
    keywords=""
    s_ok=False
    m_ok=False
    k_ok=False
    rng=100

    

    try:
        opts, args = getopt.getopt(argv, "hs:m:o:k:r:", ["student_answer=","model_answer=", "outfile_path=","keywords=","range="])
    except getopt.GetoptError:
        err()

    for opt, arg in opts:
        ####################################
        if opt == '-h':
            print("#-----------------------------------#")
            print("options")
            print("s | student_answer        | selected  student answer path")                        
            print("m | model_answer          | selected  model answer path")
            print("o | outfile_path          | selected  outfile path")
            print("k | keywords              | selected  keywords path")
            print("r | range                 | training times")            
            print("-------------------------------------")
            print("usage")
            if system == "Windows":
                print("cptc.py -s <student_answer> ")      
            else:
                print("cptc -s <student_answer>") 
            sys.exit()
        ####################################
        if opt in ['-s','--student_answer']:
            student_answer=arg
            s_ok=True

        ####################################
        if opt in ['-m','--model_answer']:
            model_answer=arg
            m_ok=True

        ####################################
        if opt in ['-o','--outfile_path']:
            outfile_path=arg
        ####################################
        if opt in ['-k','--keywords']:
            keywords=arg
            k_ok=True
        if opt in ['-r','--range']:
            rng=int(arg)


        ####################################
        ####################################

    if s_ok:
        with open(student_answer, 'r') as st:
            content = st.read()
        if m_ok and k_ok:
            with open(model_answer, 'r') as st:
                model_answers = st.readlines()
            with open(keywords, 'r') as st:
                keywordslist = st.readlines()
            c=engin(content,model_answers,keywordslist,rng)
            
            with open(outfile_path, 'w') as st:
                st.write(c.correct())
        else:
            c=engin(content,[],[],rng)
            with open(outfile_path, 'w') as st:
                st.write(c.correct())            
    else:
        print("provide student answer")
        

    

    ###---        main-end       ---###
main(sys.argv[1:])