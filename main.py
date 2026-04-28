moods = {
 "happy": ["Happy - Pharrell Williams"],
 "sad": ["Fix You - Coldplay"],
 "stressed": ["Weightless - Marconi Union"],
 "relaxed": ["Better Together - Jack Johnson"]
}

choice = input("Choose a mood: ").lower()

if choice in moods:
    print("Your playlist:")
    for song in moods[choice]:
        print(song)

else:
    print("Invalid mood entered.")        