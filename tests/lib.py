from spacy.language import Language
from structure_detective import Structure, trs
from spacy import displacy
from pathlib import Path
import json
import csv
from importlib import import_module
import os.path, pkgutil
 
@Language.factory("structure")
def create_structure(nlp: Language, name: str):
  return Structure(nlp)
 
def print_structure(doc, lang):
  content = doc._.structure
  print(content)
  #print(lang)
  analysis = trs(doc, content, lang)
  print(analysis)
  #for c in content:
  #  print("{}\t{}\t{}\t{}".format(c["text"], c["dep"], c["start"], c["end"]))


def print_doc(doc):
  for t in doc:
    print("{} {} {} {} {} {}".format(t.text, t.pos_, t.dep_, t.tag_, t.morph, t.lemma_))

def graph(doc, lang):
  svg = displacy.render(doc, style="dep", jupyter=False)
  file_name = '-'.join([w.text for w in doc if not w.is_punct]) + ".svg"
  output_path = Path(lang+ "_images/" + file_name)
  output_path.open("w", encoding="utf-8").write(svg)

def display_structure(sentences, nlp):
  for s in sentences:
    doc = nlp(s)
    print("*"*10)
    print(s)
    print_structure(doc, nlp.meta["lang"])
    print_doc(doc)
    print("*"*10)
    graph(doc, nlp.meta["lang"])

def write_to_csv(fields, content, csvfile="review.csv"):
  #print('Create {} file'.format(csvfile))
  with open(csvfile, encoding="utf8", mode='w') as output_file:
    dict_writer = csv.DictWriter(output_file, restval="-", fieldnames=fields, delimiter='\t')
    dict_writer.writeheader()
    dict_writer.writerows(content)

def read_from_json(filename):
  data = []
  with open(filename) as f:
    data = json.load(f)
  return data


def write_to_json(filename, content):
  with open(filename, 'w') as outfile:
    json.dump(content, outfile)

