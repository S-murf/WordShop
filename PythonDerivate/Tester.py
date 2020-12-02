# Used to conduct unit tests on different modules. No functional use within program.
# For debugging purposes only.

from LanguageContexts.usa_englishlc import AmericanEnglishLangContext
from Modules.Brainstorm.rc_alliteration import AlliterationRuleContext
from Modules.Map.mapper import Mapper

def main():
    objA = AmericanEnglishLangContext()
    allit = AlliterationRuleContext()
    mapp = Mapper()
    k = mapp.maptolist("pokemon is a really fun game uwu.", objA)
    l = allit.evaluate(k, objA)

    testingincrement = 0
    for t in l:
        print("List #" + str(testingincrement))
        print(t)
        print("\n")
        testingincrement += 1

    return

if __name__ == "__main__":
    main()