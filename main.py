# https://github/baptisteCanac
import random

characters = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'j',
"J", 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u',
'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# 7 characters for the password
randomLetter1 = random.randint(0, len(characters)-1)
randomLetter2 = random.randint(0, len(characters)-1)
randomLetter3 = random.randint(0, len(characters)-1)
randomLetter4 = random.randint(0, len(characters)-1)
randomLetter5 = random.randint(0, len(characters)-1)
randomLetter6 = random.randint(0, len(characters)-1)
randomLetter7 = random.randint(0, len(characters)-1)

allPassword = characters[randomLetter1] + characters[randomLetter2] + characters[randomLetter3] + characters[randomLetter4] + characters[randomLetter5] + characters[randomLetter6] + characters[randomLetter7]

print(allPassword)
