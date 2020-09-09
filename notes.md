# # Runtime Complexity

# commands = ['n', 's', 'w', 'e']

# selection = input()

# # In the worst case, we'd have to iterate over every element in the list to find what we're looking for
# # So this is a linear operation
# if selection in commands:
#   # this is a valid command
#   # perform the user's command


# # Constant time
# # Constant time doesn't grow at all as the size of the input increases
# commands[3] # the size of the input has no bearing on the effiency of this operation

# # Big 0 allows us to drop constants because it only cares about the "dominating" contributor to growth

# # Linear time
# # Linear runtime grows 1 to 1 as the size of the input increases
# for command in commands: # the size of the input has direct bearing on the effiency
#   print(command) # what's the runtime of the `print` function? 0(1)

#   for _ in commands:
#       # 0(n) * 0(n) ~ 0(n * n) == 0(n^2)

# # 0(n) * 0(1) ~ 0(n * 1) == 0(n)

# # Constant < Linear

# # What's being compared is how quickly the efficiency grows as a result of the input size