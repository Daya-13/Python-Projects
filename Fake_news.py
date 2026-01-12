# 1- import random module
import random

# 2- INSANE subjects
subjects = [
    "Shah Rukh Khan stuck in traffic",
    "Virat Kohli after losing one run",
    "A neighbourhood aunty with full confidence",
    "A government website at midnight",
    "A cat who pays no rent",
    "An auto driver who knows everything",
    "A WhatsApp university professor",
    "A hostel senior with unlimited attitude",
    "A politician reading comments accidentally",
    "An Indian parent during result season",
    "A monkey with main-character energy"
]

# CHAOTIC actions
actions = [
    "starts motivational speech about",
    "angrily blames aliens for",
    "goes viral after fighting with",
    "announces life-changing decision regarding",
    "gets emotional because of",
    "refuses to explain",
    "creates national panic over",
    "calls emergency meeting about",
    "files complaint against",
    "starts arguing loudly with",
    "cries silently thinking about"
]

# PURE NONSENSE places/things
places_or_things = [
    "one missing sock",
    "slow Wi-Fi connection",
    "a samosa that betrayed expectations",
    "the last seat in Mumbai local",
    "battery at 1%",
    "a government form with 12 pages",
    "Monday morning existence",
    "relatives asking life updates",
    "salary disappearing in 2 days",
    "alarm ringing at 6 AM",
    "online exam server crash"
]

# 3- Headline generator loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}!!!"
    print("\n" + headline)

    user_input = input("\nGenerate another disaster? (yes/no): ").strip().lower()
    if user_input == "no":
        break

print("\nThanks for using the Fake News Generator. Society may never recover.")
