This project has been created as part of the 42 curriculum by sedeniz, bakarsu.

# A-Maze-ing

## Description

*A-Maze-ing* is a maze generation and solving project developed as part of the 42 curriculum.

The program generates a maze from a configuration file, represents the maze using hexadecimal cell values, and provides a terminal-based visualisation of the generated maze. It supports different maze generation approaches and can calculate and display the shortest path between the entrance and exit.

The main goals of the project are:

•⁠  ⁠Parsing and validating a maze configuration.
•⁠  ⁠Representing a maze using reusable entities.
•⁠  ⁠Generating perfect mazes using the *Hunt and Kill* algorithm.
•⁠  ⁠Generating an alternative maze layout using a *Pac-Man-style maze braiding algorithm*.
•⁠  ⁠Finding the shortest path between the entry and exit using *Breadth-First Search (BFS)*.
•⁠  ⁠Rendering the maze in the terminal using ASCII/ANSI characters.
•⁠  ⁠Providing an interactive menu for regenerating mazes, changing the maze style, displaying the shortest path, and changing wall colours.

The project was developed collaboratively, with the code divided into independent components so that the main entities, algorithms, parser, renderer, and utilities can be reused or extended independently.

---

## Features

•⁠  ⁠Configuration-file based maze generation.
•⁠  ⁠Random maze dimensions and entry/exit generation.
•⁠  ⁠Perfect maze generation using Hunt and Kill.
•⁠  ⁠Alternative Pac-Man-style maze generation.
•⁠  ⁠Shortest-path calculation using BFS.
•⁠  ⁠Terminal ASCII rendering.
•⁠  ⁠Optional shortest-path visualisation.
•⁠  ⁠Rotating wall colours.
•⁠  ⁠Reproducible maze generation through seeds.
•⁠  ⁠Restricted cells that cannot be carved through.
•⁠  ⁠Hexadecimal maze output compatible with the project specification.
•⁠  ⁠Modular architecture allowing additional maze-generation algorithms to be added.

---

## Bonus

### Zero Dead Ends

Our maze generator supports the generation of mazes with **0 dead ends**.

The generator identifies dead-end cells and opens additional walls while preserving the maze structure, resulting in a maze without any dead-end cells.


## Instructions

### Requirements

The project requires:

•⁠  ⁠Python 3
•⁠  ⁠⁠ pip ⁠
•⁠  ⁠The dependencies listed in ⁠ requirements.txt ⁠
•⁠  ⁠⁠ make ⁠

### Installation

Install the required Python dependencies with:

⁠ bash
make install
 ⁠

This runs:

⁠ bash
python3 -m pip install -r requirements.txt
 ⁠

### Running the program

The default configuration can be run with:

⁠ bash
make run
 ⁠

This executes:

⁠ bash
python3 a_maze_ing.py config.txt
 ⁠

### Debugging

The program can be launched using Python's built-in debugger:

⁠ bash
make debug
 ⁠

This is equivalent to:

⁠ bash
python3 -m pdb a_maze_ing.py config.txt
 ⁠

### Code checks

Run the standard linting and type checking with:

⁠ bash
make lint
 ⁠

This runs:

⁠ bash
flake8 .
mypy . --warn-return-any --warn-unused-ignores \
    --ignore-missing-imports --disallow-untyped-defs \
    --check-untyped-defs
 ⁠

For stricter type checking:

⁠ bash
make lint-strict
 ⁠

This runs:

⁠ bash
flake8 .
mypy . --strict
 ⁠

### Cleaning generated files

To remove Python cache directories and the mypy cache:

⁠ bash
make clean
 ⁠

This removes:

•⁠  ⁠⁠ __pycache__/ ⁠
•⁠  ⁠⁠ .mypy_cache/ ⁠


### Requirements

The project requires:

•⁠  ⁠Python 3.10 or newer
•⁠  ⁠⁠ make ⁠
•⁠  ⁠A terminal supporting ANSI escape sequences

No external Python packages are required.

### Running the project

Clone the repository and enter the project directory:

⁠ bash
git clone https://github.com/Soda0001/42-A-maze-ing.git
cd a-maze-ing
 ⁠

The project can be run using:

⁠ bash
python3 main.py config.txt
 ⁠

or, if using the provided Makefile:

⁠ bash
make
 ⁠

Follow the instructions displayed by the program to interact with the maze.

### Main menu

The program provides the following options:

 1.⁠ ⁠Regenerate a new random maze
 2.⁠ ⁠Turn the maze into a Pac-Man maze
 3.⁠ ⁠Show / hide the shortest path
 4.⁠ ⁠Rotate the wall colours
 5.⁠ ⁠Quit

---

# Configuration File

The program receives its initial settings from a configuration file.

The configuration file contains the following mandatory parameters:

⁠ text
WIDTH=10
HEIGHT=10
ENTRY=0,0
EXIT=9,9
OUTPUT_FILE=maze.txt
PERFECT=True
 ⁠

### ⁠ WIDTH ⁠

Defines the width of the maze.

⁠ text
WIDTH=10
 ⁠

### ⁠ HEIGHT ⁠

Defines the height of the maze.

⁠ text
HEIGHT=10
 ⁠

### ⁠ ENTRY ⁠

Defines the coordinates of the entrance cell.

⁠ text
ENTRY=0,0
 ⁠

The coordinates are represented as:

⁠ text
x,y
 ⁠

### ⁠ EXIT ⁠

Defines the coordinates of the exit cell.

⁠ text
EXIT=9,9
 ⁠

### ⁠ OUTPUT_FILE ⁠

Defines the file in which the generated maze is written.

⁠ text
OUTPUT_FILE=maze.txt
 ⁠

### ⁠ PERFECT ⁠

Determines whether the initial maze should be generated as a perfect maze.

⁠ text
PERFECT=True
 ⁠

or

⁠ text
PERFECT=False
 ⁠

Comments can be included using ⁠ # ⁠.

Example:

⁠ text
# Maze configuration

WIDTH=10
HEIGHT=10

ENTRY=0,0
EXIT=9,9

OUTPUT_FILE=maze.txt

PERFECT=True
 ⁠

The parser validates the configuration and converts the values into the appropriate Python types before they are passed to the rest of the program.

---

# Maze Representation

Each maze cell contains information about its position and its walls.

The four walls are represented using four bits:

⁠ text
Bit 0 = North
Bit 1 = East
Bit 2 = South
Bit 3 = West
 ⁠

A set bit represents a *closed wall*.

The four bits are converted into a hexadecimal character when the maze is written to the output file.

For example, a cell with all four walls closed is represented as:

⁠ text
1111 -> F
 ⁠

while a cell with no walls closed is:

⁠ text
0000 -> 0
 ⁠

This representation makes the maze compact while retaining all wall information.

---

# Maze Generation Algorithm

## Hunt and Kill

The main perfect-maze generation algorithm used by the project is *Hunt and Kill*.

The algorithm consists of two main phases:

### 1. Kill phase

The algorithm starts from a cell and randomly moves to an unvisited neighbouring cell.

When moving to a neighbouring cell, the wall between the two cells is removed.

This continues until the current cell has no unvisited neighbours.

### 2. Hunt phase

When the current path reaches a dead end, the algorithm searches for an unvisited cell that has at least one visited neighbour.

That cell becomes the new starting point, and the kill phase begins again.

The process continues until every available cell has been visited.

Restricted cells are excluded from the generation process.

## Why Hunt and Kill?

We chose Hunt and Kill because it is relatively simple to implement while producing valid perfect mazes.

It also fits the architecture of the project well because the algorithm can operate directly on the maze and cell entities without requiring a complicated additional data structure.

Another advantage is that it naturally produces a maze where cells are connected without unnecessary loops, making it suitable for the project's definition of a perfect maze.

---

# Pac-Man Maze

As an additional feature, the project includes a second maze-generation approach inspired by Pac-Man-style mazes.

The Pac-Man maze generation is handled separately from Hunt and Kill, allowing different generation algorithms to coexist within the project.

The ⁠ MazeGenerator ⁠ acts as the higher-level component responsible for selecting the generation approach.

This architecture makes it possible to add other algorithms in the future without having to rewrite the maze representation or rendering system.

---

# Pathfinding

The shortest path between the entry and exit is calculated using *Breadth-First Search (BFS)*.

BFS is appropriate because the maze can be represented as an unweighted graph:

•⁠  ⁠Each cell is a node.
•⁠  ⁠An open wall between two cells represents an edge.
•⁠  ⁠Every edge has the same cost.

BFS explores the maze level by level. Therefore, when it reaches the exit, the resulting path contains the minimum number of cell-to-cell moves.

The algorithm keeps track of previously visited cells and their predecessors so that the final path can be reconstructed from the exit back to the entry.

The resulting path can optionally be displayed by the renderer.

---

# Reusable Code

The project was designed around reusable components rather than putting all functionality into ⁠ main.py ⁠.

### Entities

The maze and cell classes form the core representation of the project.

The same entities are used by:

•⁠  ⁠Maze generation
•⁠  ⁠Pathfinding
•⁠  ⁠Rendering
•⁠  ⁠Maze validation
•⁠  ⁠Output generation

This means that a new maze-generation algorithm can operate on the existing ⁠ Maze ⁠ and ⁠ Cell ⁠ classes without needing to create a separate representation.

### Maze generation

The generation algorithms are implemented independently.

The Hunt and Kill implementation can therefore be replaced or supplemented with another algorithm without changing the renderer or pathfinding implementation.

### Pathfinding

The BFS implementation works on the maze structure rather than on a specific generation algorithm.

Therefore, it can find paths through mazes generated by either Hunt and Kill or the Pac-Man-style generator.

### Parsing

The configuration parser is separated from the rest of the program.

This allows configuration validation and conversion to be handled independently from maze generation.

### Rendering

The renderer receives the maze state and displays it without being responsible for how the maze was generated.

This separation allows different generation algorithms to use the same renderer.

---

# Project Structure

The project is divided into several components:

⁠ text
a-maze-ing/
│
├── entities/
│   ├── cell.py
│   └── maze.py
│
├── generators/
│   ├── maze_generator.py
│   ├── hunt_and_kill.py
│   └── maze_braider.py
│
├── parsing_utils/
│   └── parsing_utils.py
│
├── pathfinding/
│   └── bfs.py
│
├── render/
│   └── ascii.py
│
├── main.py
├── Makefile
├── config.txt
└── README.md
 ⁠

The exact structure may evolve as the project develops.

---

# Team and Project Management

## Team

### sedeniz

Responsible for:

•⁠  ⁠Maze and Cell entities
•⁠  ⁠Hunt and Kill maze-generation algorithm
•⁠  ⁠Breadth-First Search pathfinding algorithm
•⁠  ⁠Configuration parsing

### bakarsu

Responsible for:

•⁠  ⁠ASCII/terminal rendering
•⁠  ⁠Pac-Man maze braiding algorithm
•⁠  ⁠Makefile

### Shared responsibilities

Although individual components were assigned to each member, important architectural decisions were discussed together.

In particular, we discussed:

•⁠  ⁠How the program should be launched and how the different components should interact.
•⁠  ⁠How the maze and cell entities should be designed.
•⁠  ⁠How constants should be organised and shared.
•⁠  ⁠How configuration parsing should work.
•⁠  ⁠How the different maze-generation algorithms should fit into the overall architecture.

This helped keep independently developed components compatible with each other.

---

# Project Planning

At the beginning of the project, we divided the work according to the major components of the program.

The initial plan was to establish the maze representation and configuration parsing first, since the generation algorithms, pathfinding, and renderer all depend on these components.

The project then progressed approximately as follows:

 1.⁠ ⁠Design the maze and cell entities.
 2.⁠ ⁠Implement configuration parsing and validation.
 3.⁠ ⁠Implement the Hunt and Kill maze-generation algorithm.
 4.⁠ ⁠Implement BFS pathfinding.
 5.⁠ ⁠Implement the terminal renderer.
 6.⁠ ⁠Implement the Pac-Man-style maze generation.
 7.⁠ ⁠Connect all components through the main program.
 8.⁠ ⁠Add interactive features and improve validation.
 9.⁠ ⁠Test different maze dimensions, entry/exit positions, and generation modes.
10.⁠ ⁠Integrate the final components and prepare the project for evaluation.

During development, some architectural decisions evolved as we encountered new requirements.

For example, the maze-generation architecture was kept flexible so that different algorithms could coexist rather than making the program dependent on a single generation algorithm.

---

# What Worked Well

The separation between the maze representation, algorithms, parsing, and rendering worked well.

In particular:

•⁠  ⁠The ⁠ Maze ⁠ and ⁠ Cell ⁠ entities provide a common structure for all algorithms.
•⁠  ⁠BFS does not depend on how the maze was generated.
•⁠  ⁠The renderer does not need to know which generation algorithm created the maze.
•⁠  ⁠Configuration parsing is isolated from the rest of the application.
•⁠  ⁠Generation algorithms can be added without rewriting the existing maze representation.
•⁠  ⁠Working on separate components allowed both team members to develop parts of the project independently.

The use of constants also helped avoid duplicating important values throughout the project.

---

# What Could Be Improved

With more time, several aspects could be improved.

The project could support additional maze-generation algorithms, such as:

•⁠  ⁠Binary Tree
•⁠  ⁠Recursive Backtracking
•⁠  ⁠Prim's algorithm
•⁠  ⁠Kruskal's algorithm

The rendering system could also be extended with additional visualisation options.

Testing could be expanded with more automated tests for:

•⁠  ⁠Configuration validation
•⁠  ⁠Boundary conditions
•⁠  ⁠Restricted cells
•⁠  ⁠Entry and exit validation
•⁠  ⁠Maze connectivity
•⁠  ⁠BFS shortest-path correctness
•⁠  ⁠Different maze dimensions

The project management process could also be improved by defining smaller milestones earlier and integrating components more frequently during development.

---

# Tools

We used several tools during development:

•⁠  ⁠*Git* for version control.
•⁠  ⁠*GitHub* for repository hosting and collaboration.
•⁠  ⁠*Python* for implementation.
•⁠  ⁠*Make* for project commands and code-quality checks.
•⁠  ⁠*VS Code* for development and debugging.
•⁠  ⁠*42 evaluation tools/environment* for testing the project against the project requirements.

Git was particularly useful for allowing both team members to work on separate components and integrate their work throughout the project.

---

# Resources

The project was developed using the 42 subject as the primary specification, together with documentation and educational resources about maze generation, graph traversal, and pathfinding.

### Python

Python documentation and general references were used for:

•⁠  ⁠Classes and object-oriented programming
•⁠  ⁠Type hints
•⁠  ⁠⁠ random ⁠
•⁠  ⁠File handling
•⁠  ⁠Data structures
•⁠  ⁠Exceptions

### Video References

The following YouTube resources were consulted throughout the development of the project. They were used as supplementary learning material to better understand maze generation, maze solving, graph traversal, pathfinding, and different approaches to representing and manipulating mazes.

These resources helped us understand the underlying concepts and algorithms. We did not directly copy implementations from them; instead, we used the ideas we learned to develop our own implementation according to the requirements of the 42 project and our own architecture.

•⁠  ⁠*Maze generation and maze algorithms*
  https://youtu.be/ioUl1M77hww
  Used as supplementary material for understanding maze-generation algorithms and how cells and passages can be represented.

•⁠  ⁠*Maze generation concepts*
  https://youtu.be/zbXKcDVV4G0
  Helped us understand different approaches to generating mazes and the characteristics of the resulting maze structures.

•⁠  ⁠*Maze algorithms and implementation*
  https://youtu.be/powd-2TXj5g
  Used to better understand maze construction and the relationship between cells, walls, and neighbouring cells.

•⁠  ⁠*Maze generation and solving concepts*
  https://youtu.be/Y37-gB83HKE
  Used as additional material when researching possible approaches to generating and solving mazes.

•⁠  ⁠*Maze algorithms*
  https://www.youtube.com/watch?v=KiCBXu4P-2Y
  Consulted while researching maze-generation techniques and different ways of approaching maze construction.

•⁠  ⁠*Maze generation and solving*
  https://www.youtube.com/watch?v=kgKa3axL_dM
  Used as supplementary material for understanding maze traversal and solving techniques.

•⁠  ⁠*Maze algorithms and pathfinding*
  https://www.youtube.com/watch?v=V1oZQm1HtVw
  Helped reinforce concepts related to navigating a maze and finding paths between cells.

•⁠  ⁠*Breadth-First Search and pathfinding*
  https://www.youtube.com/watch?v=34SNQHapJYE
  Used as learning material for graph traversal, shortest-path algorithms, and concepts relevant to our BFS implementation.

•⁠  ⁠*Maze solving and pathfinding*
  https://www.youtube.com/watch?v=25B66fOb0GA
  Consulted as additional material for understanding maze-solving strategies and shortest-path concepts.

These resources were used for *learning and conceptual reference*. The final implementation was developed specifically for this project and adapted to our own ⁠ Maze ⁠, ⁠ Cell ⁠, maze-generation, BFS pathfinding, parsing, and rendering architecture.

---

# AI Usage

AI tools were used as a supplementary development and learning resource.

AI assistance was used for:

•⁠  ⁠Understanding Breadth-First Search and shortest-path reconstruction.
•⁠  ⁠Discussing possible project architectures and how the different components could interact.
•⁠  ⁠Debugging Python errors and unexpected behaviour.
•⁠  ⁠Reviewing code for logical errors.
•⁠  ⁠Discussing edge cases involving maze boundaries, restricted cells, entry/exit cells, and neighbouring cells.
•⁠  ⁠Reviewing and improving parts of the documentation.
•⁠  ⁠Help writing this README.md file

AI was *not used as a replacement for implementing and understanding the project*. The final architecture and implementation decisions were discussed, tested, and adapted by the team.

The use of AI was mainly focused on learning, debugging, explaining concepts, and evaluating possible approaches.

---

# Conclusion

A-Maze-ing combines maze generation, graph traversal, configuration parsing, object-oriented design, and terminal rendering into a single project.

The modular structure allows the project to be extended with new maze-generation algorithms, pathfinding methods, or rendering systems without requiring the entire application to be rewritten.