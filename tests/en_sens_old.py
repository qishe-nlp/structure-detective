_cop_adv_sens = [
  #"It's not easy for Tom to find a job because he has been in prison for many years.",
  #"Is your teacher always in class on time?",
  #"I am really proud of my group because we're always discussing and sharing study secrets together.",
  #"It's very important for us to make a plan before a new term begins.",
  #"Stephen Hawking was famous as a scientist.",
  #"If there were no air or water, there would be no living things on the earth.",
  #"As we all know, typing is a tiring job.",
  #"It's sometimes embarrassing when you have to ask people for money.",
  #"It's really annoying when a train is late and there's no explanation.",
  #"We were very shocked when we heard the news.",
  #"Dad was so exhausted when he came home from work.",
  #"I was really amazed when I was offered it.",
  #"When they heard the surprising news, they were surprised to look at each other.",
  #"All of us were excited when we watched the exciting football match.",
  #"Although this dish isn't so delicious as that one, it is more expensive than that one.",
  #"Is Lily's home farther away from school than Linda's?",
  #"The nearest one is about 90 miles away.",
  #"It will be four days before they come back.",
  #"I have been in Beijing since you left.",
  #"He is absent today, for he is ill.",
  #"Men are happy in proportion as they are virtuous.",
  #"His mother was angry, because he did the worst job in examination in his class.",
]

_compound_sens = [
  "We bought a present for Granny, but she didn't like it.",
  "Mother is cooking in the kitchen, while father is watching TV in the sitting room.", # < compound
  "My shoes are worn out, so I need new ones.", # compound
  "The day is short, for it is now December.", # < compound
  "I usually walk to school, but by bus when it rains.", # compound
  "One is white, the other is black.", # compound
  "Either is OK, I don't mind.", # compound
  "Almost two thirds of the students in this class wear glasses, that is 60 percent of them.", # compound ?
  "Not only you are funny, but also you are witty.", # compound 
  "The first was not good, neither was the second.", # compound
  "One step more and you are a dead man.", # PASS
  "It is raining hard, however we have to go out.", # compound
  "He is not a miser, on the contrary, no one could be more generous.", # compound
  "While I like the colour of the hat, I do not like its shape.", # < compound
  "I had a headache, so I went to bed.", # compound
  "On the one hand I have to work, on the other hand, I have a great many visitors.", # compound
  "I don't know much about China, therefore I can't advise you about it.", # compound
  "Jen hadn’t enjoyed the play; as a result, she didn't recommend it.", # compound
]

_cop_verb_sens = [
  "Laws that punish parents for their little children's actions against the laws get parents worried.",
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

_verb_prep_sens_1 = [
  "The war broke out in 1939",
  "She didn't want to fall behind in her studies.",
  "How did the accident come about?",
  "The wind has died down a bit.",
]

_verb_prep_sens_2 = [
  "He could not account for his absence from school.",
  "I called on her this morning.",
  "I ran across her in the library yesterday.",
  "You'd better wait and watch for a better chance.",
]

_verb_prep_sens_3 = [
  "He is trying to bring about a reconciliation",
  "I'll try to hurry him up.",
  "The trolley-bus stopped to put down three passengers.",
  "They are going to knock down those old houses",
  "Don't build on his promises",
  "He talked me into changing my job",
  "They showed her around the house",
  "She set the children against their father.",
]


_verb_prep_sens_4 = [
  "I can't put up with these noisy people.",
  "You might come up against a bit of opposition",
  "Don't look down on this kind of work.",
  "I'm looking forward to her arrival.",
]

_unsure_sens = [
  "Lin Tao, an 8-year-old boy, was very brave and helped his classmates run out of the classroom when the earthquake happened.",
  "Who is that tall woman?",
  "Let's go and help her.",
  "I found this answer wrong.",
  "What boring films!",
  "I like eating fish and chicken.",
  "It was obvious that the meeting was concerned with the housing reform and everyone present was concerned for their own interests.",
  "Mr. Smith bought a small black leather purse for his wife.",
  "Who do you think is the funniest actor?",
  "It' s a great TV program whose purpose is to bring the habit of reading back into the public.",
  "John invited about 40 people to his wedding, most of whom are family members.",
  "After the flooding, people were suffering in that area, who urgently needed clean water, medicine and shelter to survive.",
  "I have news for you.",
  "It's a most beautiful one, I think.",
  "A warm thought suddenly came to me that I might use the pocket money to buy some flowers for my mother's birthday.",
  "News came from the school office that Wang Lin had been admitted to Beijing University.",
]

_to_sens = [
  "Someone is asking to see you.",
  "We can't afford to pay such a price.",
  "I don't wish to leave my mother",
]

_doing_sens = [
  "Would you mind waiting a few minutes?",
  "I don't recommend buying that book.",
  "Do you like reading novels?",
]

_clause_sens = [
  "I guess we'll leave now.",
  "I didn't know where they had gone.",
  "I will tell you what I hear.",
  "I will make you pretty."
]

_copula_sens = [
  "She remained standing for a good hour.",
  "She didn't look convinced.",
  "The prisoner broke free.",
  "The teachers have returned safe and sound.",
  "I still stand your friend.",
  "They parted the best of friends.",
  "Don't act the fool",
  "I was very sorry to hear that you were ill.",
  "I am glad that you are here."
]

#_sentences = _sentences + _cop_adv_sens #DONE

#_sentences = _sentences + _compound_sens

#_sentences = _sentences + _cop_verb_sens

#_sentences = _sentences + _half_aux_sens
#_sentences = _sentences + _verb_prep_sens
#_sentences = _sentences + _unsure_sens

#_sentences = _sentences + _verb_prep_sens_1
#_sentences = _sentences + _verb_prep_sens_2
#_sentences = _sentences + _verb_prep_sens_3
#_sentences = _sentences + _verb_prep_sens_4
#_sentences = _sentences + _to_sens
#_sentences = _sentences + _doing_sens
#_sentences = _sentences + _clause_sens
#_sentences = _sentences + _copula_sens


