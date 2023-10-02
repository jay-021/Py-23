def main():
    items = {"bra": 450, "penti": 450, "top": 600,
            "shirt": 500, "shoes": 900, "one piece": 1000}
    colors = {"black": 100, "white": 100, "gray": 120, "pink": 90, "blue": 70}
    name = input("Enter your name: ").lower()

    while True:
        item_select = input(f"Hello {name}, What would you like to buy: ")
        if item_select in items.keys():
            break
        else:
            print("Sorry, we don't have that item yet so Choose deferent item.")

    while True:
        color_select = input(
            f"Hello {name}, Which color would you like to select for your item: ")
        if color_select in colors.keys():
            break
        else:
            print("Sorry, we don't have that color yet so choose deferent color")

    total_price = items[item_select] + colors[color_select]
    print(
        f"Your total price before discount is {total_price}, \n {item_select} cost you {items[item_select]}. \n {color_select} : this color cost : {colors[color_select]}")
    if name not in ["bff", "bestfriend", "bro", "bestie"]:
        discount = int(input("How much discount do you want: "))
        if discount >= 100:
            print("100% discount is only available for my bestfriend.")
            print(f"Your total price is: {total_price}.")
        else:
            print(
                f"Your total price is: {total_price - (total_price*(discount/100))}.")
    else:
        print("Everything is free for you.")
        print(f"Your total price is: $ 00.")


if __name__ == "__main__":
    main()
