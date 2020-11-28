from enum import Enum
from nltk import RegexpTokenizer
from nltk.corpus import wordnet
from Interfaces.langbounds import LanguageBoundsInterface

class AmericanEnglishLangContext(LanguageBoundsInterface):
    """Defines the properties and implementation of standard American English."""

    class ContextTags(Enum):  # [deprecated] word replacement allows for simpler algorithm
        """Defines all possible context tags for this language."""
        NP = 0
        VP = 1
        ADJP = 2
        ADVP = 3
        PREP = 4

    def similarity(self, arg1, arg2):
        return 1

    def split(self, arg):
        # Returns all non-whitespace tokens.
        return RegexpTokenizer('\w+|\$[\d\.]+|\S+').tokenize(arg)