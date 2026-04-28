moods = {
 "happy": ["Happy - Pharrell Williams"],
 "sad": ["Fix You - Coldplay"],
 "stressed": ["Weightless - Marconi Union"],
 "relaxed": ["Better Together - Jack Johnson"]
}

choice = input("Choose a mood: ").lower()

if choice in moods:
    print(moods[choice])