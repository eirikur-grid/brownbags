# Generated from /Users/eirikur/brownbags/antlr-py/search.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .searchParser import searchParser
else:
    from searchParser import searchParser

# This class defines a complete generic visitor for a parse tree produced by searchParser.

class searchVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by searchParser#start.
    def visitStart(self, ctx:searchParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#filters.
    def visitFilters(self, ctx:searchParser.FiltersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#not_author_flt.
    def visitNot_author_flt(self, ctx:searchParser.Not_author_fltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#not_before_flt.
    def visitNot_before_flt(self, ctx:searchParser.Not_before_fltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#not_after_flt.
    def visitNot_after_flt(self, ctx:searchParser.Not_after_fltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#author_flt.
    def visitAuthor_flt(self, ctx:searchParser.Author_fltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#before_flt.
    def visitBefore_flt(self, ctx:searchParser.Before_fltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#after_flt.
    def visitAfter_flt(self, ctx:searchParser.After_fltContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#terms.
    def visitTerms(self, ctx:searchParser.TermsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by searchParser#term.
    def visitTerm(self, ctx:searchParser.TermContext):
        return self.visitChildren(ctx)



del searchParser