import re
def preprocessing(text):
    cleaned = []
    processed_paragraphs = []
    paragraphs = [ i.split('\n\n') for i in text ]

    for item in paragraphs:
      for paragraph in item:
        processed_paragraph = coref_resolution(paragraph)
        processed_paragraphs.append(processed_paragraph)
          
    for string in  processed_paragraphs:
      s = re.sub('[!#&()/;=@[\]^_`{|}~]', "", string)
      s = s.replace("\n" ,"")
      i = s.split()
      if len(i) > 5:
        cleaned.append(s)
    return cleaned   