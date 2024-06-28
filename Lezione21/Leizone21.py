# def say_hello(name: str) -> None:
#     print(f"Hello, {name}")

# def say_ciao(name: str) -> None:
#     print(f"Ciao, {name}")

# def saluta(func):
#     func("Flavio")

# saluta(say_hello)

# saluta(say_ciao)

# def get_time(func):

#     def wrapper(*args):
#         import time

#         start = time.time()

#         func(*args)

#         end = end.time()
#         elapsed_time = end - start

#         print(f"{elapsed_time}")

#     return wrapper

# @get_time


# def say_hello(name: str) -> None:

#     print(f"Hello, {name}")


def generatore():


    yield "A"
    yield "B"
    yield "C"


prova_generatore = generatore()

print(next(prova_generatore))
print(next(prova_generatore))
print(next(prova_generatore))


