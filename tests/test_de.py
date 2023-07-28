import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
#from tests.constants import tbr_en_sentences as _sentences
from importlib import import_module
import os.path, pkgutil

lang = "de"
pkg = PKG_INDICES[lang]

#_sentences = read_from_json("{}_sens/test_{}_{}.json".format(lang, lang, "prep")) 

oc_sentences = [
  "Sie müssen enttäuscht sein, dass ich mich nicht persönlich bei Ihnen abgemeldet habe, aber...", # unmet
  "Der Ärztekongress stand Kopf, hat man mir erzählt.", # oc
  "Ich denke, uns trennt doch mehr, als uns verbindet.", # oc
  "Ich habe gelesen, dass es in Amerika eine Kamera geben soll,", # ADD ep
  "Der glaubt, kann sich alles erlauben!", # oc 
  "Er hat gesagt, es ginge um einen neuen Detektivroman.", # ADD ep
  "Wollten Sie bei Erprobe ohne mir gesprochen zu haben?",
  "Therese, wenn Sie wüssten, was alles passiert ist.", #BUG: oc
]

verb_sentences = [
  "Es hat schon einen Grund, dass wir Diakonissen keine weltliche Bindung eingehen sollen.", # AUX VS VERB
  "Weil Sie eine Fleischwunde haben?", # AUX VS VERB
  "Wer will schon einen Jungen?", # MODAL VS VERB
  "Sie haben doch Behring und Kitasato.", # AUX VS VERB
  "Die Beide haben zwar interessante Ansätze.",
  "Haben Sie einen schönen Tag.",
  "Ich habe heute keinen Ausgang.",
  "Ich kann kein Englisch.",
  "Innerhalb von drei Wochen kann die Dosis um das 500Fache gesteigert werden.",
  "Seien Sie nicht überheblich, Lenze.",
  "Sie müssen nach Zürich.",
  "Dafür hatten Sie die geniale Idee.",
  "Wir haben endlich ein stabiles Antiserum.",
  "Was wollte sie?",
  "Ich habe gestern dieses Buch gelesen.",
  "Ich will morgen dich besuchen.",
  "Er muss Hausaufgaben fertig machen.",
  "Lass die bösen Männer ziehen",
]


_sentences = [
  #"Wenn Sie erstmal meinen Vater kennengelernt haben, wird dann alles anders.", #BUG: wird 表语/其他
  #"Das kann mir fast egal sein.", # oc - verb
  #"Statt dieser ewigen Beterei brauchen wir mehr Zeit zum Ausruhen.",
  #"Es ist nicht egal uns, welche Schwester die Handlanger der Ärzte sind?", # dependency tree error
  #"Frauen sollten Recht bekommen, selbst Medizin zu studieren.", # oc
  #"Ich könnte ohne Verfahren das Land verwiesen werden.", #oc-verb
  #"Hier ist das Kalkwasser zum Gurgeln.", # dependency tree error

  #"Aber tut das Lotte nicht trotzdem ganz arg weh?", # svp mo
  #"Bei intravenöser Gabe wird das Antitoxin sofort aktiv.", # copula
  #"Wir wollten doch vorher allein sein.", #oc-verb-copula
  #"Wir hatten etwas Wichtiges mit meinem Vater zu regeln.", #VERB-AUX
  #"Ich hoffe, Doktor, meine Zukunft nicht nur darauf beschränkt.", #oc
  #"Bei meiner Ehre, ich bin Korpsstudent.", # copula
  "Er muss Hausaufgaben fertig machen.",
] 

def test_de_structure():
  sentences = _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  display_structure(sentences, nlp)

