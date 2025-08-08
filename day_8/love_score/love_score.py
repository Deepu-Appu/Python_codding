def calculate_love_score(name1, name2):
    letter = { 't':0,'r':0,'u':0,'e':0,'l':0,'o':0,'v':0,'e':0}
    combined_name = name1+name2 
    new_combined_name = combined_name.lower()
    for char in new_combined_name:
        for l in letter.keys():
            if l == char:
                letter[l] += 1

    first = ['t','r','u','e']
    second = ['l','o','v','e']
    
    total1 = 0
    total2 = 0

    for k in letter.keys():
        if k in first:
            total1 += letter[k]
        if k in second:
            total2 += letter[k]
    
    Grand_total = str(total1) + str(total2)
    print(Grand_total)
        
calculate_love_score('kanye West','Kim Kardashian')