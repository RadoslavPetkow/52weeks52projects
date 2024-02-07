def decode(message_file):
    with open(message_file, "r") as f:
        lines = f.readlines()

    message_words = []

    for x in range(100):
        message_words.append('')

    for line in lines:
        number = int(line.split()[0])

        for x in range(100):
            if number == (int((x * x + x) / 2)):
                message_words[x] = line.split()[1]
                break

    text = ""

    for x in message_words:
        if x != '':
            text = text + x + " "

    return text


file_path = "text.txt"
decoded_message = decode(file_path)
print(decoded_message)
