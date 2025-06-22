
def cat(fp):
    with open(fp, 'r') as file:
        file.seek(0)
        print(file.readline(1024))