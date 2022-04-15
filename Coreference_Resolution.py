import spacy
import neuralcoref

# Load SpaCy
nlp = spacy.load('en_core_web_sm')
# Add neural coref to SpaCy's pipe
neuralcoref.add_to_pipe(nlp)

def coref_resolution(text):
  doc = nlp(text)
  # fetches tokens with whitespaces from spacy document
  tok_list = list(token.text_with_ws for token in doc)
  for cluster in doc._.coref_clusters:
      # get tokens from representative cluster name
      cluster_main_words = set(cluster.main.text.split(' '))
      for coref in cluster:
            if coref != cluster.main:  # if coreference element is not the representative element of that cluster
                if coref.text != cluster.main.text and bool(set(coref.text.split(' ')).intersection(cluster_main_words)) == False:
                    # if coreference element text and representative element text are not equal and none of the coreference element words 
                    # are in representative element. This was done to handle nested coreference scenarios
                    tok_list[coref.start] = cluster.main.text + \
                        doc[coref.end-1].whitespace_
                    for i in range(coref.start+1, coref.end):
                        tok_list[i] = ""

  return "".join(tok_list)