# import subprocess


# def execute_command(command):
#     subprocess.call(command, shell=True)


# def main():
#     user_input = input("Enter a command to execute: ")
#     execute_command(user_input)


# if __name__ == "__main__":
#     main()

import subprocess

def execute_command(command):
    subprocess.run(command.split())


def main():
    user_input = input("Enter a command to execute: ")
    execute_command(user_input)


if __name__ == "__main__":
    main()