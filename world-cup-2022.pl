/* 
 *  FACTS ABOUT WORLD CUP 2022.
 */
/* defines stages */
stage(group).
stage(knockout).
stage(quarter).
stage(semi_final).
stage(third_playoff).
stage(final).
/* defines teams */
team(qatar). team(ecuador). team(senegal). team(netherlands).
team(england). team(iran). team(usa). team(wales).
team(argentina). team(saudi_arabia). team(mexico). team(poland).
team(france). team(australia). team(denmark). team(tunisia).
team(spain). team(costa_rica). team(germany). team(japan).
team(belgium). team(canada). team(morocco). team(croatia).
team(brazil). team(serbia). team(switzerland). team(cameroon).
team(portugal). team(ghana). team(uruguay). team(south_korea).
/* defines groups */
group(a). group(b). group(c). group(d). group(e). group(f). group(g). group(h).
groupList([a,b,c,d,e,f,g,h]).
/* defines team is belongs to group */
groupTeams(a, [qatar, ecuador, senegal, netherlands]).
groupTeams(b, [england, iran, usa, wales]).
groupTeams(c, [argentina, saudi_arabia, mexico, poland]).
groupTeams(d, [france, australia, denmark, tunisia]).
groupTeams(e, [spain, costa_rica, germany, japan]).
groupTeams(f, [belgium, canada, morocco, croatia]).
groupTeams(g, [brazil, serbia, switzerland, cameroon]).
groupTeams(h, [portugal, ghana, uruguay, south_korea]).
/* defines pair group to knockout */
groupPair(a,b).
groupPair(c,d).
groupPair(e,f).
groupPair(g,h).
/* defines all matches */
/* defines matches of group A */
match(group, qatar, ecuador, 0, 2, 0, 0).
match(group, senegal, netherlands, 0, 2, 0, 0).
match(group, qatar, senegal, 1, 3, 0, 0).
match(group, netherlands, ecuador, 1, 1, 0, 0).
match(group, ecuador, senegal, 1, 2, 0, 0).
match(group, netherlands, qatar, 2, 0, 0, 0).
/* defines matches of group B */
match(group, england, iran, 6, 2, 0, 0).
match(group, usa, wales, 1, 1, 0, 0).
match(group, wales, iran, 0, 2, 0, 0).
match(group, england, usa, 0, 0, 0, 0).
match(group, wales, england, 0, 3, 0, 0).
match(group, iran, usa, 0, 1, 0, 0).
/* defines matches of group C */
match(group, argentina, saudi_arabia, 1, 2, 0, 0).
match(group, mexico, poland, 0, 0, 0, 0).
match(group, poland, saudi_arabia, 2, 0, 0, 0).
match(group, argentina, mexico, 2, 0, 0, 0).
match(group, poland, argentina, 0, 2, 0, 0).
match(group, saudi_arabia, mexico, 1, 2, 0, 0).
/* defines matches of group D */
match(group, denmark, tunisia, 0, 0, 0, 0).
match(group, france, australia, 4, 1, 0, 0).
match(group, tunisia, australia, 0, 1, 0, 0).
match(group, france, denmark, 2, 1, 0, 0).
match(group, australia, denmark, 1, 0, 0, 0).
match(group, tunisia, france, 1, 0, 0, 0).
/* defines matches of group E */
match(group, germany, japan, 1, 2, 0, 0).
match(group, spain, costa_rica, 7, 0, 0, 0).
match(group, japan, costa_rica, 0, 1, 0, 0).
match(group, spain, germany, 1, 1, 0, 0).
match(group, japan, spain, 2, 1, 0, 0).
match(group, costa_rica, germany, 2, 4, 0, 0).
/* defines matches of group F */
match(group, morocco, croatia, 0, 0, 0, 0).
match(group, belgium, canada, 1, 0, 0, 0).
match(group, belgium, morocco, 0, 2, 0, 0).
match(group, croatia, canada, 4, 1, 0, 0).
match(group, croatia, belgium, 0, 0, 0, 0).
match(group, canada, morocco, 1, 2, 0, 0).
/* defines matches of group G */
match(group, switzerland, cameroon, 1, 0, 0, 0).
match(group, brazil, serbia, 2, 0, 0, 0).
match(group, cameroon, serbia, 3, 3, 0, 0).
match(group, brazil, switzerland, 1, 0, 0, 0).
match(group, serbia, switzerland, 2, 3, 0, 0).
match(group, cameroon, brazil, 1, 0, 0, 0).
/* defines matches of group H */
match(group, uruguay, south_korea, 0, 0, 0, 0).
match(group, portugal, ghana, 3, 2, 0, 0).
match(group, south_korea, ghana, 2, 3, 0, 0).
match(group, portugal, uruguay, 2, 0, 0, 0).
match(group, ghana, uruguay, 0, 2, 0, 0).
match(group, south_korea, portugal, 2, 1, 0, 0).

match(knockout, netherlands, usa, 3, 1, 0, 0).
match(knockout, argentina, australia, 2, 1, 0, 0).
match(knockout, france, poland, 3, 1, 0, 0).
match(knockout, england, senegal, 3, 0, 0, 0).
match(knockout, japan, croatia, 1, 1, 1, 3).
match(knockout, brazil, south_korea, 4, 1, 0, 0).
match(knockout, morocco, spain, 0, 0, 3, 0).
match(knockout, portugal, switzerland, 6, 1, 0, 0).

match(quarter, croatia, brazil, 1, 1, 4, 2).
match(quarter, netherlands, argentina, 2, 2, 3, 4).
match(quarter, morocco, portugal, 1, 0, 0, 0).
match(quarter, england, france, 1, 2, 0, 0).

match(semi_final, argentina, croatia, 3, 0, 0, 0).
match(semi_final, france, morocco, 2, 0, 0, 0).

match(third_playoff, croatia, morocco, 2, 1, 0, 0).

match(final, argentina, france, 3, 3, 4, 2).

/*
 *  RULES ABOUT WORLD CUP.
 */

/* utils */
specificTeamCleanSheets(SpecificTeam, CleanSheets) :-
    findall(1, match(_, SpecificTeam, _, 0, _, _, _), CleanSheetMatches1),
    findall(1, match(_, _, SpecificTeam, _, 0, _, _), CleanSheetMatches2),
    length(CleanSheetMatches1, CleanSheets1),
    length(CleanSheetMatches2, CleanSheets2),
    CleanSheets is CleanSheets1 + CleanSheets2.
stageHasPenaltyShootouts(Stage) :- match(Stage, _, _, _, _, Pen1, Pen2), (Pen1 > 0; Pen2 > 0).
totalGoalsScored(TotalGoals) :-
    findall(Goals, (match(_, _, _, Goals, _, _, _); match(_, _, _, _, Goals, _, _)), GoalsList),
    sum_list(GoalsList, TotalGoals).

/* win - draw rules */
win(Stage, Team1, Team2) :- 
    match(Stage, Team1, Team2, Goals1, Goals2, Pen1, Pen2) -> (Goals1 + Pen1 > Goals2 + Pen2); 
    match(Stage, Team2, Team1, GoalsA, GoalsB, PenA, PenB) -> (GoalsA + PenA < GoalsB + PenB).

draw(Stage, Team1, Team2) :- 
    match(Stage, Team1, Team2, Goals1, Goals2, Pen1, Pen2) -> (Goals1 == Goals2 -> Pen1 == Pen2); 
    match(Stage, Team2, Team1, GoalsA, GoalsB, PenA, PenB) -> (GoalsA == GoalsB -> PenA == PenB).
/*
draw(Stage, Team2, Team1) :- match(Stage, Team1, Team2, Goal, Goal, Pen, Pen). 
*/
/* check team is in group */
teamInGroup(Group, Team) :- groupTeams(Group, TeamList), member(Team, TeamList).
/* get group of a team */
groupOfTeam(Team, GoalGroup) :- groupList(GroupList),getTeamGroup(Team,GroupList,GoalGroup).
getTeamGroup(_, [], _) :- fail.
getTeamGroup(Team, [Group | RestGroup], GoalGroup) :-
    (teamInGroup(Group, Team) -> (GoalGroup = Group) ; getTeamGroup(Team, RestGroup, GoalGroup)).

/* rule for group stage */
matchesPlayedInGroupStage(TotalMatches) :-
    findall(1, match(group, _, _, _, _, _, _), Matches),
    length(Matches, TotalMatches).
score(Team1, Team2, Score) :- win(group, Team1, Team2) -> Score = 3; draw(group, Team1, Team2) -> Score = 1;  Score = 0.

calculateScoreHelper(_, [], Acc, Acc).

calculateScoreHelper(GoalTeam, [Team | RestTeams], Acc, Score) :- 
    score(GoalTeam, Team, ScoreOf),
    NewAcc is Acc + ScoreOf,
    calculateScoreHelper(GoalTeam, RestTeams, NewAcc, Score).

calculateScore(GoalTeam, Score) :-
    groupOfTeam(GoalTeam, GroupOfGoalTeam),
    groupTeams(GroupOfGoalTeam, Teams),
    calculateScoreHelper(GoalTeam, Teams, 0, Score).

goalsFor(Team, TotalGoals, Stage) :-
    findall(GoalsFor1, match(Stage, Team, _, GoalsFor1, _, _, _), GoalsList1),
    sum_list(GoalsList1, TotalGoals1),
    findall(GoalsFor2, match(Stage, _, Team, _, GoalsFor2, _, _), GoalsList2),
    sum_list(GoalsList2, TotalGoals2),
    TotalGoals is TotalGoals1 + TotalGoals2.
goalsAgainst(Team, TotalGoals, Stage) :-
    findall(GoalsAgainst1, match(Stage, Team, _, _, GoalsAgainst1, _, _), GoalsList1),
    sum_list(GoalsList1, TotalGoals1),
    findall(GoalsAgainst2, match(Stage, _, Team, GoalsAgainst2, _, _, _), GoalsList2),
    sum_list(GoalsList2, TotalGoals2),
    TotalGoals is TotalGoals1 + TotalGoals2.

goalDifference(Team, Difference) :-
    goalsFor(Team, GoalsFor, group),
    goalsAgainst(Team, GoalsAgainst, group),
    Difference is GoalsFor - GoalsAgainst.

topTeams(Group, TopTeams) :-
    groupTeams(Group, Teams),
    findall(Score-GoalDiff-Team, (member(Team, Teams), calculateScore(Team, Score), goalDifference(Team, GoalDiff)), ScoredTeams),
    keysort(ScoredTeams, SortedScoredTeams),
    reverse(SortedScoredTeams, ReversedScoredTeams),
    pairs_values(ReversedScoredTeams, TopTeams).

top2Teams(Group, FirstTeam, SecondTeam):-
    topTeams(Group, TopTeams),
    [FirstTeam | RestTeams] = TopTeams,
    [SecondTeam | _] = RestTeams.

/* rule for knockout stage */
knockOutMatchPairs(MatchPairs) :-
    findall(BestOfFirstGroup-SecondBestOfSecondGroup,
        (groupPair(FirstGroup, SecondGroup),
        top2Teams(FirstGroup, BestOfFirstGroup, _),
        top2Teams(SecondGroup, _,SecondBestOfSecondGroup),
        BestOfFirstGroup \= SecondBestOfSecondGroup), MatchPairsBestAndSecond),
    findall(SecondBestOfFirstGroup-BestOfSecondGroup,
        (groupPair(FirstGroup, SecondGroup),
        top2Teams(FirstGroup, _, SecondBestOfFirstGroup),
        top2Teams(SecondGroup, BestOfSecondGroup,_),
        BestOfSecondGroup \= SecondBestOfFirstGroup), MatchPairsSecondAndBest),
    append(MatchPairsBestAndSecond, MatchPairsSecondAndBest, MatchPairs).

getWinner(Team1-Team2, Winner, Stage) :-
    win(Stage, Team1, Team2) -> Winner = Team1; Winner = Team2.
getLoser(Team1-Team2, Loser, Stage) :-
    win(Stage, Team1, Team2) -> Loser = Team2; Loser = 1.

loopAndGetWinners([], [], _).
loopAndGetWinners([MatchPair|RestPairs], [Winner|RestWinners], Stage) :-
    getWinner(MatchPair, Winner, Stage),
    loopAndGetWinners(RestPairs, RestWinners, Stage).

loopAndGetLosers([], [], _).
loopAndGetLosers([MatchPair|RestPairs], [Loser|RestLosers], Stage) :-
    getLoser(MatchPair, Loser, Stage),
    loopAndGetLosers(RestPairs, RestLosers, Stage).

knockOutWinners(Winners) :- 
   knockOutMatchPairs(Pairs), 
   loopAndGetWinners(Pairs, Winners, knockout).
/* rule for quarter stage */
loopAndGetPairs([], []).
loopAndGetPairs([Winner1, Winner2|RestWinners], [MatchPair|RestPairs]) :-
    MatchPair = Winner1-Winner2,
    loopAndGetPairs(RestWinners, RestPairs).
quarterFinalMatchPairs(MatchPairs) :- knockOutWinners(Winners), loopAndGetPairs(Winners, MatchPairs).

quaterFinalWinners(Winners):-
   quarterFinalMatchPairs(Pairs), 
   loopAndGetWinners(Pairs, Winners, quarter).
    
/* rule for semi-final stage */
semiFinalMatchPairs(MatchPairs) :- quaterFinalWinners(Winners), loopAndGetPairs(Winners, MatchPairs).
semiFinalWinners(Winners):-
   semiFinalMatchPairs(Pairs), 
   loopAndGetWinners(Pairs, Winners, semi_final).
semiFinalLosers(Losers):-
    semiFinalMatchPairs(Pairs), 
    loopAndGetLosers(Pairs, Losers, semi_final).
/* rule for third_playoff stage */
thirdPlayOffMatchPairs(Pair) :- semiFinalLosers(Winners), loopAndGetPairs(Winners, MatchPairs), MatchPairs = [Pair|_].
thirdWinner(Winner) :- thirdPlayOffMatchPairs(Pair), getWinner(Pair, Winner, third_playoff). 
/* rule for final stage */
finalMatchPair(Pair) :- semiFinalWinners(Winners), loopAndGetPairs(Winners, MatchPairs), MatchPairs = [Pair|_].
finalLoser(RunnerUp) :- finalMatchPair(Pair), getLoser(Pair, RunnerUp, final). 
finalWinner(Champion) :- finalMatchPair(Pair), getWinner(Pair, Champion, final). 