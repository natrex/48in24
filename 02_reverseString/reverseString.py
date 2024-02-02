#test_string = 'stressed'
#test_string = 'strops'
test_string = 'racecar'

def reverse(text):
    if len(text) == 0:
        return ""
    if len(text) == 1:
        return text[-1]
    return text[-1] + reverse(text[:-1])

print(reverse(test_string))