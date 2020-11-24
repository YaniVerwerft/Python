with open('Files Chapter 7/irish_song.txt') as file:
    line = file.readline().rstrip()
    shortest = len(line)
    sentence = line
    while line:
        if len(line) < shortest:
            shortest = len(line)
            sentence = line
        line = file.readline().rstrip()

    print('The shortest line has', shortest, 'characters')
    print(sentence)