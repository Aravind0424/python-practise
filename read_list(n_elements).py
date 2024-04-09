# number of elements
n = int(input("Enter number of elements : "))
# Below line read n inputs for list from user using map() function
a = list(map(int, input("Enter the numbers : ").strip().split()))[:n]
print("List:", a)
