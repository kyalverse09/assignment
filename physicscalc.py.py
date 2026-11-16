# Function 1: Speed
def speed():
    distance = float(input("Enter distance (m): "))
    time = float(input("Enter time (s): "))
    if time == 0:
        print("Time cannot be zero.")
        return
    result = distance / time
    print("Speed =", result, "m/s")


# Function 2: Force
def force():
    mass = float(input("Enter mass (kg): "))
    acceleration = float(input("Enter acceleration (m/s^2): "))
    result = mass * acceleration
    print("Force =", result, "N")


# Function 3: Density
def density():
    mass = float(input("Enter mass (kg): "))
    volume = float(input("Enter volume (m^3): "))
    if volume == 0:
        print("Volume cannot be zero.")
        return
    result = mass / volume
    print("Density =", result, "kg/m^3")


# Function 4: Work Done
def work():
    force_value = float(input("Enter force (N): "))
    distance = float(input("Enter distance (m): "))
    result = force_value * distance
    print("Work Done =", result, "J")


# Function 5: Kinetic Energy
def kinetic_energy():
    mass = float(input("Enter mass (kg): "))
    velocity = float(input("Enter velocity (m/s): "))
    result = 0.5 * mass * velocity ** 2
    print("Kinetic Energy =", result, "J")


# Main program:
while True:
    print("\nPHYSICS CALCULATOR")
    print("1. Speed")
    print("2. Force")
    print("3. Density")
    print("4. Work Done")
    print("5. Kinetic Energy")

    choice = input("Choose a formula (1-5): ")

    if choice == "1":
        speed()
    elif choice == "2":
        force()
    elif choice == "3":
        density()
    elif choice == "4":
        work()
    elif choice == "5":
        kinetic_energy()
        break
    else:
        print("Invalid choice. Please try again.")
