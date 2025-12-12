crear_tablero(1,[1]).
crear_tablero(N,R):-
    N>1,
    N1 is N-1,
    crear_tablero(N1,R1),
    append(R1,[N],R).
insertar(E,L,[E|L]).
insertar(E,[X|Y],[X|Z]) :- insertar(E,Y,Z).

permutacion([],[]).
permutacion([X|Y],Z) :- permutacion(Y,L),
                        insertar(X,L,Z).

v_abs(J,M):-
    J<0,
    M is -J.
v_abs(J,M):-
    J>0,
    M is J.

amenaza(X, Y) :-
    length(Y, N),
    Fila_N is N + 1,
    amenaza(X, Fila_N, 1, Y).


amenaza(X, Fila_N, Fila_A, [C|_]) :-
    (   X = C
    ;   Columna is X - C,
        Fila is Fila_N - Fila_A,
        v_abs(Columna,C1),
        v_abs(Fila,F1),
        C1=F1
    ), !.

amenaza(X, Fila_N, Fila_A, [_|R]) :-
    Fila_A1 is Fila_A + 1,
    amenaza(X, Fila_N, Fila_A1, R).


amenaza(_, _, _, []) :-
    false.

tablero_correcto(X,N,K):-not(amenaza(X,N)),
    append(N,[X],K).

