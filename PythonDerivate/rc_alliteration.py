from nltk.corpus import wordnet
from nltk.wsd import lesk
from Interfaces.rulebounds import RuleBoundsInterface

class AlliterationRuleContext(RuleBoundsInterface):
    """Defines the properties and rules of the alliteration rhetorical figure."""

    def _applyrule(self, sourcetoken, tokenlist):
        """Trim interal-map token list to only retain tokens that constrau=in to the alliteration ruleset."""
        return tokenlist
    
    def _internalmap(self, tokenlist):
        """Map relevant replacement tokens to list. This return token list will have a one-to-to corresspondence to the passed tokenlist argument."""

        replacements = []
        for token in tokenlist:
            context = lesk(tokenlist, token)
            ruleapplied = _applyrule(context)
            replacements.append(ruleapplied)

        return replacements

    def evaluate(self, tokenlist, langbound):
        return _internalmap(tokenlist)