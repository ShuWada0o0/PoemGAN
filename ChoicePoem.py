"""
生成された文章から5・7・5の文章を選定する



"""

import MeCab
import csv
import pdb
tagger = MeCab.Tagger('-Oyomi')


with open("generateFailPath") as f:
    with open("OutputPoemFailPath", 'w') as k:
        content = f.readlines()
        writer = csv.writer(k)
        
        for sent in content:
            
            sents = sent.split()
            try:
                words = sents[0:sents.index("</S>")]
                
                flag = 0
                
                for i in range(len (words)+1):
                    
                    word = words[0:i]
                    wflag = 0
                    PoemWord = ''
                    for f in word:
                        PoemWord += f
                        if (flag == 0 and len(tagger.parse(PoemWord))==6):
                            flag += 1
                            
                        elif (flag == 1 and len(tagger.parse(PoemWord))==13):
                            flag += 1
                            
                        elif(flag == 2 and len(tagger.parse(PoemWord))==18):
                            flag += 1
                            
                        elif(flag == 3 and len(tagger.parse(PoemWord))>18):
                            
                            flag += 1


                
                if flag == 3:
                    
                    writer.writerow(word)
            except ValueError:
                pass
                

            