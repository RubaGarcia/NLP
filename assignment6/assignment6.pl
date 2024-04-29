% determiners: la, las ,el, los, un, una, unos, unas
lex(la, det(sg,fem)).
lex(las, det(pl,fem)).
lex(el, det(sg,masc)).
lex(los, det(pl,masc)).
lex(un, det(sg,masc)).
lex(una, det(sg, fem)).
lex(unos, det(pl, masc)).
lex(unas, det(pl, fem)).

% nouns: perra, perras, perro, perros, hueso, huesos, estudiante
lex(perra, n(sg,fem)).
lex(perras, n(pl,fem)).
lex(perro, n(sg,masc)).
lex(perros, n(pl,masc)).
lex(hueso, n(sg,masc)).
lex(huesos, n(pl,masc)).
lex(estudiante, n(sg,_)).

% adj: bonito, bonita, bonitas, bonitos
lex(bonito, adj(sg,masc)).
lex(bonita, adj(sg,fem)).
lex(bonitos, adj(pl,masc)).
lex(bonitas, adj(pl,fem)).

% verbs:ladra, ladran, muerde, muerden
lex(ladra, itv(sg,_)).
lex(ladran, itv(pl,_)).
lex(muerde, tv(sg,_)).
lex(muerden, tv(pl,_)).

% S -> NP VP
s --> np(NUM,GEN), vp(NUM,GEN).

% NP -> Det N | Det N Adj
np(NUM,GEN) --> deter(NUM,GEN), noun(NUM,GEN).
np(NUM,GEN) --> deter(NUM,GEN), noun(NUM,GEN), adje(NUM,GEN).

% VP -> V | V NP
vp(NUM,GEN) --> verb(itv(NUM,GEN)).
vp(NUM,GEN) --> verb(tv(NUM,GEN)), np(_,_).

% Det -> la | las | el | los | un | una | unos | unas
deter(NUM,GEN) --> [Det], {lex(Det,det(NUM,GEN))}.

% N -> perra | perras | perro | perros | hueso | huesos | estudiante
noun(NUM,GEN) --> [N], {lex(N,n(NUM,GEN))}.

% Adj -> bonito | bonita | bonitos | bonitas
adje(NUM, GEN) --> [Adj], {lex(Adj,adj(NUM,GEN))}.

% V -> ladra | ladran | muerde | muerden
verb(TYPE) --> [V], {lex(V,TYPE)}.