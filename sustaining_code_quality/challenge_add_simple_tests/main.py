def reverse_string(s):
    return s[::-1]

assert reverse_string("hello") == "olleh", "Expected olleh but got {}".format(reverse_string("hello"))
assert reverse_string("") == "", "Expected  but got {}".format(reverse_string(""))
assert reverse_string("Python") == "nohtyP", "Expected nohtyP but got {}".format(reverse_string("Python"))