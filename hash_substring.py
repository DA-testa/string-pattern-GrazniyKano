# python3

def read_input():
    # this function needs to acquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern

    # return both lines in one return

    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurrences using Rabin-Karp algorithm

    # Initialize variables
    p = len(pattern) # length of pattern
    t = len(text) # length of text
    prime = 101 # a prime number for hashing
    p_hash = 0 # hash value of pattern
    t_hash = 0 # hash value of text
    power = 1 # prime^(p-1)

    # Calculate hash value of pattern and the first window of text
    for i in range(p):
        p_hash = (p_hash + ord(pattern[i]) * power) % prime
        t_hash = (t_hash + ord(text[i]) * power) % prime
        if i != p-1:
            power = (power * prime) % prime

    # Find the matches
    matches = []
    for i in range(t - p + 1):
        if p_hash == t_hash and pattern == text[i:i+p]:
            matches.append(i)
        if i < t - p:
            t_hash = (t_hash - ord(text[i]) * power) % prime
            t_hash = (t_hash * prime + ord(text[i+p])) % prime

    return matches

# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

