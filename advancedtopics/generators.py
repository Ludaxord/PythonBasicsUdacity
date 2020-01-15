def my_range(x):
    i = 0
    while i < x:
        yield i
        i += 1

r = my_range(5)
print(type(r))

for x in r:
    print(x)


lessons = ["Why Python Programming", "Data Types and Operators", "Control Flow", "Functions", "Scripting"]

def my_enumerate(iterable, start=0):    
    # Implement your generator function here
    count = start
    for e in iterable:
        yield count, e
        count += 1

for i, lesson in my_enumerate(lessons, 1):
    print("Lesson {}: {}".format(i, lesson))


def chunker(iterable, size):
    for index in range(0, len(iterable), size):
        print(index)
        yield iterable[index:index + size]
    """Yield successive chunks from iterable of length size."""

for chunk in chunker(range(25), 4):
    print(list(chunk))