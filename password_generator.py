import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters= random.randint(3,4) 
    nr_symbols = random.randint(3,4)
    nr_numbers = random.randint(3,4)

    generated_password=[]

    for i in range(nr_letters):
        generated_password+=random.choice(letters)
    for i in range(nr_symbols):
        generated_password+=random.choice(symbols)
    for i in range (nr_numbers):
        generated_password+=random.choice(numbers)

    random.shuffle(generated_password)
    password=""
    for character in generated_password:
        password+=character
    return password
