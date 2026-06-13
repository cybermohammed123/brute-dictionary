#WE ARE GONNA IMPORT 1 IMPORT FOR THIS TOOL AND THAT IST PRODUCT FROM ITERTOOLS

from itertools import product
def variants(word):
    #HERE WE ARE GONNA RETURN THA MAIN IDEA FROM THIS TOOL WHICH IS RETURN THE SAME WORD IN A DIFFERENT FORMS
    #ONE WITH THE REGULAR WORD THE OTHER WITH ONLY THE FIRST LETTER CAPITALIZE AND THE LAST WITH THE WHOLE WORD AS UPPER
    return [word, word.capitalize(), word.upper()]
#HERE IS THE IMPORTANT PART CHOOSE THE NAME AND THE ROLE AND THE SEPRATE 
#THE NAME IS GONNA BE THE PART IN EVERY RESULT WIT ALL THE ROLES DEPENDING ON HOW MANY WORDS YOU PUT IN THE ROLE SECTION WHICH IS IN THIS CEASE TWO
#ALSO THE SEPRATE IS IT UNDERSCORE OR NO SEPERATE WHICH IS THE ONLY TWO OPTIONS IN PASSWORD CREATION
names = ['mohammed']
role = ('administrator', 'admin')
seprate = ("", "_")
#CREATE A FILE NAME AND PUT THE MODE ON W FOR WRITE
with open('list.txt', 'w',) as f:
    #FOR LOOP INSIDE A FOR LOOP
    for n, r, sep in product(names, role, seprate):
        for nv, rv in product(variants(n), variants(r)):
            print(f"{nv}{sep}{rv}\n")
            #AND HERE YOU HAVE IT
            f.write(f"{nv}{sep}{rv}\n")

