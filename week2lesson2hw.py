# Lesson Two - Problem One

def reformat(customer_information):
    output = ""
    i = 0
    for traveler_name, origin, destination in customer_information:
        i += 1
        output += f"\nItinerary {i}: {traveler_name} - From {origin} to {destination}"
    return output
print(reformat([("Alice","New York", "London"), ("Bob", "Tokyo", "San Francisco")]))    

# Problem Two
def add_book(library, title, author):
    
    for book in library:
        if book[0] == title and book[1] == author:
            return f"The book '{title}' by {author} is already in the library."

    library.append((title, author))
    return f"The book '{title}' by {author} has been added to the library."

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]

print(add_book(library, "In Five Years", "Rebecca Serle")) 
print(add_book(library, "1984", "George Orwell"))   
print(add_book(library, "Brave New World", "Aldous Huxley"))  


#  Problem Three - Task One
stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0),
    # More data...
]

def calculate_average_closing_price(stock_symbol, stock_data):
    total_closing_price = 0
    count = 0
    for data_point in stock_data:
        if data_point[0] == stock_symbol:
            total_closing_price += data_point[2]
            count += 1
    if count == 0:
        return f"No data found for stock symbol {stock_symbol}"
    else:
        return total_closing_price / count

stock_symbol = "AAPL"
print(f"Average closing price of {stock_symbol}: {calculate_average_closing_price(stock_symbol, stock_data)}")

# Problem Three - Task Two
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit"),
    # More attendees...
]
def list_attendees(event_name, attendees):
    event_attendees = []
    for attendee in attendees:
        if attendee[1] == event_name:
            event_attendees.append(attendee[0])
    return event_attendees

def count_attendees(attendees):
    event_counts = {}
    for attendee in attendees:
        event_name = attendee[1]
        if event_name in event_counts:
            event_counts[event_name] += 1
        else:
            event_counts[event_name] = 1
    return event_counts

event_name = "Python Conference"
print(f"Attendees of {event_name}: {list_attendees(event_name, attendees)}")
print("\nNumber of attendees for each event:")
attendee_counts = count_attendees(attendees)
for event, count in attendee_counts.items():
    print(f"{event}: {count}")


