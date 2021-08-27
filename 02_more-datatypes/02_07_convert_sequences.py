# Convert some sequences you got to know into other sequences:
# - Convert the string shown below into a tuple.
# - Convert the tuple into a list.
# - Change the `c` character in your list into a `k`
# - Convert the list back into a tuple.

string = "codingnomads"
string = "codingnomads"
StringtoTuple = tuple(string)
print(StringtoTuple)
TupletoList = list(StringtoTuple)
print(TupletoList)
TupletoList[0] = "k"
print(TupletoList)
ListtoTuple = tuple(TupletoList)
print(ListtoTuple)
