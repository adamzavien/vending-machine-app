"""
Vending Machine App : To return the least amount of notes back to the customers.
"""

# Create a sample list of beverage tuples
beverages_tuple = [
    (1, "Mineral Water", 1.00),
    (2, "Soda", 3.00),
    (3, "Tea", 5.00),
    (4, "Red Bull", 6.00),
    (5, "Latte", 7.00)
]

    # Create a list of note(s) dictionary
notes = {
    # Key: Type of Notes : 100 = RM 100
    # Value: The number of notes returned
    100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 1: 0
}


def main():
    print(f"\n{'='*25} Welcome to Vending Machine {'='*25}\n\n") 

    display_beverage_details(beverages_tuple)

    while True:
        try:
            # Customer selects a beverage
            bev_selected = int(input(""))

            if validate_selection(bev_selected, beverages_tuple):
                break

        except ValueError:
            print("\nInvalid Beverage Selection Number\n")
    
    # Get beverage price
    price = float(get_bev_price(bev_selected, beverages_tuple))

    display_notes_details(notes)

    while True:
        try:
            # Customer insert a note value
            payment = float(input("RM "))

            if validate_payment(payment, notes):
                break
        except ValueError:
            print("\nInvalid : Note inserted is not a number\n")
    
    # Calculate the payment based on price
    calculate_fee(price, payment)

    print(f"{'='*75}") # Decoration Purpose


def count_notes(balance):
    # To keep track of updated balance
    remaining_amount = balance

    for note in sorted(notes.keys(), reverse=True):

        if remaining_amount >= note:

            counter = int(remaining_amount // note)
            notes[note] = counter
            remaining_amount -= counter * note

        
    count = 0
    print("\nNote(s) Returned: ")
    for note, counter in notes.items():
            if counter > 0:
                print(f"RM {note}\t: {counter}")
                count += counter
    
    print(f"Least amount of notes return back to the customers: {count}")
    

def calculate_fee(price, payment):

    fee = payment - price

    if fee == 0:
        print(f"\nBeverage Purchases Completed\n")
    elif fee > 0:
        print(f"\nBalanced: RM {fee:.2f}\n")
        count_notes(fee)
    else:
        fee *= -1
        print(f"\nNot enough note inserted\nCustomer Owed: RM {fee:.2f}\n")


def validate_payment(payment, notes):
    
    if payment in notes:
        return True
    else:
        print("\nInvalid - Note inserted value's does not exist.\nPlease inserted a valid note value listed above.\n")



def display_notes_details(notes):
    
    prompt = "\nInsert one of the notes value above to purchase the beverage: "

    for notes_value in notes:
        
        note_detail = f"- RM {notes_value}"
        print(note_detail)
    
    print(prompt, end="")


def get_bev_price(bev_selected, beverages_tuple):
    
    for bev_index, bev_name, bev_price in beverages_tuple:

        if bev_index == bev_selected:
            print(f"\nYou have selected {bev_name} beverage.\nThe price is RM {bev_price:.2f}\n")
            return bev_price
    
        

def validate_selection(bev_selected, beverages_tuple):

    bev_indexes = []
    
    for bev_index, *others in beverages_tuple:
        bev_indexes.append(bev_index)
        
    if bev_selected in bev_indexes:
        return True
    else:
        print("\nInvalid range number of beverage. Please choose between 1 - 5\n")
    

def display_beverage_details(beverages_tuple):

    prompt = f"\nSelect a beverage by its number between 1 - 5 : "
    
    for bev_index, bev_name, bev_price  in beverages_tuple:

        bev_detail = f"{bev_index}. {bev_name:<15} --- RM {bev_price:.2f}"

        print(bev_detail)
    
    print(prompt, end="")


if __name__ == "__main__":
    main()