import spacy
from spacy import displacy
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
import re
from nltk.stem import PorterStemmer
sp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words('english'))

def question_processing(qquestion):

    words_relations ={'winner': ['win' , "winning" ,'won', 'wins'],
                  'occupant':["occupant"],
                  'position played on team / speciality':['role' , 'position on team ', 'position' , 'speciality' , "play"],
                  'participating team':['participating' ,'participating team'],
                  'father':['father'],
                  'league':['league'],
                  'country of citizenship': ['citizenship' , 'nationality', 'race',  'located' , "locate"],
                  'work in': ['part , member','instance' , "work" , "working"],
                  'country': ['country'],
                  'sports season of league or competition': ["season"],
                  'owned by':["owned" ,'own', 'owner'],
                  'field of work':['field', 'job', "occupation" , 'do'],
                  'developer':['develop', "developing" , 'develops'],
                  'head of government':['head of government'],
                  'participant of' :['participant' , 'contribute'],
                  'located in or next to body of water':["located in or next to body of water"],
                  'sibling' : ["sibling"],
                  'taxon rank':['taxon rank'],
                  'position held' :['position held'],
                  'subsidiary':["subsidiary"],
                  'architect' :["architect"],
                  'language of work or name':['language'],
                  'publisher':["publisher"],
                  'residence':["residence"]}
                  
                  
    question = re.sub('[!?#&()/;=@[\]^_`{|}~]', "", qquestion)
    text1= sp(qquestion)
    results =[]
    for word in text1.ents:
        results.append((word.text,word.label_))
    
    sub = 'null' 
    obj = 'null' 
    for tup in results :
        if tup[1] in ["PERSON" ,"EVENT"]:
            sub = tup[0]
        else :
            obj = tup[0]
            
    diff = sub.split(" ") + obj.lower().split(" ")
    word_tokens = word_tokenize(question)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    spec = [ k for k in filtered_sentence if k not in diff]
    st = PorterStemmer()
    ques  = [st.stem(word) for word in spec]

    rel = "null"
    for k ,v  in words_relations.items():
        for ele in ques:
            if ele in v:
                rel = k
                
    return [sub , rel , obj]