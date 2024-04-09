#This code is to find the indices of the two numbers that add up to the target
def indices_finder(num_list, target):
  for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
      if num_list[i]+num_list[j] == target:
        return i, j
#driver code to take input of target and lis
target = int(input("Enter the target number: "))
num_list=list(map(int,input("Enter the list of numbers:").split(" ")))#in order to to read input as list where each element is seperated by space
print(indices_finder(num_list, target)).split(" ")
