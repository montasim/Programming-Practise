# Lists

collages = ['Carmichael', 'Gov', "Cant Public"]
print(collages[0])

collages[1] = "Government Collage"
print(collages[1])

print(collages)
print(collages[1:3])

dailyNeeds = ['table', 'chair', 'books', 'pen', 'soap']
print(dailyNeeds)

dailyNeeds.append('food')
print(dailyNeeds)

dailyNeeds.insert(1, 'bed')
print(dailyNeeds)

dailyNeeds.remove('bed')
print(dailyNeeds)

print(dailyNeeds + ['pillow, tubelight'])

print("Size of dailyNeeds")
print(len(dailyNeeds))

print(max(dailyNeeds))
print(min(dailyNeeds))