import random
import string

def generate_password(length=12, complexity='medium'):
    if complexity == 'low':
        chars = string.ascii_letters + string.digits
    elif complexity == 'medium':
        chars = string.ascii_letters + string.digits + string.punctuation
    elif complexity == 'high':
        chars = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase
    else:
        raise ValueError("Complexity level should be 'low', 'medium', or 'high'.")

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    complexity = input("Enter the complexity level (low/medium/high): ")
    password=generate_password(length,complexity)
    print("Genarated Password",password)
