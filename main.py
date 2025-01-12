import sys

def main():
    # Проверяем, передано ли имя пользователя
    if len(sys.argv) > 1:
        name = sys.argv[1]
        print(f'Hello, {name}!')
    else:
        print('Hello from ChatGPT!')

if __name__ == "__main__":
    main()