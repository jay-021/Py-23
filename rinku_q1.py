def main():
    name = input("Welcome to my clothing shop, please enter your name: ")

    print("What do you want to buy?")
    item_select = input("shirt, pant, bra, top & one piece: ").lower()

    print("Which color do you want?")
    color_select = input("white, black, pink, blue & gray: ").lower()

    item_price = item(item_select)
    color_price = color(color_select)

    total_price = item_price + color_price
    print("Your total price without any discount is:", total_price)

    discount = int(input("How much discount do you want? "))
    discounted_price = total_price - (total_price * (discount / 100))  # Corrected the discount calculation
    print("Hello", name, "Your final price after a", discount, "% discount is:", discounted_price)

def item(i):
    match i:
        case "shirt":
            item1 = 500
            print("RS. 500")
        case "pant":  # Corrected the spelling of 'pant'
            item1 = 550
            print("RS. 550")
        case "top":
            item1 = 500
            print("RS. 500")
        case "bra":
            item1 = 450
            print("RS. 450")
        case "one piece":
            item1 = 1000
            print("RS. 1000")

    return item1

def color(c):
    match c:
        case "black":
            item2 = 0
            print("Normal")
        case "white":
            item2 = 0
            print("Normal")
        case "gray":
            item2 = 100
            print("Extra 100 rs")
        case "pink":
            item2 = 50
            print("Extra 50 rs")
        case "blue":
            item2 = 20
            print("Extra 20 rs")

    return item2

# Check if the script is being run as the main program
if __name__ == "__main__":
    main()  # Call the main function
