"""Dump file
"""
import os
from mytype import System, Atom
from utilities import v2lattice

class Dump():
    def __init__(self, dumpfile):
        self.name = ""
        self.natom = 0
        self.a = []
        self.b = []
        self.c = []
        self.coords = []
        self.read(dumpfile)
    def read(self, dumpfile):
        """ read lammps dump file
        """
        f = open(dumpfile, 'r')
        f.readline()
        self.name = f.readline().strip()
        f.readline()
        self.natom = int(f.readline())
        f.readline()
        self.a = f.readline().strip().split()
        self.b = f.readline().strip().split()
        self.c = f.readline().strip().split()
        f.readline()
        # sort the data
        temp = []
        for i in range(self.natom):
            tokens = f.readline().strip().split()
            a = "%06d"%(int(tokens[0]))
            temp.append([a, tokens])
        temp.sort()
        for i in temp:
            self.coords.append(i[1])
    def parseInp(self, ):
        n2mol = {}
        f = open("inp", "r")
        for i in f:
            tokens = i.strip().split()
            if len(tokens) == 2:
                n2mol[int(tokens[0])] = tokens[1]
        return n2mol

    def parser(self,):
        """ parse dump file into System
        """
        s = System()
        s.name = self.name

        # transform a, b, c to [xx, xy, yz]
        # [yx, yy, yz] and [zx, zy, zz]
        # caution! A hard coded code for specified dump file
        a = []
        # some dump file only have xl and xh. Normalize to three terms
        if len(self.a) == 2:
            self.a.append(0.0)
        if len(self.b) == 2:
            self.b.append(0.0)
        if len(self.c) == 2:
            self.c.append(0.0)
        #a.append(float(self.a[1]) - float(self.a[0]))
        #@ref: http://lammps.sandia.gov/doc/Section_howto.html#howto_12
        xlo = float(self.a[0]) - min(0.0, float(self.a[2]), float(self.b[2]),\
              float(self.a[2]) + float(self.c[2])) 
        xhi = float(self.a[1]) - max(0.0, float(self.a[2]), float(self.b[2]),\
              float(self.a[2]) + float(self.c[2]))
        a.append(xhi - xlo)
        a.append(0.0)
        a.append(0.0)
        #print a
        b = []
        b.append(float(self.a[2]))
        ylo = float(self.b[0]) - min(0.0, float(self.c[2]))
        yhi = float(self.b[1]) - max(0.0, float(self.c[2]))
        b.append(yhi - ylo)
        b.append(0.0)
        #print b
        c = []
        c.append(float(self.b[2]))
        c.append(float(self.c[2]))
        c.append(float(self.c[1]) - float(self.c[0]))
        s.pbc = v2lattice(a, b, c)
        #print c
        # begin to parse atoms
        flag = 0
        if os.path.exists("inp"):
            flag = 1
            n2a = self.parseInp()
        counter = 0
        for i in self.coords:
            atom = Atom()
            if flag:
                atom.name = n2a[int(i[1])]
            else:
                atom.name = i[1]
            """
            atom.x[0] = float(i[3])
            atom.x[1] = float(i[4])
            atom.x[2] = float(i[5])
            """
            atom.an = counter + 1
            atom.x[0] = float(i[2])
            atom.x[1] = float(i[3])
            atom.x[2] = float(i[4])
            s.atoms.append(atom)
            counter += 1
        return s

