# Write a Python script to create a list of first N odd natural numbers.

print([x for x in range(1,2*int(input("enter a no "))+1) if x%2!=0 ])