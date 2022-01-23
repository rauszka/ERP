import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):

    name = []
    for i in range(number_of_small_letters):
        name.append(random.choice(string.ascii_lowercase))
    for i in range(number_of_capital_letters):
        name.append(random.choice(string.ascii_uppercase))
    for i in range(number_of_digits):
        name.append(str(random.randint(0,9)))
    for i in range(number_of_special_chars):
        name.append(random.choice(allowed_special_chars))
    
    id = random.sample(name, len(name))
    return ''.join(id)


def generate_quote():
    quotes = ["D-J-A-N-G-O. The D is silent.", "There's a passage I got memorized. Ezekiel 25:17...", "When You Get To Hell, John, Tell Them Daisy Sent You.", "Are you gonna bark all day, li'l doggie, or are you gonna bite?", "I Need Me Eight Soldiers. Eight Jewish-American Soldiers.", "AK-47. The very best there is. When you absolutely, positively got to kill every motherf***** in the room, accept no substitutes.", "Do you find me sadistic? You know, I'll bet I could fry an egg on your head right now if I wanted to.",
    "Say 'what' again. Say 'what' again, I dare you, I double dare you motherf*****, say what one more Goddamn time!", "I'm gonna give you a little somethin' you can't take off.", "That's a pretty f*cking good milkshake. I don't know if it's worth five dollars but it's pretty f*cking good.", "I hid this uncomfortable piece of metal up my a** for two years. Then, after seven years, I was sent home to my family. And now, little man, I give the watch to you.", "You probably heard we ain't in the prisoner-takin' business; we in the killin' Nazi business. And cousin, business is a-boomin.", "You only need to hang mean bastards, but mean bastards you need to hang.", "A good cop will never let you know he knows you're full of shit.", "If you shoot me in a dream you better wake up and apologize.", "I'm Winston Wolf. I Solve Problems." ]
    quote = random.choice(quotes)
    return quote