import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
import json
from importlib import import_module

lang = "es"
pkg = PKG_INDICES[lang]

def _add_bracket(ex):
  return "(" + ex + ")" if ex!=None else ""

def sen_structure(sentences, nlp):
  content = []
  for s in sentences:
    doc = nlp(s)
    structure_with_explanation = trs(doc, doc._.structure, lang)
    analysis = " ".join([t["text"] + _add_bracket(t["explanation"]) for t in structure_with_explanation])
    _data = {
      "sentence": s,
      "analysis": analysis,
      "tbr": analysis,
    }
    content.append(_data) 
  return content

def test_structure_tbr_gen():
  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  sens_dir = "{}_sens".format(lang)
  for x in os.listdir(sens_dir):
    filename = "{}/{}".format(sens_dir, x)
    sentences = read_from_json(filename)
    content = sen_structure(sentences, nlp) 
    write_to_csv(["sentence", "analysis", "tbr"], content, csvfile="tbr/{}/{}.csv".format(lang, x))

