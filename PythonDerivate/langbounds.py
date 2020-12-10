class LanguageBoundsInterface:
    """This interface is used to define different properties and implementation of a language.
These properties will create a ruleset for a language, which will be the bounds an algorithm
can work in the given context."""

    # In future implementations, this is where hypernyms/hyponyms/phenomes/similarity/token-spliting/unknown-handling will be handled.
    # Makes it so rule implementation can use any language can use rule implementation modularly. As of right now, English is the only supported language.

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
        pass

    def messageonlyresult(self, arg):
        """Produces a indicator message if only one result was possible from the input parameters given."""
        pass
    
    def messagetopresult(self, resultlen, requestedresultcount):
        """Produces the top 'x' results message to users in this language if the process has multiple results."""
        pass

    def similarity(self, arg, arg2):
        """Returns a token similarity score based on language-based weights. Used for determining optimal replacement for
        contexts."""
        pass

    def split(self, arg):
        """Returns an ordered list of tokens, split at delimiters based off of the the language context settings."""
        pass