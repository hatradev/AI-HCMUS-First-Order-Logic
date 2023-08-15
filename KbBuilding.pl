% Facts


% parent predicate
% Define the children of Queen Elizabeth II and Prince Philip as a list
childrens_of_queen(['Prince Charles', 'Princess Anne', 'Prince Andrew', 'Prince Edward']).
% Define the parent-child relationships using member/2
parent('Queen Elizabeth II', Child) :- childrens_of_queen(Childrens), member(Child, Childrens).
parent('Prince Philip', Child) :- childrens_of_queen(Childrens), member(Child, Childrens).

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


% male predicate
male('Prince Philip').

male('Prince Charles').
male('Captain Mark Phillips').
male('Timothy Laurence').
male('Prince Andrew').
male('Prince Edward').

male('Prince William').
male('Prince Harry').
male('Peter Phillips').
male('Mike Tindall').

male('James, Viscount Severn').
male('Prince George').


% married predicate
married('Queen Elizabeth II', 'Prince Philip').
married('Prince Charles', 'Camilla Parker Bowles').
married('Timothy Laurence', 'Princess Anne').
married('Sophie Rhys-jones', 'Prince Edward').
married('Prince William', 'Kate Middleton').
married('Autumn Kelly', 'Peter Phillips').
married('Zara Phillips', 'Mike Tindall').

married(Person1, Person2) :- married(Person2, Person1).


% female predicate
female('Queen Elizabeth II').

female('Princess Diana').
female('Camilla Parker Bowles').
female('Princess Anne').
female('Sarah Ferguson').
female('Sophie Rhys-jones').

female('Kate Middleton').
female('Autumn Kelly').
female('Zara Phillips').
female('Princess Beatrice').
female('Princess Eugenie').
female('Lady Louise Mountbatten-Windsor').

female('Princess Charlotte').
female('Savannah Phillips').
female('Isla Phillips').
female('Mia Grace Tindall').


% divorced predicate
divorced('Princess Diana', 'Prince Charles').
divorced('Captain Mark Phillips', 'Princess Anne').
divorced('Sarah Ferguson', 'Prince Andrew').

divorced(Person1, Person2) :- divorced(Person2, Person1).



% Rules
husband(Person, Wife) :- male(Person), married(Person, Wife).
wife(Person, Husband) :- female(Person), married(Husband, Person).
father(Parent, Child) :- male(Parent), parent(Parent, Child).
mother(Parent, Child) :- female(Parent), parent(Parent, Child).
child(Child, Parent) :- parent(Parent, Child).
son(Child, Parent) :- male(Child), parent(Parent, Child).
daughter(Child, Parent) :- female(Child), parent(Parent, Child).

grandparent(GP, GC) :- parent(GP, P), parent(P, GC).
grandmother(GM, GC) :- female(GM), grandparent(GM, GC).
grandfather(GF, GC) :- male(GF), grandparent(GF, GC).
grandchild(GC, GP) :- grandparent(GP, GC).
grandson(GS, GP) :- male(GS), grandchild(GS, GP).
granddaughter(GD, GP) :- female(GD), grandchild(GD, GP).

sibling(Sibling, Person) :-
    setof(S, P^(parent(P, Person), parent(P, S), Person \= S), Siblings),
    member(Sibling, Siblings).
brother(Person, Sibling) :- male(Person), sibling(Person, Sibling).
sister(Person, Sibling) :- female(Person), sibling(Person, Sibling).
aunt(Person, NieceNephew) :- female(Person), sibling(Person, Parent), parent(Parent, NieceNephew).
uncle(Person, NieceNephew) :- male(Person), sibling(Person, Parent), parent(Parent, NieceNephew).
niece(Person, AuntUncle) :- female(Person), parent(Parent, Person), sibling(Parent, AuntUncle).
nephew(Person, AuntUncle) :- male(Person), parent(Parent, Person), sibling(Parent, AuntUncle).