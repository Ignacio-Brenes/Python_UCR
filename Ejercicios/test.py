def add_ticket_sale(num_tickets, file_name="ticket_sales.txt"):
    # Open the file for appending
    with open(file_name, "a") as file:
        # Write the ticket sale to the file
        file.write(str(num_tickets) + "\n")

def get_total_tickets_sold(file_name="ticket_sales.txt"):
    # Initialize a variable to store the total number of tickets sold
    total_tickets = 0

    # Open the file for reading
    with open(file_name, "r") as file:
        # Read each line from the file and add it to the total
        for line in file:
            total_tickets += int(line.strip())

    # Return the total number of tickets sold
    return total_tickets

# Example usage
while True:
    # Ask the user how many tickets they want to buy
    num_tickets = int(input("Enter the number of tickets you want to buy (0 to quit): "))

    # If the user entered 0, break out of the loop
    if num_tickets == 0:
        break

    # Add the ticket sale to the file
    add_ticket_sale(num_tickets)

# Get the total number of tickets sold and print it
total_tickets = get_total_tickets_sold()
print("Total tickets sold:", total_tickets)
