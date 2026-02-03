def board(b):
   N=len(b)
   print("Board")
   for i in range(N):
      print(" ".join("Q" if j==b[i] else "." for j in range(N)))
   print()
def is_safe(b,row,col):
   return all(b[i]!=col and b[i]-i!=col-row and b[i]+i!=col+row for i in range (row))
def heuristic(b,row):
   return sum(i for i in range (row) if not is_safe(b,row,b[i]))
def solve_astar(N):
   b=[-1]*N
   states=[(0+heuristic(b,0),0,b[:],[])]
   solutions=[]
   while states:
      states.sort(key=lambda x:x[0])
      cost,row,curr,moves=states.pop(0)
      if row==N:
         solutions.append((curr,moves))
         continue
      for col in range(N):
         if is_safe(curr,row,col):
            new=curr[:]
            new[row]=col
            new_mov=[(row+1,col+1)]
            new_cost=row+1,heuristic(new,row+1)
            states.append((new_cost,row+1,new,new_mov))
   return solutions
def display(solutions):
   for idx,(sol,moves) in enumerate(solutions):
      print(f"\n Solution {idx+1}:")
      board(sol)
      print("Moves:")
      for move in moves:
         print(f"Place Q {move[0]} in column {move[1]}")
      print()
N=int(input("Enter number of queens:\n"))
print(f"Solving {N} queens using A*:")
sol=solve_astar(N)
display(sol)
if not sol:
   print("Solution not found \n")
