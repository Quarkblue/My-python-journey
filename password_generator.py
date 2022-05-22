import random


def generate_password_list(upper, lower, nums, syms, amount, length):
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = uppercase.lower()
    digits = '0123456789'
    symbols = '()[]{},.;:`~/?><-_+=*&^%$#@!|\\'
    final_list = []

    all = ""

    if upper:
        all += uppercase

    if lower:
        all += lowercase

    if nums:
        all += digits

    if syms:
        all += symbols

    for x in range(amount):
        password = "".join(random.sample(all, length))
        final_list.append(password.split('\n')[0])

    return final_list


if __name__ == '__main__':
    length = int(input("Enter the length you want for the password(Cannot be greater than 40): "))
    amount = int(input("Enter how many passwords you want: "))
    seed_ask = input("Do you want a seed for the same passwords?[Y,N]: ")
    seed = input("Enter seed: ")
    random.seed(seed)
    count = 0

    a = input("Do you want lowercase letters?[Y,N]: ")
    b = input("Do you want uppercase letter?[Y,N]: ")
    c = input("Do you want digits?[Y,N]: ")
    d = input("Do you want special Characters?[Y,N]: ")

    if a.lower() == 'y':
        upper = True
    else:
        upper = False
    if b.lower() == 'y':
        lower = True
    else:
        lower = False
    if c.lower() == 'y':
        nums = True
    else:
        nums = False
    if d.lower() == 'y':
        syms = True
    else:
        syms = False

    final_list = generate_password_list(upper, lower, nums, syms, amount, length)

    for i in final_list:
        count += 1
        print(f"{count}: {i}")
