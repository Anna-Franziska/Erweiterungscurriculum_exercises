# Exercise 6
def transform_to_row(infile, outfile):
    with open("infile.txt", "r") as reader:
        f = reader.readlines()
        for line in f:
            f = line.split(",")

    with open("outfile.txt", "w") as writer:
        for line in f:
            writer.write(line + "\n")


def add_greeting(infile, outfile):
    with open("infile.txt", "r") as reader:
        f = reader.readlines()
    with open("outfile.txt", "w") as writer:
        for line in f:
            writer.write("hello" + line)


def strip_greeting(infile, outfile):
    with open("infile.txt", "r") as reader:
        f = reader.readlines()
        strip_the_greeting = []
        for line in f:
            strip_the_greeting.append(line.strip("hello"))

    with open(outfile, "w") as writer:
        for line in strip_the_greeting:
            writer.write(line)


def combine_files(file1, file2, outfile):



#Exercise 7
import random
from nltk.corpus import names, wordnet

def generate_names(char, num):
    male_names = names.words("male.txt")
    female_names = names.words("female.txt")

    male_names_filtered = [(n, "male") for n in male_names if n[0].lower() == char.lower()]
    female_names_filtered = [(n, "female") for n in female_names if n[0].lower() == char.lower()]

    n_male_names = choose_n_random(male_names_filtered, num)
    n_female_names = choose_n_random(female_names_filtered, num)

    write_names_file(n_male_names, char, num, "male")
    write_names_file(n_female_names, char, num, "female")

    return n_male_names + n_female_names


def choose_n_random(l, n):
    if n <= 0:
        return list()  #if n value is larger than the list return the whole list instead

    if n >= len(l):
        return l

    choices = list()
    while len(choices) != n:
        c = random.choice(l)
        if c not in choices:
            choices.append(c)

    return choices


def write_names_file(l, char, num, gender):
    with open(f"{char.upper()} names-{gender}-{num}.txt", "w") as male_file:
        for n in l:
            line = f"{n[0]}\n"
            male_file.write(line)


class SynAnt:
    wordlist: list

    def __init__(self, wordlist):
        self.wordlist = wordlist


    def output(self):
        synyms = syn.find_synonyms()
        anyms = syn.find_antonyms()

        all_words = {
            word: {
                "Synonyms": synyms[word],
                "Antonyms": anyms[word]
            }
            for word in self.wordlist
        }

        for word in all_words:
            nice_synonyms = ", ".join(all_words[word]["Synonyms"])
            nice_antonyms = ", ".join(all_words[word]["Antonyms"])
            o = f"{word}:\n\tSynonyms: {nice_synonyms}\n\tAntonyms: {nice_antonyms}"  #organizes the output more
            print(o)



    def find_synonyms(self):
        synonyms = {
            # word: [list of synonyms]
            word: list()
            for word in self.wordlist
        }
        for word in self.wordlist:
            # find synonyms
            synsets = wordnet.synsets(word)

            for synset in synsets:
                for lemma in synset.lemmas():  #lemma helps find the dictionary form of a word
                    synonym = lemma.name()
                    if synonym not in synonyms[word]:
                        synonyms[word].append(synonym)

        return synonyms

    def find_antonyms(self):
        antonyms = {
            # word: [list of antonyms]
            word: list()
            for word in self.wordlist
        }

        for word in self.wordlist:
            # find synonyms
            synsets = wordnet.synsets(word)
            for synset in synsets:
                for lemma in synset.lemmas():
                    if lemma.antonyms():
                        for antonym in lemma.antonyms():
                            a = antonym.name()
                            if a not in antonyms[word]:
                                antonyms[word].append(a)

        return antonyms

















