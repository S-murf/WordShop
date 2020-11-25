from enum import Enum
from nltk import RegexpTokenizer
from nltk.corpus import wordnet
from Interfaces.langbounds import LanguageBoundsInterface

class AmericanEnglishLangContext(LanguageBoundsInterface):
    """Defines the properties and implementation of standard American English."""

    class ContextTags(Enum):
        """Defines all possible context tags for this language."""
        NP = 0
        VP = 1
        ADJP = 2
        ADVP = 3
        PREP = 4

    def getlangcontext(self, arg):
        return "No"

    def islegal(self, arg1, arg2):
        return "No"

    def split(self, arg):
        # Returns all non-whitespace tokens.
        return RegexpTokenizer('\w+|\$[\d\.]+|\S+').tokenize(arg)

    def _contextsuggestion(self, arg):
        """Takes an ordered token-set and calculates the overall wordsense of each token."""
        # Stack-trace algorithm using wordnet and bigrams
        # Highest probability chain is selected. Score calc'd by adding up probs
        # If a chain is interuptted(lang rule is broken), the score automatically becomes zero and next trace is calc'd
        # O(n) minimum time complexity (this can potentially be very slow for longer sentences); Tradeoff for speed is increased precision
        # Alternatively a most-frequent sense approach can be taken. This will allow for locked O(n) complexity while losing precision.

    def _rulesuggestion(self, arg1, arg2):
        """Enforces language-context rules to a context-symbol bigram. Returns true if language rules are sustained."""