def hash_mark_no_m_check(str_list):
    print(f"Hash marks & no 'm' check: ")
    for string in str_list:
        if '#' in string and not string.startswith('m'):
            print(string, "contains hash mark and does not start with m")

def common_char_check(str_list):
    print(f"Common character check:")
    common_chars = set(str_list[0])
    for string in str_list[1:]:
        common_chars.intersection_update(set(string))
    for char in common_chars:
        print(f"Character {char} appears in all items")
        for string in str_list:
            count = string.count(char)
            print(f"{string} contains {count} {char}")

# Test the functions with the given input list
input_list = ["boby#", "borya#n", "#mallibons#", "morbs", "mobking#", "bunst#or"]
hash_mark_no_m_check(input_list)
print()
common_char_check(input_list)
