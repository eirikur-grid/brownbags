grammar search;

start: filters? terms EOF;

filters:
    author_flt not_author_flt?
    | before_flt not_before_flt?
    | after_flt not_after_flt?;

not_author_flt:
    before_flt after_flt?
    | after_flt before_flt?;

not_before_flt:
    author_flt after_flt?
    | after_flt author_flt?;

not_after_flt:
    author_flt before_flt?
    | before_flt author_flt?;

author_flt:
    AUTHOR term;

before_flt: BEFORE DATE;

after_flt: AFTER DATE;

terms: term*;

term: WORD | QUOTED_TERM;

AUTHOR: 'author:';
BEFORE: 'before:';
AFTER: 'after:';

DATE: YYYY '-' MM '-' DD;

fragment YYYY: [1-9][0-9]*;
fragment MM: '0'? [1-9] | '1' [0-2];
fragment DD: '0'? [1-9] | [1-2] [0-9] | '3' [0-1];

QUOTED_TERM: '"' (~["] | '""')* '"';

WORD: [@!#$%&_()A-Za-z0-9\u0080-\ufffe]+;

WS: [ \t\r\n\u000C]+ -> channel(HIDDEN);
