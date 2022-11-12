# Lab Exercise 03
print('Lab Exercise 03 \n')

# Setup
shows = [
    ["The Imperfects", "Science Fiction", "1", "entertaining"],
    ["Devil in Ohio", "Thriller", "1", "spooky"],
    ["The Crown", "Historical Drama", "4", "Powerful"],
    ["Narco-Saints", "Thriller", "1", "Entertaining"],
    ["In the Dark", "Crime Drama", "4", "intriguing"],
    ["Cyberpunk: Edgerunners", "Anime", "1", "amazing"],
    ["Dated & Related", "Reality", "1", "awkward"],
    ["Diary of a Gigolo", "Mystery", "1", "intriguing"],
    ["Cobra Kai", "Dramedy", "5", "nostalgic"],
    ["I Survived a Crime", "True Crime", "1", "violent"],
    ["Echoes: Limited Series", "Thriller", "1", "intriguing"],
    ["The Sandman", "Fantasy", "1", "striking"],
    ["Partner Track", "Legal Drama", "1", "Enjoyable"],
    ["Stranger Things", "Science Fiction", "4", "Spooky"],
    ["I AM A KILLER", "Crime", "3", "somber"],
    ["Manifest", "Supernatural", "4", "mysterious"],
    ["Never Have I Ever", "Dramedy", "3", "entertaining"],
    ["Selling The OC", "Reality", "1", "dramatic"],
    ["Glow Up", "Reality", "4", "entertaining"],
    ["Locke & Key", "Horror", "3", "intriguing"]
]

# Problem 01 (1 points)
every_other_reversed = shows[::-2]

print(f"\n1. every_other_reversed = {every_other_reversed}")

# Problem 02 (3 points)

genres = []
for i in range(0, len(shows)): 
    genres.append(shows[i][1])

print(f"\n2. genres = {genres}")

# Problem 03 (3 points)

entertaining_shows = []
for i in range(0, len(shows)):
    if 'entertaining' in shows[i][-1].lower():
        entertaining_shows.append(shows[i][0])

print(f"\n3. entertaining_shows = {entertaining_shows}")

# Problem 04 (3 points)
count = 0
for i in range(0, len(shows)):
    if len(shows[i][0].split()) > 3:
        count += 1
print(f"There are a total of {count} shows with more than three words in their title.")

# Problem 05 (3 points)
for i in range(0, len(shows)):
    shows[i][-2] = int(shows[i][-2])

# Problem 06 (3 points)
new_shows = []
for i in range(0, len(shows)):
    if shows[i][-2] < 2:
        new_shows.append(shows[i][0])

num_seasons = 1
longest_show = None
# Problem 07 (4 points)
for i in range(0, len(shows)):
    if shows[i][-2] >= num_seasons:
        num_seasons = shows[i][-2]
        longest_show = shows[i][0]
print(longest_show)
