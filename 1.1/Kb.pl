% parent predicate
% Queen Elizabeth II's children
parent('Queen Elizabeth II','Prince Charles').
parent('Queen Elizabeth II','Prince Andrew').
parent('Queen Elizabeth II','Prince Edward').
parent('Queen Elizabeth II','Princess Anne').

% Prince Philip's children
parent('Prince Philip','Prince Charles').
parent('Prince Philip','Prince Andrew').
parent('Prince Philip','Prince Edward').
parent('Prince Philip','Princess Anne').

% Princess Diana's children
parent('Princess Diana', 'Prince William').
parent('Princess Diana', 'Prince Harry').
% Prince Charles's children
parent('Prince Charles', 'Prince William').
parent('Prince Charles', 'Prince Harry').

% Captain Mark Phillips's children
parent('Captain Mark Phillips', 'Peter Phillips').
parent('Captain Mark Phillips', 'Zara Phillips').
% Princess Anne's children
parent('Princess Anne', 'Peter Phillips').
parent('Princess Anne', 'Zara Phillips').

% Prince Andrew's children
parent('Prince Andrew', 'Princess Beatrice').
parent('Prince Andrew', 'Princess Eugenie').
% Sarah Ferguson's children
parent('Sarah Ferguson', 'Princess Beatrice').
parent('Sarah Ferguson', 'Princess Eugenie').

% Prince Edward's children
parent('Prince Edward', 'Lady Louise Mountbatten-Windsor').
parent('Prince Edward',  'James, Viscount Severn').
% Sophie Rhys-Jones's children
parent('Sophie Rhys-Jones', 'Lady Louise Mountbatten-Windsor').
parent('Sophie Rhys-Jones',  'James, Viscount Severn').

% Prince William's children
parent('Prince William', 'Prince George').
parent('Prince William', 'Princess Charlotte').
% Kate Middleton's children
parent('Kate Middleton', 'Prince George').
parent('Kate Middleton', 'Princess Charlotte').

% Peter Phillips's children
parent('Peter Phillips', 'Savannah Phillips').
parent('Peter Phillips', 'Isla Phillips').
% Autumn Kelly's children
parent('Autumn Kelly', 'Savannah Phillips').
parent('Autumn Kelly', 'Isla Phillips').

% Mike Tindall's children
parent('Mike Tindall', 'Mia Grace Tindall').
% Zara Phillips's children
parent('Zara Phillips', 'Mia Grace Tindall').

% female predicate
female('Queen Elizabeth II').
female('Princess Diana').
female('Kate Middleton').
female('Princess Charlotte').
female('Camilla Parker Bowles').
female('Sarah Ferguson').
female('Princess Beatrice').
female('Princess Eugenie').
female('Sophie Rhysjones').
female('Lady Louise MountbattenWindsor').
female('Princess Anne').
female('Autumn Kelly').
female('Isla Phillips').
female('Savannah Phillips').
female('Zara Phillips').

% male predicate
male('Prince Philip').
male('Prince Charles').
male('Prince William').
male('Prince George').
male('Prince Harry').
male('Prince Andrew').
male('Prince Edward').
male('Jame Viscount Severn').
male('Captain Mark Phillips').
male('Timothy Laurence').
male('Peter Phillips').
male('Mike Tindall').
male('Mia Grace Tindall').

% married predicate
married('Prince Philip', 'Queen Elizabeth II').
married('Queen Elizabeth II', 'Prince Philip').
married('Prince Charles', 'Camilla Parker Bowles').
married('Camilla Parker Bowles', 'Prince Charles').
married('Prince William','Kate Middleton').
married('Kate Middleton', 'Prince William').
married('Prince Edward', 'Sophie Rhysjones').
married('Sophie Rhysjones', 'Prince Edward') .
married('Princess Anne','Timothy Laurence').
married('Timothy Laurence', 'Princess Anne').
married('Peter Phillips','Autumn Kelly').
married('Autumn Kelly', 'Peter Phillips').
married('Zara Phillips','Mike Tindall').
married('Zara Phillips', 'Mike Tindall').

% divorced predicate
divorced('Princess Diana', 'Prince Charles').
divorced('Prince Charles', 'Princess Diana').
divorced('Princess Anne', 'Captain Mark Phillips').
divorced('Captain Mark Phillips', 'Princess Anne').
divorced('Sarah Ferguson', 'Prince Andrew').
divorced('Prince Andrew', 'Sarah Ferguson').

father(Parent,Child) :- parent(Parent,Child), male(Parent).
mother(Parent,Child) :- parent(Parent,Child), female(Parent).

husband(Person,Wife) :- married(Person,Wife), male(Person).
wife(Person,Husband) :- married(Person,Husband), female(Person).

child(Child,Parent) :- parent(Parent,Child).
son(Child,Parent) :- child(Child,Parent), male(Child).
daughter(Child,Parent) :- child(Child,Parent), female(Child).

grandparent(GP,GC) :- parent(GP,Parent), parent(Parent,GC).
grandmother(GM,GC) :- grandparent(GM,GC), female(GM).
grandfather(GF,GC) :- grandparent(GF,GC), male(GF).

grandchild(GC,GP) :- grandparent(GP,GC).
grandson(GS,GP) :- grandchild(GS,GP),male(GS).
granddaughter(GD,GP) :- grandchild(GD,GP), female(GD).


sibling(Sibling, Person) :-
    setof(S, P^(parent(P, Person), parent(P, S), Person \= S), Siblings),
    member(Sibling, Siblings).
brother(Person, Sibling) :- male(Person), sibling(Person, Sibling).
sister(Person, Sibling) :- female(Person), sibling(Person, Sibling).
aunt(Person, NieceNephew) :- female(Person), sibling(Person, Parent), parent(Parent, NieceNephew).
uncle(Person, NieceNephew) :- male(Person), sibling(Person, Parent), parent(Parent, NieceNephew).
niece(Person, AuntUncle) :- female(Person), parent(Parent, Person), sibling(Parent, AuntUncle).
nephew(Person, AuntUncle) :- male(Person), parent(Parent, Person), sibling(Parent, AuntUncle).







