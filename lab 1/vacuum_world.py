def get_room_states():
    while True:
        states = input("\nEnter room states (1 = Dirty, 0 = Clean): ").strip().split()

        if states and all(state in ("0", "1") for state in states):
            return [int(state) for state in states]

        print("Invalid input.")
        print("Enter only 0 or 1 separated by spaces.")
        print("Example: 1 0 1 0")

def get_vacuum_location(num_rooms):

    while True:
        try:
            location = int(
                input(
                    f"Enter vacuum location (1-{num_rooms}): "
                )
            )

            if 1 <= location <= num_rooms:
                return location - 1

            print(
                f"Location must be between 1 and {num_rooms}."
            )

        except ValueError:
            print("Enter a valid room number.")


def display_state(rooms, vacuum_location, direction):

    num_rooms = len(rooms)

    # Room labels
    labels = []
    for i in range(num_rooms):
        labels.append(chr(ord('A') + i))

    print("\n")

    # Room labels
    print(" ".join(labels))

    # Room states
    print(" ".join(map(str, rooms)))

    # Vacuum position
    vacuum_line = []

    for i in range(num_rooms):
        if i == vacuum_location:
            vacuum_line.append("V")
        else:
            vacuum_line.append(" ")

    print(" ".join(vacuum_line))

    print(f"\nVacuum: Room {labels[vacuum_location]}")
    print(f"Direction: {direction}")


def all_rooms_clean(rooms):
    return all(room == 0 for room in rooms)


def vacuum_agent(rooms, vacuum_location, direction):

    num_rooms = len(rooms)

    while True:

        display_state(
            rooms,
            vacuum_location,
            direction
        )

        if rooms[vacuum_location] == 1:

            print(
                f"Action: S (Suck) - "
                f"Room {vacuum_location + 1}"
            )

            rooms[vacuum_location] = 0

            display_state(
                rooms,
                vacuum_location,
                direction
            )


        if direction == "R":

            # Last room reached
            if vacuum_location == num_rooms - 1:

                print("\nReached the last room.")

                # Check if all rooms are clean
                if all_rooms_clean(rooms):
                    print("All rooms are clean!")
                    return vacuum_location, direction

                # Change direction
                direction = "L"

                print("Direction changed: R -> L")

            else:

                vacuum_location += 1

                print(
                    f"Action: R - "
                    f"Move to Room {vacuum_location + 1}"
                )

        elif direction == "L":

            # First room reached
            if vacuum_location == 0:

                print("\nReached the first room.")

                # Check if all rooms are clean
                if all_rooms_clean(rooms):
                    print("All rooms are clean!")
                    return vacuum_location, direction

                # Change direction
                direction = "R"

                print("Direction changed: L -> R")

            else:

                vacuum_location -= 1

                print(
                    f"Action: L - "
                    f"Move to Room {vacuum_location + 1}"
                )


def main():

    print("=" * 50)
    print("          VACUUM CLEANER AGENT")
    print("=" * 50)

    rooms = get_room_states()

    num_rooms = len(rooms)

    vacuum_location = get_vacuum_location(num_rooms)

    # Initial direction is ALWAYS Right
    direction = "R"

    print("\nInitial State:")

    display_state(
        rooms,
        vacuum_location,
        direction
    )

    while True:

        # Run vacuum agent
        vacuum_location, direction = vacuum_agent(
            rooms,
            vacuum_location,
            direction
        )

        print("\n" + "=" * 50)
        print("FINAL STATE")

        display_state(
            rooms,
            vacuum_location,
            direction
        )

        choice = input(
            "\nEnter new room states? (Y/N): "
        ).strip().upper()

        if choice != "Y":
            print("\nProgram terminated.")
            break

        while True:

            new_rooms = get_room_states()

            # Number of rooms must remain the same
            if len(new_rooms) == num_rooms:
                rooms = new_rooms
                break

            print(
                f"Please enter exactly {num_rooms} "
                f"room states."
            )

if __name__ == "__main__":
    main()
