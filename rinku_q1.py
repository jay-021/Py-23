def main ():
    name= input("Welcome to my clothing shop , please enter your name: ")
    print("What do you want to buy ? ")
    item = input("shirt,pent,bra, top & one piece : ").lower()
    print("Which color do you want ?")
    color = input("white, black , pink , blue & Gray : ").lower()
    discount = int(input("How much discount do you want? "))
    
def item(i):
    # while i==True:
    match i:
        case "shirt":
            item1 = "shirt"
            print("RS. 500")
    match i:
        case "pent":
            item1 = "pent"
            print("RS. 550")
    match i:
        case "top":
            item1 = "top"
            print("RS. 500")
    match i:
        case "bra":
            item1 = "bra"
            print("RS. 450")
    match i:
        case "one piece":
            item1 = "one piece"
            print("RS. 1000")  
    return item1            

def color(c):
    def item(c):
    # while i==True:
    match c:
        case "black":
            item2 = "black"
            print("NOrmal")
    match c:
        case "white":
            item2 = "white"
            print("NOrmal")
    match c:
        case "Gray":
            item2 = "gray"
            print("extra 100 rs")
    match c:
        case "pink":
            item2 = "pink"
            print("extra 50 rs")
    match c:
        case "blue":
            item2 = "blue"
            print("extra 20 rs")  
    return item = item2  