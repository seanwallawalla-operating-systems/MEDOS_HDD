in1 = str
print ("Command testing")
print ("Test the Calculator command")
print ("Type 'CALC' to try out the command!")
print ("Warning! Commands are CaSe SeNsItIvE")
in1 = str(input("FC:\\"))
if in1 == ("CALC"):
	print ("FC:\\")
	print ("|||Calculator|||[-][{}][X]|||")
	print ("|||||||||||||||||||||||||||||")
	print ("|##########################0|")
	print ("|||||||||||||||||||||||||||||")
	print ("| + | * | X | Y | - | / | % |")
	print ("|||||||||||||||||||||||||||||")
	print ("| $ | < | > | . | Z | ^ | B |")
	print ("|||||||||||||||||||||||||||||")
	print ("| 0 | 1 | 2 | 3 | 4 | 5 | ( |")
	print ("|||||||||||||||||||||||||||||")
	print ("| 6 | 7 | 8 | 9 | ) | K | M |")
	print ("|||||||||||||||||||||||||||||")
	print ("| C | T | _ | { | } | ! | \ |")
	print ("|||||||||||||||||||||||||||||")
	print ("|||||||||||||||||||||||||||||")
	print ("ERROR: Calculator does not function in COMMAND DEMO")
	print (in1)
testconfirm = int(input("Did the command info look right? type 1 to confirm, type anything else and/or press enter to quit "))
if testconfirm == 1:
    print ("Test successful!")
    print ("Shutting down, please wait")
else:
    print ("Shutting down")
   