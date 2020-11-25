class LanguageBoundsInterface:
    """This interface is used to define different properties and implementation of a language.
These properties will create a ruleset for a language, which will be the bounds an algorithm
can work in the given context."""

    
    def getlangcontext(self, arg):
        """Returns standardized symbol(s) for a given token-set, dependent on the language-context type."""
        pass

    def islegal(self, arg1, arg2):
        """Returns if it is valid within language-context for two standardized symbols to be adjacent."""
        pass

    def split(self, arg):
        """Returns an ordered list of tokens, split at delimiters based off of the the language context settings."""
        pass

    #Add avg token count per phrase?