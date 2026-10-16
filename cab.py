import random
while True:
    print("\n1:Book Ride")
    print("2:Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        print("\n1.Auto:Rs=12 per km")
        print("2.Sedan:Rs=18 per km")
        print("3.SUV:Rs=25 per km")

        cab = input("Choose cab: ")

        if cab == "1":
            cab_type = "Auto"
            rate = 12
        elif cab == "2":
            cab_type = "Sedan"
            rate = 18
        elif cab == "3":
            cab_type = "SUV"
            rate = 25
        else:
            print("Invalid cab choice!")
            continue

        print("\n1.Pune Station to Shivajinagar:5 km")
        print("2.Swargate to Kothrud:8 km")
        print("3.Hinjawadi to Wakad:10 km")

        route = input("Choose route: ")

        if route == "1":
            source = "Pune Station"
            destination = "Shivajinagar"
            distance = 5
        elif route == "2":
            source = "Swargate"
            destination = "Kothrud"
            distance = 8
        elif route == "3":
            source = "Hinjawadi"
            destination = "Wakad"
            distance = 10
        else:
            print("Invalid route choice!")
            continue

        fare = rate * distance

        print("\nCab:", cab_type)
        print("Source:", source)
        print("Destination:", destination)
        print("Distance:", distance, "km")
        print("Rate: Rs.", rate, "per km")
        print("Total Fare: Rs.", fare)

        print("\n1. Confirm & Share OTP")
        print("2. Cancel Ride")

        confirm = input("Enter choice: ")

        if confirm == "1":
            otp = random.randint(1000, 9999)
            print("Your OTP is:", otp)
            print("Booking Confirmed!")
            print("Ride cannot be cancelled after OTP sharing.")

        elif confirm == "2":
            print("Ride cancelled. OTP not shared.")

        else:
            print("Invalid choice. Ride cancelled.")

    elif choice == "2":
        print("Thank you! Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")
