a={
'X' : ('XX     XX','  X   X  ','   X X   ','    X    ','   X X   ','  X   X  ','XX     XX'),
'S' : ('  SSSSSS ',' S      S','S        ',' SSSSSSS ','        S','S      S ',' SSSSSSS '),
}
name = raw_input('please enter dg: ').upper()
for i in range(0,7):
    for o in name:
	    print a[o][i],
    print ''