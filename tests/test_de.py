import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
#from tests.constants import tbr_en_sentences as _sentences
from importlib import import_module
import os.path, pkgutil

lang = "de"
pkg = PKG_INDICES[lang]

#_sentences = read_from_json("{}_sens/test_{}_{}.json".format(lang, lang, "prep")) 

_sentences = [
  "Bis zum Kongress, hast du gesagt, wegen der vielen Arbeit.",
  "was für ein glühender Theaterfreund du inzwischen geworden bist.",
  "Das könnte doch der Durchbruch sein.",
  "Für die japanische Delegation sind die Sprachkenntnisse des Dr. Kitasatos wichtig.",
  "Meine eingeschlossen.",
  "Ist hoffentlich nicht mangels Neuigkeiten aus dem Bereich der Bazillen geschuldet.",
  "Die Bedeutung eines Vortrags bemisst sich wohl kaum an seiner Länge.",
  "Wie geht's",
  "Unverändert.",
  "Wie, Sie können nicht?",
  "Ich kann nicht weg.",
  "Haben Sie an so einem Tag nichts Besseres zu tun, als mit einem Hammel spazieren zu führen?",
  "Danke der Nachfrage.",
  "Lieber wäre ich bei der Kongresseröffnung.",
  "Mein Hinweis war die Geburt der Nächstenliebe.",
  "solange fast alle Ärzte außer Haus sind.",
  "Sie werden diese Entwicklung nicht aufhalten können, Verehrteste!",
  "Ich halte ja große Stück auf ihn.",
  "Möge diese Schlachtenreihe der Besten",
]


_sentences = [
  "Reißen Sie sich mal zusammen, Tischendorf, vergessen Sie für ein Moment Ihre Hilfswärterin.",
  "Zu Recht nennen wir die Tuberkulose die größte Geißel der Menschheit.",
  "Aber der Pastor ist nicht da.",
  "Jeder Schlachter könnte das, da muss man kein Arzt sein.",
]

_sentences = [
  "Aber es ist sonst niemand da.",
  "Bitte drängen Sie nicht weiter.",
  "Das ist kein schöner Anblick, aber die einzige Möglichkeit, das tote Kind zu holen.",
  "Möchten Sie wirklich einen so großen Abstand zwischen sich einer bürgerlichen Ehe bringen?",
]


_sentences = [
  "Wo war dann Ihre Ritterlichkeit, als wir Sie im Kreißsaal gebraucht haben.", # re wrong
  "Weil Sie eine Fleischwunde haben?", # AUX VS VERB
  "Ich möchte aber keine Diakonisse werden.", # mo
  "Lassen Sie uns das vergessen.", # dependency tree wrong, morph
  "Die Gelder sind so gut wie bewilligt.", # dependency tree wrong
  "Na wie klingt das?", # add restriction with POS
  "Hier steht alles Kopf wegen deines Heilmittels.", # OK
  "Ich bin die ganze Nacht auf gewesen und habe auf dich gewartet.", # dependency tree wrong
  "Du wirst es nicht wagen, Robert,", # OK
  "Ich denke, uns trennt doch mehr, als uns verbindet.", #OK
  "Es hat schon einen Grund, dass wir Diakonissen keine weltliche Bindung eingehen sollen.", # AUX VS VERB
  "Bitte treten Sie vor!", # morph
  "Also bitte, verlassen Sie den Hörsaal.",  # morph
  "Die Frau steht in aller Beziehung dem Kind näher als dem Mann.", #OK
  "Schau mal Mama, ich kann das ganz allein.", # add restriction of POS
  "Nein, nein, lass nur, das mache ich selber",# add restriction of POS
  "Wer will schon einen Jungen?", # MODAL VS VERB
  "Komm, wir lassen die beiden alleine.", # handle dm
  "Der Ärztekongress stand Kopf, hat man mir erzählt.", # oc recursive
  "Sie müssen enttäuscht sein, dass ich mich nicht persönlich bei Ihnen abgemeldet habe, aber...", # unmet
]

def test_de_structure():
  sentences = _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  display_structure(sentences, nlp)

