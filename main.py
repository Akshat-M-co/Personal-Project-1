import act, save, tutorial, char_sel
print("Warrior's Quest - A terminal Adventure!")
print("Enter the number of the option you wish to choose.")
print("1. NEW GAME")
print("2. LOAD GAME")
print("3. TUTORIAL")
print("4. SETTINGS")
def valid():
    try:
        num = int(input("\n"))
        if num > 4 or num < 1:
            print("Invalid option.")
            num = valid()
    except:
        print("Please enter a number for the option you choose.")
        valid()
    else:
        return num
opt = valid()
if opt == 1:
    print("Starting New Game...")
    name, cl, wp, mgs = char_sel.char_sel()
    if cl.lower() == "fighter":
         player = act.Fighter(name, act.Weapon(wp, 10, 100, 20))
    elif cl.lower() == "barbarian":
         player = act.Barbarian(name, act.Weapon(wp, 8, 150, 15))
    elif cl.lower() == "mage":
         player = act.Mage(name, mgs)
    elif cl.lower() == "healer":
         player = act.Healer(name, mgs)
    save.save_game([])

