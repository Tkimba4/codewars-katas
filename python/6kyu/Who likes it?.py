"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
Note: For 4 or more names, the number in "and 2 others" simply increases.

StringsFundamentals
"""
def likes(n):
    l = len(n)
    if not l : return "no one likes this"
    elif l == 1: return f"{n[0]} likes this"
    elif l == 2 : return f"{n[0]} and {n[1]} like this"
    elif l == 3 : return f"{n[0]}, {n[1]} and {n[2]} like this"
    else : return f"{n[0]}, {n[1]} and {l-2} others like this"
