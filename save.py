import json
auto_save = False
def save_game(details, save_slot):
    keys = ["name", "class", "weapon", "spell", "level", "health", "cash", "xp", "next_level", "inventory", "stats"]
    print(details)
    if auto_save:
        savedict = dict(zip(keys, details))
        with open(f"Save file {save_slot}.json", "w") as f:
            json.dumps(savedict, f, indent=4)
        print("Save complete. Turn off autosave in the settings, if not wanted.")

    else:
        print("Are you sure you wish to save the game? (y/n)")
        ans = input("\n")
        if ans.lower() == 'y':
            print("Saving your game.")
            savedict = dict(zip(keys, details))
            with open(f"Save file {save_slot}.json", "w") as f:
                json.dump(savedict, f, indent=4)
            print("Save complete.")
        else:
            print("Exitting save mode...")
    return
def load_game(save_slot):
    keys = ["name", "class", "weapon", "spell", "level", "health", "cash", "xp", "next_level", "inventory", "stats"]
    try:
        with open(f"Save file {save_slot}.json", "r") as l:
            result = json.load(l)
    except FileNotFoundError:
        return 1
    details = []
    for i in keys:
        details.append(result[i])
    print("Loading complete.")
    return details
def delete(save_slot):
    o = open(f"Save file {save_slot}.json", "w")
    o.close()
    print("Deleted save game.")
    return
def switch_autosave(auto_save):
    return not(auto_save)
