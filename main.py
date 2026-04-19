import act, save, tutorial, char_sel, random, json
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
def mainmenu():
    print("Warrior's Quest - A terminal Adventure!")
    print("Enter the number of the option you wish to choose.")
    print("1. NEW GAME")
    print("2. LOAD GAME")
    print("3. TUTORIAL")
    print("4. SETTINGS")
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
        print("Enter the save slot you wish to save to.")
        slot = valid()
        save.save_game([player.name, cl, str(wp), str(mgs), str(player.level), str(player.health), str(player.cash), str(player.xp), str(player.next_level), " ".join(player.inventory)], slot, player.stats)
        return player
    if opt == 2:
        print("Enter the save slot you wish to load.")
        slot = input("\n")
        details = save.load_game(slot, mainmenu)
        if not(details):
            print("File cannot be loaded from. Please try again.")
            mainmenu()
        if details[1].lower() == "fighter":
            player = act.Fighter(details[0], act.Weapon(details[2], 10, 100, 20))
        elif details[1].lower() == "barbarian":
             player = act.Barbarian(details[0], act.Weapon(details[2], 8, 150, 15))
        elif details[1].lower() == "mage":
            player = act.Mage(details[0], details[3])
        elif details[1].lower() == "healer":
            player = act.Healer(details[0], details[3])
        player.level = details[4]
        player.health = details[5]
        player.cash = details[6]
        player.xp = details[7]
        player.next_level = details[8]
        player.inventory = details[9]
        player.stats = details[10]
        return player
    if opt == 3:
        tutorial.gent()
        mainmenu()
    if opt == 4:
        settings()
def settings():
    print("Settings")
    print("1. Autosave")
    print("2. Delete Save")
    print("3. Exit Settings")
    opto = valid()
    if opto == 1:
         save.auto_save = save.switch_autosave(save.auto_save)
         if save.auto_save:
             o = "On"
         else:
             o = "Off"
         print("Autosave is now", o)
    if opto == 2:
         print("Enter the save slot you wish to delete.")
         slot = input("\n")
         save.delete(slot)
    if opto == 3:
         print("Exitting settings...")
         mainmenu()
    else:
         print("Invalid option.")
         settings()
    return
player = mainmenu()
print("Welcome to the world of Warrior's Quest!")
print("You are a", player, "named", player.name)
print("You have", player.health, "HP")
print("You have", player.cash, "cash")
print("You have", player.xp, "XP")
print("You have", player.next_level, "XP to level up.")
def fight(player, enemy):
    print("Choose an option:")
    print("1. Attack")
    if player.cl.lower() == "fighter":
        print("2. Focus")
    if player.cl.lower() == "barbarian":
        print("2. Rage")
    if player.cl.lower() == "mage":
        print("2. Spell")
        print("3. Improve Potency")
    ch = valid()
    
    
def market(player):
    print("What would you like to buy?")
    print("1. Simple Potion - 10 cash - Heal 50 hp")
    print("2. Materium - 15 cash - Restore 50 magic")
    print("3. Deluxe Potion - 20 cash - Heal all hp")
    print("4. Empowered Materium - 25 cash - Restore all magic")
    print("5. Strength Potion - 8 cash - Increase strength by 5")
    print("6. Defence Potion - 8 cash - Increase defence by 5")
    print("7. Speed Potion - 8 cash - Increase speed by 5")
    print("8. Luck Potion - 8 cash - Increase luck by 5")
    print("9. Horn of Mead - 15 cash - Increase all stats by 2")
    print("10. Mysterious Orb - 30 cash - Unknown effect")
    print("11. Exit Shop")
    ch = valid()
    if ch == 1:
        if player.cash < 10:
             print("Not enough cash!")
             market(player)
        else:
             player.cash -= 10
             player.add_to_inventory("Simple Potion")
             print("Purchased Simple Potion!")
             market(player)
    if ch == 2:
          if player.cash < 15:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 15
               player.add_to_inventory("Materium")
               print("Purchased Materium!")
               market(player)
    if ch == 3:
         if player.cash < 20:
             print("Not enough cash!")
             market(player)
         else:
             player.cash -= 20
             player.add_to_inventory("Deluxe Potion")
             print("Purchased Deluxe Potion!")
             market(player)
    if ch == 4:
          if player.cash < 25:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 25
               player.add_to_inventory("Empowered Materium")
               print("Purchased Empowered Materium!")
               market(player)
    if ch == 5:
          if player.cash < 8:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 8
               player.add_to_inventory("Strength Potion")
               print("Purchased Strength Potion!")
               market(player)
    if ch == 6:
          if player.cash < 8:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 8
               player.add_to_inventory("Defence Potion")
               print("Purchased Defence Potion!")
               market(player)
    if ch == 7:
          if player.cash < 8:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 8
               player.add_to_inventory("Speed Potion")
               print("Purchased Speed Potion!")
               market(player)
    if ch == 8:
          if player.cash < 8:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 8
               player.add_to_inventory("Luck Potion")
               print("Purchased Luck Potion!")
               market(player)
    if ch == 9:
          if player.cash < 15:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 15
               player.add_to_inventory("Horn of Mead")
               print("Purchased Horn of Mead!")
               market(player)
    if ch == 10:
          if player.cash < 30:
               print("Not enough cash!")
               market(player)
          else:
               player.cash -= 30
               player.add_to_inventory("Mysterious Orb")
               print("Purchased Mysterious Orb!")
               market(player)
    if ch == 11:
          print("Exitting shop...")
          return
    else:
          print("Invalid option.")
          market(player)
def tournament(player):
     print("Welcome to the tournament!")
     print("You will be fighting 3 enemies in a row.")
     print("You will be rewarded with cash and XP for winning.")
     print("You must pay an entry fee of 25 cash to enter.")
     ent = input("Enter?(y/n)\n")
     if ent.lower() == 'y':
          if player.cash < 25:
               print("Not enough cash!")
               return
          else:
               player.cash -= 25
               print("You have entered the tournament!")
                #enemy 1
     else:
          print("Exitting tournament...")
          return
def tournament_round(player, round_no):
    print("Round", round_no, "of the tournament!")
    if round_no == 1:
        enemy = act.Mage("Eregrin", "Fireball")
        print("You are fighting a mage named Eregrin!")
        print("You attack first!")
        
