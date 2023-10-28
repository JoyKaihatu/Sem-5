import numpy as np
import pprint as pp
import pandas as pd

Comb1 = ["ya", "tidak"]
Comb2 = ["ya", "tidak"]
Comb3 = ["burung", "mamalia", "ikan","reptil","amfibi"]
Comb4 = ["omnivora", "herbivora", "karnivora"]

Comb1_len = len(Comb1)
Comb2_len = len(Comb2)
Comb3_len = len(Comb3)
Comb4_len = len(Comb4)

total_row = Comb1_len*Comb2_len*Comb3_len*Comb4_len

Final_Comb = []

Comb1_counter = 0
Comb2_counter = 0
Comb3_counter = 0
Comb4_counter = 0

for i in range(total_row):
    temporary = []

    temporary.append(Comb1[Comb1_counter])
    temporary.append(Comb2[Comb2_counter])
    temporary.append(Comb3[Comb3_counter])
    temporary.append(Comb4[Comb4_counter])
    Comb4_counter += 1


    if Comb4_counter > 2:
        Comb3_counter += 1
        Comb4_counter = 0

    if Comb3_counter > 4:
        Comb2_counter += 1
        Comb3_counter = 0

    if Comb2_counter > 1:
        Comb1_counter += 1
        Comb2_counter = 0

    if Comb1_counter > 1:
        Comb1_counter = 0

    Final_Comb.append(temporary.copy())

pp.pprint(Final_Comb)
np.savetxt("Final.txt", Final_Comb)
