import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
#from tests.constants import tbr_en_sentences as _sentences
from importlib import import_module
import os.path, pkgutil

lang = "en"
pkg = PKG_INDICES[lang]

_sentences = read_from_json("{}_sens/test_{}_{}.json".format(lang, lang, "adj")) 

def test_en_structure():
  sentences = _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  display_structure(sentences, nlp)

