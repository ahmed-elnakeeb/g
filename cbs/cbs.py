import os
import sys
import getopt
import io
import platform
from nltk.corpus import stopwords
from gensim.models.word2vec import Word2Vec


system = platform.system()
version = platform.python_version()
if version[0] != '3':
    print("sorry! this only works for python3")
    sys.exit()

def err():
    if system == "Windows":
        print('python cbs.py -h')
    else:
        print('python cptc.py -h')
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
    s=[]
    m=[]
    

    try:
        opts, args = getopt.getopt(argv, "hs:m:o:k:", ["student_answer=","model_answer=", "outfile_path=","keywords=","range="])
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
            print("-------------------------------------")
            print("usage")
            if system == "Windows":
                print("cbs.py -s <student_answer> ")      
            else:
                print("cbs -s <student_answer>") 
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


        ####################################
        ####################################

    if s_ok and m_ok:
        with open(student_answer, 'r') as st:
            student_answer = st.read()
        with open(model_answer, 'r') as st:
            model_answer = st.read()
        stop_words=stopwords.words('english')
        s=[]
        m=[]
        for i in  student_answer.split():
            if i not in stop_words:
                s.append(i)       
        for i in model_answer.split():
            if i not in stop_words:
                m.append(i)
        
        
        with open(outfile_path, 'w') as st:
            pass                    
    else:
        print("provide student answer")
    model=Word2Vec()
    model=model.wv.load("1.bin")
    print(model.n_similarity(s,m))
    with open(outfile_path, 'w') as st:
        st.write(str(model.n_similarity(s,m)))

    
 
    ###---        main-end       ---###
main(sys.argv[1:])
