from assignment1 import *
import vector
import orchestra

__author__ = 'bruno'

original = '12lb2323232323lah'
original1 = 'a3tx2z'
original2 = '12x'
test = 'bbbbbbbbb'
new = blowup(original)

print(original, new )

maxV = assignment1.maxRun(test)
maxV2 = assignment1.maxRun(original)

if maxV == len(test):
    print "maxrun correct"
print maxV, test
print maxV2, original

v = vector.Vector(0.0,2.0)
v2 = v.scalarMultiple(2)
v3 = v2.vectorSum(v)

print v3.getx()

print v3.toString()
print v2.toString()
print v3.magnitude()

myString = 'bl2'
if myString[1].isdigit():
    print "is a digit baby"

cello = orchestra.Cello("nylon")
violin = orchestra.Violin("steel")#internet claims this is a thing
clarinet = orchestra.Clarinet_BFlat(4)#given in inches.. i am guessing

