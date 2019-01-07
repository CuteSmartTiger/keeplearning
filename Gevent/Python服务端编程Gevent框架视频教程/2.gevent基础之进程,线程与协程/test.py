def simple_generator_func():
    yield 1
    yield 2
    yield 3

gen = simple_generator_func()
for value in gen:
    print value
