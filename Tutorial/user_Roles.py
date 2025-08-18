user_Role = input("Are you an Admin? Please type (A) to confirm: ")
password = "1234"

access = "Admin" if user_Role == "A" else "Employee"

if access == "Admin":
    admin_Name = input("Please enter your name: ")
    print(f"Welcome, {admin_Name}. Your role is {access}")
    input_password = input(f"To continue, {admin_Name}. please input your admin password: ")

    if input_password == password:
        print("You now have full access. Congratulations.")
    
    else:
        print("Access Denied.")

else:
    employee_Name = input("Please enter your name: ")
    print(f"Welcome, {employee_Name}. Welcome to the company.")
