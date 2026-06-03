def heal():
  h = ("purify", "blessing", "barrier")
  hls = input("Enter spell:\n")
  if hls not in h:
      print("Invalid spell. Please choose again.")
      heal()
  else:
      print("You have chosen the", hls, "spell.")
      wp = None
      return hls, wp
def magic():
  mg = ("fireball", "ice shard", "lightning bolt", "poison cloud", "tidal wave", "earthquake", "air blow")
  mgs = input("Enter spell:\n").lower()
  if mgs not in mg:
    print("Invalid spell. Please choose again.")
    magic()
  else:
    print("You have chosen the", mgs, "spell.")
    return mgs
def weapon():
  wp = ("longsword", "poleaxe", "war bow", "claws", "katana", "spear",   "gauntlets")
  s = input("Enter weapon:\n")
  if s not in wp:
    print("Invalid weapon. Please choose again.")
    weapon()
  else:
    print("You have chosen the", s, "weapon.")
    return s
def cls():
  cl = ["fighter", "barbarian", "mage", "healer"]
  print("\nChoose your class: ")
  print("Fighter")
  print("Barbarian")
  print("Mage")
  print("Healer")
  clss = input()
  if clss.lower() not in cl:
     print("Invalid class. Please choose again.")
     cls()
  else:
    print("You have chosen the", clss, "class.")
    return clss
#Character selection
def char_sel():
  print("Character Selection Process Beginning...")
  print("Give your character a name: \n")
  name = input()
  cl = cls()

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
    mgs = None

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
    wp = None

  if cl.lower() == "healer":
    print("Choose a starter spell: ")
    print("1. Purify ")
    print("2. Blessing")
    print("3. Barrier")
    mgs = heal()
    wp = None

  print("Character creation complete.")
  print("Name: ", name)
  print("Class: ", cl)
  if cl in ("fighter", "barbarian"):
    print("Starter Weapon: ", wp)
  else:
    print("Starter Spell: ", mgs)
  return name, cl, wp, mgs
