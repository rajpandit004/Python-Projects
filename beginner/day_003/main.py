import time
from ascii_art import treasure_logo, game_title, lost_message, win_message, restart_message

# Main gameplay function
def game(lives_left):
    # Game runs until no lives remain
    while lives_left > 0:
        print("🌊 You arrive at the island's shore.")
        print("A dense jungle path leads \'LEFT\' into darkness.")
        print("A treacherous cliff path winds \'RIGHT\' along the coast.")

        choice1 = input("\nWhich path do you take? (LEFT/RIGHT): ").lower()

        if choice1 == "left":
            print("\n🌴 You hack through vines and vegetation.")
            print("Strange whispers echo through the trees.")
            print("Suddenly, the ground gives way!")

            input() # Pause for dramatic effect

            print("💀 You fall into a pit of poisoned spikes left by the island's former inhabitants.")

            lives_left -= 1

            if lives_left > 0:
                print(f"\nYou Have {lives_left} More Lives Left.")
                print(restart_message)
            else:
                print(lost_message)
        elif choice1 == "right":
            print("\n⛰️ You navigate the narrow cliff edge.")
            print("Below, jagged rocks meet crashing waves.")
            print("You reach an ancient stone bridge.")

            input()

            print("🌉 The rope bridge sways dangerously.")
            print("Dark storm clouds gather overhead.")
            print("\'WAIT\' for the storm to pass? or \'CROSS\' immediately?")

            choice2 = input("\nWhat is your decision? (WAIT/CROSS): ").lower()

            if choice2 == "cross":
                print("\n🌊 Mid-crossing, the storm hits!")
                print("The bridge collapses beneath you!")

                input()

                print("💀 You're swept away by the raging current, pulled into the depths by cursed underflow.")

                lives_left -= 1

                if lives_left > 0:
                    print(f"\nYou Have {lives_left} More Lives Left.")
                    print(restart_message)
                else:
                    print(lost_message)
            elif choice2 == "wait":
                print("\n⛈️ The storm intensifies!")
                print("Lightning strikes reveal a hidden cave entrance.")
                print("You take shelter and discover a secret passage.")

                input()

                print("🕯️ The passage leads to an underground chamber with three ornate doors, each marked with symbols.")
                print("\'BLUE\' door: Carved with waves and sea creatures.")
                print("\'RED\' door: Scorched with flame patterns")
                print("\'YELLOW\' door: Decorated with golden skulls.")

                choice3 = input("\nWhich door would you choose? (BLUE/RED/YELLOW): ").lower()

                if choice3 == "blue":
                    print("\n🌊 You open the door to find a flooded chamber.")
                    print("The water rises rapidly!")

                    input()

                    print("💀 You're trapped as the chamber floods completely.")
                    print("The cursed waters claim another victim.")

                    lives_left -= 1

                    if lives_left > 0:
                        print(f"\nYou Have {lives_left} More Lives Left.")
                        print(restart_message)
                    else:
                        print(lost_message)
                elif choice3 == "red":
                    print("\n🔥 Flames burst forth!")
                    print("Ancient fire traps ignite the room!")

                    input()

                    print("💀 The flames consume everything.")
                    print("You become another ghost haunting the island.")

                    lives_left -= 1

                    if lives_left > 0:
                        print(f"\nYou Have {lives_left} More Lives Left.")
                        print(restart_message)
                    else:
                        print(lost_message)
                elif choice3 == "yellow":
                    print("\n💀 The door creaks open to reveal Captain Blackheart's inner sanctum!")
                    print("Skeletal guardians stand watch, but they part as you approach, recognizing the map bearer.")

                    input()

                    print("💎 Before you lies an altar with three chests:")
                    print("A \'JEWELLED\' chest encrusted with gems.")
                    print("A \'GOLDEN\' chest that gleams in torchlight.")
                    print("An old \'WOODEN\' chest, plain and weathered.")

                    choice4 = input("\nWhich contains the true treasure? (JEWELLED/GOLDEN/WOODEN): ").lower()

                    if choice4 == "jewelled":
                        print("\n💀 The chest explodes with cursed energy!")
                        print("Greed has sealed your fate.")

                        lives_left -= 1

                        if lives_left > 0:
                            print(f"\nYou Have {lives_left} More Lives Left.")
                            print(restart_message)
                        else:
                            print(lost_message)
                    elif choice4 == "golden":
                        print("\n💀 The chest is a mimic!")
                        print("It's jaws snap shut on you forever.")

                        lives_left -= 1

                        if lives_left > 0:
                            print(f"\nYou Have {lives_left} More Lives Left.")
                            print(restart_message)
                        else:
                            print(lost_message)
                    elif choice4 == "wooden":
                        print("\n🏆 VICTORY!")
                        print("Inside the humble chest lies the true treasure:")
                        print("Not gold, but Captain Blackheart's compass that reveals the locations of a hundred more treasure!")
                        print("You've learned that true wealth comes from wisdom, not greed.")
                        print("The island's curse is broken, and the seas await your next adventure!")

                        print(win_message)
                        break # End game loop
                    else:
                        print("\nYou Entered an Invalid Choice!")
                        print(restart_message)
                else:
                    print("\nYou Entered an Invalid Choice!")
                    print(restart_message)
            else:
                print("\nYou Entered an Invalid Choice!")
                print(restart_message)
        else:
            print("\nYou Entered an Invalid Choice!")
            print(restart_message)

print(treasure_logo)
print(game_title)

time.sleep(3) # Small delay for dramatic effect

print("🏴‍☠️ Your're a seasoned pirate who discovered Captain Blackheart's legendary map.")
print("The treasure lies deep within cursed island.")

input() # Pause for dramatic effect
lives_left = 3 # Initial lives

game(lives_left)
