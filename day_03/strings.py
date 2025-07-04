def semipalindromes(word):
    n=len(word)
    z=0
    for i in range(0,int(n/2)):
        if word[i:n-i-1:1].lower()== word[n-i-1:i:-1].lower():
            z+=1
            print(f"{z}: {word[i:n-i:1]} is a semipalindrome")
    if z == 0:
        print(f"{word} does not have any semipalindromes")

def main():
    word = input("Enter a word or quit: ")
    while word.lower() != 'quit':
        semipalindromes(word)
        word = input("Enter a word or quit: ")

main()