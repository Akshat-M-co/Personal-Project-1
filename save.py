auto_save = False
details = ["Name", "Class", "Weapon", "Spell", "Level", "Health", "Cash", "XP", "Next Level", "Inventory", "Stats"]
def save_game(details, save_slot):
    if auto_save:
        with open(f"Save file {save_slot}.txt", "w") as save:
            for i in details:
                save.write(i)
                save.write("\n")
                print("Save complete. Turn off autosave in the settings, if not wanted.")
    else:
        print("Are you sure you wish to save the game? (y/n)")
        ans = input("\n")
        if ans.lower() == 'y':
            print("Saving your game.")
            with open(f"Save file {save_slot}.txt", "w") as save:
                for i in details:
                    save.write(i)
                    save.write("\n")
            print("Save complete.")
        else:
            print("Exitting save mode...")
    return
def load_game(save_slot):
    load = open(f"Save file {save_slot}", "r")
    r = load.readline()
    details = []
    while (r):
        details.append(r)
    load.close()
    print("Loading complete.")
    return details
def delete(save_slot):
    o = open(f"Save file {save_slot}.txt", "w")
    o.close()
    print("Deleted save game.")
    return
def switch_autosave(auto_save):
    return not(auto_save)
