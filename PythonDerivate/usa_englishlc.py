from enum import Enum
from nltk import RegexpTokenizer
from nltk.corpus import cmudict
from nltk.corpus import wordnet
from nltk.wsd import lesk
from Interfaces.langbounds import LanguageBoundsInterface

class AmericanEnglishLangContext(LanguageBoundsInterface):
    """Defines the properties and implementation of standard American English."""

    ########## Variables ##########
    
    _SIMILARITY_THRESHOLD = 0.5 # The threshold that must be passed for a word to be considered similar. Scaled from 0-1.
    
    ###############################
    def getphenomes(self, arg):
        """Returns all phenome-lists related to the token."""
        pass

    def hypernyms(self, arg):
        """Returns all hypernyms related to the token."""
        pass

    def hyopnyms(self, arg):
        """Returns all hyponyms related to the token."""
        pass

    def leskequivalent(self, origin, arg):
        """Returns the context related to the token."""
        pass

    def messagefail(self, input):
        """Produces the fail message to print to users in this language if the process cannot return a value."""
        built = " ".join(input)
        return ("Your input: '" + built + "' was not able to be parsed under the conditions you desired. Please try new conditions or try a new phrase.")

    def messageonlyresult(self, arg):
        """Produces a indicator message if only one result was possible from the input parameters given."""
        return ("This is the only result processed from the given input:\n" + arg)
    
    def messagetopresult(self, resultlen, requestedresultcount):
        """Produces the top 'x' results message to users in this language if the process has multiple results."""
        if resultlen < requestedresultcount:
            return ("Top " + str(resultlen) + " result(s):\n")
        else:
            return ("Top " + str(requestedresultcount) + " result(s):\n")

    def similarity(self, contextclues, arg1, arg2):
        """Returns a key-value pair for scoring similarity. [0] a bool that determines if the word is similar enough to satisfy language criteria
        and the score associated with the evaluation."""

        evaluation = False
        score = 0

        if arg1 is arg2:
            evaluation = True
            score = 0.8 # Penalizing score to prevent paraphrases from returning themselves

        else:
            contextA = lesk(contextclues, arg1)
            contextB = lesk(contextclues, arg2)

            if contextA and contextB: # Otherwise score will stay zero
                score = contextA.path_similarity(contextB)

                if score is not None and self._SIMILARITY_THRESHOLD <= score:
                    evaluation = True

        return (evaluation, score)

    def split(self, arg):
        # Returns all non-whitespace tokens.
        return RegexpTokenizer('\w+|\$[\d\.]+|\S+').tokenize(arg)