# mélange les lettres d'un mot

import numpy as np

mot_entree = list(input("Mot à mélanger stp ? "))

try:
    np.random.shuffle(mot_entree)
    print("".join(mot_entree))
except:
    print("Erreur")
