def save_to_file(func):
    def inner(*args, **kwargs):
        with open("result.txt", "a+") as f:
            f.write(f"{func(*args, **kwargs)}\n")
    return inner


def my_decorator(func):
    def inner(*args, **kwargs):
        with open("result.txt", "r+") as f:
            file_result = f.read()
            print(f"Before function run{file_result}")
        func(*args, **kwargs)
        with open("result.txt", "r+") as f:
            file_result = f.read()
            print(f"After function run{file_result}")
    return inner


# @my_decorator
# @save_to_file
def fibo(numbers: int):
    num = [1, 1]
    while True:
        num.append(sum(num[-2:]))
        yield num[-1]
        # if len(num) > numbers:
        #     break


data = fibo(15)
with open("result_again.txt", "w+") as f:
    for i in range(15):
        try:
            value = next(data)
            f.write(f'{value}\n')
        except StopIteration:
            break


with open("result_again_0.txt", "w+") as f:
    for i in range(15):
        try:
            value = next(data)
            f.write(f'{value}\n')
        except StopIteration:
            break
