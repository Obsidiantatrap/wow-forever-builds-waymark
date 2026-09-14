"""Zones: level bands for the classic route, in order."""

ZONES = [
    ("Elwynn Forest", 1, 10),
    ("Westfall", 10, 18),
    ("Redridge Mountains", 18, 24),
    ("Duskwood", 24, 30),
    ("Stranglethorn Vale", 30, 38),
    ("Badlands", 38, 45),
    ("Searing Gorge", 45, 50),
    ("Un'Goro Crater", 50, 55),
    ("Western Plaguelands", 55, 60),
]


def zone_for_level(level):
    for name, lo, hi in ZONES:
        if lo <= level <= hi:
            return name
    return ZONES[-1][0]
