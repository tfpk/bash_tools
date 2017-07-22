#!/usr/bin/python3
import argparse
import subprocess
import csv

COMMAND_FILE = "commands.csv"
HELP_FILE = "command_help.txt"
NOT_FOUND = "Couldn't execute command {key} - not found."

FUNCTION_HELP = open(HELP_FILE, 'r').read()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="The function you want to run.")
    arguments = parser.parse_args()

    functions = {}
    with open(COMMAND_FILE, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            functions[row[0]] = row[1]
    
    command = arguments.command
    
    if command.lower() in ["h", "help"]:
        print(FUNCTION_HELP)
        exit() 
    
    # list all commands that start with the input
    commands = sorted(filter(lambda arg:arg.startswith(command), functions))
    
    # prioritize uppercase commands
    if 64 < ord(command[0]) < 65 + 26:
        try:
            command = filter(lambda arg:64 < ord(arg[0]) < (65 + 26), commands)[0]
        except IndexError:
            print(NOT_FOUND.format(key=command))
            exit()
    elif commands:
        command=commands[0]
    else:
        print(NOT_FOUND.format(key=command))
        exit()

    subprocess.Popen(functions[command], shell=True)
