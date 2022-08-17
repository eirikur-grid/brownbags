# Generated from /Users/eirikur/Brownbags/antlr/search.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\t")
        buf.write("Z\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\5\2\30\n\2\3\2\3\2")
        buf.write("\3\2\3\3\3\3\5\3\37\n\3\3\3\3\3\5\3#\n\3\3\3\3\3\5\3\'")
        buf.write("\n\3\5\3)\n\3\3\4\3\4\5\4-\n\4\3\4\3\4\5\4\61\n\4\5\4")
        buf.write("\63\n\4\3\5\3\5\5\5\67\n\5\3\5\3\5\5\5;\n\5\5\5=\n\5\3")
        buf.write("\6\3\6\5\6A\n\6\3\6\3\6\5\6E\n\6\5\6G\n\6\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\n\7\nS\n\n\f\n\16\nV\13\n\3")
        buf.write("\13\3\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22\24\2\3\3\2\7")
        buf.write("\b\2_\2\27\3\2\2\2\4(\3\2\2\2\6\62\3\2\2\2\b<\3\2\2\2")
        buf.write("\nF\3\2\2\2\fH\3\2\2\2\16K\3\2\2\2\20N\3\2\2\2\22T\3\2")
        buf.write("\2\2\24W\3\2\2\2\26\30\5\4\3\2\27\26\3\2\2\2\27\30\3\2")
        buf.write("\2\2\30\31\3\2\2\2\31\32\5\22\n\2\32\33\7\2\2\3\33\3\3")
        buf.write("\2\2\2\34\36\5\f\7\2\35\37\5\6\4\2\36\35\3\2\2\2\36\37")
        buf.write("\3\2\2\2\37)\3\2\2\2 \"\5\16\b\2!#\5\b\5\2\"!\3\2\2\2")
        buf.write("\"#\3\2\2\2#)\3\2\2\2$&\5\20\t\2%\'\5\n\6\2&%\3\2\2\2")
        buf.write("&\'\3\2\2\2\')\3\2\2\2(\34\3\2\2\2( \3\2\2\2($\3\2\2\2")
        buf.write(")\5\3\2\2\2*,\5\16\b\2+-\5\20\t\2,+\3\2\2\2,-\3\2\2\2")
        buf.write("-\63\3\2\2\2.\60\5\20\t\2/\61\5\16\b\2\60/\3\2\2\2\60")
        buf.write("\61\3\2\2\2\61\63\3\2\2\2\62*\3\2\2\2\62.\3\2\2\2\63\7")
        buf.write("\3\2\2\2\64\66\5\f\7\2\65\67\5\20\t\2\66\65\3\2\2\2\66")
        buf.write("\67\3\2\2\2\67=\3\2\2\28:\5\20\t\29;\5\f\7\2:9\3\2\2\2")
        buf.write(":;\3\2\2\2;=\3\2\2\2<\64\3\2\2\2<8\3\2\2\2=\t\3\2\2\2")
        buf.write(">@\5\f\7\2?A\5\16\b\2@?\3\2\2\2@A\3\2\2\2AG\3\2\2\2BD")
        buf.write("\5\16\b\2CE\5\f\7\2DC\3\2\2\2DE\3\2\2\2EG\3\2\2\2F>\3")
        buf.write("\2\2\2FB\3\2\2\2G\13\3\2\2\2HI\7\3\2\2IJ\5\24\13\2J\r")
        buf.write("\3\2\2\2KL\7\4\2\2LM\7\6\2\2M\17\3\2\2\2NO\7\5\2\2OP\7")
        buf.write("\6\2\2P\21\3\2\2\2QS\5\24\13\2RQ\3\2\2\2SV\3\2\2\2TR\3")
        buf.write("\2\2\2TU\3\2\2\2U\23\3\2\2\2VT\3\2\2\2WX\t\2\2\2X\25\3")
        buf.write("\2\2\2\21\27\36\"&(,\60\62\66:<@DFT")
        return buf.getvalue()


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
        self.checkVersion("4.9.2")
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





