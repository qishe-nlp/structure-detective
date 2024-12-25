import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
import json
from importlib import import_module
from tests.en_sens import *
lang = "es"
pkg = PKG_INDICES[lang]

def _add_bracket(ex):
  return "(" + ex + ")" if ex!=None else ""

def sen_structure(sentences, nlp):
  content = []
  for s in sentences:
    doc = nlp(s)
    # Write lang_images
    graph(doc, lang)
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

_zu_sentences = [
  "Im letzten Jahr hat er sich keine Reise leisten können.", # hat ... leisten können
  "Es hängt ganz von dir ab, ob du die Prüfung bestehst.",
  "Es ist mir wichtig, dich zu treffen.",
  "Der Krach von Straßenbauarbeiten ist nicht auszuhalten.", # ist nicht auszuhalten
  "Alter hat heute noch viel zu tun.", # hat ... zu tun
  "Ich habe vergessen, Natalie anzurufen.", # habe vergessen
  "Bei dieser Firma brauchst du dich gar nicht zu bewerben, die nimmt nur Leute mit abgeschlossener Ausbildung.", # brauchst ... zu tun
  "Der Verletzte war nur zu retten, indem er sofort operiert wurde.", # war ... zu retten
  "Das Kind ist zu kein, um die Frage zu beantworten.",
]

_oc_sentences = [
  "Je schnelleren Fortschritt man macht, desto mehr Lust hat man zu lernen.", # hat ... zu lernen
  "Ich möchte Sie bitten, nach 22 Uhr das Radio leiser zu stellen.", # möchte ... bitten 
  "Die helle Bluse passt gut zu dem Rock.",
  "Am Rand der kleinen Stadt ist ein Wald.",
  "Ich möchte Frau Müller, die ich dir gestern vorgestellt habe, zum Abendessen einladen.", # möchte ... einladen
  "Frau Li ist nicht gekommen, woraus wir geschlossen haben, dass sie krank ist.", # is ... gekommen
  "Der Autor verwendet alte Volkslieder, was dem Stück eine lyrische Note gibt.",
  "Wen ich nicht kenne, den grüße ich nicht.",
  "Ja, die beiden, die zusammen im Wohnmobil auf dem Schulparkplatz gewohnt haben.",
  "Wir werden sehen, welche verschiedenen Möglichkeiten es gibt?", # werden sehen
  "Ich heiße Thomas Bahr und ich bin der Vater von Lisa und Felix.",
]

_cross_sentences = [
  "Es hängt ganz von dir ab, ob du die Prüfung bestehst.",
  "Es ist mir wichtig, dich zu treffen.",
  "Er soll den Wecker dann so weit vom Bett weg stellen, dass er aufstehen muss, wenn der Wecker klingelt.",
  "Heute wollen wir über einige Probleme diskutieren, mit denen wir in Zukunft leben müssen.",
  "Schlagen Sie die Wörter im Wörterbuch nach, deren Bedeutung Sie nicht kennen!",
  "Wir haben alles erreicht, wofür wir gekämpft haben.",
  "Du solltest alles aufschreiben, was du für die Reise vorzubereiten hast.",
  "Herr Spätler hatte eine Alarmanlage gekauft, mit der er sein Haus gegen Einbrecher schützen wollte.",
  "Es ist möglich, dass es im Jahre 2020 auf der Erde 8 Milliarden Menschen gibt.",
  "Es ist toll, was wir in diesem Jahr erreicht haben.",
  "Ich begrüße Sie zum Seminar 'Geschichten erzählen' .",
  "In diesem Seminar lernen wir verschiedene Möglichkeiten kennen, wie man eine Geschichte spannend erzählen kann.",
]


#_sentences = _zu_sentences + _oc_sentences
#_sentences = _cross_sentences

#filename = "de_S01E05.json"
#_sentences = read_from_json(filename)


#_sentences = half_have_got_to_sentences 

filename = "es_test.json"
_sentences = read_from_json(filename)

#filename = "other"
#_sentences = other_sens


def _test_write_to_sen():
  with open('review_sens.txt', 'w') as f:
    for s in _sentences[:130]:
      f.write('"'+s+'",')
      f.write('\n')

def _test_structure_tbr():
  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  content = sen_structure(_sentences, nlp) 
  write_to_csv(["sentence", "analysis", "tbr"], content, csvfile="tbr/{}/{}.csv".format(lang, filename))


