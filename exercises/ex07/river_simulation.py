from ex07.fish import Fish
from ex07.bear import Bear
from ex07.river import River

"""Creating river ecosystem using bear, fish, and river classes"""

my_river: River = River(num_fish=10, num_bears=2)
my_river.one_river_week()
