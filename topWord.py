from tkinter.constants import S

def replace(text):
    str = ""
    for i in range(len(text)):
        c = text[i]
        if (c < 'A' or (c > 'Z' and c < 'a') or c > 'z'):
            c = ' '
        str += c
        i += 1
    return str

def count_freq(text):
    frequency = {}
    for word in text.split():
        if word not in frequency:
            frequency[word] = 1
        else:
            frequency[word] += 1
    return frequency

def sort(frequency):
    a = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    a = a[:30]
    print(a)

if "__main__" == __name__:
    text = "Story of a man who has unnatural feelings for a pig. Starts out with a opening scene that is a terrific example of absurd comedy. A formal orchestra audience is turned into an insane, violent mob by the crazy chantings of it's singers. Unfortunately it stays absurd the WHOLE time with no general narrative eventually making it just too off putting. Even those from the era should be turned off. The cryptic dialogue would make Shakespeare seem easy to a third grader. On a technical level it's better than you might think with some good cinematography by future great Vilmos Zsigmond. Future stars Sally Kirkland and Frederic Forrest can be seen briefly."
    text = replace(text)
    frequency = count_freq(text)
    sort(frequency)

