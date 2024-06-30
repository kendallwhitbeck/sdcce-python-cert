# Iterators
my_string = "hello"

# Iterating backwards using negative indexing
for i in range(len(my_string) - 1, -1, -1):
    print(my_string[i])

# Iterating backwards using reversed function
print(reversed(my_string))
for i in reversed(my_string):
    print(i)

# Iterate using range
for i in range(20, 100, 10):
    print(i)

# using `pass` in a for loop
letter = "Hizthere,zThisziszhowzazpasszstatementzworks!"
for i in letter:
    if i == "mn":
        pass
    elif i == "z":
        print(" ",end="")
    else:
        print(i, end="")


# Truncate the cell data if longer than char_lim characters.
rows = [
    ['Action/Sci-fi', 'Star Wars: Episode III - Revenge of the Sith', 'George Lucas', '2005', 'It has been three years since the Clone Wars began. Jedi Master Obi-Wan Kenobi (Ewan McGregor) and Jedi Knight Anakin Skywalker (Hayden Christensen) rescue Chancellor Palpatine (Ian McDiarmid) from General Grievous, the commander of the droid armies, but Grievous escapes. Suspicions are raised within the Jedi Council concerning Chancellor Palpatine, with whom Anakin has formed a bond. Asked to spy on the chancellor, and full of bitterness toward the Jedi Council, Anakin embraces the Dark Side.'],
    ['Action/Sci-fi', 'Thor: Ragnarok', 'Taika Waititi', '2017', "Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial contest that pits him against the Hulk, his former ally and fellow Avenger. Thor's quest for survival leads him in a race against time to prevent the all-powerful Hela from destroying his home world and the Asgardian civilization."],
    ['Family/Fantasy', 'Harry Potter and the Half-Blood Prince', 'David Yates', '2009', 'As Death Eaters wreak havoc in both Muggle and Wizard worlds, Hogwarts is no longer a safe haven for students. Though Harry (Daniel Radcliffe) suspects there are new dangers lurking within the castle walls, Dumbledore is more intent than ever on preparing the young wizard for the final battle with Voldemort. Meanwhile, teenage hormones run rampant through Hogwarts, presenting a different sort of danger. Love may be in the air, but tragedy looms, and Hogwarts may never be the same again.']
]
char_lim = 44
for row in rows:
    for col, cell in enumerate(row):
        if len(str(cell)) > char_lim:
            row[col] = str(cell)[:char_lim] + "..."


