def count():
    yield "yousaf"
    yield 2
    yield 3

g=count()
print(next(g))
#generator using loops:
# def numbers():
#     for i in range(5):
#         yield i

# g=numbers()
# for x in g:
#     print(x)