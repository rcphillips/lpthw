from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

	def enter(self):
		print("This scene is not yet configured.")
		print("Subclass it and implement enter().")
		exit(1)


class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()


class Death(Scene):

	quips = [
			"Good Job!",
			"Bad Job!"]

	def enter(self):
		print(Death.quips[randint(0, len(self.quips)-1)])
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print(dedent("""
			Your ship yada yada, you are the last surviving so and so. Etc etc.
			"""))

		action = input('> ')

		if action == "shoot!":
			print("You shoot, you score! on yourself tho.")
			return 'death'

		elif action == "dodge!":
			print("You dodge! but not very well.")
			return 'death'

		elif action == "tell a joke":
			print("hahaha, good one!")
			return 'laser_weapon_armory'

		else:
			print("DOES NOT COMPUTE!")
			return 'central_corridor'


class LaserWeaponArmory(Scene):

	def enter(self):
		print(dedent("""some sick lasers in here"""))

		code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
		guess = input('> ')
		guesses = 0

		while guess != code and guesses < 10:
			print("NOPE!")
			guesses += 1
			guess = input("[keypad]> ")

		if guess == code:
			print(dedent("""Nice you got it!!"""))
			return 'the_bridge'
		else:
			print(dedent("""Oh no you dead."""))
			return 'death'


class TheBridge(Scene):

	def enter(self):
		print(dedent("""it's a rickety old bridge."""))

		action = input('> ')

		if action == "throw the bomb":
			print(dedent("""Wowwww"""))
			return 'death'

		elif action == "slowly place the bomb":
			print(dedent("""Yeah it's a bomb so like probably be real careful."""))
			return 'escape pod'


class EscapePod(Scene):

	def enter(self):
		print(dedent("""So many pods! Which one to choose?"""))

		good_pod = randint(1, 5)
		guess = input("[pod #]> ")

		if int(guess) != good_pod:
			print(dedent("""Nope, you dead."""))
			return 'death'
		else:
			print(dedent("Nice onnnnne!"))
			return 'finished'


class Finished(Scene):

	def enter(self):
		print("You won! Good job.")
		return 'finished'


class Map(object):

	scenes = {
			'central_corridor': CentralCorridor(),
			'laser_weapon_armory': LaserWeaponArmory(),
			'the_bridge': TheBridge(),
			'escape_pod': EscapePod(),
			'death': Death(),
			'finished': Finished()
			}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
print(a_map.next_scene(a_map.start_scene))
a_game = Engine(a_map)
a_game.play()
