// Generated from /Users/eirikur/Brownbags/antlr/search.g4 by ANTLR 4.9.2
// jshint ignore: start
import antlr4 from 'antlr4';
import searchListener from './searchListener.js';
import searchVisitor from './searchVisitor.js';


const serializedATN = ["\u0003\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786",
    "\u5964\u0003\tZ\u0004\u0002\t\u0002\u0004\u0003\t\u0003\u0004\u0004",
    "\t\u0004\u0004\u0005\t\u0005\u0004\u0006\t\u0006\u0004\u0007\t\u0007",
    "\u0004\b\t\b\u0004\t\t\t\u0004\n\t\n\u0004\u000b\t\u000b\u0003\u0002",
    "\u0005\u0002\u0018\n\u0002\u0003\u0002\u0003\u0002\u0003\u0002\u0003",
    "\u0003\u0003\u0003\u0005\u0003\u001f\n\u0003\u0003\u0003\u0003\u0003",
    "\u0005\u0003#\n\u0003\u0003\u0003\u0003\u0003\u0005\u0003\'\n\u0003",
    "\u0005\u0003)\n\u0003\u0003\u0004\u0003\u0004\u0005\u0004-\n\u0004\u0003",
    "\u0004\u0003\u0004\u0005\u00041\n\u0004\u0005\u00043\n\u0004\u0003\u0005",
    "\u0003\u0005\u0005\u00057\n\u0005\u0003\u0005\u0003\u0005\u0005\u0005",
    ";\n\u0005\u0005\u0005=\n\u0005\u0003\u0006\u0003\u0006\u0005\u0006A",
    "\n\u0006\u0003\u0006\u0003\u0006\u0005\u0006E\n\u0006\u0005\u0006G\n",
    "\u0006\u0003\u0007\u0003\u0007\u0003\u0007\u0003\b\u0003\b\u0003\b\u0003",
    "\t\u0003\t\u0003\t\u0003\n\u0007\nS\n\n\f\n\u000e\nV\u000b\n\u0003\u000b",
    "\u0003\u000b\u0003\u000b\u0002\u0002\f\u0002\u0004\u0006\b\n\f\u000e",
    "\u0010\u0012\u0014\u0002\u0003\u0003\u0002\u0007\b\u0002_\u0002\u0017",
    "\u0003\u0002\u0002\u0002\u0004(\u0003\u0002\u0002\u0002\u00062\u0003",
    "\u0002\u0002\u0002\b<\u0003\u0002\u0002\u0002\nF\u0003\u0002\u0002\u0002",
    "\fH\u0003\u0002\u0002\u0002\u000eK\u0003\u0002\u0002\u0002\u0010N\u0003",
    "\u0002\u0002\u0002\u0012T\u0003\u0002\u0002\u0002\u0014W\u0003\u0002",
    "\u0002\u0002\u0016\u0018\u0005\u0004\u0003\u0002\u0017\u0016\u0003\u0002",
    "\u0002\u0002\u0017\u0018\u0003\u0002\u0002\u0002\u0018\u0019\u0003\u0002",
    "\u0002\u0002\u0019\u001a\u0005\u0012\n\u0002\u001a\u001b\u0007\u0002",
    "\u0002\u0003\u001b\u0003\u0003\u0002\u0002\u0002\u001c\u001e\u0005\f",
    "\u0007\u0002\u001d\u001f\u0005\u0006\u0004\u0002\u001e\u001d\u0003\u0002",
    "\u0002\u0002\u001e\u001f\u0003\u0002\u0002\u0002\u001f)\u0003\u0002",
    "\u0002\u0002 \"\u0005\u000e\b\u0002!#\u0005\b\u0005\u0002\"!\u0003\u0002",
    "\u0002\u0002\"#\u0003\u0002\u0002\u0002#)\u0003\u0002\u0002\u0002$&",
    "\u0005\u0010\t\u0002%\'\u0005\n\u0006\u0002&%\u0003\u0002\u0002\u0002",
    "&\'\u0003\u0002\u0002\u0002\')\u0003\u0002\u0002\u0002(\u001c\u0003",
    "\u0002\u0002\u0002( \u0003\u0002\u0002\u0002($\u0003\u0002\u0002\u0002",
    ")\u0005\u0003\u0002\u0002\u0002*,\u0005\u000e\b\u0002+-\u0005\u0010",
    "\t\u0002,+\u0003\u0002\u0002\u0002,-\u0003\u0002\u0002\u0002-3\u0003",
    "\u0002\u0002\u0002.0\u0005\u0010\t\u0002/1\u0005\u000e\b\u00020/\u0003",
    "\u0002\u0002\u000201\u0003\u0002\u0002\u000213\u0003\u0002\u0002\u0002",
    "2*\u0003\u0002\u0002\u00022.\u0003\u0002\u0002\u00023\u0007\u0003\u0002",
    "\u0002\u000246\u0005\f\u0007\u000257\u0005\u0010\t\u000265\u0003\u0002",
    "\u0002\u000267\u0003\u0002\u0002\u00027=\u0003\u0002\u0002\u00028:\u0005",
    "\u0010\t\u00029;\u0005\f\u0007\u0002:9\u0003\u0002\u0002\u0002:;\u0003",
    "\u0002\u0002\u0002;=\u0003\u0002\u0002\u0002<4\u0003\u0002\u0002\u0002",
    "<8\u0003\u0002\u0002\u0002=\t\u0003\u0002\u0002\u0002>@\u0005\f\u0007",
    "\u0002?A\u0005\u000e\b\u0002@?\u0003\u0002\u0002\u0002@A\u0003\u0002",
    "\u0002\u0002AG\u0003\u0002\u0002\u0002BD\u0005\u000e\b\u0002CE\u0005",
    "\f\u0007\u0002DC\u0003\u0002\u0002\u0002DE\u0003\u0002\u0002\u0002E",
    "G\u0003\u0002\u0002\u0002F>\u0003\u0002\u0002\u0002FB\u0003\u0002\u0002",
    "\u0002G\u000b\u0003\u0002\u0002\u0002HI\u0007\u0003\u0002\u0002IJ\u0005",
    "\u0014\u000b\u0002J\r\u0003\u0002\u0002\u0002KL\u0007\u0004\u0002\u0002",
    "LM\u0007\u0006\u0002\u0002M\u000f\u0003\u0002\u0002\u0002NO\u0007\u0005",
    "\u0002\u0002OP\u0007\u0006\u0002\u0002P\u0011\u0003\u0002\u0002\u0002",
    "QS\u0005\u0014\u000b\u0002RQ\u0003\u0002\u0002\u0002SV\u0003\u0002\u0002",
    "\u0002TR\u0003\u0002\u0002\u0002TU\u0003\u0002\u0002\u0002U\u0013\u0003",
    "\u0002\u0002\u0002VT\u0003\u0002\u0002\u0002WX\t\u0002\u0002\u0002X",
    "\u0015\u0003\u0002\u0002\u0002\u0011\u0017\u001e\"&(,026:<@DFT"].join("");


const atn = new antlr4.atn.ATNDeserializer().deserialize(serializedATN);

const decisionsToDFA = atn.decisionToState.map( (ds, index) => new antlr4.dfa.DFA(ds, index) );

const sharedContextCache = new antlr4.PredictionContextCache();

export default class searchParser extends antlr4.Parser {

    static grammarFileName = "search.g4";
    static literalNames = [ null, "'author:'", "'before:'", "'after:'" ];
    static symbolicNames = [ null, "AUTHOR", "BEFORE", "AFTER", "DATE", 
                             "QUOTED_TERM", "WORD", "WS" ];
    static ruleNames = [ "start", "filters", "not_author_flt", "not_before_flt", 
                         "not_after_flt", "author_flt", "before_flt", "after_flt", 
                         "terms", "term" ];

    constructor(input) {
        super(input);
        this._interp = new antlr4.atn.ParserATNSimulator(this, atn, decisionsToDFA, sharedContextCache);
        this.ruleNames = searchParser.ruleNames;
        this.literalNames = searchParser.literalNames;
        this.symbolicNames = searchParser.symbolicNames;
    }

    get atn() {
        return atn;
    }



	start() {
	    let localctx = new StartContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 0, searchParser.RULE_start);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 21;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        if((((_la) & ~0x1f) == 0 && ((1 << _la) & ((1 << searchParser.AUTHOR) | (1 << searchParser.BEFORE) | (1 << searchParser.AFTER))) !== 0)) {
	            this.state = 20;
	            this.filters();
	        }

	        this.state = 23;
	        this.terms();
	        this.state = 24;
	        this.match(searchParser.EOF);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	filters() {
	    let localctx = new FiltersContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 2, searchParser.RULE_filters);
	    var _la = 0; // Token type
	    try {
	        this.state = 38;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case searchParser.AUTHOR:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 26;
	            this.author_flt();
	            this.state = 28;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.BEFORE || _la===searchParser.AFTER) {
	                this.state = 27;
	                this.not_author_flt();
	            }

	            break;
	        case searchParser.BEFORE:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 30;
	            this.before_flt();
	            this.state = 32;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.AUTHOR || _la===searchParser.AFTER) {
	                this.state = 31;
	                this.not_before_flt();
	            }

	            break;
	        case searchParser.AFTER:
	            this.enterOuterAlt(localctx, 3);
	            this.state = 34;
	            this.after_flt();
	            this.state = 36;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.AUTHOR || _la===searchParser.BEFORE) {
	                this.state = 35;
	                this.not_after_flt();
	            }

	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	not_author_flt() {
	    let localctx = new Not_author_fltContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 4, searchParser.RULE_not_author_flt);
	    var _la = 0; // Token type
	    try {
	        this.state = 48;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case searchParser.BEFORE:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 40;
	            this.before_flt();
	            this.state = 42;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.AFTER) {
	                this.state = 41;
	                this.after_flt();
	            }

	            break;
	        case searchParser.AFTER:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 44;
	            this.after_flt();
	            this.state = 46;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.BEFORE) {
	                this.state = 45;
	                this.before_flt();
	            }

	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	not_before_flt() {
	    let localctx = new Not_before_fltContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 6, searchParser.RULE_not_before_flt);
	    var _la = 0; // Token type
	    try {
	        this.state = 58;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case searchParser.AUTHOR:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 50;
	            this.author_flt();
	            this.state = 52;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.AFTER) {
	                this.state = 51;
	                this.after_flt();
	            }

	            break;
	        case searchParser.AFTER:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 54;
	            this.after_flt();
	            this.state = 56;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.AUTHOR) {
	                this.state = 55;
	                this.author_flt();
	            }

	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	not_after_flt() {
	    let localctx = new Not_after_fltContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 8, searchParser.RULE_not_after_flt);
	    var _la = 0; // Token type
	    try {
	        this.state = 68;
	        this._errHandler.sync(this);
	        switch(this._input.LA(1)) {
	        case searchParser.AUTHOR:
	            this.enterOuterAlt(localctx, 1);
	            this.state = 60;
	            this.author_flt();
	            this.state = 62;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.BEFORE) {
	                this.state = 61;
	                this.before_flt();
	            }

	            break;
	        case searchParser.BEFORE:
	            this.enterOuterAlt(localctx, 2);
	            this.state = 64;
	            this.before_flt();
	            this.state = 66;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	            if(_la===searchParser.AUTHOR) {
	                this.state = 65;
	                this.author_flt();
	            }

	            break;
	        default:
	            throw new antlr4.error.NoViableAltException(this);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	author_flt() {
	    let localctx = new Author_fltContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 10, searchParser.RULE_author_flt);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 70;
	        this.match(searchParser.AUTHOR);
	        this.state = 71;
	        this.term();
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	before_flt() {
	    let localctx = new Before_fltContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 12, searchParser.RULE_before_flt);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 73;
	        this.match(searchParser.BEFORE);
	        this.state = 74;
	        this.match(searchParser.DATE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	after_flt() {
	    let localctx = new After_fltContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 14, searchParser.RULE_after_flt);
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 76;
	        this.match(searchParser.AFTER);
	        this.state = 77;
	        this.match(searchParser.DATE);
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	terms() {
	    let localctx = new TermsContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 16, searchParser.RULE_terms);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 82;
	        this._errHandler.sync(this);
	        _la = this._input.LA(1);
	        while(_la===searchParser.QUOTED_TERM || _la===searchParser.WORD) {
	            this.state = 79;
	            this.term();
	            this.state = 84;
	            this._errHandler.sync(this);
	            _la = this._input.LA(1);
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}



	term() {
	    let localctx = new TermContext(this, this._ctx, this.state);
	    this.enterRule(localctx, 18, searchParser.RULE_term);
	    var _la = 0; // Token type
	    try {
	        this.enterOuterAlt(localctx, 1);
	        this.state = 85;
	        _la = this._input.LA(1);
	        if(!(_la===searchParser.QUOTED_TERM || _la===searchParser.WORD)) {
	        this._errHandler.recoverInline(this);
	        }
	        else {
	        	this._errHandler.reportMatch(this);
	            this.consume();
	        }
	    } catch (re) {
	    	if(re instanceof antlr4.error.RecognitionException) {
		        localctx.exception = re;
		        this._errHandler.reportError(this, re);
		        this._errHandler.recover(this, re);
		    } else {
		    	throw re;
		    }
	    } finally {
	        this.exitRule();
	    }
	    return localctx;
	}


}

searchParser.EOF = antlr4.Token.EOF;
searchParser.AUTHOR = 1;
searchParser.BEFORE = 2;
searchParser.AFTER = 3;
searchParser.DATE = 4;
searchParser.QUOTED_TERM = 5;
searchParser.WORD = 6;
searchParser.WS = 7;

searchParser.RULE_start = 0;
searchParser.RULE_filters = 1;
searchParser.RULE_not_author_flt = 2;
searchParser.RULE_not_before_flt = 3;
searchParser.RULE_not_after_flt = 4;
searchParser.RULE_author_flt = 5;
searchParser.RULE_before_flt = 6;
searchParser.RULE_after_flt = 7;
searchParser.RULE_terms = 8;
searchParser.RULE_term = 9;

class StartContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_start;
    }

	terms() {
	    return this.getTypedRuleContext(TermsContext,0);
	};

	EOF() {
	    return this.getToken(searchParser.EOF, 0);
	};

	filters() {
	    return this.getTypedRuleContext(FiltersContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterStart(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitStart(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitStart(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class FiltersContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_filters;
    }

	author_flt() {
	    return this.getTypedRuleContext(Author_fltContext,0);
	};

	not_author_flt() {
	    return this.getTypedRuleContext(Not_author_fltContext,0);
	};

	before_flt() {
	    return this.getTypedRuleContext(Before_fltContext,0);
	};

	not_before_flt() {
	    return this.getTypedRuleContext(Not_before_fltContext,0);
	};

	after_flt() {
	    return this.getTypedRuleContext(After_fltContext,0);
	};

	not_after_flt() {
	    return this.getTypedRuleContext(Not_after_fltContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterFilters(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitFilters(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitFilters(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Not_author_fltContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_not_author_flt;
    }

	before_flt() {
	    return this.getTypedRuleContext(Before_fltContext,0);
	};

	after_flt() {
	    return this.getTypedRuleContext(After_fltContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterNot_author_flt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitNot_author_flt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitNot_author_flt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Not_before_fltContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_not_before_flt;
    }

	author_flt() {
	    return this.getTypedRuleContext(Author_fltContext,0);
	};

	after_flt() {
	    return this.getTypedRuleContext(After_fltContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterNot_before_flt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitNot_before_flt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitNot_before_flt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Not_after_fltContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_not_after_flt;
    }

	author_flt() {
	    return this.getTypedRuleContext(Author_fltContext,0);
	};

	before_flt() {
	    return this.getTypedRuleContext(Before_fltContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterNot_after_flt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitNot_after_flt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitNot_after_flt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Author_fltContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_author_flt;
    }

	AUTHOR() {
	    return this.getToken(searchParser.AUTHOR, 0);
	};

	term() {
	    return this.getTypedRuleContext(TermContext,0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterAuthor_flt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitAuthor_flt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitAuthor_flt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class Before_fltContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_before_flt;
    }

	BEFORE() {
	    return this.getToken(searchParser.BEFORE, 0);
	};

	DATE() {
	    return this.getToken(searchParser.DATE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterBefore_flt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitBefore_flt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitBefore_flt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class After_fltContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_after_flt;
    }

	AFTER() {
	    return this.getToken(searchParser.AFTER, 0);
	};

	DATE() {
	    return this.getToken(searchParser.DATE, 0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterAfter_flt(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitAfter_flt(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitAfter_flt(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TermsContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_terms;
    }

	term = function(i) {
	    if(i===undefined) {
	        i = null;
	    }
	    if(i===null) {
	        return this.getTypedRuleContexts(TermContext);
	    } else {
	        return this.getTypedRuleContext(TermContext,i);
	    }
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterTerms(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitTerms(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitTerms(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}



class TermContext extends antlr4.ParserRuleContext {

    constructor(parser, parent, invokingState) {
        if(parent===undefined) {
            parent = null;
        }
        if(invokingState===undefined || invokingState===null) {
            invokingState = -1;
        }
        super(parent, invokingState);
        this.parser = parser;
        this.ruleIndex = searchParser.RULE_term;
    }

	WORD() {
	    return this.getToken(searchParser.WORD, 0);
	};

	QUOTED_TERM() {
	    return this.getToken(searchParser.QUOTED_TERM, 0);
	};

	enterRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.enterTerm(this);
		}
	}

	exitRule(listener) {
	    if(listener instanceof searchListener ) {
	        listener.exitTerm(this);
		}
	}

	accept(visitor) {
	    if ( visitor instanceof searchVisitor ) {
	        return visitor.visitTerm(this);
	    } else {
	        return visitor.visitChildren(this);
	    }
	}


}




searchParser.StartContext = StartContext; 
searchParser.FiltersContext = FiltersContext; 
searchParser.Not_author_fltContext = Not_author_fltContext; 
searchParser.Not_before_fltContext = Not_before_fltContext; 
searchParser.Not_after_fltContext = Not_after_fltContext; 
searchParser.Author_fltContext = Author_fltContext; 
searchParser.Before_fltContext = Before_fltContext; 
searchParser.After_fltContext = After_fltContext; 
searchParser.TermsContext = TermsContext; 
searchParser.TermContext = TermContext; 
