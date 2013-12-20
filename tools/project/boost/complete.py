"""
convert the simulation time to real time.
"""

import os
#import argparse

<<<<<<< HEAD
def get_sim_time(n = 66):

    flag = 0

=======
def get_sim_time(n, args):
     
    
>>>>>>> 7cbb0b6e8df1b1608e2e80109294c84099813f67
    f = open("water.mol", "r")

    counter = 0
    for i in f :
        if "step" in i:
             step = int(i.strip().split()[0][4:])
<<<<<<< HEAD
             if counter == 0:
                 start = step
             counter += 1
        if "C3H6O3" in i:
            tokens = i.strip().split()
            nwater = int(tokens[0])
            if nwater <= n:
                flag = 1
                break

=======
        if 0:
            tokens = i.strip().split()
            if len(tokens) > 2:
                if "H2" == tokens[2]:
                    tokens = i.strip().split()
                    nh2 = int(tokens[0])
                    if nh2 <= n:
                        break
        if 1:
            if "H2O1" in i:
                tokens = i.strip().split()
                nwater = int(tokens[0])
                if nwater >= n:
                    break
>>>>>>> 7cbb0b6e8df1b1608e2e80109294c84099813f67
    f.close()

    if flag:
        return step, start
    else:
        print "Warning: not finish half reaction!"
        print "Only %d molecules have reacted"%nwater
        return 0, 0

def get_real_time(nstep, args):
    
    if not os.path.exists("water.bboost"):
        realtime = nstep
    else:
        counter = 0
        realtime = 0.0
        f = open("water.bboost", "r")
        for i in f:
            if counter > 0:
                tokens = i.strip().split()
                step = int(tokens[0])
                if step >= nstep:
                    break
                realtime += float(tokens[7])
            counter += 1
        f.close()
    return realtime

<<<<<<< HEAD
def get_half_time():
    nstep, start = get_sim_time(16)
    realtime = get_real_time(nstep)
    print nstep - start, realtime

def main():
    #parser = argparse.ArgumentParser()
    #parser.add_argument("fname", default="geo", nargs="?", help="geo file name")
    #parser.add_argument("-c", action="store_true", help="convert the file to other formats (geo, xyz, gjf, lammps)")
    #parser.add_argument("-pbc", action="store_true", help="using default pbc 5nm * 5nm * 5nm")
    #parser.add_argument("-b", nargs=2, type=int, help="get the bond distance between a1, a2, a3")
    #parser.add_argument("-a", nargs=3, type=int,help="get the angle of a1-a2-a3")
    #parser.add_argument("-vol", action="store_true", help="get the volume of the simulation box")
    #args = parser.parse_args()
    get_half_time()
=======
def get_half_time(args):
    nstep = get_sim_time(33, args)
    realtime = get_real_time(nstep, args)
    print nstep, realtime

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fname", default="geo", nargs="?", help="geo file name")
    parser.add_argument("-c", action="store_true", help="convert the file to other formats (geo, xyz, gjf, lammps)")
    parser.add_argument("-pbc", action="store_true", help="using default pbc 5nm * 5nm * 5nm")
    parser.add_argument("-b", nargs=2, type=int, help="get the bond distance between a1, a2, a3")
    parser.add_argument("-a", nargs=3, type=int,help="get the angle of a1-a2-a3")
    parser.add_argument("-vol", action="store_true", help="get the volume of the simulation box")
    args = parser.parse_args()
    get_half_time(args)
>>>>>>> 7cbb0b6e8df1b1608e2e80109294c84099813f67

if __name__ == "__main__":
    main()
