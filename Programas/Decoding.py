from sys import stdin


def decoding(decoded_total):
    message = stdin.readline().strip()
    while message != '':
        words = message.split()
        decoded = ""
        cont = 0
        for i in range(len(words)):
            if cont < len(words[i]):
                decoded += words[i][cont]
                cont += 1
        decoded_total += decoded + "\n"
        message = stdin.readline().strip()
    return decoded_total


def main():
    cases = int(stdin.readline().strip())
    space = stdin.readline().strip()
    for i in range(1, cases + 1):
        decoded_total = "Case #" + str(i) + ":\n"
        print(decoding(decoded_total))


main()
