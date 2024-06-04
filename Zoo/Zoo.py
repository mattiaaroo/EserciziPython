class Animal:
	def __init__(self, name, species, age, height, width, preferred_habitat):
		self.name = name
		self.species = species
		self.age = age
		self.height: float = height
		self.width: float = width
		self.preferred_habitat = preferred_habitat
		self.health = round(100 * (1 / self.age), 3)
		self.area: float = height * width
		self.fence = None
    
	def __str__(self):
		return f"(name={self.name} species={self.species} age={self.age})"
	
class Fence:
	def __init__(self, area, temperature, habitat):
		self.area = area
		self.temperature = temperature
		self.habitat = habitat
		self.available_space = area
		self.animals: list = []
		zoo.fences.append(self)
	
	def __str__(self):
		return f"(area={self.area} temperature={self.temperature} habitat={self.habitat})"
	
class ZooKeeper:
	def __init__(self, name, surname, id):
		self.name = name
		self.surname = surname
		self.id = id
		zoo.zoo_keepers.append(self)

	def feed(self, animal: Animal):
			fence = animal.fence
			newHealth: float = animal.health 
			newHeight: float = animal.height
			newWidth: float = animal.width
			newHealth += 0.01
			newHeight *= 1.02
			newWidth *= 1.02
			newArea: float = newHeight * newWidth
			newAvailableSpace = fence.available_space + animal.area - newArea
			if fence.available_space + animal.area - newArea  >= 0:
				animal.health = newHealth
				animal.height = newHeight
				animal.width = newWidth
				animal.area = newArea
				fence.available_space = newAvailableSpace
			else:
				print (f"!!!Cannot feed {animal.name} due to predicted dimensions!!!")

	def clean(self, fence: Fence):
		occupied_space = fence.area - fence.available_space
		if fence.animals:
			if fence.available_space == 0:
				cleaning_time = occupied_space
				for animal in fence.animals:
					fence.animals.remove(animal)
			else: 
				for animal in fence.animals:
					fence.animals.remove(animal)
				cleaning_time = occupied_space / fence.available_space
		else:
			cleaning_time = 0
		return cleaning_time

	def __str__(self):
		return f"(name={self.name} surname={self.surname} id={self.id})"
	
class Zoo:
	def __init__(self):
		self.fences: list = []
		self.zoo_keepers: list = []
	
	def add_animal(self, animal: Animal, fence: Fence):
		if fence.habitat == animal.preferred_habitat:
			if animal not in fence.animals:
				if fence.available_space - animal.area >= 0:
					fence.animals.append(animal)
					fence.available_space -= animal.area
					animal.fence = fence
				else: 
					print (f"!!!There is not enough space to add {animal.name} in {fence.habitat}!!!")
			else: 
				print (f"!!!{animal.name} is already in {fence.habitat}!!!")
		else:
			print (f"!!!{animal.name} cannot stay in {fence.habitat} due to habitat preferences!!!")
		
	def remove_animal(self, animal: Animal, fence: Fence):
		if animal not in fence.animals:
			print (f"!!!{animal} not in {fence}!!!")
		else:
			fence.animals.remove(animal)
			animal.fence = None
			fence.available_space += animal.area
		
	def describe_zoo(self):
			print("\nGuardians:")
			for zoo_keeper in self.zoo_keepers:
				print(f"\nZooKeeper{zoo_keeper}")

			print("\nFences:")
			for fence in self.fences:
				fence:Fence
				if fence.animals:
					print(f"\nFence{fence}")
					print(f"\nwith animals:")
					for animal in fence.animals:
						print(f"\nAnimal{animal}")
					print("#" * 30)
				else:
					print(f"\nFence:{fence}")
					print(f"\nwith animals: ")
					print(f"\nNone")
					print("#" * 30)