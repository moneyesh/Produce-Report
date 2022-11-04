def melon_report(day_number, path):
    '''This will create a report that the company can run daily that will display the report of the day'''

    print("Day", day_number)     #prints whatever day it is at the top of the report
    delivery_file = open(path)   #opens the path that matches the day number

    for line in delivery_file:   #checks each line in the file
        line = line.rstrip()     #removes blank space on the right
        words = line.split('|')  #splits the line to create a list of elements

        #creating variables for each element in list
        melon = words[0]
        count = words[1]
        amount = words[2]

        print(f"Delivered {count} {melon}s for total of ${amount}")
    delivery_file.close()

melon_report(1, "um-deliveries-day-1.txt")
melon_report(2, "um-deliveries-day-2.txt")
melon_report(3, "um-deliveries-day-3.txt")
