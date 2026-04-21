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
        return True
  def inrange(self, distance):
    return self.range <= distance
class Spell:
    def __init__(self, name, damage, magic_cost, level = 1):
        self.name = name
        self.damage = damage
        self.magic_cost = magic_cost
        self.level = level
    def upgrade(self):
        self.level += 1
        self.damage += 10
    def use(self, target):
        print(f"{self.name} cast!")
        target.health -= self.damage
        if target.health <= 0:
            print(f"{target.name} has been defeated!")
            return True
        else:
            print(f"{target.name} has {target.health} health left!")
            return False
        
  

class Player:
   def __init__(self, name, level = 1):
     self.name = name
     self.health = 150
     self.max = 150  
     self.inventory = []
     self.level = level
     self.cash = 100
     self.xp = 0
     self.next_level = 100
   def __str__(self):
     return f"{self.name} has {self.health} HP"

   def damage(self, src, dmg_amt, num_hits):
     self.health -= dmg_amt * num_hits
     print("Took damage from", src.name, "for", dmg_amt * num_hits)
     if self.health <= 0:
       print(self.name, "is dead.")
  
   def inv_access(self):
     print("Inventory: ")
     for i in self.inventory:
       print(i)
     if len(self.inventory) > 10:
       print("no space available.")

   def add_to_inventory(self, item):
     if len(self.inventory) > 10:
        print("no space available.")
        return
     self.inventory.append(item)
  
   def remove_from_inventory(self, item):
      self.inventory.remove(item)
   

   
class Fighter(Player):
  def __init__(self, name, weapon):
     super().__init__(name)
     self.weapon = weapon
     self.proficiency = 100
     self.stats = {"strength": 10, "speed": 5, "defence": 7, "luck": 4}
     self.magic = 0
     self.focus = False

  def __str__(self):
    return "Fighter"
    
  def attack(self, target):
    if self.weapon.durability <= 0:
      print("Weapon is broken")
      return 0
    dmg = self.weapon.damage + self.stats["strength"] * self.proficiency / 100 
    ran = random.randint(1, 10)
    sel = random.randint(1, 10)
    if abs(ran - sel) <= self.stats["luck"]:
      print("Attack successful!")
      target.health -= dmg - target.stats["defence"]
      self.weapon.durability -= 1
      if self.focus:
          self.focus = False
          self.stats["luck"] /= 2
  def Focus(self):
      if not(self.focus):
          self.focus = True
          self.stats["luck"] *= 2
          print("Focus activated!")
      else:
          print("Focus already activated!")
  def level_up(self):
         if self.xp >= self.next_level:
             self.level += 1
             for val in self.stats.values():
                 val += 1
             self.next_level *= 1.5
             self.health += 50
             self.max += 50


class Barbarian(Player):
  def __init__(self, name, weapon):
    super().__init__(name)
    self.magic = 20
    self.weapon = weapon
    self.stats = {"strength": 15, "speed": 5, "defence": 3, "luck": 2}
    self.rage = False
  def __str__(self):
    return "Barbarian"
  def Rage(self):
    if self.magic < 10:
      print("Not enough magic! Consume a materium to restore Magic potential")
      return
    print("Rage Activated!")
    self.stats["strength"] *= 1.5
    self.magic -= 10
    self.rage = True
    
  def attack(self, target):
    if self.weapon.durability <= 0:
      print("Weapon is broken")
      return 0
    dmg = self.weapon.damage + self.stats["strength"]
    ran = random.randint(1, 10)
    sel = random.randint(1, 10)
    if abs(ran - sel) <= self.stats["luck"]:
      print("Attack successful!")
      target.health -= dmg - target.stats["defence"]
      self.weapon.durability -= 1
    if self.rage:
      self.rage = False
      self.stats["strength"] /= 1.5
  def level_up(self):
         if self.xp >= self.next_level:
             self.level += 1
             for val in self.stats.values():
                 val += 1
             self.next_level *= 1.5
             self.health += 50
             self.max += 50

class Mage(Player):
    def __init__(self, name, spell):
        super().__init__(name)
        self.magic = 100
        self.mps = [spell]
        self.stats = {"strength":2, "defence":8, "speed":10, "luck": 10}
        self.potent = False
    def __str__(self):
        return "Mage"
    def spell(self, target):
        print("Choose spell:")
        for i in self.mps:
            print(f"{self.mps.index(i) + 1}. {i}")
        chosen = input("\n")
        if chosen.lower() not in self.mps:
            print("Invalid Spell. Choose again.")
            self.spell(target)
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
                self.stats["luck"] *= 2
            x, y = random.randint(1, 30), random.randint(1, 30)
            if abs(x-y) <= self.stats["luck"]:
                print("Spell successful!")
                target.health -= dmg
    def Potency(self):
        if not(self.potent):
            self.potent = True
            self.magic *= 2
            self.stats["luck"] /= 2
            print("Potency activated!")
    def level_up(self):
           if self.xp >= self.next_level:
               self.level += 1
               for val in self.stats.values():
                   val += 1
               self.next_level *= 1.5
               self.health += 50
               self.max += 50
class Healer(Player):
    def __init__(self, name, spell):
        super().__init__(name)
        self.magic = 150
        self.mps = [spell]
        self.stats = {"strength":1, "defence":8, "speed": 7, "luck": 8}
        self.wind = False
    def __str__(self):
        return "Healer"
    def heal(self, target):
        if self.magic < 15:
            print("Not enough magic! Use a materium to restore magical potential.")
            return
        if target.health <= 0:
            print("Cannot heal dead ally.")
            return
        self.magic -= 15
        if self.wind:
            target.health += 10*self.level
        else:
            target.health += 5*self.level
        if target.health > target.max:
            target.health = target.max
        print("successfully healed ally")
    def revive(self, target):
        if self.magic < 30:
            print("Not enough magic! Use a materium to restore magical potential")
            return
        if target.health > 0:
            print("Cannot revive a target that is alive.")
            return
        self.magic -= 30
        target.health = 100
        print("Successfully revived ally!")
    def Wind(self):
        self.wind = True
        print("Healing Wind Active!")
    def level_up(self):
           if self.xp >= self.next_level:
               self.level += 1
               for val in self.stats.values():
                   val += 1
               self.next_level *= 1.5
               self.health += 50



