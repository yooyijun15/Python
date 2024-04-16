from beverage import RESOURCES, MENU

# < 추가하고 싶은 기능 >
# - 데이터베이스 연동
# - 재료 추가
# - 얼음, 버블, 크림 등 옵션 추가
# - 화폐 단위 (동전, 카드)
# - 거스름돈 반환

machine_cache = 0
user_cache = 100

def print_report():
    print("---------------------")
    print("    - RESOURCES -    ")
    print(f" Water : {RESOURCES["water"]}ml\n Milk : {RESOURCES["milk"]}ml\n Coffee : {RESOURCES["coffee"]}g\n Chocolate : {RESOURCES["chocolate"]}g\n Syrup : {RESOURCES["syrup"]}g")
    print("---------------------")
    print(f" TOTAL : ${machine_cache}")
    print("---------------------")

def current_cache():
    print("\n---------------------")
    print(f" User cache: ${user_cache}")
    print(f" machine cache: ${machine_cache}")
    print("---------------------\n")

def calculate_cache(cost):
    global user_cache, machine_cache
    user_cache -= cost
    machine_cache += cost

def check_ingredients(choice_ingredients):
    for item in choice_ingredients:
        if RESOURCES[item] < choice_ingredients[item]:
            print(f"Sorry there is not enough '{item}'.")
            return False
    else:
        return True

def use_ingredients(choice_ingredients):
    for item in choice_ingredients:
        RESOURCES[item] -= choice_ingredients[item]

def get_order():
    current_cache()
    print("---------------------")
    print("       - MENU -      ")
    print(" Americano.........3$")
    print(" Latte.............4$")
    print(" Chocolatte........5$")
    print(" Juice.............5$")
    print("---------------------\n")
    get_order = True
    while get_order:
        # 메뉴 이름  ex) latte
        choice_menu = input("What would you like? ").lower()
        if choice_menu in MENU:
            # 메뉴 상세 정보 (필요 재료, 가격)
            choice_information = MENU[choice_menu]
            # 메뉴 필요 재료
            choice_ingredients = choice_information["ingredients"]
            # 메뉴 가격
            choice_cost = int(choice_information["cost"])
            conduct = check_ingredients(choice_ingredients)
            if conduct == True:
                use_ingredients(choice_ingredients)
                calculate_cache(choice_cost)
                print(f"Here is your {choice_menu}. Enjoy!")
                current_cache()
            if input("Would you like to order more? ").lower() == "yes":
                get_order = True
            else:
                print("Bye Bye~")
                get_order = False
        else:
            print("Sorry, that item is not on the menu.")

FUNCTION = {
    "report" : print_report,
    "order"  : get_order
}

is_on = True

while is_on:
    choice_task = input("What do you want to do? ('report' or 'order') ")
    if choice_task == "off":
        print("[ POWER OFF ]")
        is_on = False
    else:
        task = FUNCTION[choice_task]
        task()
