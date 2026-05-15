def solution(number):
    if number < 0 : return 0
    number -=1
    multiple = []
    both = False
    while number >= 3 :
        if not number % 5 and not number % 3 and not both :
            multiple.append(number)
            number -=1
            both = True
            continue
        elif not number % 3 or not number % 5:
            multiple.append(number)
        number -=1    
    return sum(multiple) 
