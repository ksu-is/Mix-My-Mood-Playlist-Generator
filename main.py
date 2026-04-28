moods = {
 "happy": ["Happy - Pharrell Williams", "Good as Hell - Lizzo"],
 "sad": ["Fix You - Coldplay", "Someone Like You - Adele"],
 "stressed": ["Weightless - Marconi Union", "Breathe - Télépopmusik"],
 "relaxed": ["Better Together - Jack Johnson", "Sunflower - Post Malone"]
}

choice = input("Choose a mood: ").lower()

if choice in moods:
    print("Your playlist:")
    for song in moods[choice]:
        print(song)

else:
    print("Invalid mood entered.")        