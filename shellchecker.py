import requests
import sys

def check_shell(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return True
    except requests.RequestException:
        pass
    return False

def main():
    banner = """
    ╔╗      ╔╗ ╔╗         ╔╗          ╔╗         
    ║║      ║║ ║║         ║║          ║║         
    ╔══╗║╚═╗╔══╗║║ ║║     ╔══╗║╚═╗╔══╗╔══╗║║╔╗╔══╗╔═╗
    ║══╣║╔╗║║╔╗║║║ ║║     ║╔═╝║╔╗║║╔╗║║╔═╝║╚╝╝║╔╗║║╔╝
    ╠══║║║║║║║═╣║╚╗║╚╗    ║╚═╗║║║║║║═╣║╚═╗║╔╗╗║║═╣║║ 
    ╚══╝╚╝╚╝╚══╝╚═╝╚═╝    ╚══╝╚╝╚╝╚══╝╚══╝╚╝╚╝╚══╝╚╝ 


    version : 0.1
    author : secluis 
    telegram : secluis8
    """

    if len(sys.argv) != 2:
        print("Usage: python shellchecker.py listshell.txt")
        return

    list_shell_filename = sys.argv[1]

    try:
        with open(list_shell_filename, 'r') as file:
            list_shell = file.read().splitlines()
    except FileNotFoundError:
        print(f"File '{list_shell_filename}' not found.")
        return

    live_shells = []

    for shell in list_shell:
        if check_shell(shell):
            live_shells.append(shell)

    with open('live_shell_by_secluis.txt', 'w') as file:
        file.write(banner)
        file.write("\nLive Shells:\n")
        for live_shell in live_shells:
            file.write(live_shell + '\n')

if __name__ == "__main__":
    main()