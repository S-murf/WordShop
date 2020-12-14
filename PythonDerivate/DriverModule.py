################################
# Date of Creation: 10/2020
# Author: Mervin Guy
# Application: WordShop AlphaFork
#
# This file is intended to be the driver of an alpha-stage 
# WordShop application. All user-side functionality should
# be called from this module alone.
################################

from LanguageContexts.usa_englishlc import AmericanEnglishLangContext
from Modules.Analyze.analyzer import Analyzer
from Modules.Brainstorm.rc_alliteration import AlliterationRuleContext
from Modules.Map.mapper import Mapper

def main():
    return

def alliteration(arg, proportion, sensitivity):
    langcontext = AmericanEnglishLangContext(sensitivity)
    mapsection = Mapper()
    rule = AlliterationRuleContext()
    interpreter = Analyzer()
    mappedtokens = mapsection.maptolist(arg, langcontext)

    # Calculate exact proportion
    calcd = len(mappedtokens)
    if proportion < 1:
        calcd *= proportion
        calcd = round(calcd)

    applied = rule.evaluate(mappedtokens, calcd, langcontext)
    finalresult = interpreter.analyze(mappedtokens, applied, langcontext, calcd)
    print(finalresult)

# Will execute the driver function, iff it is the main call.
# Driver should ALWAYS be the main call.
if __name__ == "__main__":
    main()