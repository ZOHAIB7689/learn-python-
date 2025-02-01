while True:
    user_num =input("Enter Value between 1 to 10: ")
    user_num = int(user_num)
    if 1 <= user_num <= 10:
        print("Thanks")
        break
    else:
        print("Invalid input")