%Comments in Prolog
%anything that ends in a period is a fact.
%loves(romeo, juliet). <- this is a fact
%The above statement says, romeo loves juliet
%loves(juliet, romeo) :- loves(romeo, juliet).
%^ above statement says, juliet loves romeo if romeo loves juliet.
%" :- " = means if

%rectangle([X,Y,W,H]).
%functioncheck(rectangle([X,Y,W,H]),[PX,PY]):-
   % PX >= X,
   % PX =< X + W,
   % PY >= Y,
    %PY =< Y + H.


%make the world, establish the grid 12x10, just like the farmer problem where the it is established that everyone is in the west

%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GRID@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
point(1,1). point(1,2). point(1,3). point(1,4). point(1,5). point(1,6). point(1,7). point(1,8). point(1,9). point(1,10).
point(2,1). point(2,2). point(2,3). point(2,4). point(2,5). point(2,6). point(2,7). point(2,8). point(2,9). point(2,10).
point(3,1). point(3,2). point(3,3). point(3,4). point(3,5). point(3,6). point(3,7). point(3,8). point(3,9). point(3,10).
point(4,1). point(4,2). point(4,3). point(4,4). point(4,5). point(4,6). point(4,7). point(4,8). point(4,9). point(4,10).
point(5,1). point(5,2). point(5,3). point(5,4). point(5,5). point(5,6). point(5,7). point(5,8). point(5,9). point(5,10).
point(6,1). point(6,2). point(6,3). point(6,4). point(6,5). point(6,6). point(6,7). point(6,8). point(6,9). point(6,10).
point(7,1). point(7,2). point(7,3). point(7,4). point(7,5). point(7,6). point(7,7). point(7,8). point(7,9). point(7,10).
point(8,1). point(8,2). point(8,3). point(8,4). point(8,5). point(8,6). point(8,7). point(8,8). point(8,9). point(8,10).
point(9,1). point(9,2). point(9,3). point(9,4). point(9,5). point(9,6). point(9,7). point(9,8). point(9,9). point(9,10).
point(10,1). point(10,2). point(10,3). point(10,4). point(10,5). point(10,6). point(10,7). point(10,8). point(10,9). point(10,10).
point(11,1). point(11,2). point(11,3). point(11,4). point(11,5). point(11,6). point(11,7). point(11,8). point(11,9). point(11,10).
point(12,1). point(12,2). point(12,3). point(12,4). point(12,5). point(12,6). point(12,7). point(12,8). point(12,9). point(12,10).
%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@GRID@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
%
%established where the person can potentially be, *human size is 6x2
% person(3,10). person(3,9). person(3,8). person(3,7). person(3,6).
% person(3,5).
% person(4,10). person(4,9). person(4,8). person(4,7). person(4,6).
% person(4,5).
% person(5,10). person(5,9). person(5,8). person(5,7). person(5,6).
% person(5,5).
% person(6,10). person(6,9). person(6,8). person(6,7). person(6,6).
% person(6,5).
% person(7,10). person(7,9). person(7,8). person(7,7). person(7,6).
% person(7,5).
% person(8,10). person(8,9). person(8,8). person(8,7). person(8,6).
% person(8,5).
% person(9,10). person(9,9). person(9,8). person(9,7). person(9,6).
% person(9,5).

person([point(3,5), point(3,6), point(3,7), point(3,8), point(3,9), point(3,10),
        point(4,5), point(4,6), point(4,7), point(4,8), point(4,9), point(4,10)]).

person([point(4,5), point(4,6), point(4,7), point(4,8), point(4,9), point(4,10),
		point(5,5), point(5,6), point(5,7), point(5,8), point(5,9), point(5,10)]).

person([point(5,5), point(5,6), point(5,7), point(5,8), point(5,9), point(5,10),
		point(6,5), point(6,6), point(6,7), point(6,8), point(6,9), point(6,10)]).

person([point(6,5), point(6,6), point(6,7), point(6,8), point(6,9), point(6,10),
		point(7,5), point(7,6), point(7,7), point(7,8), point(7,9), point(7,10)]).

person([point(7,5), point(7,6), point(7,7), point(7,8), point(7,9), point(7,10),
		point(8,5), point(8,6), point(8,7), point(8,8), point(8,9), point(8,10)]).

person([point(8,5), point(8,6), point(8,7), point(8,8), point(8,9), point(8,10),
		point(9,5), point(9,6), point(9,7), point(9,8), point(9,9), point(9,10)]).

person([point(9,5), point(9,6), point(9,7), point(9,8), point(9,9), point(9,10),
		point(10,5), point(10,6), point(10,7), point(10,8), point(10,9), point(10,10)]).


%the obstacle coordinate is established with the placed_mirror function.
%check to see if the coordinate of the obstacle is valid.

% use the check function to see if the obstacle is within the grid

rectangle([Xcoor,Ycoor,Width,Height]).

functioncheck(rectangle([X,Y,W,H]),[PX,PY]):-
    PX > X,
    PX =< X + W,
    PY >= Y,
    PY =< Y + H.
%
inObstacle([PX,PY],[FarLeft, Width, Height]) :-
    functioncheck(rectangle([FarLeft, 0, Width, Height]), [PX,PY]).

% check if coordinate (x,y), in this case [PX,PY], is contained in the
% the obstacle, which is assumed as a special rectangle


legalGridPoint([PX,PY],[FarLeft, Width, Height]) :-
    point(PX,PY),
    not(inObstacle([PX,PY],[FarLeft, Width, Height])).
%current coordinate = lazer
%check if a coordinate is where it is suppose to be.
%it is legal if it is inside the room and it is not within an
%obstacle.


%this is checking if the gridpoint is inside the room
%this is checking safety if the gridpoint is outside an obstacle


%recurse through each obstacle and not just one
%extend ^ so it is recursive

%basecase
legalGridPointVersion2(_,[]).
%terminating condition is when there is no more obstacle to compare to

legalGridPointVersion2([PX,PY],[Obstacle|Obstacle2]):-
    point(PX,PY),
    not(inObstacle([PX,PY],Obstacle)),
    legalGridPointVersion2([PX,PY],Obstacle2).
%recursive version of legalgridpoint

%startlaser([1,_]).
%if a list has 2 elements and starts with integer 1
%it is a start laser

%endlaserdetector([12,_]).



% lazermove
move([X,SqY],right,[Xv2,SqY]) :- Xv2 is X+1.

move([SqX,Y],up,[SqX,Yv2]) :- Yv2 is Y-1.

move([SqX,Y],down,[SqX,Yv2]) :- Yv2 is Y+1.



%Given
%place_mirrors(3, [[2,2,3],[9,2,4]], X).
%X = [[2,3,/],[2,7,/],[9,7,\],[9,3,\]]


%reflect(DirectionFrom, Mirror, DirectionGoingTo).
%reflect(incoming, _angle_, heading)
reflect(down, \, right).
%reflect(fromNorth, /, goLeft).

%reflect(fromSouth, \, goLeft).
reflect(up, /, right).

reflect(right, \, down).
reflect(right, /, up).

%sensorheight is where to expect the sensor on the other wall
%the y value is the input sensor height
%this goes straight right
%if the above two things are met return the list of mirrors

% think of function of the same name, as an if else
%statement

navigate(SensorHeight, point(12,SensorHeight), right, Mirrors, Mirrors,_, _).
% terminating condition, when the lazer is in coordinate x= 12 and the
% given sensor height, it is going right, then returning mirrors.

%navigate straight line
navigate(SensorHeight,point(PX,PY), Direction, InputMirrors, ReturnMirrors,Obstacles, person(X)) :-
    move([PX,PY], Direction, [NX,NY]),
    legalGridPointVersion2([NX,NY],Obstacles),
    not(member(point(NX,NY),X)),
    navigate(SensorHeight,point(NX,NY), Direction, InputMirrors, ReturnMirrors,Obstacles, person(X)).
    %fails when it encounters a human, or


%navigate turning/reflect
%right on top of where it is needed to put a mirror
navigate(SensorHeight,point(PX,PY), Direction, InputMirrors, ReturnMirrors,Obstacles, person(X)) :-
    length(InputMirrors, MirrorAmount),
    MirrorAmount < 8,
    %check if input mirrors has less than eight elements
    reflect(Direction, Mirror, NDirection),
    move([PX,PY],NDirection,[NX,NY]),
    legalGridPointVersion2([NX,NY],Obstacles),
    %record where the mirror is place using append
    append(InputMirrors,[[PX,PY,Mirror]],NewMirrors),
    not(member(point(NX,NY),X)),
    navigate(SensorHeight,point(NX,NY), NDirection, NewMirrors, ReturnMirrors,Obstacles, person(X)).

%make sure that the lazer does not intersect with the human
%human is 6x2 obstacle

% place_mirrors(OFFTHEGROUND, [obstacleSize], MirrorPlacement).
% //predicate, for place mirror to return true we need to make sure that
% the lazer emitter has to go to the detector, but it cannot be a
% straight line
% it must leave atleast one human size hole
% it has to place mirrors in a way that the lazer follows a path that
% does not intersect with any obstacle.
% less than 8 mirrors
% if the conditions above are met, place_mirrors is true
place_mirrors(OffTheGround,Obstacles,MirrorPlacement) :-
    person(X),
    navigate(OffTheGround, point(1,OffTheGround), right, [],MirrorPlacement, Obstacles, person(X)).


%the condition that must be met is that
%a person can exist in this points stated as facts.
% then navigate with this given starting point, direction; that it
% is going right, initial empty mirror placement, list of resulted
% mirrors, given obstacles, and an instance of the person where it can
% legally be at.

