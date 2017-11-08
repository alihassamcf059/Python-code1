# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 17:50:18 2017

@author: ali-hassam
"""

import random

class food(object):
    def __init__(self, n, v, w):
        self.name=n
        self.value=v
        self.calories=w
        
    def getvalue(self):
        return self.value
    
    def getname(self):
        return self.name
        
    def getcost(self):
        return self.calories
    
    def density(self):
        return self.getvalue()/self.getcost()
        
    def __str__(self):
        return self.name+ ':<' + str(self.value) +',' +str(self.calories)+'>'

def buildmenue(names, values, calories):
        menu=[]
        for i in range (len(values)):
            menu.append(food(names[i],values[i],calories[i]))
        return menu

def greedy(items, maxcost, keyfunction, rev):
        itemscopy=sorted(items, key=keyfunction, reverse=rev)
        result=[]
        total_value, total_cost=0.0, 0.0
        for i in range(len(itemscopy)):
            if (total_cost+itemscopy[i].getcost() <= maxcost):
                result.append(itemscopy[i])
                total_cost += itemscopy[i].getcost()
                total_value += itemscopy[i].getvalue()
        return (result, total_value)
        
def testgreedy(items, constrain, keyfunction, rev):
        [taken, val] = greedy(items, constrain, keyfunction, rev)
        print('Total value of items taken is: ', val)
        for i in taken:
            print(i);

def testgreedys(foods,maxunit):
       print('use greedy by value to allocate', maxunit, 'of calories')
       #print(food.getvalue)
       testgreedy(foods, maxunit, food.getvalue, True)
       print('\n use greedy by cost to allocate', maxunit, 'of calories')
       testgreedy(foods, maxunit, food.getcost, False)
       print('\n use greedy by density to allocate', maxunit, 'of calories')
       testgreedy(foods, maxunit, food.density, True)

def maxVal(consider, avail):
    if consider==[] or avail==0:
        result=(0,())
    elif consider[0].getcost() > avail:
        result=maxVal(consider[1:],avail)
    else:
        nextItem=consider[0]
        [val, take]=maxVal(consider[1:],avail-nextItem.getcost())
        val+=nextItem.getvalue();
        [notval, notake]=maxVal(consider[1:], avail) 
        if val>notval:
            result=(val, take+(nextItem,))
        else:
            result=(notval, notake)
    return result

def testMaxVal(food_in, maxUnits, printItems = True):
    print('Use search tree to allocate', maxUnits,
          'calories')
    val, taken = maxVal(food_in, maxUnits)
    print('Total value of items taken =', val)
    if printItems:
        for item in taken:
            print('   ', item)
def buildLargemenu(numitems, maxval, maxcost):
    items=[]
    for i in range(numitems):
        items.append(food(str(i), random.randint(1,maxval),random.randint(1,maxcost)))
    return items
#for numItems in (5, 10, 15, 20, 25, 30, 35, 40, 45):
#    print('Try a menu with', numItems, 'items')
#    items = buildLargemenu(numItems, 90, 250)
#    testMaxVal(items, 750, False)  


names = ['biryani', 'korma', 'pizza', 'burger', 'fries', 'cola', 'apple', 'donut', 'cake']
values = [89,90,95,100,90,79,50,10]
calories = [123,154,258,354,365,150,95,195]
foods = buildmenue(names, values, calories)
testMaxVal(foods,900)
print('')
testMaxVal(foods, 750)