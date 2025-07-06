# set has unique collection
letters = {'a','a','b','c'}
print(letters)
#mas mabilis mag hanap ng value si set compare kay 'in'
# "nathan" in collection --> using in

letters.add('k')
#random kung saan ilalagay na index
#kapag existing hindi mag eerror
print(letters)
letters.discard('a')
print(letters)

print("--------")
set1 ={'a','b','c','d'}
set2 ={'d','e','f'}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))


