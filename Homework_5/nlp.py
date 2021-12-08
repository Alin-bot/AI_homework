import lightrdf
import nltk
from nltk.stem import WordNetLemmatizer

NOUNS = ["NNP", "NNPS", "NN", "NNS"]
VERBS = ["VBN", "VBP", "VBZ", "VB", "VBD", "VBG"]


def exercise_2():
    parser = lightrdf.Parser()
    word_to_search = str(input("Please input a word:"))

    for triple in parser.parse("Homework_5/CSO.3.3.owl", base_iri=None):
        if word_to_search in triple[0] and "superTopicOf" in triple[1]:
            print(triple)


def find_index_of_tuple(sentence: list, word: tuple):
    position = 0
    for tuple_word in sentence:
        if tuple_word == word:
            return position
        position += 1


def exercise_3():
    with open("Homework_5/computer-science.txt", "r", encoding="mbcs") as f:
        text = f.read()
    result = open("Homework_5/sentences.txt", "a", encoding="mbcs")

    sentences = nltk.sent_tokenize(text)
    parsed_sentence = []

    for sentence in sentences:
        parsed_sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
        first_noun = -1
        last_noun = -1
        verb = -1
        for word in parsed_sentence:
            if word[1] in NOUNS:
                first_noun = find_index_of_tuple(parsed_sentence, word)
                break
        for word in reversed(parsed_sentence):
            if word[1] in NOUNS:
                last_noun = find_index_of_tuple(parsed_sentence, word)
                break
        for word in parsed_sentence:
            if word[1] in VERBS:
                verb = find_index_of_tuple(parsed_sentence, word)
                break
        if first_noun != -1 and last_noun != -1 and verb != -1:
            if first_noun < verb and verb < last_noun:
                result.write(sentence)

    result.close()


# 4)
def search_concept_in_ontology(word: str):
    parser = lightrdf.Parser()
    for triple in parser.parse("Homework_5/CSO.3.3.owl", base_iri=None):
        if word in triple[0] or word in triple[2]:
            return True
    return False


def exercise_4():
    lematized = open("Homework_5/concepts.txt", "a", encoding="mbcs")
    word_lemmatizer = WordNetLemmatizer()
    with open("Homework_5/sentences.txt", "r", encoding="mbcs") as f:
        extracted_text = f.read()

    parsed_sentence = []
    sentences = nltk.sent_tokenize(extracted_text)
    for sentence in sentences:
        parsed_sentence = nltk.pos_tag(nltk.word_tokenize(sentence))
        for word in parsed_sentence:
            if word[1] in NOUNS:
                if search_concept_in_ontology(word_lemmatizer.lemmatize(word[0])):
                    lematized.write(sentence)
                    break
    print("Done")
    lematized.close()


exercise_2()
# exercise_3()
# exercise_4()
