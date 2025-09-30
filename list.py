# # Consider a list (list = []). You can perform the following commands:

# # insert i e: Insert integer  at position .
# # print: Print the list.
# # remove e: Delete the first occurrence of integer .
# # append e: Insert integer  at the end of the list.
# # sort: Sort the list.
# # pop: Pop the last element from the list.
# # reverse: Reverse the list.
# # Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# # Example






# # : Append  to the list, .
# # : Append  to the list, .
# # : Insert  at index , .
# # : Print the array.
# # Output:
# # [1, 3, 2]

# solution:- 


# if __name__ == '__main__':
#     N = int(input())
#     my_list = []
#     for _ in range(N):
#         cmd = input().split()
#         if cmd[0] == "insert":
#             my_list.insert(int(cmd[1]), int(cmd[2]))
#         elif cmd[0] == "print":
#             print(my_list)
#         elif cmd[0] == "remove":
#             my_list.remove(int(cmd[1]))
#         elif cmd[0] == "append":
#             my_list.append(int(cmd[1]))
#         elif cmd[0] == "sort":
#             my_list.sort()
#         elif cmd[0] == "pop":
#             my_list.pop()
#         elif cmd[0] == "reverse":
#             my_list.reverse()


# output:- [6, 5, 10]

#          [1, 5, 9, 10]

#          [9, 5, 1]