gen=[]
gen2=[]

def user_word(u):
    with open("genshin.txt") as f:
        for line in f:
            gen.append(line.strip())
    if u in gen:
        print("Yes")
