print("Available movies today:")
print("A)12 Strong:     1)2:30  2)4:40	3)7:50	4)10:50")
print("B)Coco:          1)12:40 2)3:45")
print("C)The Post:      1)12:45 2)3:35	3)7:05	4)9:55")
choice = str(input("Movie choice: "))
if choice not in ("A", "B", "C"):
    print("Invalid option; please restart app...")
else:
    showtime = int(input("Showtime: "))
    if (choice == "A" and showtime in [1,2,3,4]):
        adultTicket = int(input("Adult tickets: "))
        kidTicket = int(input("Kid tickets: "))
        totalTickets = adultTicket + kidTicket
        if totalTickets > 30:
            print("Invalid option; please restart app...")
        else:
            adultPrice = 12.45
            kidPrice = 9.68
            cost = (adultPrice * adultTicket) + (kidPrice * kidTicket)
            print(f"Total cost: ${cost:.2f}")
    elif (choice == "B" and showtime in [1, 2]):
        adultTicket = int(input("Adult tickets: "))
        kidTicket = int(input("Kid tickets: "))
        totalTickets = adultTicket + kidTicket
        if totalTickets > 30:
            print("Invalid option; please restart app...")
        else:
            if showtime == 2:
                adultPrice = 12.45
                kidPrice = 9.68
            else:
                adultPrice = 11.17
                kidPrice = 8.00
            cost = (adultPrice * adultTicket) + (kidPrice * kidTicket)
            print(f"Total cost: ${cost:.2f}")
    elif (choice == "C" and showtime in [1,2,3,4]):
        adultTicket = int(input("Adult tickets: "))
        kidTicket = int(input("Kid tickets: "))
        totalTickets = adultTicket + kidTicket
        if totalTickets > 30:
            print("Invalid option; please restart app...")
        else:
            if showtime == 1:
                adultPrice = 11.17
                kidPrice = 8.00
            else:
                adultPrice = 12.45
                kidPrice = 9.68
            cost = (adultPrice * adultTicket) + (kidPrice * kidTicket)
            print(f"Total cost: ${cost:.2f}")
    else:
        print("Invalid option; please restart app...")

#To find price, we need to figure out firstly the showtime, then
#the number of adult and kid tickets


