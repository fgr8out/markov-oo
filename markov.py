import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        
        word_bucket = ""
        #loop through each file name and loop them all together
        for filename in filenames:
            text_file = open(filename).read()
            word_bucket = word_bucket + text_file

        # print word_bucket
        
        self.make_chains(word_bucket)

    def make_chains(self, corpus):
        chains = {}

        words = corpus.split()
        # print words 

        for i in range(len(words) - 2):
            key = (words[i], words[i +1])
            value = words[i + 2]

            if key not in chains:
                chains[key] = []

            chains[key].append(value)

        self.chains = chains

        """Takes input text as string; stores chains."""

        # your code here
        #print corpus

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""

        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        test = " ".join(words)
        print test




       #print self.chains       



if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    arguments = sys.argv
    
    # we should make an instance of the class
    generator = SimpleMarkovGenerator() 
    # we should call the read_files method with the list of filenames
    generator.read_files(arguments[1:])
    # we should call the make_text method 5x
    generator.make_text(self.chains)

    pass

