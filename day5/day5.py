
def read_input():
    out = []
    with open('input.txt', 'r') as file:
        for line in file:
            stripped = file.readline().strip()
            out.append(stripped)
    return out

def main():
    print(read_input())

if __name__ == "__main__":
    main()

