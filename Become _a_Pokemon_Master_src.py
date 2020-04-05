class pokemon:
  def __init__ (self, name, level, type, max_health, current_health, knocked_out):
    self.name = name
    self.level = level
    self.type = type
    self.max_health = max_health
    self.current_health = current_health
    self.knocked_out = knocked_out
    self.exp = 0
    
  def lose_health(self, dmg):
    if self.knocked_out == True:
      print(self.name + " is knocked out and cannot receive damage.")
      return 
    else:
      self.current_health -= dmg 
      return self.current_health
    
  def gain_health(self, heal):
    if self.current_health == self.max_health:
      print(self.name + " is already at max health.")
      return self.current_health
    elif (self.current_health + heal) < self.max_health:
      print (self.name + " now has " + str(self.current_health + heal) + " health.")
      return (self.current_health + heal)
    elif (self.current_health + heal) >= self.max_health:
      print (self.name + " now has " + str(self.max_health) + " hp.")
      return self.max_health
    
    if (self.current_health + heal) >= self.max_health:
      print(self.name + " currently has " + self.max_health)
      return self.max_health
  
  def knock_out(self):
    if self.current_health == 0:
      print (self.name + " has been knocked out.")
    else:
      print (self.name + " is not knocked out.")
  
  def attack(self, other, dmg):
    if self.knocked_out == True:
      print("You cannot attack, " + self.name + " has been knocked out.")
      return 
      
    if self.type == "fire":
      if other.type == "grass":
        dmg *= 2
      elif other.type == "water":
        dmg /= 2
      elif other.type == "fire":
        dmg /= 2
    
    elif self.type == "water":
      if other.type == "grass":
        dmg /= 2
      elif other.type == "water":
        dmg /= 2
      elif other.type == "fire":
        dmg *= 2
      
    elif self.type == "grass":
      if other.type == "grass":
        dmg /= 2
      elif other.type == "water":
        dmg *= 2
      elif other.type == "fire":
        dmg /= 2
    
    return other.lose_health(dmg)
  
  def gain_exp(self, exp):
    self.exp += exp
    if self.exp >= 3:
      self.level_up()
    
  def level_up (self):
    self.exp = 0
    if self.level == 100:
      print("The pokemon is already lvl 100.")
    else:
      self.level += 1
      print(self.name + " has levelled up to " + str(self.level) + ".")
      if self.level == 10:
        print("The pokemon is evolving.")
   
  #def evolve(self):
    #if self.level_up == 10:
      #print(self.name + " is evolving.")
    #elif self.level_up == 20:
      #print(self.name + " is evolving.")
      
      
#evolution occurs at lvl20 and lvl40      

class trainer():
  
  def __init__ (self, name, pokemons, current_pokemon, potions):
    self.name = name
    self.pokemons = pokemons
    self.current_pokemon = current_pokemon
    self.potions = potions
  
  def __repr__ (self):
    return self.name
  
  def use_potion (self):
    if self.current_pokemon.current_health == self.current_pokemon.max_health:
      print(self.current_pokemon + " is already at full health.")
      return self.current_pokemon.current_health
    
    elif self.current_pokemon.current_health < self.current_pokemon.max_health:
      self.potions -= 1
      return self.current_pokemon.gain_health(50)
    
  def switch_pokemon(self, pokemon):
    if pokemon.knocked_out == True:
      print("You cannot switch to a pokemon that is knocked out.")
    elif pokemon in self.pokemons:
      self.current_pokemon = pokemon
      print ("The current pokemon is " + self.current_pokemon.name)
      
 
class charmander_class (pokemon):
  def __init__ (self, name, level, type, max_health, current_health, knocked_out):
    super().__init__(name, level, type, max_health, current_health, knocked_out)
    
  def __repr__(self):
    return "At level 16, Charmander evolves into a Charmeleon. Its final evolution is Charizard which it evolves into at Level 36."
  
#each potion restores 50 health 
charmander = pokemon("charmander", 9, "fire", 100, 90, False)
 
squirtle = pokemon("squirtle", 10 ,"water", 100, 50, False)

ash = trainer("Ash", [charmander, squirtle], charmander, 1)

charmander.gain_exp(10) #prints "The pokemon is evolving."

print(ash) # prints out string representation of ash object, "Ash"
 
ash.use_potion()

charmander.attack(squirtle,10)

ash.switch_pokemon(charmander)

#current_pokemon has to be object of pokemon class already 

print(charmander.lose_health(50)) #prints out current value of charmander after health deduction.

charmander1 = charmander_class("charmander", 10, "fire", 100, 50, False)

print(charmander1)







  