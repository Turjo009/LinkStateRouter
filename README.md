# Routing-Algorithm
Writing code to simulate a network of routers performing implementing a Link State routing protocol, such as OSPF (Open Shorted Path First) based on Dijkstra's algorithm.

## Tasks:
1. Reads information about a topology from the standard input (typed using a keyboard).
2. Uses link state updates and Dijkstra's algorithm, as appropriate and:
Output the information in various tables in the required format during intermediate steps.
3. Read updates to the topology from standard input and repeat step 2 above, until no further input is
provided.

## Aims:
* Implement a basic links state routing algorithm.
* Learn about routing protocols and route propagation.

## Key Assumptions:
In this environment, to simplify your programs:
* Link state routing messages are not part of the simulation and you can assume that all of the
routers will have their Link-State Databases synchronized the moment a new link is established/
added/removed by reading a link state from the standard input. So the Link-State Databases
(LSDBs) are always synchronised and no intermediate steps need to be modelled.
* All neighbour tables are instantly updated at every router, the moment a new link is established/
added/removed by reading a link state from the standard input.
* When Dijkstra algorithm is run, and multiple least cost paths exist to select from in an iteration,
always select the first one in alphabetical order (in alphabetical order, by router name, so if you
have a choice of A, B and C, then select A and add it to the list of nodes for which the shorted
path is now known).
* Where multiple best routes exist, always select the first one in an alphabetical ordering of the next
hop router name.

## Expected Output:
* Neighbour Table
* Link-state Database (LSDB)
* Routing Table

## How to run:
The expected input format is shown below:

```
X
Y
Z
LINKSTATE
X-Z 1 X,Y
X-Y 5 
Y-Z 3 X,Z
UPDATE
X-Z -1 X,Y
Y-Z 9 Y,Z
END
```

### This is a sample input provided. Simply copy and paste those inputs in a terminal to see the result. For more detailed explanation, Check below:

### The input begins with name of each router/node in the topology.
Each name is on a new line.
Router names are case-sensitive, use alphanumeric characters only.
Router names may not contain spaces.
This section ends with the keyword "LINKSTATE".

### The input continues with the details of each link/edge in the topology followed by a list of
chosen router(s)
Written as the names of two routers/nodes with a - in between, followed by the weight of that
link/edge, then an optional list of routers (names separated by comma , and the list of
chosen routers can be empty). 
Your algorithm should run after each line of "LINKSTATE" input and build/update the neighbour
table, link-state database (LSDB), and routing tables for all routers with links to other routers,
according to the details of the link/edge given in the input. Then, show the Expected
Output for each router in the list of chosen routers. Weight values should always be integers.
A weight value of -1 indicates a link/edge to remove from the topology if present.
This section ends with the keyword "UPDATE"

### The input continues with the link state update details of each link/edge in the topology given a
The values in each line of input in this section should be used to update the current topology.
As above, a weight value of -1 indicates a link/edge to remove from the topology if present.
Your implementation should update the neighbour tables, link-state databases, and routing
tables as a result of receiving the link state update given in the input. Then, show the
Expected Output for each router according to the list of chosen routers (if any).
If an unseen new router/node name has been inputted in this section, your program should be
able to add this new router into the topology.
Y-A 10 X,Y
From the example input given above, your program should add A as a new router into the
topology where it has a link with a cost of 10 to Y. Then show the Expected Output for
routers X and then Y. Again, the list of chosen routers (X,Y in the example) is optional and
none may be given.
A user may input 0 or more lines of link-state updates in this section.
Continues until the keyword, "END" is inputted, at which point the program exits normally.
