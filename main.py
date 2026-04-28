moods = {
 "happy": ["Happy - Pharrell Williams"],
 "sad": ["Fix You - Coldplay"]
}

choice = input("Choose a mood: ").lower()

if choice in moods:
    print(moods[choice])