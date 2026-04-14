import random
class Weapon:
  def __init__(self, name, range, durability, damage, level = 1):
    self.name = name
    self.range = range
    self.durability = durability
    self.damage = damage
    self.level = level
  def upgrade(self):
    self.level += 1
    self.damage += 10
    self.durability += 50
  def destroy(self):
    if self.durability <= 0:
        print("Weapon destroyed")
        del self
  

class Player:
   def __init__(self, name, level = 1):
     self.name = name
     self.health = 150
     self.inventory = []
     self.level = level
     self.cash = 100
     self.xp = 0
     
   def __str__(self):
     return f"{self.name} has {self.health} HP"

   def damage(self, src, dmg_amt, num_hits):
     self.health -= dmg_amt * num_hits
     print("Took damage from", src.name, "for", dmg_amt * num_hits)
     if self.health <= 0:
       print(self.name, "is dead.")
  
   def inventory_access(self):
     print("Inventory: ", self.inventory)
     if len(self.inventory) > 10:
       print("no space available.")

   def add_to_inventory(self, item):
     if len(self.inventory) > 10:
        print("no space available.")
        return
     self.inventory.append(item)
  
   def remove_from_inventory(self, item):
      self.inventory.remove(item)
   def level_up(self):
       if self.xp >= 100:
           self.level += 1
           for val in self
   
class Fighter(Player):
  def __init__(self, name, weapon):
     super().__init__(name)
     self.weapon = weapon
     self.proficiency = 100
     self.__stats = {"strength": 10, "speed": 5, "defence": 7, "luck": 4}
     self.magic = 0
     self.focus = False
    
  def attack(self, target):
    if self.weapon.durability <= 0:
      print("Weapon is broken")
      return 0
    dmg = self.weapon.damage + self.__stats["strength"] * self.proficiency / 100 
    ran = random.randint(1, 10)
    sel = random.randint(1, 10)
    if abs(ran - sel) <= self.__stats["luck"]:
      print("Attack successful!")
      target.health -= dmg - target.__stats["defence"]
      self.weapon.durability -= 1
      if self.focus:
          self.focus = False
          self.__stats["luck"] /= 2
  def Focus(self):
      if not(self.focus):
          self.focus = True
          self.__stats["luck"] *= 2
          print("Focus activated!")
      else:
          print("Focus already activated!")


class Barbarian(Player):
  def __init__(self, name, weapon):
    super().__init__(name)
    self.magic = 20
    self.weapon = weapon
    self.__stats = {"strength": 15, "speed": 5, "defence": 3, "luck": 2}
    self.rage = False
  
  def Rage(self):
    if self.magic < 10:
      print("Not enough magic! Consume a materium to restore Magic potential")
      return
    print("Rage Activated!")
    self.__stats["strength"] *= 1.5
    self.magic -= 10
    self.rage = True
    
  def attack(self, target):
    if self.weapon.durability <= 0:
      print("Weapon is broken")
      return 0
    dmg = self.weapon.damage + self.__stats["strength"]
    ran = random.randint(1, 10)
    sel = random.randint(1, 10)
    if abs(ran - sel) <= self.__stats["luck"]:
      print("Attack successful!")
      target.health -= dmg - target.stats["defence"]
      self.weapon.durability -= 1
    if self.rage:
      self.rage = False
      self.__stats["strength"] /= 1.5
class Mage(Player):
    def __init__(self, name, spell):
        super().__init__(name)
        self.magic = 100
        self.mps = [spell]
        self.__stats = {"strength":2, "defence":8, "speed":10, "luck": 10}
        self.potent = False
    def spell(self, target):
        print("Choose spell:")
        for i in self.mps:
            print(f"{self.mps.index(i) + 1}. {i}")
        chosen = input("\n")
        if chosen.lower() not in self.mps:
            print("Invalid Spell. Choose again.")
            spell()
        else:
            if self.magic < 10:
                print("Not enough magical potential. Use a materium to regain magical strength!")
                return
            print("Casting", chosen.title())
            self.magic -= 10
            dmg = 20 + 1.2 * self.level
            if self.potent:
                self.potent = False
                self.magic /= 2
                dmg *= 2
                self.__stats["luck"] *= 2
            x, y = random.randint(1, 30), random.randint(1, 30)
            if abs(x-y) <= self.__stats["luck"]:
                print("Spell successful!")
                target.hp -= dmg
      def Potency(self):
          if not(self.potent):
             self.potent = True
             self.magic *= 2
             self.__stats["luck"] /= 2
             print("Potency activated!")