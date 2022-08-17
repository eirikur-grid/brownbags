# Generated from /Users/eirikur/Brownbags/antlr/search.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\t")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\7\6")
        buf.write("\67\n\6\f\6\16\6:\13\6\3\7\5\7=\n\7\3\7\3\7\3\7\5\7B\n")
        buf.write("\7\3\b\5\bE\n\b\3\b\3\b\3\b\3\b\3\b\5\bL\n\b\3\t\3\t\3")
        buf.write("\t\3\t\7\tR\n\t\f\t\16\tU\13\t\3\t\3\t\3\n\6\nZ\n\n\r")
        buf.write("\n\16\n[\3\13\6\13_\n\13\r\13\16\13`\3\13\3\13\2\2\f\3")
        buf.write("\3\5\4\7\5\t\6\13\2\r\2\17\2\21\7\23\b\25\t\3\2\n\3\2")
        buf.write("\63;\3\2\62;\3\2\62\64\3\2\63\64\3\2\62\63\3\2$$\n\2#")
        buf.write("#%(*+\62;B\\aac|\u0082\0\5\2\13\f\16\17\"\"\2j\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\21\3\2\2\2")
        buf.write("\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\37\3\2\2\2\7")
        buf.write("\'\3\2\2\2\t.\3\2\2\2\13\64\3\2\2\2\rA\3\2\2\2\17K\3\2")
        buf.write("\2\2\21M\3\2\2\2\23Y\3\2\2\2\25^\3\2\2\2\27\30\7c\2\2")
        buf.write("\30\31\7w\2\2\31\32\7v\2\2\32\33\7j\2\2\33\34\7q\2\2\34")
        buf.write("\35\7t\2\2\35\36\7<\2\2\36\4\3\2\2\2\37 \7d\2\2 !\7g\2")
        buf.write("\2!\"\7h\2\2\"#\7q\2\2#$\7t\2\2$%\7g\2\2%&\7<\2\2&\6\3")
        buf.write("\2\2\2\'(\7c\2\2()\7h\2\2)*\7v\2\2*+\7g\2\2+,\7t\2\2,")
        buf.write("-\7<\2\2-\b\3\2\2\2./\5\13\6\2/\60\7/\2\2\60\61\5\r\7")
        buf.write("\2\61\62\7/\2\2\62\63\5\17\b\2\63\n\3\2\2\2\648\t\2\2")
        buf.write("\2\65\67\t\3\2\2\66\65\3\2\2\2\67:\3\2\2\28\66\3\2\2\2")
        buf.write("89\3\2\2\29\f\3\2\2\2:8\3\2\2\2;=\7\62\2\2<;\3\2\2\2<")
        buf.write("=\3\2\2\2=>\3\2\2\2>B\t\2\2\2?@\7\63\2\2@B\t\4\2\2A<\3")
        buf.write("\2\2\2A?\3\2\2\2B\16\3\2\2\2CE\7\62\2\2DC\3\2\2\2DE\3")
        buf.write("\2\2\2EF\3\2\2\2FL\t\2\2\2GH\t\5\2\2HL\t\3\2\2IJ\7\65")
        buf.write("\2\2JL\t\6\2\2KD\3\2\2\2KG\3\2\2\2KI\3\2\2\2L\20\3\2\2")
        buf.write("\2MS\7$\2\2NR\n\7\2\2OP\7$\2\2PR\7$\2\2QN\3\2\2\2QO\3")
        buf.write("\2\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2")
        buf.write("\2VW\7$\2\2W\22\3\2\2\2XZ\t\b\2\2YX\3\2\2\2Z[\3\2\2\2")
        buf.write("[Y\3\2\2\2[\\\3\2\2\2\\\24\3\2\2\2]_\t\t\2\2^]\3\2\2\2")
        buf.write("_`\3\2\2\2`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\13\2\2c\26")
        buf.write("\3\2\2\2\f\28<ADKQS[`\3\2\3\2")
        return buf.getvalue()


class searchLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    AUTHOR = 1
    BEFORE = 2
    AFTER = 3
    DATE = 4
    QUOTED_TERM = 5
    WORD = 6
    WS = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'author:'", "'before:'", "'after:'" ]

    symbolicNames = [ "<INVALID>",
            "AUTHOR", "BEFORE", "AFTER", "DATE", "QUOTED_TERM", "WORD", 
            "WS" ]

    ruleNames = [ "AUTHOR", "BEFORE", "AFTER", "DATE", "YYYY", "MM", "DD", 
                  "QUOTED_TERM", "WORD", "WS" ]

    grammarFileName = "search.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


