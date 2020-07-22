import os
import sys
import getopt
import io
import platform
from nltk import word_tokenize
from spellchecker import SpellChecker


system = platform.system()
version = platform.python_version()
if version[0] != '3':
    print("sorry! this only works for python3")
    sys.exit()

def err():
    if system == "Windows":
        print('corr.exe -h')
    else:
        print('corr -h')
    sys.exit()
def non_context(text:str)->str:
    words=word_tokenize(text)
    return str(words)


def main(argv):
    ###---        main        ---###
    t_ok=False
    textPath=""
    outfile_path=os.path.join(os.getcwd(),'report.txt')
    

    try:
        opts, _ = getopt.getopt(argv, "ht:o:", ["textPath=", "outfile_path="])
    except getopt.GetoptError:
        err()

    for opt, arg in opts:
        ####################################
        if opt == '-h':
            print("#-----------------------------------#")
            print("options")
            print("t | textPath         | selected  img path")
            print("-------------------------------------")
            print("usage")
            if system == "Windows":
                print("imtote.exe -t <textPath> ")      
            else:
                print("imtote -t <textPath>") 
            sys.exit()
        ####################################
        if opt in ['-t','--textPath']:
            textPath=arg
            t_ok=True
        ####################################

        if opt in ['-o','--outfile_path']:
            outfile_path=arg

    if t_ok :
        with io.open(textPath, 'r') as text_file:
            content = text_file.readlines()
            print(str(content[0]))
            words=word_tokenize(str(content[0]))
            corrected=""
            for word in words :
                spell = SpellChecker()
                corrected +=spell.correction(word) +" "
            print (corrected)

            report = open(outfile_path,"w")
            report.write(corrected)
            report.close()
            

        #################################

         
        
###---        main        ---###


if __name__ == "__main__":
    main(sys.argv[1:])