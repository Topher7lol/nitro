import random
import string
try:
    import requests
except ImportError:
    print("This code requires requests. Run 'pip install requests' to install requests.")

codelength = random.randint(7, 13)

def generate_random_line():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(codelength))
def confirm_nitro_code(url):
    req = requests.get("https://discord.com/api/v8/entitlements/gift-codes/" + url)
    if req.status_code == 404:
        print("Invalid nitro code: " + url)
        return False
    elif req.status_code == 200:
        return "true"
    
def main():
    print("This may take a long time. ")
    num_lines = 1
    while num_lines != 0:
        if num_lines == 0:
            break
        code = generate_random_line()
        check = confirm_nitro_code(code)
        if check == "true":
            print("Found nitro code: " + "https://discord.com/gifts/" + code)
            num_lines == 0
            pass
        else:
            pass
    input("Press any key, then press enter to exit...")

main()
