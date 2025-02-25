def get_count(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in s if char in vowels)