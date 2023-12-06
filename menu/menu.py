class menu():
    def __init__(self):
        self.menu = True
        self.menu_loop()

    def menu_loop(self):
        while self.menu:
            print("\n***************")
            print("1. 写入数据")
            print("2. 修改数据")
            print("3. Exit")
            print("***************\n")
            choice = input("Enter your choice: ")
            if choice == "1":
                self.write_menu()
            elif choice == "2":
                self.re_menu()
            elif choice == "3"or choice == "exit":
                self.exit()
            else:
                print("Invalid choice")

    def write_menu(self):
        print("写入菜单")
        write_menu = True
        while write_menu:
            print("\n***************\n退出请在下方输入exit\n")
            date = input("请输入姓名，编号或exit\n")
            if date == "exit":
                write_menu = False
            else:
                print("这里还没写好")

    def re_menu(self):
        print("修改菜单")
        re_menu = True
        while re_menu:
            print("\n***************\n退出请在下方输入exit\n")
            date = input("请输入姓名，编号或exit\n")
            if date == "exit":
                re_menu = False
            else:
                print("这里还没写好")

    def exit(self):
        print("Exit")
        self.menu = False