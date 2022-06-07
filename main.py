
from Resistor import Resistor
from TwoWayList import TwoWayList

print("------lab10-------\n")

resistor1 = Resistor("OMLT", 1000, 1, 5)
resistor2 = Resistor("KMLT3", 700, 0.5, 6)
resistor3 = Resistor("BMLT", 2000, 0.5, 1)
twoWayList = TwoWayList()
twoWayList.append(resistor1)
twoWayList.append(resistor2)
twoWayList.append(resistor3)
twoWayList.sortListByNom()

print("------ Sort by nominal ------\n")

twoWayList.show()

twoWayList.sortListByType()

print()
print("------ Sort by type ------\n")

twoWayList.show()

accuracy = int(input("Please, enter minimum accuracy: "))

twoWayList.showByAccuracy(accuracy)


# if __name__ == '__main__':
#     main()