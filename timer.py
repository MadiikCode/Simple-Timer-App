import time

def countdown(seconds):
    while seconds > 0:
        print(f"Осталось: {seconds} сек")
        time.sleep(1)
        seconds -= 1
    print("Время вышло!")

def main():
    try:
        user_input = int(input("Введите время в секундах: "))
        if user_input <= 0:
            print("Введите положительное число.")
        else:
            countdown(user_input)
    except ValueError:
        print("Пожалуйста, введите целое число.")

if __name__ == "__main__":
    main()
