class RuleBoundsInterface:
    """This interface is used to define different properties of a rhetorical figure generating algorithm.
These properties will create a ruleset for a rhectorical figure, allowing the algorithm to produce results relevant
to the user-request."""

    def evaluate(self, tokenlist, langbound):
        """Returns a key-value pair of an 'application-score' (a score that shows to which degree a rhetorical figure can be applied;
        scales from 0 to 1) and a 2D-list of potential replacements per relevant phrase (where 'phrase' is defined as an individual word OR
        sequence of words)"""
        pass

