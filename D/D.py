def determine_county_name(n, m, city_names):
    final_name = []
    for i in range(m):
        letter_count = {}
        for name in city_names:
            letter = name[i]
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        max_count = max(letter_count.values())
        best_letters = [letter for letter, count in letter_count.items() if count == max_count]
        final_name.append(min(best_letters))
    return ''.join(final_name)

n = 3  
m = 5  
city_names = ["apple", "maple", "alpha"] 

new_county_name = determine_county_name(n, m, city_names)
print("The new county name is:", new_county_name)
