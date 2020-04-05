"""
 Write a Python function invoice_totals(orders, min) which returns a list with 2-tuples. Each 
 tuple consists of the order number and the total (the product of the price per item by the 
 quantity). The total should be increased by 10€ if the value of the order is smaller than the 
 min value.
""" 

def invoice_totals(orders, min_):
    return list(map(lambda x: (x[0], x[2] * x[3] if x[2] * x[3] >= min_ else x[2] * x[3] + 10), 
                    orders))

print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95]], 0))
print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95], [98762, 'Book of Silly Walks, Monty Python', 5, 56.8]], 500))
print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95], [98762, 'Book of Silly Walks, Monty Python', 5, 56.8], [77226, 'Flying Circus: Treasures, Monty Python', 3, 32.95], [88112, 'Diaries, Michael Palin', 3, 24.99]], 100))
print(invoice_totals([[34587, 'Always Look on the Bright, Eric Idle', 4, 40.95], [98762, 'Book of Silly Walks, Monty Python', 5, 56.8], [77226, 'Flying Circus: Treasures, Monty Python', 3, 32.95], [88112, 'Diaries, Michael Palin', 3, 24.99]], 0))
print(invoice_totals([[32341, 'The Adventures of Augie March, Saul Bellow', 4, 40.95], [45432, "All the King's Men, Robert Penn Warren", 5, 56.8]], 50))
print(invoice_totals([[32341, 'The Adventures of Augie March, Saul Bellow', 4, 40.95], [45432, "All the King's Men, Robert Penn Warren", 5, 56.8], [93834, 'American Pastoral, Philip Roth', 3, 32.95], [35322, 'An American Tragedy, Theodore Dreiser', 3, 24.99]], 500))
print(invoice_totals([[45643, 'Animal Farm, George Orwell', 3, 32.95], [24342, "Appointment in Samarra, John O'Hara", 3, 24.99], [34587, 'Always Look on the Bright, Eric Idle', 4, 40.95]], 0))
print(invoice_totals([[93834, 'American Pastoral, Philip Roth', 3, 32.95], [35322, 'An American Tragedy, Theodore Dreiser', 3, 24.99], [45643, 'Animal Farm, George Orwell', 3, 32.95], [24342, "Appointment in Samarra, John O'Hara", 3, 24.99]], 100))
