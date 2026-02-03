def toh(n,s,d,a):
   if n==1:
      print(f"Move disk 1 from {s} to {d}")
      return
   toh(n-1,s,a,d)
   print(f"Move disk {n} from {s} to {d}")
   toh(n-1,a,d,s)
n=int(input("Enter number of disks:\n"))
s=input("Enter source rod:\n")
d=input("Enter destination rod:\n")
a=input("Enter auxilary rod:\n")
toh(n,s,d,a)
