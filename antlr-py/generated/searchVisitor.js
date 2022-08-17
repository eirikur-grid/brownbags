// Generated from /Users/eirikur/Brownbags/antlr/search.g4 by ANTLR 4.9.2
// jshint ignore: start
import antlr4 from 'antlr4';

// This class defines a complete generic visitor for a parse tree produced by searchParser.

export default class searchVisitor extends antlr4.tree.ParseTreeVisitor {

	// Visit a parse tree produced by searchParser#start.
	visitStart(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#filters.
	visitFilters(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#not_author_flt.
	visitNot_author_flt(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#not_before_flt.
	visitNot_before_flt(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#not_after_flt.
	visitNot_after_flt(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#author_flt.
	visitAuthor_flt(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#before_flt.
	visitBefore_flt(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#after_flt.
	visitAfter_flt(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#terms.
	visitTerms(ctx) {
	  return this.visitChildren(ctx);
	}


	// Visit a parse tree produced by searchParser#term.
	visitTerm(ctx) {
	  return this.visitChildren(ctx);
	}



}