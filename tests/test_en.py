import spacy
from structure_detective import PKG_INDICES
from tests.lib import *
from importlib import import_module
import os.path, pkgutil
from tests.en_sens import *
lang = "en"
pkg = PKG_INDICES[lang]

#_sentences = read_from_json("{}_sens/test_{}_{}.json".format(lang, lang, "verb")) 

#_sentences = s_13_2_1 
_sentences_2_3 = [ # need enumeration
  "Her temperature came down in the morning.", # pending: down -> svp
  "The scheme fell through.", # pending: fell -> svp
]

_sentences_2_4 = [
  "The door blew open.", # pending: 动状
]

_sentences_3_1_a = [
  "Shall I call a taxi?", # done: The punct was wrong as period, so we are fine.
]

_sentences_3_1_b = [
  "We'll make room for you in the back of the car.", # pending: prep for + pron consider as a mark
  "She's always making trouble for her friends.", # pending: prep for as a mark
] 

_sentences_3_2_b = [
  "She busied herself tidying up her desk.", # done: xcomp rule
  "Don't strain yourself talking, dear.", # done: xcomp rule
]

_sentences_3_3 = [
  "They were to dance the Rose-dance together.", # pending: half aux (xcomp rule - were to)
]

_sentences_3_4_a = [
  "She has put aside a good sum of money.", # pending: aside -> svp
  "All the chestnut trees have put forth blossoms.", # pending: forth -> svp 
  "I'll put the particulars down in my notebook.", # pending: down -> svp
]


#_sentences_3_4_b = s_13_3_4_b

_sentences_3_4_b = [
  "We must abide by the rules of the game.", # pending: abide by
  "The Yellowston Park abounds in wild animals.", # pending: abound in
  "They will not agree to that arragement.", # pending: agree to
  "I called upon Mrs. Froster this evening.", # pedning: call upon
  "She's been looking after the luggage.", # pending: look after
  "He was looking for summer employment.", # pending: look for
  "We'll look into this matter together.", # pending: look into
  "He came on an old friend in the library.", # pending: come on
  "I don't object to the idea.", # pending: object to
  "Her suggestion met with opposition.", # pending: meet with
  "He thought of his boyhood.", # pending: think of
  "Light consists of waves.", # pending: consist of
  "The baby was looked after by her little sister.", # pending: look after
  "Many difficulties and setbacks will be met with.", # pending: meet with
]


#_sentences_3_4_d = s_13_3_4_d

_sentences_3_4_d = [
  "We shouldn't look down on his work.", # pending: look down on
  "The children were eargerly looking forward to the party.", # pending: look forward to
  "Look out for snakes.", # pending: look out for
  "The window looks out on the flower-beds.", # pending: look out on
  "He will carry on with his plan.", # pending: carry on with
  "We must catch up with them.", # pending: catch up with
  "The teacher came down on me for talking in class.", # pending: come down on
  "Many Congressmen came out against the bill.", # pending: come out against
  "This town dates back to Roman times.", # pending: date back to
  "They have done away with this barbarous custom.", # pending: do away with
  "We must face up to our difficulties.", # pending: face up to
  "He doesn't feel up to the job.", # pending: feel up to
  "They are looked down on by everyone.", # pending: look down on
  "The day had been looked forward to for a month.", # pending: look forward to
  "These priviledges must be done away with.", # pending: do away with
  "The truth has to be faced up to.", # pending: face up to
]

_sentences_3_4_e = [
  #"He made no reference to Peter.", # pass 
  "No reference was made by anyone to the past.", # cross problem
  "Preparations are being made for the sports meet.", # cross problem
] 

_sentences_3_4_f = [
  "He had to accustom himeself to the cold weather here.", # pending: half aux
  "She has to familiarize herself with the use of the new tool.", #  # pending: half aux
]

_sentences_3_5_b = [
  "Ask him where to go.", # done: add xcomp rule
]

_sentences_3_7_a = [
  "We have to admit that he's a highly competent man.", # pending: half aux
]

_sentences_3_8_c = [
  "I'll tell you what I hear.", # done: add ccomp rule 
]

_sentences_4_1_a = [
  "Please throw the key to me.", # done: It is OK now
  "I'll phone the news to her.", # pass: hard to handle
]

_sentences_4_1_b = [
  "She'll find a situation for you.", # pass: dependecy tree, semantics meaning 
  "That will save a lot of trouble for us.", # pass: hard to handle 
]

_sentences_4_1_c = [
  "She still bore a grudge against him.", # pass: dependecy tree, semantics meaning
  "She kissed her mother goodbye.", # pass: minor problems 
  "I'll stay and keep you company.", # pass: could be right
]

# 双宾语, iobj, dobj
_sentences_4_2_a = [ # done
  "Tell him I'm out.",
  "I'll call Betty and remind her that we are meeting at 8.",
  "Our teacher notified us that there would be a test on Monday.",
  "She informed me that she was to send for it the next day.",
  "He assured the passengers that there was no danger.",
  "I promise you I'll never conceal anything any more.",
  "He instantly convinced himself that it was so.",
  "She wrote Tom that she was coming to Paris.",
  "I have warned him that it is not allowed.",
  "She persuaded them that she had done right.",
]

_sentences_4_2_b = [ #done
  "Can you inform me where Miss Green lives?",
  "I can't tell you how pleased I am to be here tonight.",
  "She asked me what time it was.",
  "Write me how you got through.",
  "Show me where your leg hurts.",
  "He taught us why we should love our country.",
  "Please advise me whether I ought to go with them.",
]

_sentences_4_2_c = [ # done
  "Show me what you bought.",
  "I'll tell you what I read in today's paper.",
  "Give me what books you have on the subject.",
  "Tell me whatever you know about it.",
]

_sentences_5_1_a = [ # copula
  "You're not looking very well.", # pass: hard to deal
  "The medicine tastes awful.", # done: tasks -> tastes
  "She appeared calm.", # done: add appear to copula
]

_sentences_5_1_b = [ # copula
  "The sea is growing calm.", # done: add grow to copula
  "She went pale at the news.", # done: add go to copula
  "Things will come right in the end.", # pass: hard to deal
  "When he saw this, his blood ran cold.", # done: add run to copula
  "He has fallen ill.", # done: add fall to copula
]

_sentences_5_1_c = [ # copula
  "They stayed awake to see the eclipse.", # done: add stay to copula
  "Jennie, alone, kept silent.", # done: add keep to copula
  "His temper continued very uncertain.", # pass: hard to deal
  "This law holds good.", # done: add hold to copula
]

_sentences_5_1_d = [ # copula
  "He nearly got hit by that car.", # pass: could be right
  "After a time I grew dissatisfied with the work.", # done: add grow to copula
]

_sentences_5_1_e = [ # copula
  "The rent falls due today.", # pass: add fall to copula
]

_sentences_5_2_a = [ # copula
  "He stood there and felt a stranger.", # pass: hard to deal
  "The affair rests a mystery.",  # done: add rest to copula
  "He appeared a fool.", # done: add appear to copula
  "He fell victim to her charms.", # done: add fall to copula
]

_sentences_5_2_b = [
  "From these debates the Prime Minister emerged victor.", # question ? # copula VS adv
  "They parted the best of friends.", # pass: hard to deal
  "She often played the great lady.", # pass: hard to deal
]

_sentences_5_3_a = [ # adv
  "I have been out for a walk.", # pass: could be right 
  "But I've got to be off now.", # done: adjust xcomp rule
  "If he's not here, he's about somewhere.", # done: adjust advcl rule
  "She had been away on a long trip.", # pass: could be right
  "I'll be down immediately.", # pass: hard to deal
  "The television was still on.", # pass: hard to deal
  "He was up all night with sick child.", # pass: hard to deal 
  "When will you be back?", # done: add pos restriction
]

_sentences_5_4_a = [ # adv
  "She was beside herself with joy.", # pass: hard to deal
  "She is out of work on strike.", # pass: hard to deal
]

_sentences_5_4_b = [ # copula
  "They remained in sad poverty.", # done: refine prep rule
  "He seemed on the watch to control himself.", # pass
  "He looked in splendid health.", # done
  "It has grown out of date.", # done
  "They ran out of petrol.", # pass
]

_sentences_5_4_c = [ # copula
  "This book may be of use to you.", # pass
  "We must get in touch with her.", # done
  "Soon he fell in love with her.", # pass
  "He seemed out of touch with the outside world.", # done
]

_sentences_5_6_b = [ # copula
  "Buying such a white elephant is simply wasting money.", # pass: could be right
  "Talking to him is talking to a wall.", # pass: dependency tree error
  "Doing that would be playing with fire.", # pass: could be right
]

_sentences_5_7_a = [ # done: add rule in root
  "Their first idea was that he had hidden it.",
  "My opinion is that the plan won't work.",
  "His view is that it's better not to increase investments.",
  "The fact is, I never liked him.",
  "His only fault is that he lacks ambition.",
  "The reason for my lateness is that I missed my bus.",
  "The only trouble is the plan won't work.",
  "What surprised me was that he spoke English so well.",
]
  

_sentences_5_7_b = [ # done: add rule in root
  "The question is what you want to do.",
  "The problem is who can be put in charge of the job.",
  "What I want to know is how we can solve the fuel problem.",
  "That's how I look at it.",
]

_sentences_5_7_c = [ # done: add rule in root
  "That's what I wish to do.",
  "That's what I'm here for.",
  "Power is what they are after.",
  "Times aren't what they were.",
]

_sentences_5_8_a = [ # copula
  "She was delighted with the boat.", # pass: could be right
]

_sentences_5_8_b = [ # copula
  "I've grown accustomed to traveling.", # done: add grow to copula
  "Your exam results fell short of our expectations.", # pass: could be right
]

_sentences_5_9 = [ # copula
  "I'm inclinded to think she's right.", # pass: could be right
]

_sentences_5_10_a = [ # copula
  "I'm convinced that he knew the truth.", # pass: could be right
  "The team feels proud that it has won every match this year.", # done: add feel in copula
]

_sentences_5_10_b = [ # copula
  "We're not clear yet what they're up to.", # pass: could be right, caused by "yet"
]

#_copula_adv_sentences = _sentences_5_1_a + _sentences_5_1_b + _sentences_5_1_c + _sentences_5_1_d + _sentences_5_1_e \
#                      + _sentences_5_2_a + _sentences_5_2_b + _sentences_5_3_a \
#                      + _sentences_5_4_a + _sentences_5_4_b + _sentences_5_4_c  + _sentences_5_6_b \
#                      + _sentences_5_7_a + _sentences_5_7_b + _sentences_5_7_c \
#                      + _sentences_5_8_a + _sentences_5_8_b + _sentences_5_9 + _sentences_5_10_a + _sentences_5_10_b


#_2obj_sentences = _sentences_4_*


# _svp_sentences = _sentences_2_3 + _sentences_3_4_a



# cross problem:
#_cross_sentences = _sentences_3_4_e


# enumerate rule: set to root

# 3_4_b: 
#   1 followed token has dep prep, head is root
#   2 followed token has only one child pobj or none
#   3 the phrase matches enumeration set

# 3_4_d:
#   1 the first followed token has dep prep, advmod, prt, head is root
#   2 the second followed token has dep prep
#   3 head of the second followed token is root or the first followed token
#   4 the second followed token has only one child pobj or none
#   5 the phrase matches enumeration set
#_verb_phrase_sentences = _sentences_3_4_b + _sentences_3_4_d


# half_have_to:
#   1 phrase is 'have to'
#   2 followed token has dep aux and dep of its head is xcomp and its head's head is root


# half_have_got_to
#   1 text of root is got
#   2 root has aux child with lemma have
#   3 followed token has dep aux and dep of its head is xcomp and its head's head is root

# half_be_going_to
#   1 text of too is going
#   2 root has aux child with lemma be
#   3 followed token has dep aux and dep of its head is xcomp and its head's head is root

#_half_aux_sentences = _sentences_3_4_f + _sentences_3_7_a + _sentences_3_3


# TODO: others
#_xcomp_rule

_xcomp_sens = [
  "It just goes to show there are no rules when it comes to crawling.", # xcomp
  "Stop teasing me.", # xcomp
  "This time, how we learn to move in ways no other animal can.", # xcomp
  "The moment James starts to take control of his body.", # xcomp
  "From now on, his mum, Nikita, will need to keep an eagle eye on him.", # xcomp
  "a baby's next physical struggle is trying to sit up.", # xcomp
  "But not everyone seems to realize it's a race.", # xcomp
  "The pincer grip can take years to perfect.", # xcomp
  "they need to stop relying on them to get around.", # xcomp
  "Learning to walk.", # xcomp 
  "After three weeks, he's taught himself to stand.", # xcomp
  "His next breakthrough is learning to cruise,", # xcomp
  "His biggest challenge will be learning to ride a reindeer.", # xcomp
  "And first, he'll need to be able to get onto one.", # xcomp
  "This time, dad breaks down how to get on step by step.", # xcomp
  "Now keep pulling like this and we'll head home.", # xcomp
  "As we approach 2,000 days, we're beginning to physically excel.", # xcomp
  "But no matter how hard she tries, she keeps losing her balance.", # xcomp
  "The temptation is to look down at her feet.", # xcomp
  "What's difficult is getting them in the right order and at the right time.", # xcomp
]

_ccomp_sens = [
  "Theo has discovered he's equipped with the perfect tools", # ccomp
  "he'll find it easier to balance", # ccomp
  "Let me tie it from here.", # let ccomp
  "Let's start with a small reindeer.", # let ccomp
  "If you pull on the reins you'll make it stop.", # ccomp
  "Let's make a swimming pool", # ccomp
  "it allows us to trust our body...", # ccomp
]

_copula_sens = [
  "But for now, he's not going anywhere.", # copula verb, be going to
  "Don't just stay there with your toys.", # copula verb
  "Holding their breath for up to three minutes at a time.", # copula verb
  "he's on the move for two and a half hours every day.", # copula + prep 
  "Look at that balloon.", # copula
  "It might not look like much,", # copula + prep
  "Look at my robot.", # copula
  "Rufus, should we go for a walk?", # copula
  "A child's first steps hold a special place in every culture.", # copula
  "You fell on all your toys.", # copula verb
  "How are you feeling, Eva?", # copula
  "For us, moving isn't just about surviving.", # copula + prep
]

_npadvmod = [
  "You've learnt it, my boy.", # npadvmod
]

_gonna_sens = [
  "James, it's gonna be a great day today.", # gonna 缩写
  "It's gonna be fun.", # gonna
]


#_ccomp_rule

def test_en_structure():
  #sentences = half_had_better_sentences + half_had_best_sentences
  #sentences = _sentences_3_4_b
  #sentences = _sentences_3_4_d
  #sentences = _half_aux_sentences
  #sentences = half_have_to_sentences
  #sentences = half_have_got_to_sentences
  #sentences = half_be_going_to_sentences
  sentences = subtitle_sens 

  nlp = spacy.load(pkg)
  nlp.add_pipe('structure')
  display_structure(sentences, nlp)

