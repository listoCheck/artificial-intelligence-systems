% Student exercise profile
:- set_prolog_flag(occurs_check, error).        % disallow cyclic terms
:- set_prolog_stack(global, limit(8 000 000)).  % limit term space (8Mb)
:- set_prolog_stack(local,  limit(2 000 000)).  % limit environment space

gender(liza_m, female, 2012, 0).
gender(artem_a, male, 2005, 0).
gender(kate_a, female, 1994, 0).
gender(urii_v, male, 1991, 0).
gender(olga_v, female, 1973, 0).
gender(mark_a, male, 1970, 0).
gender(andrey_v, male, 1967, 0).
gender(elena_e, female, 1971, 0).
gender(galina_k, female, 1944, 0).
gender(vladimir_n, male, 1942, 1990).
gender(dina_d, female, 1945, 0).
gender(eduard_a, male, 1944, 1987).
gender(konstantin_p, male, 1901, 1980).
gender(agnia_a, female, 1900, 1977).
gender(alexey_m, male, 1904, 1970).
gender(arina_i, female, 1899, 1970).
gender(pavel_a, male, 1946, 2014).
gender(olga_p, female, 1943, 2000).
gender(tatiana_p, female, 1968, 0).
gender(lubov_p, female, 1973, 0).
gender(anna_p, female, 1980, 0).
gender(mikhail_p, male, 1975, 0).
gender(elena_k, female, 1975, 0).
gender(konstantin_m, male, 1993, 0).
gender(pavel_a, male, 2000, 0).
gender(grigorii_a, male, 1947, 2003).
gender(anna_m, female, 1950, 2006).
gender(vasilii_g, male, 1978, 0).
gender(natalia_g, female, 1980, 0).
gender(alexey_g, female, 1988, 0).
gender(anna_a, female, 1956, 0).

marriage(kate_a, urii_v, 2022, 0).
marriage(andrey_v, elena_e, 1987, 0).
marriage(olga_v, mark_a, 1991, 0).
marriage(galina_k, vladimir_n, 1966, 0).
marriage(dina_d, eduard_a, 1962, 1968).
marriage(agnia_a, konstantin_p, 1940, 0).
marriage(arina_i, alexey_m, 1939, 0).
marriage(anna_m, grigorii_a, 1967, 0).
marriage(olga_m, pavel_a, 1971, 0).
marriage(elena_k, mikhail_p, 1992, 0).

parent(mark_a, liza_m, 2012).
parent(olga_v, liza_m, 2012).
parent(andrey_v, artem_a, 2005).
parent(elena_e, artem_a, 2005).
parent(andrey_v, kate_a, 1994).
parent(elena_e, kate_a, 1994).
parent(galina_k, olga_v, 1967).
parent(vladimir_n, olga_v, 1967).
parent(galina_k, andrey_v, 1967).
parent(vladimir_n, andrey_v, 1967).
parent(dina_d, elena_e, 1971).
parent(eduard_a, elena_e, 1971).
parent(konstantin_p, galina_k, 1944).
parent(agnia_a, galina_k, 1944).
parent(alexey_m, vladimir_n, 1942).
parent(arina_i, vladimir_n, 1942).
parent(alexey_m, pavel_a, 1942).
parent(arina_i, pavel_a, 1942).
parent(alexey_m, grigorii_a, 1942).
parent(arina_i, grigorii_a, 1942).
parent(alexey_m, anna_a, 1942).
parent(arina_i, anna_a, 1942).


ex_spouse(Person1, Person2) :-
    marriage(Person1, Person2, _, End),
    End \= 0.

sibling(X, Y, Year) :-
    parent(P, X, Year),
    parent(P, Y, Year),
    X \= Y.

grandparent(GP, GC, Year) :-
    parent(GP, P, Year),
    parent(P, GC, Year).

alive(Person, Year) :-
    gender(Person, _, Birth, Death),
    Year >= Birth,
    (Death = 0; Year =< Death).

married_longer_than(Person1, Person2, Years) :-
    marriage(Person1, Person2, Start, End),
    (End = 0 -> DeathYear = 2025; DeathYear = End),
    Duration is DeathYear - Start,
    Duration >= Years.

uncle_aunt(UncleAunt, Person, Year) :-
    parent(P, Person, Year),
    sibling(UncleAunt, P, Year),
    gender(UncleAunt, _, _, _).
