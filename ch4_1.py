def search4vowels(phrase: str)  -> set:
    """Return the set of vowels found in 'phase'"""
    return set('aeiou').intersection(set(phrase))

print(search4vowels("ajkshdgfieoukjashdfgkjashdfasdf"))

def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Return the set of 'letters' found in 'phrase'."""
    return set(letters).intersection(set(phrase))

print(search4letters("qwieruqyweruiyasdfjkshadfjkahzxnbcvzx"))
