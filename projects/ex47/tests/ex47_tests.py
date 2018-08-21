from nose.tools import *
from ex47.game import Room


def test_rooom():
	gold = Room("GoldRoom", """this room has gold in it you can grab.""")
	assert_equal(gold.name, "GoldRoom")
	assert_equal(gold.paths, {})


def test_room_paths():
	center = Room("Center", "test room in center")
	north = Room("North", "test room in north")
	south = Room("South", "test room in south")

	center.add_paths({'north': north, 'south': south})
	assert_equal(center.go('north'), north)
	assert_equal(center.go('south'), south)


def test_map():
	start = Room("start", "you can go west and down")
	west = Room("trees", "there are trees, you can go east")
	down = Room("dungeons", "it's dark. You can go up.")

	start.add_paths({'west': west, 'down': down})
	west.add_paths({'east': start})
	down.add_paths({'up': start})

	assert_equal(start.go('west'), west)
	assert_equal(start.go('west').go('east'), start)
	assert_equal(start.go('down').go('up'), start)