import random

peopleNames = ("Itai", "Eliya", "Orian", "Adiel", "Aharon")
verbs = ("sees", "knows", "buys", "owns", "keeps")
adjectives = ("big", "pretty", "low", "nice", "handsome")
adverbs = ("slowly", "tomorrow", "now", "soon","suddenly")
animatedObjects = ("flowers", "oranges", "leaves", "stones", "stars")
inanimateObjects = ("a stone", "a chair","a flower", "a flag","a tie")


    
def crpoem(n):
    def randsong():
        return ' '.join([random.choice(peopleNames)]+[random.choice(adverbs)]+[random.choice(verbs)]+[random.choice(adjectives)]+[random.choice(animatedObjects)])
    if n==0:
        return []
    return [(randsong())]+crpoem(n-1)


print(crpoem(5))
print(crpoem(5))
print(crpoem(5))
