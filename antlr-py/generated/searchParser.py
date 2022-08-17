# Generated from /Users/eirikur/brownbags/antlr-py/search.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,7,88,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,
        2,7,7,7,2,8,7,8,2,9,7,9,1,0,3,0,22,8,0,1,0,1,0,1,0,1,1,1,1,3,1,29,
        8,1,1,1,1,1,3,1,33,8,1,1,1,1,1,3,1,37,8,1,3,1,39,8,1,1,2,1,2,3,2,
        43,8,2,1,2,1,2,3,2,47,8,2,3,2,49,8,2,1,3,1,3,3,3,53,8,3,1,3,1,3,
        3,3,57,8,3,3,3,59,8,3,1,4,1,4,3,4,63,8,4,1,4,1,4,3,4,67,8,4,3,4,
        69,8,4,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,8,5,8,81,8,8,10,8,12,
        8,84,9,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,1,1,0,5,6,
        93,0,21,1,0,0,0,2,38,1,0,0,0,4,48,1,0,0,0,6,58,1,0,0,0,8,68,1,0,
        0,0,10,70,1,0,0,0,12,73,1,0,0,0,14,76,1,0,0,0,16,82,1,0,0,0,18,85,
        1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,21,22,1,0,0,0,22,23,1,0,0,0,
        23,24,3,16,8,0,24,25,5,0,0,1,25,1,1,0,0,0,26,28,3,10,5,0,27,29,3,
        4,2,0,28,27,1,0,0,0,28,29,1,0,0,0,29,39,1,0,0,0,30,32,3,12,6,0,31,
        33,3,6,3,0,32,31,1,0,0,0,32,33,1,0,0,0,33,39,1,0,0,0,34,36,3,14,
        7,0,35,37,3,8,4,0,36,35,1,0,0,0,36,37,1,0,0,0,37,39,1,0,0,0,38,26,
        1,0,0,0,38,30,1,0,0,0,38,34,1,0,0,0,39,3,1,0,0,0,40,42,3,12,6,0,
        41,43,3,14,7,0,42,41,1,0,0,0,42,43,1,0,0,0,43,49,1,0,0,0,44,46,3,
        14,7,0,45,47,3,12,6,0,46,45,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,
        48,40,1,0,0,0,48,44,1,0,0,0,49,5,1,0,0,0,50,52,3,10,5,0,51,53,3,
        14,7,0,52,51,1,0,0,0,52,53,1,0,0,0,53,59,1,0,0,0,54,56,3,14,7,0,
        55,57,3,10,5,0,56,55,1,0,0,0,56,57,1,0,0,0,57,59,1,0,0,0,58,50,1,
        0,0,0,58,54,1,0,0,0,59,7,1,0,0,0,60,62,3,10,5,0,61,63,3,12,6,0,62,
        61,1,0,0,0,62,63,1,0,0,0,63,69,1,0,0,0,64,66,3,12,6,0,65,67,3,10,
        5,0,66,65,1,0,0,0,66,67,1,0,0,0,67,69,1,0,0,0,68,60,1,0,0,0,68,64,
        1,0,0,0,69,9,1,0,0,0,70,71,5,1,0,0,71,72,3,18,9,0,72,11,1,0,0,0,
        73,74,5,2,0,0,74,75,5,4,0,0,75,13,1,0,0,0,76,77,5,3,0,0,77,78,5,
        4,0,0,78,15,1,0,0,0,79,81,3,18,9,0,80,79,1,0,0,0,81,84,1,0,0,0,82,
        80,1,0,0,0,82,83,1,0,0,0,83,17,1,0,0,0,84,82,1,0,0,0,85,86,7,0,0,
        0,86,19,1,0,0,0,15,21,28,32,36,38,42,46,48,52,56,58,62,66,68,82
    ]

class searchParser ( Parser ):

    grammarFileName = "search.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'author:'", "'before:'", "'after:'" ]

    symbolicNames = [ "<INVALID>", "AUTHOR", "BEFORE", "AFTER", "DATE", 
                      "QUOTED_TERM", "WORD", "WS" ]

    RULE_start = 0
    RULE_filters = 1
    RULE_not_author_flt = 2
    RULE_not_before_flt = 3
    RULE_not_after_flt = 4
    RULE_author_flt = 5
    RULE_before_flt = 6
    RULE_after_flt = 7
    RULE_terms = 8
    RULE_term = 9

    ruleNames =  [ "start", "filters", "not_author_flt", "not_before_flt", 
                   "not_after_flt", "author_flt", "before_flt", "after_flt", 
                   "terms", "term" ]

    EOF = Token.EOF
    AUTHOR=1
    BEFORE=2
    AFTER=3
    DATE=4
    QUOTED_TERM=5
    WORD=6
    WS=7

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terms(self):
            return self.getTypedRuleContext(searchParser.TermsContext,0)


        def EOF(self):
            return self.getToken(searchParser.EOF, 0)

        def filters(self):
            return self.getTypedRuleContext(searchParser.FiltersContext,0)


        def getRuleIndex(self):
            return searchParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStart" ):
                return visitor.visitStart(self)
            else:
                return visitor.visitChildren(self)




    def start(self):

        localctx = searchParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << searchParser.AUTHOR) | (1 << searchParser.BEFORE) | (1 << searchParser.AFTER))) != 0):
                self.state = 20
                self.filters()


            self.state = 23
            self.terms()
            self.state = 24
            self.match(searchParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FiltersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def author_flt(self):
            return self.getTypedRuleContext(searchParser.Author_fltContext,0)


        def not_author_flt(self):
            return self.getTypedRuleContext(searchParser.Not_author_fltContext,0)


        def before_flt(self):
            return self.getTypedRuleContext(searchParser.Before_fltContext,0)


        def not_before_flt(self):
            return self.getTypedRuleContext(searchParser.Not_before_fltContext,0)


        def after_flt(self):
            return self.getTypedRuleContext(searchParser.After_fltContext,0)


        def not_after_flt(self):
            return self.getTypedRuleContext(searchParser.Not_after_fltContext,0)


        def getRuleIndex(self):
            return searchParser.RULE_filters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilters" ):
                listener.enterFilters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilters" ):
                listener.exitFilters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilters" ):
                return visitor.visitFilters(self)
            else:
                return visitor.visitChildren(self)




    def filters(self):

        localctx = searchParser.FiltersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_filters)
        self._la = 0 # Token type
        try:
            self.state = 38
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [searchParser.AUTHOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.author_flt()
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.BEFORE or _la==searchParser.AFTER:
                    self.state = 27
                    self.not_author_flt()


                pass
            elif token in [searchParser.BEFORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.before_flt()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.AUTHOR or _la==searchParser.AFTER:
                    self.state = 31
                    self.not_before_flt()


                pass
            elif token in [searchParser.AFTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.after_flt()
                self.state = 36
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.AUTHOR or _la==searchParser.BEFORE:
                    self.state = 35
                    self.not_after_flt()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_author_fltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def before_flt(self):
            return self.getTypedRuleContext(searchParser.Before_fltContext,0)


        def after_flt(self):
            return self.getTypedRuleContext(searchParser.After_fltContext,0)


        def getRuleIndex(self):
            return searchParser.RULE_not_author_flt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_author_flt" ):
                listener.enterNot_author_flt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_author_flt" ):
                listener.exitNot_author_flt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_author_flt" ):
                return visitor.visitNot_author_flt(self)
            else:
                return visitor.visitChildren(self)




    def not_author_flt(self):

        localctx = searchParser.Not_author_fltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_not_author_flt)
        self._la = 0 # Token type
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [searchParser.BEFORE]:
                self.enterOuterAlt(localctx, 1)
                self.state = 40
                self.before_flt()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.AFTER:
                    self.state = 41
                    self.after_flt()


                pass
            elif token in [searchParser.AFTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.after_flt()
                self.state = 46
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.BEFORE:
                    self.state = 45
                    self.before_flt()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_before_fltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def author_flt(self):
            return self.getTypedRuleContext(searchParser.Author_fltContext,0)


        def after_flt(self):
            return self.getTypedRuleContext(searchParser.After_fltContext,0)


        def getRuleIndex(self):
            return searchParser.RULE_not_before_flt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_before_flt" ):
                listener.enterNot_before_flt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_before_flt" ):
                listener.exitNot_before_flt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_before_flt" ):
                return visitor.visitNot_before_flt(self)
            else:
                return visitor.visitChildren(self)




    def not_before_flt(self):

        localctx = searchParser.Not_before_fltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_not_before_flt)
        self._la = 0 # Token type
        try:
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [searchParser.AUTHOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.author_flt()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.AFTER:
                    self.state = 51
                    self.after_flt()


                pass
            elif token in [searchParser.AFTER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.after_flt()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.AUTHOR:
                    self.state = 55
                    self.author_flt()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Not_after_fltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def author_flt(self):
            return self.getTypedRuleContext(searchParser.Author_fltContext,0)


        def before_flt(self):
            return self.getTypedRuleContext(searchParser.Before_fltContext,0)


        def getRuleIndex(self):
            return searchParser.RULE_not_after_flt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNot_after_flt" ):
                listener.enterNot_after_flt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNot_after_flt" ):
                listener.exitNot_after_flt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNot_after_flt" ):
                return visitor.visitNot_after_flt(self)
            else:
                return visitor.visitChildren(self)




    def not_after_flt(self):

        localctx = searchParser.Not_after_fltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_not_after_flt)
        self._la = 0 # Token type
        try:
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [searchParser.AUTHOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.author_flt()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.BEFORE:
                    self.state = 61
                    self.before_flt()


                pass
            elif token in [searchParser.BEFORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.before_flt()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==searchParser.AUTHOR:
                    self.state = 65
                    self.author_flt()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Author_fltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AUTHOR(self):
            return self.getToken(searchParser.AUTHOR, 0)

        def term(self):
            return self.getTypedRuleContext(searchParser.TermContext,0)


        def getRuleIndex(self):
            return searchParser.RULE_author_flt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAuthor_flt" ):
                listener.enterAuthor_flt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAuthor_flt" ):
                listener.exitAuthor_flt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAuthor_flt" ):
                return visitor.visitAuthor_flt(self)
            else:
                return visitor.visitChildren(self)




    def author_flt(self):

        localctx = searchParser.Author_fltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_author_flt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(searchParser.AUTHOR)
            self.state = 71
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Before_fltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BEFORE(self):
            return self.getToken(searchParser.BEFORE, 0)

        def DATE(self):
            return self.getToken(searchParser.DATE, 0)

        def getRuleIndex(self):
            return searchParser.RULE_before_flt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBefore_flt" ):
                listener.enterBefore_flt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBefore_flt" ):
                listener.exitBefore_flt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBefore_flt" ):
                return visitor.visitBefore_flt(self)
            else:
                return visitor.visitChildren(self)




    def before_flt(self):

        localctx = searchParser.Before_fltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_before_flt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(searchParser.BEFORE)
            self.state = 74
            self.match(searchParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class After_fltContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AFTER(self):
            return self.getToken(searchParser.AFTER, 0)

        def DATE(self):
            return self.getToken(searchParser.DATE, 0)

        def getRuleIndex(self):
            return searchParser.RULE_after_flt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAfter_flt" ):
                listener.enterAfter_flt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAfter_flt" ):
                listener.exitAfter_flt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAfter_flt" ):
                return visitor.visitAfter_flt(self)
            else:
                return visitor.visitChildren(self)




    def after_flt(self):

        localctx = searchParser.After_fltContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_after_flt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(searchParser.AFTER)
            self.state = 77
            self.match(searchParser.DATE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(searchParser.TermContext)
            else:
                return self.getTypedRuleContext(searchParser.TermContext,i)


        def getRuleIndex(self):
            return searchParser.RULE_terms

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerms" ):
                listener.enterTerms(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerms" ):
                listener.exitTerms(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerms" ):
                return visitor.visitTerms(self)
            else:
                return visitor.visitChildren(self)




    def terms(self):

        localctx = searchParser.TermsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_terms)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==searchParser.QUOTED_TERM or _la==searchParser.WORD:
                self.state = 79
                self.term()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(searchParser.WORD, 0)

        def QUOTED_TERM(self):
            return self.getToken(searchParser.QUOTED_TERM, 0)

        def getRuleIndex(self):
            return searchParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = searchParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==searchParser.QUOTED_TERM or _la==searchParser.WORD):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





