import requests
from cfonts import render

# Rendered text with colors
NIKZ = render('{NiKZ}', colors=['yellow', 'cyan'], align='center')
print(NIKZ)
print("▩" * 60)

print(f"""\x1b[38;5;117m 1\x1b[38;5;231m - Gmail Specific Year + Meta Hunter | \x1b[1;32m Active ✅
\x1b[38;5;117m 2\x1b[38;5;231m - Pass reset Tool | \x1b[1;32m Active ✅
""")

# Dictionary of script URLs
scripts = {
    "1": "https://raw.githubusercontent.com/nikzffx/insta/refs/heads/main/meta.py",
    "2": "https://raw.githubusercontent.com/nikzffx/insta/refs/heads/main/passrest.py",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
}

def execute_script(url):
    """Fetch and execute a script from a given URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        exec(response.text)  # **Security risk: use with caution!**
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

def main_menu():
    """Display menu and handle user input."""
    print("▩" * 60)
    choice = input(" • Enter your choice (1-2): ")

    if choice in scripts:
        execute_script(scripts[choice])
    else:
        print("Invalid input. Please choose a number between 1 and 6.")
        main_menu()  # Recursively call the menu again

if __name__ == "__main__":
    main_menu()
