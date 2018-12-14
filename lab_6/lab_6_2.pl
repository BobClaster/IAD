father("Huan", "Henrich").
father("Huan", "Margo").
father("Alex", "Karmen").
father("Alex", "Etual").

father("Henrich", "Tomas").
father("Henrich", "Rob").
father("Moris", "Antuanett").

father("Tomas","Sid").
father("Tomas","Herbert").

mother("Maria", "Henrich").
mother("Maria", "Margo").
mother("Jun", "Karmen").
mother("Jun", "Etual").

mother("Etual","Tomas").
mother("Etual","Rob").
mother("Helga","Antuanett").

mother("Antuanett","Sid").
mother("Antuanett","Herbert").

man("Huan").
man("Henrich").
man("Alex").
man("Tomas").
man("Rob").
man("Sid").
man("Herbert").
woman("Maria").
woman("Margo").
woman("Jun").
woman("Karmen").
woman("Etual").
woman("Antuanett").

parents(X,Y) :-
    father(X,Y), man(X);
    mother(X,Y), woman(X).
grandfather(X,Y):-
  father(X,Z), parents(Z,Y).
grandmother(X,Y):-
  mother(X,Z), parents(Z,Y).

ancestorm(X,Y):-
  parents(X,Y), man(X).
ancestorm(X,Y):-
  parents(X,Z),ancestorm(Z,Y),man(X).

ancestorw(X,Y):-
  parents(X,Y), woman(X).
ancestorw(X,Y):-
  parents(X,Z),ancestorw(Z,Y),woman(X).

oldm(X,Y):-
    grandfather(X,Y), man(X).

oldw(X,Y):-
    grandmother(X,Y), woman(X)