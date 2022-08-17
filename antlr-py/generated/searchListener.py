# Generated from /Users/eirikur/Brownbags/antlr/search.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .searchParser import searchParser
else:
    from searchParser import searchParser

# This class defines a complete listener for a parse tree produced by searchParser.
class searchListener(ParseTreeListener):

    # Enter a parse tree produced by searchParser#start.
    def enterStart(self, ctx:searchParser.StartContext):
        pass

    # Exit a parse tree produced by searchParser#start.
    def exitStart(self, ctx:searchParser.StartContext):
        pass


    # Enter a parse tree produced by searchParser#filters.
    def enterFilters(self, ctx:searchParser.FiltersContext):
        pass

    # Exit a parse tree produced by searchParser#filters.
    def exitFilters(self, ctx:searchParser.FiltersContext):
        pass


    # Enter a parse tree produced by searchParser#not_author_flt.
    def enterNot_author_flt(self, ctx:searchParser.Not_author_fltContext):
        pass

    # Exit a parse tree produced by searchParser#not_author_flt.
    def exitNot_author_flt(self, ctx:searchParser.Not_author_fltContext):
        pass


    # Enter a parse tree produced by searchParser#not_before_flt.
    def enterNot_before_flt(self, ctx:searchParser.Not_before_fltContext):
        pass

    # Exit a parse tree produced by searchParser#not_before_flt.
    def exitNot_before_flt(self, ctx:searchParser.Not_before_fltContext):
        pass


    # Enter a parse tree produced by searchParser#not_after_flt.
    def enterNot_after_flt(self, ctx:searchParser.Not_after_fltContext):
        pass

    # Exit a parse tree produced by searchParser#not_after_flt.
    def exitNot_after_flt(self, ctx:searchParser.Not_after_fltContext):
        pass


    # Enter a parse tree produced by searchParser#author_flt.
    def enterAuthor_flt(self, ctx:searchParser.Author_fltContext):
        pass

    # Exit a parse tree produced by searchParser#author_flt.
    def exitAuthor_flt(self, ctx:searchParser.Author_fltContext):
        pass


    # Enter a parse tree produced by searchParser#before_flt.
    def enterBefore_flt(self, ctx:searchParser.Before_fltContext):
        pass

    # Exit a parse tree produced by searchParser#before_flt.
    def exitBefore_flt(self, ctx:searchParser.Before_fltContext):
        pass


    # Enter a parse tree produced by searchParser#after_flt.
    def enterAfter_flt(self, ctx:searchParser.After_fltContext):
        pass

    # Exit a parse tree produced by searchParser#after_flt.
    def exitAfter_flt(self, ctx:searchParser.After_fltContext):
        pass


    # Enter a parse tree produced by searchParser#terms.
    def enterTerms(self, ctx:searchParser.TermsContext):
        pass

    # Exit a parse tree produced by searchParser#terms.
    def exitTerms(self, ctx:searchParser.TermsContext):
        pass


    # Enter a parse tree produced by searchParser#term.
    def enterTerm(self, ctx:searchParser.TermContext):
        pass

    # Exit a parse tree produced by searchParser#term.
    def exitTerm(self, ctx:searchParser.TermContext):
        pass



del searchParser