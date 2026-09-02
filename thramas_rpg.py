from random import choice
import time

#TYPEWRITER EFFECT FUNCTION
def type_line(text, delay=0.02, pause=0.6):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
    time.sleep(pause)

#CHOICE HANDLING FUNCTIONS

#CHOICE 1
def handle_choice_1(choice):
    if choice == "1":
        type_line("You plant an armored hand against the collapsed plating.")
        type_line("Your damaged servos whine as you force the wreckage upward.")
        type_line("With a final heave, the slab crashes aside.")
        type_line("You rise slowly, warning runes flickering across your visor.")
    elif choice == "2":
        type_line("You force your vox-link onto the squad frequency.")
        type_line("Brother-Sergeant? Squad, respond.")
        type_line("Only static answers.")
        type_line("Then, beneath the interference, you hear something.")
        type_line("Three broken bursts of gunfire. Then silence.")
        type_line("You brace yourself beneath the wreckage and push.")
        type_line("Damaged armor servos protest, but the plating finally rolls aside.")
        type_line("You pull yourself to your feet.")
    elif choice == "3":
        type_line("You remain beneath the wreckage and study the corridor through your damaged lenses.")
        type_line("The emergency lumens pulse weakly along the bulkheads.")
        type_line("Bolt impacts scar the walls. Dark blood streaks the deck.")
        type_line("Several meters away lies a legionary in blackened plate.")
        type_line("Lightning markings crawl across one shattered shoulder guard.")
        type_line("You turn your attention to the weight pinning you down.")
        type_line("With a grunt, you force the wreckage aside and drag yourself free.")
        type_line("You rise.")
    else:
        print("Invalid choice.")

#CHOICE 2
def handle_choice_2(choice):
    if choice == "1":
        type_line("You step into the darkness without activating your lumen.")
        type_line("Your helm lenses adjust, painting the corridor in muted outlines.")
        type_line("You let training and instinct guide you, moving cautiously forward.")
        type_line("The faint heat of recent weapons fire still clings to the deck.")
        type_line("A smear of blood marks the bulkhead ahead.")
        type_line("Someone passed through here recently.")
    elif choice == "2":
        type_line("You activate your armor's lumen.")
        type_line("White light cuts through the darkness.")
        type_line("The corridor resolves around you in harsh detail.")
        type_line("Spent bolt casings litter the deck.")
        type_line("Two mortal crewmen lie motionless near the bulkhead.")
        type_line("Farther ahead, something catches the light.")
        type_line("A bolter bearing the winged sowrd of the First Legion.")
        type_line("Then, somewhere beyond the reach of the beam, metal scrapes against metal.")
    elif choice == "3":
        type_line("You remain motionless at the threshold.")
        type_line("For several seconds, there is only the low groan of the wounded ship.")
        type_line("Then you hear it.")
        type_line("Ceramite scraping softly against metal.")
        type_line("Far ahead.")
        type_line("A burst of static whispers across your damaged vox.")
        type_line(f"\"...Brother {player_name}...\"")
        type_line("The transmission vanishes almost as quickly as it appeared.")
    else:
        print("Invalid choice.")

         
#INTRO / SCENE 1
print("+++ THE THRAMAS CRUSADE +++")
print()
type_line("The galaxy burns.")
type_line("Horus Lupercal has turned upon the Emperor, and brother now wages war against brother.")
type_line("Across the Thramas Sector, the First Legion hunts the murderous sons of Konrad Curze.")
type_line("For months, the Dark Angels and Night Lords have torn fleets, worlds, and one another apart.")
type_line("You are one warrior among thousands.")
type_line("And aboard one forgotten vessel, your war is about to become very small.")
print()



#PLAYER NAME INPUT
player_name = input("Enter your name: ")
#WHILE LOOP TO ENSURE NAME IS NOT EMPTY
while player_name == "":
    print("Name cannot be empty. Please enter a valid name.")
    player_name = input("Enter your name: ")
print()



type_line(f"Brother {player_name} of the I Legion. Son of the Lion.")

print()
type_line("You awaken beneath shattered plating.")
type_line("Your armor is damaged.")
type_line("Your squad vox is silent.")
type_line("Your bolter is gone.", pause=0.8)

#CHOICE 1 PROMPT
print()
print("What do you do?")
print()
print("1. Free yourself from the wreckage.")
print("2. Attempt to contact your squad.")
print("3. Examine your surroundings.")
print()

choice = input("++ Choose an option: ")
print()
handle_choice_1(choice)

#SCENE 2
print()
type_line("You steady yourself against the bulkhead.")
type_line("Your helm display flickers, struggling to reconnect with the ship's internal network.")
type_line("Deck Twelve. Port transit passage.")
type_line("Memory returns with the designation.")
type_line("Your squad had been moving forward when the VIII Legion breached this section of the vessel.")
type_line("Sergeant Corvin had ordered you through the pressure door ahead.")
type_line("Then came the explosion.")
type_line("The pressure door is still open.")
type_line("Beyond it, the corridor disappears into darkness.")

#CHOICE 2 PROMPT
print()
print("What do you do?")
print()
print("1. Enter the darkness, relying on instincts and your armor's auto-senses.")
print("2. Activate your armor's illumination and advance.")
print("3. Remain at the threshold, listening for any signs of movement.")
print()

choice = input("++ Choose an option: ")
print()
handle_choice_2(choice)

print()
type_line("Whatever lies ahead, remaining here will reveal nothing more.")
type_line("You advance.")