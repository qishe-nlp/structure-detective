import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
from importlib import import_module
import os.path, pkgutil

lang = "en"
pkg = PKG_INDICES[lang]

#_sentences = read_from_json("{}_sens/test_{}_{}.json".format(lang, lang, "verb")) 

_sentences = [
]

_unsure_sens = [
  "I found this answer wrong.",
  "The day is short, for it is now December.",
  "I like eating fish and chicken.",
  "We bought a present for Granny, but she didn't like it.",
  "Mother is cooking in the kitchen, while father is watching TV in the sitting room.",
  "I usually walk to school, but by bus when it rains.",
  "It was obvious that the meeting was concerned with the housing reform and everyone present was concerned for their own interests.",
  "What boring films!",
  "Mr. Smith bought a small black leather purse for his wife.",
  "Who do you think is the funniest actor?",
  "It' s a great TV program whose purpose is to bring the habit of reading back into the public.",
  "John invited about 40 people to his wedding, most of whom are family members.",
  "After the flooding, people were suffering in that area, who urgently needed clean water, medicine and shelter to survive.",
  "I have news for you. It is good news.",
  "Let's go and help her.",
  "One is white, the other is black.",
  "Either is OK, I don't mind.",
  "Who is that tall woman?",
  "Almost two thirds of the students in this class wear glasses, that is 60 percent of them.",
  "It's a most beautiful one, I think.",
  "Not only you are funny, but also you are witty.",
  "The first was not good, neither was the second.",
  "One step more and you are a dead man.",
  "It is raining hard, however we have to go out.",
  "He is not a miser, on the contrary, no one could be more generous.",
  "While I like the colour of the hat, I do not like its shape.",
  "I had a headache, so I went to bed.",
  "We bought a present for Granny, but she didn't like it.",
  "My shoes are worn out, so I need new ones.",
  "The day is short, for it is now December.",
  "Is your teacher always in class on time?",
  "A warm thought suddenly came to me that I might use the pocket money to buy some flowers for my mother's birthday.",
  "News came from the school office that Wang Lin had been admitted to Beijing University.",
]


_cop_adv_sens = [
  "I am really proud of my group because we're always discussing and sharing study secrets together.",
  "It's very important for us to make a plan before a new term begins.",
  "If there were no air or water, there would be no living things on the earth.",
  "As we all know, typing is a tiring job.",
  "It's sometimes embarrassing when you have to ask people for money.",
  "It's really annoying when a train is late and there's no explanation.",
  "We were very shocked when we heard the news.",
  "Dad was so exhausted when he came home from work.",
  "I was really amazed when I was offered it.",
  "When they heard the surprising news, they were surprised to look at each other.",
  "All of us were excited when we watched the exciting football match.",
  "Although this dish isn't so delicious as that one, it is more expensive than that one.",
  "Is Lily's home farther away from school than Linda's?",
  "The nearest one is about 90 miles away.",
  "It will be four days before they come back.",
  "I have been in Beijing since you left.",
  "He is absent today, for he is ill.",
  "It's not easy for Tom to find a job because he has been in prison for many years.",
  "His mother was angry, because he did the worst job in examination in his class.",
]

_half_aux_sens = [
  "To make your DIY work perfect, you'd better not start before you get all the tools ready.",
  "Seeing that it's raining, we'd better stay indoors.",
  "Now that you are here, you’d better stay.",
  "Men are happy in proportion as they are virtuous.",
  "Nokia, the world's largest mobile phone producer, is going to find a new research center in China.",
  "They're going to have a farewell party this evening.",
  "I was going to pay by cash when it suddenly occurred to me that I had left my purse at home.",
]

_verb_prep_sens = [
  "I looked through my test paper again and again so that I wouldn't make any mistakes.",
  "I could look after myself when I was five.",
  "Don't worry about your daughter, she can look after herself well.",
  "It depends on hard work more than luck whether you can make your dream come true.",
]

_cop_verb_sens = [
  "Laws that punish parents for their little children's actions against the laws get parents worried.",
]

_obj_adv_sens = [
  "My shoes are worn out, so I need new ones.",
  "Lin Tao, an 8-year-old boy, was very brave and helped his classmates run out of the classroom when the earthquake happened.",
  "On the one hand I have to work, on the other hand, I have a great many visitors.",
  "I don't know much about China, therefore I can't advise you about it.",
  "Jen hadn’t enjoyed the play; as a result, she didn't recommend it.",
]


#_sentences = _sentences + _unsure_sens
#_sentences = _sentences + _half_aux_sens


_sentences = _sentences + _verb_prep_sens
#_sentences = _sentences + _cop_verb_sens
#_sentences = _sentences + _obj_adv_sens

#_sentences = _sentences + _cop_adv_sens

def test_en_structure():
  sentences = _sentences

  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  display_structure(sentences, nlp)

