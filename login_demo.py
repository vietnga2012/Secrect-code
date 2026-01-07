# You have to install colorama first before editing (pip3 install colorama)
import webbrowser
from colorama import Fore, init


def information():  # Định nghĩa cụm input
    user = input(Fore.CYAN + "Username:").strip()
    input(Fore.MAGENTA + "Password:")
    return user


init(autoreset=True)


text1 = "Please note that this just a demo version, bugs and error may contain in software"
width = 120

print(f"{text1:^{width}}\n")    # Căn giữa cho lệnh print


while True:             # Vòng lặp lựa chọn (demo)
    print(Fore.YELLOW +
          "Please choose a choice, L: login , R: Register, E: exit, D: Dev Mode")
    command = input("---TomCoding System---" + ">>>").strip()

    if command.lower() in ["l", "login"]:   # Hiển thị login UI
        username = information()
        print("Login Successful!")
        print("----------------------------------")
        print(
            f"{Fore.GREEN}Welcome {Fore.WHITE}{username}{Fore.GREEN}!")
        continue
    elif command.lower() in ["r", "register"]:  # Hiển thị register UI
        print(Fore.YELLOW + "Register New Account\n")
        print("This feature will coming soon...")
        continue

    elif command.lower() in ["e", "exit"]:  # Thoát chương trình
        print(Fore.GREEN + Fore.LIGHTGREEN_EX + "Exiting System.....")
        break
    elif command.lower() == "d":
        x = input(
            "Are you sure? this feature is not for normal user, please use it as caution! Y/n:")
        if x.lower() == "y":
            print(Fore.RED + "Entering Dev Mode.....")
            admin_user = input("Admin_Username:")
            admin_password = input("Admin_Password:")

            if admin_user == "admin" and admin_password == "admin123":
                print("Login Successful, welcome admin!\n")
                permission = input(
                    "You're accessing to dev permission, are you sure and want to continue? Y/n:")
                if permission.lower() == "y":
                    print(
                        Fore.LIGHTGREEN_EX + "https://github.com/vietnga2012/My-journey-to-learn-python\n")
                    print(Fore.YELLOW + "Opening Browser.....Please wait\n")
                    webbrowser.open(
                        url="https://github.com/vietnga2012/My-journey-to-learn-python")
            else:
                print(Fore.RED + "Hey, Are you kidding me? READ THE WARNING!!!")
                break
        else:
            print(Fore.LIGHTYELLOW_EX + "Exiting Dev Mode.....")
            break
    if not command:
        continue
