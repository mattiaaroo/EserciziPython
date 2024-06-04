class Animal:
	def __init__(self, name, species, age, height, width, preferred_habitat):
		self.name = name
		self.species = species
		self.age = age
		self.height = height
		self.width = width
		self.preferred_habitat = preferred_habitat
		self.health = round(100 * (1 / self.age), 3)
		self.area = height * width
    
	def __str__(self):
		return f"(name={self.name} species={self.species} age={self.age})"

class Fence:
	animals: list = []
	def __init__(self, area, temperature, habitat):
		self.area = area
		self.temperature = temperature
		self.habitat = habitat
		self.available_space = area
	
	def addAnimal(self, animals):
		self.animals = animals

	def __str__(self):
		return f"(area={self.area} temperature={self.temperature} habitat={self.habitat})"

class ZooKeeper:
	def __init__(self, name, surname, id):
		self.name = name
		self.surname = surname
		self.id = id

	def __str__(self):
		return f"(name={self.name} surname={self.surname} id={self.id})"
    
class Zoo:
	def __init__(self):
		self.fences = []
		self.zoo_keepers = []

	def add_animal(self, animal = Animal, habitat = Fence.habitat):
		if animal.preferred_habitat != habitat:
			return (f"Cannot add {animal} in {fence} due to habitat preferences")

		if animal.area > fence.available_space:
			return (f"There is not enough space in {fence} for {animal.name}")

		fence.available_space -= animal.area
		fence.addAnimal(fence, animal)

	def remove_animal(self, animal = Animal, fence = Fence):
		if animal not in fence.animals:
			return (f"{animal.name} not in {fence}")

		fence.available_space += animal.area
		fence.animals.remove(animal)

	def feed(self, animal = Animal):
			fence: Fence
			if animal.area + (animal.height * 0.02) + (animal.width * 0.02) <= fence.available_space:
				animal.health += 0.01
				animal.height *= 1.02
				animal.width *= 1.02
			else:
				return (f"Cannot feed {animal.name} due to dimensions")

	def clean(self, fence):
		fence = Fence
		occupied_space = 0
		for animal in fence.animals:
			animal = Animal
			occupied_space += animal.area

		cleaning_time = occupied_space / fence.available_space
		if fence.available_space == 0:
			cleaning_time = occupied_space

		return cleaning_time

	def describe_zoo(self):
		print("\nGuardians:")
		for zoo_keeper in self.zoo_keepers:
			print(f"\nZooKeeper{zoo_keeper}")

		print("\nFences:")
		for fence in self.fences:
			fence = Fence
			if fence.animals:
				print(f"\nFence{fence}")
				print(f"\nwith animals:")
				for animal in fence.animals:
					print(f"\n{animal}")
			else:
				print(f"\nFence: {fence}")
				print(f"\nwith animals: ")
				print(f"\nNone")

		print("\n##############################")
zoo = Zoo()

# Crea un guardiano dello zoo
zookeeper = ZooKeeper("Lorenzo", "Maggi", 1234)
zoo.zoo_keepers.append(zookeeper)

# Crea un recinto
fence = Fence(100, 25, "Continentale")
zoo.fences.append(fence)

# Crea degli animali
scoiattolo = Animal("Scoiattolo", "Blabla", 25, 10, 5, "Continentale")
lupo = Animal("Lupo", "Lupus", 14, 80, 50, "Continentale")

# Aggiungi gli animali al recinto
fence.animals.append(scoiattolo)
zoo.add_animal(lupo, "Continentale")

# Visualizza le informazioni sullo zoo
zoo.describe_zoo()