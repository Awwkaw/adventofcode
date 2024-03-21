def find_marker(message, message_length):
    k = message_length
    while True:
        if len(i[k-message_length:k]) == len(set(i[k-message_length:k])):
            print(k)
            print(i[k-message_length:k])
            break
        k += 1


try:
    i = input()
except Exception:
    pass
find_marker(i, 4)
find_marker(i, 14)
