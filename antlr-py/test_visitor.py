from datetime import datetime

from antlr4 import *

from generated.searchLexer import searchLexer
from generated.searchParser import searchParser
from generated.searchVisitor import searchVisitor


class MySearchVisitor(searchVisitor):
    def __init__(self):
        self.result = {
            "filters": {},
            "terms": []
        }

    def visitAuthor_flt(self, ctx: searchParser.Author_fltContext):
        self.result["filters"]["author"] = self.visit(ctx.term())

    def visitAfter_flt(self, ctx: searchParser.After_fltContext):
        self.result["filters"]["after"] = datetime.fromisoformat(ctx.DATE().getText())

    def visitBefore_flt(self, ctx: searchParser.Before_fltContext):
        self.result["filters"]["before"] = datetime.fromisoformat(ctx.DATE().getText())

    def visitTerms(self, ctx:searchParser.TermsContext):
        self.result["terms"] = [self.visit(term) for term in ctx.children]

    def visitTerm(self, ctx: searchParser.TermContext):
        if ctx.WORD():
            return ctx.WORD().getText()
        elif ctx.QUOTED_TERM():
            return ctx.QUOTED_TERM().getText()[1:-1].replace('""', "")


def parse_search(search_string: str) -> dict:
    chars = InputStream(search_string)
    lexer = searchLexer(chars)
    tokens = CommonTokenStream(lexer)
    parser = searchParser(tokens)
    parser.buildParseTrees = True
    tree = parser.start()

    visitor = MySearchVisitor()
    tree.accept(visitor)

    return visitor.result


def test_search_visit():
    search_string = 'author: @me after: 2020-01-01 "happy pants" beer'
    result = parse_search(search_string)
    assert result is not None
    assert len(result["filters"]) == 2
    assert result["filters"]["author"] == "@me"
    assert result["filters"]["after"] == datetime.fromisoformat('2020-01-01')
    assert result["terms"] == ["happy pants", "beer"]