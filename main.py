#Amaria J. Robinson

def show_instructions():
    # Display the game instructions.
    print("Welcome to the Detective Clue Finding Game")
    print("Collect all seven clues before entering the Secret Lair to arrest the suspect!")
    print("Move Commands: go North, go South, go East, or go West")
    print("Type 'exit' to quit the game at any time.")


def show_status(current_room, inventory, room_items, rooms):
    # Display the player's current room, inventory, any clue in the room, and available directions.
    print("You are in the", current_room)
    print("Inventory:", inventory)

    # Display the clue if present and not yet collected.
    if current_room in room_items and room_items[current_room] not in inventory:
        print("You see a", room_items[current_room])
    else:
        print("No items in this room.")

    # Display available directions.
    if current_room in rooms and rooms[current_room]:
        available_moves = ", ".join(rooms[current_room].keys())
        print("Available directions:", available_moves)


def get_item(current_room, inventory, room_items):
    """Add the clue in the current room to the player's inventory if available."""
    if current_room in room_items:
        item = room_items[current_room]
        if item not in inventory:
            inventory.append(item)
            print("You collected:", item)
        else:
            print("Item already collected from this room.")
    else:
        print("There is no item to collect in this room.")


def main():
    """Main game loop for the Detective Clue Finding Game."""
    # Define the rooms and valid movement directions.
    rooms = {
        "Foyer": {"East": "Kitchen"},
        "Kitchen": {"North": "Dining Room", "South": "Master Bedroom", "East": "Basement", "West": "Foyer"},
        "Dining Room": {"East": "Library", "South": "Kitchen"},
        "Library": {"West": "Dining Room"},
        "Master Bedroom": {"East": "Attic", "North": "Kitchen"},
        "Attic": {"West": "Master Bedroom"},
        "Basement": {"North": "Secret Lair", "West": "Kitchen"},
        "Secret Lair": {}  # Villain room – game over if entered without all items.
    }

    # Define the clues (items) available in each room except the villain's room.
    room_items = {
        "Foyer": "Princess Peach’s heart shaped locket",
        "Kitchen": "Used champagne glass with white powdery substance",
        "Dining Room": "Princess Peach’s glass slipper",
        "Library": "Princess Peach’s blood-stained crown",
        "Master Bedroom": "Princess Peach’s dress",
        "Attic": "Rope",
        "Basement": "Blood-stained rusty pipe"
    }

    # Initialize player's state.
    inventory = []
    current_room = "Foyer"
    show_instructions()

    while True:
        show_status(current_room, inventory, room_items, rooms)

        # Prompt for clue pickup if available.
        if current_room in room_items and room_items[current_room] not in inventory:
            pickup_response = input("Do you want to add this clue to inventory? (yes/no): ").strip().lower()
            if pickup_response in ("yes", "y"):
                get_item(current_room, inventory, room_items)

        command_input = input("\nEnter your move: ").strip()
        if command_input.lower() == "exit":
            print("\nExiting game. Final Inventory:", inventory)
            break

        command_parts = command_input.split()
        if len(command_parts) < 2:
            print("Invalid command. Please use 'go [direction]' or 'get [item name]'.")
            continue

        command_type = command_parts[0].lower()

        if command_type == "go":
            direction = command_parts[1].title()
            if current_room in rooms and direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                # Check if the player enters the Secret Lair.
                if current_room == "Secret Lair":
                    if len(inventory) == len(room_items):
                        print(
                            "Congratulations! You have collected enough clues to take down Bowser in the Secret Lair!")
                    else:
                        print("OOPS... GAME OVER, he went free because you didn't get enough clues!")
                    print("Thanks for playing the game. Hope you enjoyed it.")
                    break

        elif command_type == "get":
            # Combine the remainder of the input as the item name.
            item_name = " ".join(command_parts[1:])
            if current_room in room_items and item_name.lower() == room_items[current_room].lower():
                get_item(current_room, inventory, room_items)
            else:
                print("Can't get that item here!")
        else:
            print("Invalid command. Please use 'go [direction]' or 'get [item name]'.")

        # Notify when all clues have been collected.
        if len(inventory) == len(room_items):
            print("Congratulations! You collected all the clues and took him down!!")


if __name__ == "__main__":
    main()
