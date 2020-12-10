# Used to conduct unit tests on different modules. No functional use within program.
# For debugging purposes only.

from LanguageContexts.usa_englishlc import AmericanEnglishLangContext
from Modules.Analyze.analyzer import Analyzer
from Modules.Brainstorm.rc_alliteration import AlliterationRuleContext
from Modules.Map.mapper import Mapper

def main():
    objA = AmericanEnglishLangContext()
    allit = AlliterationRuleContext()
    mapp = Mapper()
    proportion = 0.3
    k = mapp.maptolist("I do not think that flowers bloom under the sun.", objA)

    # Calculate exact proportion
    calcdproportion = len(k)
    if proportion < 1:
        calcdproportion *= proportion
        round(calcdproportion)

    l = allit.evaluate(k, calcdproportion)

    m = Analyzer()
    q = m.analyze(k, l, objA, calcdproportion)
    print(q)
    return

if __name__ == "__main__":
    main()