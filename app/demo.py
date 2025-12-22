from crud import *
from queries import *

add_museum("HeritagePlus Central Museum", "London")
add_exhibit(1, "Ancient Civilisations", "Historical artefacts", "2024-01-01", "2024-12-31")
add_visitor("John Smith", 32, "Male", "UK")
add_artefact(1, "Roman Coin", "Metal", "1902-05-10", "Italy")

print(list_exhibits())

print("Exhibits with museums:")
print(get_exhibits_with_museum())

print("Most visited exhibits:")
print(most_visited_exhibits())

print("Conservation history:")
print(conservation_history())

print("Visitors by country:")
print(visitors_by_country())