"""Creating river ecosystem using bear, fish, and river classes"""

from exercises.ex07.river import River

__author__: str = "730766559"

my_river: River = River(num_fish=10, num_bears=2)
my_river.view_river()
my_river.one_river_week()
