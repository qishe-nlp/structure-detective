import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
#from tests.constants import tbr_en_sentences as _sentences
from importlib import import_module
import os.path, pkgutil

lang = "es"
pkg = PKG_INDICES[lang]

#_sentences = read_from_json("{}_sens/test_{}_{}.json".format(lang, lang, "adj")) 

_sentences = [
  "Esta tarta está buena, pero estaría mejor con nata.",
  "Aquí estamos bien, pero estaríamos mejor en la playa.",
  "Soy feliz, pero sería más feliz con un buen empleo.",
  "¿Qué harías tú en mi lugar?",
  "Yo no diría nada.",
  "Yo tendría más cuidado.",
  "¿Cuándo dijo Marta que vendría?",
  "Europa está cambiando mucho con el euro.",
  "¡Qué pena! Se nos están pudriendo los limones.",
  "He estado corriendo.",
  "Lávalas mañana.",
  "Léelo en la biblioteca.",
  "Dale a Juan el regalo ya, Elvira.",
  "Dile a Elisa que la quieres, Jorge.",
  "Trae pan, José por favor.",
  "Pasen y esperen en la sala, por favor, señores.",
  "¿Y cuándo volveréis?",
  "¿A qué hora coméis?",
  "¿Cuantas horas al día veis la tele?",
]

def test_es_structure():
  sentences = _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  display_structure(sentences, nlp)

