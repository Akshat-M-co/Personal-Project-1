#Character selection
def char_sel():
  print("Character Selection Process Beginning...")
  print("Give your character a name: \n")
  name = input()
  def cls():
    cl = ["fighter", "barbarian", "mage", "healer"]
    print("\nChoose your class: ")
    print("1. Fighter ")
    print("2. Barbarian ")
    print("3. Mage ")
    print("4. Healer ")
    clss = input()
    if clss.lower() not in cl:
       print("Invalid class. Please choose again.")
       cls()
    else:
      print("You have chosen the", clss, "class.")
      return clss
  cl = cls()
  def weapon():
      wp = ("longsword", "poleaxe", "war bow", "claws", "katana", "spear",   "gauntlets")
      s = input("Enter weapon:\n")
      if s not in wp:
        print("Invalid weapon. Please choose again.")
        weapon()

  if cl.lower() in ("fighter", "barbarian"):
    print("Choose a Weapon selection: \n")
    print("1. Longsword")
    print("2. Poleaxe")
    print("3. War Bow")
    print("4. Claws")
    print("5. Katana")
    print("6. Spear")
    print("7. Gauntlets")
    wp = weapon()
  def magic():
    mg = ("fireball", "ice shard", "lightning bolt", "poison cloud", "tidal wave", "earthquake", "air blow")
    mgs = input("Enter spell:\n")
    if mgs not in mg:
      print("Invalid spell. Please choose again.")
      magic()

  if cl.lower() == "mage":
    print("Choose a starter spell: ")
    print("1. Fireball ")
    print("2. Ice Shard ")
    print("3. Lightning Bolt ")
    print("4. Poison Cloud")
    print("5. Tidal Wave")
    print("6. Earthquake")
    print("7. Air Blow")
    mgs = magic()

  def heal():
    h = ("heal", "revive", "purify", "blessing", "barrier")
    hls = input("Enter spell:\n")
    if hls not in h:
        print("Invalid spell. Please choose again.")
        heal()
    else:
        print("You have chosen the", hls, "spell.")
        return hls
  if cl.lower() == "healer":
    print("Choose a starter spell: ")
    print("1. Heal ")
    print("2. Revive ")
    print("3. Purify ")
    print("4. Blessing")
    print("5. Barrier")
    mgs = heal()

  print("Character creation complete.")
  print("Name: ", name)
  print("Class: ", cl)
  if cl in  ("fighter", "barbarian"):
    print("Starter Weapon: ", wp)
  else:
    print("Starter Spell: ", mgs)
