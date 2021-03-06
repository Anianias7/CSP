import datetime

from backtrack import Backtrack
from constraint import Constraint
from eight_queens_puzzle import EightQueensPuzzle
from forwardcheck import ForwardCheck
from graph import Graph
from latin_square import LatinSquare
import cProfile


# pr = cProfile.Profile()
# pr.enable()
number_of_vertices = 4

constraint_function = lambda neighbors, value: value not in neighbors

constraint = Constraint(constraint_function)
graph = Graph(number_of_vertices, constraint)
latin_square = LatinSquare(graph)

# eight_queens_puzzle = EightQueensPuzzle(graph)

backtracking = Backtrack(latin_square)
start_time_b = datetime.datetime.now()
backtracking.backtracking(graph.list_of_vertices[0])
elapsed_time_b = datetime.datetime.now() - start_time_b


# pr.disable()
# pr.print_stats()

# print(backtracking.number_of_results)
# print(elapsed_time_b.microseconds)
# # print(backtracking.number_of_backs)
# print(backtracking.number_of_results)
# print(elapsed_time_b.microseconds)


# #
start_time = datetime.datetime.now()
forwardchecking = ForwardCheck(latin_square)
forwardchecking.forwardchecking(graph.list_of_vertices[0])
elapsed_time = datetime.datetime.now() - start_time
# # print(forwardchecking.number_of_results)
# # print(forwardchecking.number_of_backs)
# # print(elapsed_time.microseconds)
#
#
print("FORWARDCHECKING")
print("Number of results: ")
print(forwardchecking.number_of_results)
print("Number of backs: ")
print(forwardchecking.number_of_backs)
print("Time: ")
print(elapsed_time.microseconds)

print("BACKTRACKING")
print("Number of results: ")
print(backtracking.number_of_results)
print("Number of backs: ")
print(backtracking.number_of_backs)
print("Time: ")
print(elapsed_time_b.microseconds)
