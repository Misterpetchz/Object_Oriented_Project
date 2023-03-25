# create a list of variable names
var_names = ["x{}".format(i) for i in range(1, 4)]

# create the variables dynamically using a loop
for var_name in var_names:
    exec("{} = 'some value'".format(var_name))

# use the variables as needed
print(x1)
print(x2)
print(x3)