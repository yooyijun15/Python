machine_cache = 0
user_cache = 100


def current_cache(user, machine):
    print("\n---------------------")
    print(f" User cache: ${user}")
    print(f" machine cache: ${machine}")
    print("---------------------\n")

def order():
    current_cache(user_cache, machine_cache)

order()
