#brute force solution
# TC : O(n log n)
s1 = "listen"
s2 = "silent"

def is_anagram(s1, s2):
    sorted_s1 = sorted(s1)
    print(sorted_s1)
    sorted_s2 = sorted(s2)
    print(sorted_s2)
    return sorted_s1 == sorted_s2


print(is_anagram(s1, s2))
# ['e' : 0, 'i' : 0 , 'l' : 0 , 'n': 0, 's': 0, 't': 0]
character_count = {}\
    # O(n) TC
def is_anagram_prime(s1, s2):
    if len(s1) != len(s2):
        return False
    print("Anagram prime")
    for char in s1 :
        if char in character_count:
            character_count[char] = character_count[char] + 1
        else:
            character_count[char] = 1
    for char in s2:
        if char in character_count:
            character_count[char] = character_count[char] - 1
        else:
            return False
    for count in character_count.values():
        if count != 0:
            return False
    return True

print(is_anagram_prime(s1, s2))