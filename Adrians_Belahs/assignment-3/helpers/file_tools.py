def save_to_file(filename, text):
    with open(filename, "a") as f:
        f.write(text + "\n")

def read_file(filename):
    with open(filename, "r") as f:
        return f.read()