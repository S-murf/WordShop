from enum import Enum
from nltk import RegexpTokenizer
from nltk.corpus import cmudict
from nltk.corpus import wordnet
from nltk.wsd import lesk
from Interfaces.langbounds import LanguageBoundsInterface

class AmericanEnglishLangContext(LanguageBoundsInterface):
    """Defines the properties and implementation of standard American English."""

    ########## Variables ##########
    
    _cmu = cmudict.dict() # Pretrained phenome generation model. Created outside of methods because it is used over iteration(s) and is expensive to generate; TREAT THIS VALUE AS AN IMMUTABLE.
    _MULTI_TOKEN_INDICATOR = "_" # Character used to identify when a token has multiple words. This functionality is specific to a corpus. Must be changed if corpus is changed.
    _NULL_PHENOME_INDICATOR = "*NONE*" # Used by algorithm to indicate if a corressponding phemone could not be found for a token
    _SIMILARITY_THRESHOLD = 0.2 # The threshold that must be passed for a word to be considered similar. Scaled from 0-1.
    vowelphenomes = ["AA", "AE", "AH", "AO", "AW", "AY",
                    "AX", "AXR", "EH", "ER", "EY", "IH",
                    "IX", "IY", "OW", "OY","UH", "UW", "UX"] # Contains all phenomes that produce vowel-related sounds for this language.
    
    ###############################

    def _getproperformattype(self, unformattoken):
        """Used to parse through the Wordnet sysnet-token return value to retrieve only relevant sections. Currently the only returns the word.
        In future implementations, this function may not be needed if the corpus has a function to return only the word as a string."""

        name, junk = unformattoken.name().split(".", 1);
        return name

    def _getproperhandlemissingphenome(self, unknowntoken):
        """Takes a unknown-phenome (a token which could not be evaluated by CMUdict) and attempts to generate a phenome. If CMUdict or
        Wordnet implementation is changed this function MUST be changed."""

        finaleval = []

        # After various testing, it has been determined that calculating for two letters yields the most consistent results for unknown phenomes.
        tokenlen = len(unknowntoken)
        if tokenlen is 0:
            finaleval.append([self._NULL_PHENOME_INDICATOR])
        elif tokenlen is 1:
            finaleval.append([unknowntoken.upper()]) # The letter IS the phenome
        else:
            relevant = unknowntoken[:2] # get first two chars
            finalattempt = self._cmu.get(relevant, None)

            if finalattempt is None: # No possible phenome can be generated by this algorithm
                finaleval.append([self._NULL_PHENOME_INDICATOR])
            elif finalattempt is list:
                finaleval.append(finalattempt)
            else:  # 'finalattempt' is guareenteed to only be of type NONE, list, or list[list].
                finaleval.extend(finalattempt) # flatten list; tis step is necessary to maintain parsability

        return finaleval

    def _getproperhandlemultitoken(self, multitoken):
        """Takes a multi-word (a token with words seperated by '_' by Wordnet) and breaks it down into a format that can be evaluated by the CMUdict. If CMUdict or
        Wordnet implementation is changed this function MUST be changed."""

        finaleval = []
        individualtokens = multitoken.split(self._MULTI_TOKEN_INDICATOR)

        for token in individualtokens: # evaluate each token phenome indiviually; then represent multitoken for EACH phenome calculated, when returned to scanning.
            phenome = self._cmu.get(token.lower(), None)
               
            if phenome is list:
                finaleval.append(phenome)

            else: # 'phenome' is guareenteed to only be of type NONE, list, or list[list].
                if phenome is None:
                    phenome = self._getproperhandlemissingphenome(token)
                    
                finaleval.extend(phenome) # flatten list; this step is necessary to maintain parsability

        return finaleval

    def getphenomes(self, arg):
        """Returns all phenome-lists related to the token. ('context' is the representation of the phrase in collection form.)"""

        generatephenome = self._cmu.get(arg.lower(), None) # _cmu is defined globally above in "VARIABLES" section. Treat as an immutable.
        if generatephenome is None:
            if arg.__contains__(self._MULTI_TOKEN_INDICATOR): # _MULTI_TOKEN_INDICATOR is defined globally above in "VARIABLES" section. Treat as an immutable.
                generatephenome = self._getproperhandlemultitoken(arg)

            else: # token is unknown by CMUdict
                generatephenome = self._getproperhandlemissingphenome(arg)

        # When multiple phenomes exist for same word, a list[list[str]] is generated
        return generatephenome

    def hypernyms(self, context, arg):
        """Returns all hypernyms related to the token. ('context' is the representation of the phrase in collection form.)"""

        # This function assumes the use of Wordnet. If Wordnet implementation changes, this function MUST change.

        eval = None
        interpretation = lesk(context, arg)
        if interpretation is not None:
            eval = map(self._getproperformattype, interpretation.hypernyms())

        return eval

    def hyponyms(self, context, arg):
        """Returns all hyponyms related to the token."""

        # This function assumes the use of Wordnet. If Wordnet implementation changes, this function MUST change.

        eval = None
        interpretation = lesk(context, arg)
        if interpretation is not None:
            eval = map(self._getproperformattype, interpretation.hyponyms())

        return eval

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

        # This function assumes the use of Wordnet. If Wordnet implementation changes, this function MUST change.

        evaluation = False
        score = 0

        if arg1 is arg2:
            evaluation = True
            score = self._SIMILARITY_THRESHOLD # Penalizing score to prevent paraphrases from returning themselves

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