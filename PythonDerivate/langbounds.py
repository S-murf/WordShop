class LanguageBoundsInterface:
    """This interface is used to define different properties and implementation of a language.
These properties will create a ruleset for a language, which will be the bounds an algorithm
can work in the given context."""

    def similarity(self, arg, arg2):
        """Returns a token similarity score based on language-based weights. Used for determining optimal replacement for
        contexts."""
        pass

    def split(self, arg):
        """Returns an ordered list of tokens, split at delimiters based off of the the language context settings."""
        pass