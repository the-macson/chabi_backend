def f(mainstream, must_watch):
    common = list(set(mainstream) & set(must_watch))
    uncommon = list(set(mainstream) ^ set(must_watch))
    return common, uncommon


Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack On Titan"]

print(f(Mainstream, must_watch))