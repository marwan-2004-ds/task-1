contacts = { "marwan": "11111111", "Youssef": "2222222", "Laila": "333333333"}

print("Contact Names:")
for name in contacts:
    print("-", name)

search_name = input("\nEnter a name to search: ")

if search_name in contacts:
    print("Phone number:", contacts[search_name])
else:
    print("Contact not found.")
