exactFunc(F):-
    F is pi.

nearestFunc(0, 1).
nearestFunc(N, F):-
    N >= 1,
    N1 is N-1,
    nearestFunc(N1, F1),

    F is F1 + sqrt(12)*((-1)^N1)*(1/((2*N1-1)*(3^N1))),
    writeln(F).

do:-
    write("Gimme N="),
    read(N),

    exactFunc(R1),
  nearestFunc(N,R2),
    write("(exact) Y="),
    writeln(R1),
    write("(aprox) Y="),
    writeln(R2).