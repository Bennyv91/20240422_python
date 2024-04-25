item = (1, "Bob", "red", "green", "blue")

# unpacking
# * is the packing operator
id, name, *colors = item

print(id)
print(name)
print(colors)

# * is the unpacking operator
new_colors = ["black", *colors, "purple"]
print(new_colors)

# * is the packing operator = * is the unpacking operator
# variable = expression

# * - packing
def my_func(*args):
    print("hello")


# * - unpacking
my_func