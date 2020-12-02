from nltk.corpus import wordnet
from nltk.wsd import lesk
from Interfaces.rulebounds import RuleBoundsInterface

class AlliterationRuleContext(RuleBoundsInterface):
    """Defines the properties and rules of the alliteration rhetorical figure."""

    def _applyrule(self, sourcetoken, tokenlist):
        """Trim interal-map token list to only retain tokens that constrain to the alliteration ruleset."""
        return tokenlist

    def _getrelevantsynonyms(self, sourcetoken):
        """Returns a list of synonyms that are relevant to the allieration rule context."""

        relevant = []
        if sourcetoken is not None:
            relevant.append(sourcetoken)
            relevant.append(sourcetoken.hypernyms())
            relevant.append(sourcetoken.hyponyms())

        return relevant

    def _internalmap(self, tokenlist):
        """Map relevant replacement tokens to list. This return token list will have a one-to-to corresspondence to the passed tokenlist argument."""

        replacements = []
        for token in tokenlist:
            context = lesk(tokenlist, token)
            similar = self._getrelevantsynonyms(context)
            ruleapplied = self._applyrule("a", similar)
            replacements.append(ruleapplied)

        return replacements

    def evaluate(self, tokenlist, langbound):
        return self._internalmap(tokenlist)