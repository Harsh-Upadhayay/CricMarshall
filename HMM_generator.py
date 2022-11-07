
from pandas import DataFrame
from nltk import word_tokenize

class HMM_matrix_generator :

    corpus = []
    wordfreq = {}
    tagfreq = {}
    word_tagfreq = {}
    transitionfreq = {}
    token_count = 0

    def __init__(self, filepath="Lab_5_corpus/test.txt") :
        self._readFile(filepath)
        self._updateFreq()
        self._initTransitionMatrix()
        self._initEmissionMatrix()

    def _readFile(self, filepath) :
        alllines = []
        singleline = []
        file = open(filepath).readlines()
        for line in file:
            self.token_count += 1
            try :
                line = line[: line.rindex(' ')]
                a, b = line.split()
                b = self.__category(b)
                line = (a, b)
            except :
                pass
            if(len(line) == 1) :
                alllines.append(singleline)
                singleline = []
            else :
                if line[1] != "NA" :
                    singleline.append(line)
                
        self.corpus = alllines   

    def _updateFreq(self):
        
        for line in self.corpus:
            prv = "eos"
            self.__insert("eos", self.tagfreq)
            try:
                self.__insert(("eos", line[0][1]), self.transitionfreq)
            except:
                continue
            for tgd_tkn in line :
                tk, tg = tgd_tkn
                
                tristn = (prv, tg)
                self.__insert(tk, self.wordfreq)
                self.__insert(tg, self.tagfreq)
                self.__insert(tgd_tkn, self.word_tagfreq)
                self.__insert(tristn, self.transitionfreq)

                prv = tg
            self.__insert((prv, "eos"), self.transitionfreq)
            self.__insert("eos", self.tagfreq)
    
    def _initTransitionMatrix(self) :
        tags = list(self.tagfreq.keys())
        tags.remove("eos")
        tags.append("eos")
        nrow = dict()
        for tag in tags :
            row = dict()
            for itag in tags :
                pt = 1
                pt = self.tagfreq[itag] / (self.token_count)
                if (tag, itag) in self.transitionfreq.keys() :
                    pt *= self.transitionfreq[(tag, itag)] / (self.tagfreq[tag])
                else:
                    pt = 0
                row[itag] = pt
            
            nrow[tag] = row;
        
        self.transitionMatrix = DataFrame(nrow)

    def _initEmissionMatrix(self):
        tags = self.tagfreq.keys()
        words = self.wordfreq.keys()
        col = dict()

        for tag in tags :
            if tag == "eos" or tag == "eos" :
                continue;
            row = dict()
            for word in words :
                if (word, tag) in self.word_tagfreq.keys() :
                    row[word] = self.word_tagfreq[(word, tag)] / self.wordfreq[word]
                else :
                    row[word] = 0

            col[tag] = row
        
        self.emmisionMatrix = DataFrame(col)

    def ssmx(self, s) :
        if not s or type(s) != str:
            return None
        
        tkns = word_tokenize(s)
        avil = []
        not_avil = []
        for tkn in tkns : 
            if tkn not in self.emmisionMatrix.index.tolist():
                not_avil.append(tkn)
            else:
                avil.append(tkn)
                
        df = DataFrame(self.emmisionMatrix.loc[avil])
        df_val = 1 / self.token_count
        for tkn in not_avil :
            df.loc[tkn] = [df_val] * len(df.columns.tolist())

        df.replace(0, df_val, inplace=True)
        return df
            
    def __category(self, tags):

        if(tags=='VB'or tags=='VBP'or tags=='VBZ' or tags=='VBD' or tags=='VBN' or tags=='VBG'):
            return "Verb"
        elif(tags=='NN'or  tags=='NNS' or tags=='NNP'or tags=='NNPS'):
            return "Noun"
        elif(tags=='PRP' or tags=='PRP$' or tags=='WP' or tags=='WP$'):
            return "Pronoun"
        elif(tags=='RBS' or tags=='RBR' or tags=='RB' or tags=='WRB'):
            return "Adverb"
        elif(tags=='TO'or tags=='IN'):
            return "Preposition"
        elif(tags=='CC'):
            return "Conjunction"
        elif(tags=='DT'):
            return "Determiner"
        elif(tags=='ADJ' or tags=="JJ" or tags=='JJR'):
            return "Adjective"
        else:
            return "NA"

    def __insert(self, a, b) :
        
        if (a in b):
            b[a] += 1
        else:
            b[a] = 1
      
    def __debug(self) :
        print("Corpus : \n", self.corpus, "\n\n\n")
        print("wordfreq : \n", self.wordfreq, "\n\n\n")
        print("tagfreq : \n", self.tagfreq, "\n\n\n")
        print("word_tagfreq : \n", self.word_tagfreq, "\n\n\n")
        print("transitionfreq : \n", self.transitionfreq, "\n\n\n")


if __name__ == "__main__":
    
    hmm = HMM_matrix_generator("Lab_5_corpus/data.txt")
    print(hmm.ssmx("current"))
    