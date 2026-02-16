def fizz_buzz(n):
    for i in range(1, n):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz") 
        elif i % 5 == 0:
            print("Buzz")
        else:
            


# Security issue
def add_user(name, password):
    users = []
    user = {"name": name, "password": password}  # Plaintext password
    users.append(user)