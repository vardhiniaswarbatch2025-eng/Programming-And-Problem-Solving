n = int(input())
contacts = {}

for _ in range(n):
    operation = input().split()
    
    if operation[0] == "ADD":
        contacts[operation[1]] = operation[2]
    
    elif operation[0] == "REMOVE":
        if operation[1] in contacts:
            del contacts[operation[1]]
    
    elif operation[0] == "DISPLAY":
        if not contacts:
            print("No contacts")
        else:
            for name in sorted(contacts):
                print(f"{name}: {contacts[name]}")

