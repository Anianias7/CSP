import datetime

from backtrack import Backtrack
from constraint import Constraint
from forwardcheck import ForwardCheck
from graph import Graph
from latin_square import LatinSquare

number_of_vertices = 25
constraint_function = lambda neighbors, value: value not in neighbors

constraint = Constraint(constraint_function)
graph = Graph(number_of_vertices, constraint)
latin_square = LatinSquare(graph)

start_time_b = datetime.datetime.now()
backtracking = Backtrack(latin_square)
backtracking.backtracking(graph.list_of_vertices[0])
elapsed_time_b = datetime.datetime.now() - start_time_b

start_time = datetime.datetime.now()
forwardchecking = ForwardCheck(latin_square)
forwardchecking.forwardchecking(graph.list_of_vertices[0])
elapsed_time = datetime.datetime.now() - start_time

print("FORWARDCHECKING")
print("Number of results: ")
print(forwardchecking.number_of_results)
print("Number of backs: ")
print(forwardchecking.number_of_backs)
print("Time: ")
print(elapsed_time)

print("BACKTRACKING")
print("Number of results: ")
print(backtracking.number_of_results)
print("Number of backs: ")
print(backtracking.number_of_backs)
print("Time: ")
print(elapsed_time_b)
