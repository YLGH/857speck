B = 512
r = 4

import math
def distinguish(ctxt_blocks):
    N = 256
    R = [0]*(N)
    for c in ctxt_blocks:
        for g in c:
            R[ord(g)] += 1

    expected = N-1
    std_dev = math.sqrt(2*expected)

    chi2 = 0
    for r in R:
        ei = B/16
        chi2 +=((ei-r)**2)/ei
     
    if math.fabs(chi2 - expected) > 3*std_dev:
        return False
    return True
    
    return 1
