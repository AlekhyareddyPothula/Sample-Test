
def execute_user_command(user_input):
    # Intentionally vulnerable: OS command injection
    command = "ping -c 1 " + user_input
    subprocess.call(command, shell=True)


def delete_file(user_input):
    # Intentionally vulnerable: command injection
    os.system("rm -f " + user_input)


def main():
    user_input = input("Enter host: ")

    execute_user_command(user_input)
    delete_file(user_input)
