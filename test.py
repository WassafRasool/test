#csp past paper
# ==========================================
# CSP: PRESENTATION SCHEDULING
# ==========================================

# List of presentations (variables)
tasks = ["T1", "T2", "T3", "T4", "T5"]

# Slots available (domain values)
slots = [1, 2, 3, 4, 5]

# Dictionary to store assignment (solution)
assignment = {}


# ------------------------------------------
# CHECK CONSTRAINTS FUNCTION
# ------------------------------------------
def is_valid(task, slot):

    # Check if slot already assigned to another task
    if slot in assignment.values():
        return False

    # -----------------------------
    # Constraint 3:
    # T5 cannot be in slot 1 or 2
    # -----------------------------
    if task == "T5" and slot in [1, 2]:
        return False

    # -----------------------------
    # Constraint 5:
    # T4 cannot be in slot 5
    # -----------------------------
    if task == "T4" and slot == 5:
        return False

    # -----------------------------
    # Constraint 6:
    # Slot 3 only for T1 or T2
    # -----------------------------
    if slot == 3 and task not in ["T1", "T2"]:
        return False

    # -----------------------------
    # Now check constraints involving other assigned tasks
    # -----------------------------
    for t, s in assignment.items():

        # Constraint 2:
        # T2 must be before T4
        if task == "T2" and t == "T4" and slot >= s:
            return False
        if task == "T4" and t == "T2" and slot <= s:
            return False

        # Constraint 4:
        # T3 must be after T1
        if task == "T3" and t == "T1" and slot <= s:
            return False
        if task == "T1" and t == "T3" and slot >= s:
            return False

        # Constraint 1:
        # T1 and T3 not consecutive
        if task == "T1" and t == "T3" and abs(slot - s) == 1:
            return False
        if task == "T3" and t == "T1" and abs(slot - s) == 1:
            return False

    return True


# ------------------------------------------
# BACKTRACKING FUNCTION
# ------------------------------------------
def backtrack(index):

    # If all tasks assigned → solution found
    if index == len(tasks):
        return True

    task = tasks[index]

    # Try all slots
    for slot in slots:

        # Check if assignment is valid
        if is_valid(task, slot):

            # Assign slot
            assignment[task] = slot

            # Recur for next task
            if backtrack(index + 1):
                return True

            # Undo assignment (backtrack)
            del assignment[task]

    return False


# ------------------------------------------
# RUN BACKTRACKING
# ------------------------------------------
if backtrack(0):
    print("Final Schedule:")

    for task in assignment:
        print(task, "-> Slot", assignment[task])
else:
    print("No solution found")





#MinimaxAgent

import math
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth
    
    def act(self, node, environment):
        value = environment.compute_minimax(node, self.depth, True)
        return f"Minimax value: {value}"

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def compute_minimax(self, node, depth, maximizing_player=True):
        if depth == 0 or not node.children:
            self.computed_nodes.append(node.value)
            return node.value
        if maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.compute_minimax(child, depth-1, False))
        else:
            value = math.inf
            for child in node.children:
                value = min(value, self.compute_minimax(child, depth-1, True))
        node.minimax_value = value
        return value

def run_agent(agent, environment, root):
    result = agent.act(root, environment)
    print(result)

# sample tree
root = Node('A')
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]
n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]
n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]
n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]
# define depth for Minimax
depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)


#Alpha beta pruning
import math
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.minimax_value = None

class MinimaxAgent:
    def __init__(self, depth):
        self.depth= depth
    
    def formulate_goal(self, node):
        return "Goal reached" if node.minimax_value is not None else "Searching"
    
    def act(self, node, environment):
        goal_status = self.formulate_goal(node)
        if goal_status == "Goal reached":
            return f"Minimax value for root node: {node.minimax_value}"
        else:
            return environment.alpha_beta_search(node, self.depth, -math.inf, math.inf, True)
        
class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computed_nodes = []

    def get_percept(self, node):
        return node
    
    def alpha_beta_search(self, node, depth, alpha, beta, Maximizing_player=True):
        self.computed_nodes.append(node)
        if depth == 0 or not node.children:
            return node.value
        
        if Maximizing_player:
            value = -math.inf
            for child in node.children:
                value = max(value, self.alpha_beta_search(child, depth-1, alpha, beta, False))
                alpha = max(alpha, value)
                if beta <= alpha:
                    print("Pruned node: ", child.value)
                    break
            node.minimax_value = value
            return value
        else: 
            value = math.inf
            for child in node.children:
                value = min(value, self.alpha_beta_search(child, depth-1, alpha, beta, True))
                beta = min(beta, value)
                if beta <= alpha:
                    print("Pruned node: ", child.value)
                    break
            node.minimax_value = value
            return value
        
def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    result = agent.act(percept, environment)
    print(result)

depth = 3
agent = MinimaxAgent(depth)
environment = Environment(root)
run_agent(agent, environment, root)
print("Computed Nodes:", environment.computed_nodes)
print("Minimax values:")
print(f"A: {root.minimax_value}")
print(f"B: {n1.minimax_value}")
print(f"C: {n2.minimax_value}")
print(f"D: {n3.minimax_value}")
print(f"E: {n4.minimax_value}")
print(f"F: {n5.minimax_value}")
print(f"G: {n6.minimax_value}")


#ALPHA BETA PRUNING
import math
class Node:
    def __init__(self, value=None):
        self.value = value        
        self.children = []       
        self.minmaxValue = None  

# Goal Based Agent
class AlphaBetaAgent:
    def __init__(self, depth):
        self.depth = depth

    def formulateGoal(self, node):
        # checks if we already computed the answer
        return "Goal reached" if node.minmaxValue is not None else "Searching"

    def act(self, node, environment):
        goalStatus = self.formulateGoal(node)
        if goalStatus == "Goal reached":
            return f"Minimax value for root node: {node.minmaxValue}"
        else:
            return environment.alphaBetaSearch(node, self.depth, -math.inf, math.inf, True)

class Environment:
    def __init__(self, tree):
        self.tree = tree
        self.computedNodes = []

    def getPercept(self, node):
        return node

    def alphaBetaSearch(self, node, depth, alpha, beta, maximizingPlayer=True):
        self.computedNodes.append(node.value)

        if depth == 0 or not node.children:
            return node.value

        if maximizingPlayer:
            value = -math.inf
            for i, child in enumerate(node.children):
                childValue = self.alphaBetaSearch(child, depth - 1, alpha, beta, False)
                value = max(value, childValue)
                alpha = max(alpha, value)     
                
                if alpha >= beta:
                    remaining = node.children[i+1:]
                    pruned_values = []
                    for n in remaining:
                        pruned_values.append(n.value)

                    print("Pruned nodes:", pruned_values)
                    break
            node.minmaxValue = value
            return value
        
        else:  
            value = math.inf
            for i, child in enumerate(node.children):
                childValue = self.alphaBetaSearch(child, depth - 1, alpha, beta, True)
                value = min(value, childValue)
                beta = min(beta, value)        
                if alpha >= beta:              
                    remaining = node.children[i + 1:]
                    pruned_values = []
                    for n in remaining:
                        pruned_values.append(n.value)

                    print("Pruned nodes:", pruned_values)
                    break
            node.minmaxValue = value
            return value

def runAgent(agent, environment, startNode):
    percept = environment.getPercept(startNode)
    result = agent.act(percept, environment)
    print("Minimax value:", result)


root = Node('A') # constructing tree
n1 = Node('B')
n2 = Node('C')
root.children = [n1, n2]
n3 = Node('D')
n4 = Node('E')
n5 = Node('F')
n6 = Node('G')
n1.children = [n3, n4]
n2.children = [n5, n6]
n7 = Node(2)
n8 = Node(3)
n9 = Node(5)
n10 = Node(9)
n3.children = [n7, n8]
n4.children = [n9, n10]
n11 = Node(0)
n12 = Node(1)
n13 = Node(7)
n14 = Node(5)
n5.children = [n11, n12]
n6.children = [n13, n14]

depth = 3   # depth = number of edges from root to leaves
agent = AlphaBetaAgent(depth)
environment = Environment(root)
runAgent(agent, environment, root)

print("Order visited:", environment.computedNodes)
print("Minimax values:")
print(f"A: {root.minmaxValue}")
print(f"B: {n1.minmaxValue}")
print(f"C: {n2.minmaxValue}")
print(f"D: {n3.minmaxValue}")
print(f"E: {n4.minmaxValue}")
print(f"F: {n5.minmaxValue}")
print(f"G: {n6.minmaxValue}")


#CSP Template
from ortools.sat.python import cp_model

variables = ['A', 'B', 'C'] 
domain = ['Red', 'Green', 'Blue'] 
model = cp_model.CpModel()

solverVars = {}
for var in variables:
   solverVars[var] = model.new_int_var(0, len(domain) - 1, var)

model.add_all_different(solverVars.values())
model.add(solverVars['A'] != solverVars['B'])
model.add(solverVars['A'] == 0)

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables
        self.solutions = []     

    def on_solution_callback(self):          
        sol = {}
        for var, intVar in self.variables.items():   
            sol[var] = domain[self.value(intVar)]  
        self.solutions.append(sol)

collector = SolutionCollector(solverVars)

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True 
status = solver.solve(model, collector)

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(f"Total solutions found: {len(collector.solutions)}\n")
    for i, sol in enumerate(collector.solutions):
        print(f"Solution {i + 1}: {sol}")
else:
    print("No solution found.")


#CSP Sudoku Solver
from ortools.sat.python import cp_model

puzzle = [
    [5, 3, 0,  0, 7, 0,  0, 0, 0],
    [6, 0, 0,  1, 9, 5,  0, 0, 0],
    [0, 9, 8,  0, 0, 0,  0, 6, 0],
    [8, 0, 0,  0, 6, 0,  0, 0, 3],
    [4, 0, 0,  8, 0, 3,  0, 0, 1],
    [7, 0, 0,  0, 2, 0,  0, 0, 6],
    [0, 6, 0,  0, 0, 0,  2, 8, 0],
    [0, 0, 0,  4, 1, 9,  0, 0, 5],
    [0, 0, 0,  0, 8, 0,  0, 7, 9]
]

model = cp_model.CpModel()

cellVars = []
for r in range(9):
    row = []
    for c in range(9):
        row.append(model.new_int_var(1, 9, f'cell_{r}_{c}'))
    cellVars.append(row)

for r in range(9):
    for c in range(9):
        if puzzle[r][c] != 0:
            model.add(cellVars[r][c] == puzzle[r][c])

for r in range(9):
    model.add_all_different(cellVars[r])

for c in range(9):
    col = []
    for r in range(9):
        col.append(cellVars[r][c])
    model.add_all_different(col)

for boxRow in range(3):
    for boxCol in range(3):
        box = []
        for r in range(boxRow * 3, boxRow * 3 + 3):
            for c in range(boxCol * 3, boxCol * 3 + 3):
                box.append(cellVars[r][c])
        model.add_all_different(box)

solver = cp_model.CpSolver()
status = solver.solve(model)

def printSudoku(grid):
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print(" --------------")
        rowStr = "  "
        for c in range(9):
            if c % 3 == 0 and c != 0:
                rowStr += "| "
            rowStr += str(grid[r][c]) + " "
        print(rowStr)

print("Original puzzle (0 = empty):")
printSudoku(puzzle)

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print("\nSolved puzzle:")
    solved = []
    for r in range(9):
        row = []
        for c in range(9):
            row.append(solver.value(cellVars[r][c]))
        solved.append(row)
    printSudoku(solved)
else:
    print("no solution found.")


# CSP - Dressing Schedule

from ortools.sat.python import cp_model
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
shirtPants = []
for s in range(1, 6):                   
    for p in range(1, 4):
        shirtPants.append(f'S{s}-P{p}')

shalwarQamees = ['SQ1', 'SQ2']  
allOutfits    = shirtPants + shalwarQamees        

model = cp_model.CpModel()

dayVars = {}
for day in days:
    dayVars[day] = model.new_int_var(0, len(allOutfits) - 1, day)

model.add(dayVars['Monday'] <= 14)      
model.add(dayVars['Thursday'] <= 14)    
model.add(dayVars['Friday'] >= 15)      
model.add_all_different(dayVars.values())

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables                    
        self.solutions = []                        

    def on_solution_callback(self):
        sol = {}
        for day, var in self.variables.items():         
            sol[day] = allOutfits[self.value(var)]      
        self.solutions.append(sol)

collector = SolutionCollector(dayVars)

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True      
status = solver.solve(model, collector)

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(f"Total valid schedules: {len(collector.solutions)}\n")
    print("First 5 solutions:")
    for i, sol in enumerate(collector.solutions[:5]):
        print(f"\n  Schedule {i}:")
        for day, outfit in sol.items():
            print(f"    {day:<12} : {outfit}")
else:
    print("No solution found.")


# CSP Graph Colouring
from ortools.sat.python import cp_model
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['B', 'D']
}

colors = ['Red', 'Green', 'Blue']
nodes = list(graph.keys()) 

model = cp_model.CpModel()

nodeVars = {}
for node in nodes:
    nodeVars[node] = model.new_int_var(0, len(colors) - 1, node)

for node, neighbors in graph.items():
    for neighbor in neighbors:
        if node < neighbor:                   
            model.add(nodeVars[node] != nodeVars[neighbor])

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)  
        self.variables = variables                       
        self.solutions = []                              

    def on_solution_callback(self):
        sol = {}
        for node, var in self.variables.items():          
            sol[node] = colors[self.value(var)]          
        self.solutions.append(sol)                        

collector = SolutionCollector(nodeVars)

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True      
status = solver.solve(model, collector)

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(f"Total valid colorings found: {len(collector.solutions)}\n")
    print("First 5 solutions:")
    for i, sol in enumerate(collector.solutions[:5]):
        print(f"Solution {i + 1}: {sol}")
else:
    print("No solution found.")


# CSP - N-Queens Problem
from ortools.sat.python import cp_model
N = 4

model = cp_model.CpModel()
queenVars = {}
for row in range(N):
    queenVars[row] = model.new_int_var(0, N - 1, f'row_{row}')

model.add_all_different(queenVars.values())

for r1 in range(N):
    for r2 in range(r1 + 1, N):
        model.add(queenVars[r1] - queenVars[r2] != r1 - r2)   
        model.add(queenVars[r1] - queenVars[r2] != r2 - r1)   

class SolutionCollector(cp_model.CpSolverSolutionCallback):
    def __init__(self, variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.variables = variables              
        self.solutions = []     

    def on_solution_callback(self):               
        sol = {}
        for row, var in self.variables.items():
            sol[row] = self.value(var)              
        self.solutions.append(sol)

collector = SolutionCollector(queenVars)

solver = cp_model.CpSolver()
solver.parameters.enumerate_all_solutions = True       
status = solver.solve(model, collector)

def printBoard(sol):
    for row in range(N):
        line = ""
        for col in range(N):
            if sol[row] == col:
                line += "Q "
            else:
                line += ". "
        print(f"  {line}")
    print()

if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
    print(f"Total solutions for {N}-queens: {len(collector.solutions)}\n")
    print("Showing first 3 solutions:\n")
    for i, sol in enumerate(collector.solutions[:3], 1):
        print(f"Solution {i}:")
        printBoard(sol)
else:
    print("No solution found.")


#Supervised Decision Tree

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

df = pd.read_csv("customers.csv")
print(df.info()) #Study
df = df.drop("applicant_id", axis=1)

numCols = df.select_dtypes(include=['number']).columns
for col in numCols:
    df[col] = df[col].fillna(df[col].median())

catCols = df.select_dtypes(exclude=['number']).columns
for col in catCols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:", df.isnull().sum().sum())

le = LabelEncoder()
textCols = df.select_dtypes(include=["str", "object"]).columns
for col in textCols:
    df[col] = le.fit_transform(df[col])

numCols = df.select_dtypes(include=['number']).columns

# Feature Selection (Correlation)
featureCorr = df[numCols].corr()['loan_approved'].drop('loan_approved')  # exclude itself
topFeatures = featureCorr.sort_values(ascending=False)

print("\nTop Features by Correlation with Loan Approval:")
print(topFeatures)

plt.figure(figsize=(12, 10))
sns.heatmap(df[numCols].corr(), cmap='coolwarm')
plt.title("Correlation Matrix of Features")
plt.show()

X = df.drop("loan_approved", axis=1) #Train
y = df["loan_approved"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

dt = DecisionTreeClassifier(random_state=42)   
dt.fit(XTrain, yTrain) # trains
yPred = dt.predict(XTest)

print("\nEvaluation")
print(f"Training Accuracy: {dt.score(XTrain, yTrain) * 100:.2f}%")
print(f"Testing Accuracy: {accuracy_score(yTest, yPred) * 100:.2f}%")
print("Precision:", precision_score(yTest, yPred, zero_division=0))
print("Recall:", recall_score(yTest, yPred, zero_division=0))
print("F1 Score:", f1_score(yTest, yPred, zero_division=0))

featureNames = X.columns.tolist()
newApplicantDf = pd.DataFrame([X.median()], columns=featureNames)

pred = dt.predict(newApplicantDf)[0]
label = "APPROVED" if pred == 1 else "REJECTED"
print(f"\nNew Applicant (Median Profile): {label}")


#Linear Regression

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

df = pd.read_csv("students.csv")
print(df.info())
df = df.drop("student_id", axis=1)

numCols = df.select_dtypes(include=['number']).columns
for col in numCols:
    df[col] = df[col].fillna(df[col].median())

catCols = df.select_dtypes(exclude=['number']).columns
for col in catCols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:", df.isnull().sum().sum())

le = LabelEncoder()
textCols = df.select_dtypes(include=["str", "object"]).columns
for col in textCols:
    df[col] = le.fit_transform(df[col])

numCols = df.select_dtypes(include=['number']).columns

featureCorr = df[numCols].corr()['final_score'].drop('final_score')  # exclude itself
topFeatures = featureCorr.sort_values(ascending=False)

print("\nTop Features by Correlation with Final Score:")
print(topFeatures)

plt.figure(figsize=(12, 10))
sns.heatmap(df[numCols].corr(), cmap='coolwarm')
plt.title("Correlation Matrix of Features")
plt.show()

X = df.drop("final_score", axis=1)
y = df["final_score"]

XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()   
lr.fit(XTrain, yTrain)        
yPred = lr.predict(XTest)

print("\nEvaluation")
r2 = r2_score(yTest, yPred)
print(f"Accuracy (R2): {r2 * 100:.2f}%")
print("MAE:", mean_absolute_error(yTest, yPred))
print("RMSE:", mean_squared_error(yTest, yPred) ** 0.5)

featureNames = X.columns.tolist() # Predicts
newStudentDf = pd.DataFrame([X.median()], columns=featureNames)

predictedScore = lr.predict(newStudentDf)[0]
print(f"\nNew Student (Median Profile): Predicted Score: {predictedScore:.1f}")


# Supervised Learning SVM

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import(
    confusion_matrix, accuracy_score,
    precision_score, recall_score, f1_score,
    ConfusionMatrixDisplay
)

df = pd.read_csv("churn.csv")
print(df.info()) 
df = df.drop("customerID", axis=1)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df["TotalCharges"] = df["TotalCharges"].fillna(0)

numCols = df.select_dtypes(include=['number']).columns
for col in numCols:
    df[col] = df[col].fillna(df[col].median())

catCols = df.select_dtypes(exclude=['number']).columns
for col in catCols:
    df[col] = df[col].fillna(df[col].mode()[0])

def treatOutliers(df, col):
    Q1  = df[col].quantile(0.25)
    Q3  = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)

for col in numCols:
    treatOutliers(df, col)

print("\nMissing values after cleaning:", df.isnull().sum().sum())

le = LabelEncoder()
textCols = df.select_dtypes(include=["str", "object"]).columns
for col in textCols:
    df[col] = le.fit_transform(df[col])

numCols = df.select_dtypes(include=['number']).columns

X = df.drop("Churn", axis=1)
y = df["Churn"]
featureNames = X.columns.tolist()

scaler = StandardScaler() 
XScaled = scaler.fit_transform(X)
XScaled = pd.DataFrame(XScaled, columns=featureNames)

XTrain, XTest, yTrain, yTest = train_test_split(XScaled, y, test_size=0.2, random_state=42, stratify=y)

svm = SVC(kernel="rbf", C=1, gamma="scale", random_state=42)
svm.fit(XTrain, yTrain)
yPred = svm.predict(XTest)

featureCorr = df[numCols].corr()['Churn'].drop('Churn')
topFeatures = featureCorr.sort_values(ascending=False)

print("\nTop Features by Correlation with Churn:")
print(topFeatures)

plt.figure(figsize=(12, 10))
sns.heatmap(df[numCols].corr(), cmap='coolwarm')
plt.title("Correlation Matrix of Features")
plt.show()

print("\nEvaluation")
print("Accuracy :", accuracy_score(yTest, yPred))
print("Precision:", precision_score(yTest, yPred, zero_division=0))
print("Recall   :", recall_score(yTest, yPred, zero_division=0))
print("F1 Score :", f1_score(yTest, yPred, zero_division=0))

cm = confusion_matrix(yTest, yPred)
print("\nConfusion Matrix")
print(cm)

newCustDf = pd.DataFrame([X.median()], columns=featureNames)
newCustScaled = scaler.transform(newCustDf)
pred = svm.predict(newCustScaled)[0]

label = "CHURN" if pred == 1 else "NO CHURN"
print(f"\nNew Customer: {label}")


#Unsupervised Learning - K-Means

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("Mall_Customers.csv")
print("Dataset shape:", df.shape)
print(df.head())

X = df.iloc[:, [3, 4]].values

scaler = StandardScaler()
XScaled = scaler.fit_transform(X)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(XScaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1,11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
yKmeans = kmeans.fit_predict(XScaled)

plt.figure(figsize=(10, 7))
colors = ['red', 'blue', 'green', 'cyan', 'magenta']
for i in range(5):
    plt.scatter(
        X[yKmeans == i, 0], X[yKmeans == i, 1], 
        s=100, c=colors[i], 
        label=f'Cluster {i+1}'
    )

centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', label='Centroids', edgecolors='black')

plt.title('Clusters of Customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()

#Unsupervised Learning - Fitness Task

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv("fitness_data.csv")
print("Data Summary")
print(df.info())

df = df.drop('UserID', axis=1)

numCols = df.select_dtypes(include=['number']).columns
for col in numCols:
    df[col] = df[col].fillna(df[col].median())

catCols = df.select_dtypes(exclude=['number']).columns
for col in catCols:
    df[col] = df[col].fillna(df[col].mode()[0])

print("\nMissing values after cleaning:", df.isnull().sum().sum())

le = LabelEncoder()
textCols = df.select_dtypes(include=["str", "object"]).columns
for col in textCols:
    df[col] = le.fit_transform(df[col])

numCols = df.select_dtypes(include=['number']).columns

print("\nStatistical Summary") # EDA
print(df.describe())

plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='Calories_Burned', kde=True)
plt.title("Distribution of Calories Burned")
plt.show()

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Steps', y='Calories_Burned')
plt.title("Steps vs Calories Burned")
plt.show()

X = df[numCols].values

scaler = StandardScaler()
XScaled = scaler.fit_transform(X)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(XScaled)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('WCSS')
plt.show()

kmeans = KMeans(n_clusters=3, init='k-means++', random_state=42)
yPred = kmeans.fit_predict(XScaled)

plt.figure(figsize=(10, 7))
colors = ['red', 'blue', 'green']
for i in range(3):
    plt.scatter(X[yPred == i, 0], X[yPred == i, 1], s=100, c=colors[i], label=f'Cluster {i+1}')

featureNames = numCols.tolist() # Plot Centroids
centroids = scaler.inverse_transform(kmeans.cluster_centers_)
plt.scatter(centroids[:, 0], centroids[:, 1], s=300, c='yellow', label='Centroids')
plt.title('User Activity Segments')
plt.xlabel(featureNames[0])
plt.ylabel(featureNames[1])
plt.legend()
plt.show()

print("\nInterpretation")
centersDf = pd.DataFrame(centroids, columns=featureNames)
print(centersDf)

for i, center in enumerate(centroids):
    steps = center[0]
    if steps > 9000:
        label = "Athletes"
    elif steps > 5000:
        label = "Active"
    else:
        label = "Casual"
    print(f"Cluster {i+1} ({label}): Steps={steps:.0f}, Duration={center[1]:.0f}, HeartRate={center[3]:.0f}")


#EDA 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Loading and Viewing Data
df = pd.read_csv('house_prices_practice.csv')
print(df.head())       # first 5 rows
print(df[12:15])       # rows 12 to 14
print(df[-1:])         # last row

# 2. Understanding the Data Structure
print(df.shape)    # rows × columns
print(df.columns)  # lists all column names
print(df.info())   # data types + non-null counts

# 3. Changing Feature Types
df['LotArea'] = df['LotArea'].astype('float64')

# 4. Basic Data Overview/Statistics (mean, std, min, max...)
print(df.describe())

# 5. Sorting Data
print(df.sort_values(by='Id', ascending=False).head()) # Sort by one column (descending)
print(df.sort_values(by=['LotFrontage', 'YrSold'], ascending=[True, False]).head()) # Sort by multiple columns

# 6. Indexing and Retrieving Data
# Single Column Access
print(df['SalePrice'].mean())   # average sale price

# Boolean indexing — filter rows by condition: 
# average of all features for houses with central air - numerical_only=True needed for full dataframe
print(df[df['CentralAir'] == 'Y'].mean(numeric_only=True))   

# average price of houses with central air
print(df[df['CentralAir'] == 'Y']['SalePrice'].mean()) 

# maximum price for houses with central air and more than 1 full bath
print(df[(df['CentralAir'] == 'Y') & (df['FullBath'] > 1)]['SalePrice'].max()) 

# loc — by label name (inclusive on both ends)
print(df.loc[0:5, 'MSZoning':'LotArea']) 

# iloc — by position number (end excluded)
print(df.iloc[0:4, 0:3])

# 7 apply() — a function to every column or row:
print(df.select_dtypes(include=[np.number]).apply(np.max))        # max of every column
print(df.select_dtypes(include=[np.number]).apply(np.max, axis=1)) # max of every row

#END
