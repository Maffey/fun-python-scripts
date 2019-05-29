print("Configuring a single router on Cisco Packet Tracer. Simplified." + "\n"
+ "Basically answer all the questions and the program will prepare a script you have to type in the router to get desired configuration." + "\n" + 
"Make sure you are typing the data correctly. There's no error-catching as of yet." + "\n"
"Let's start!")

hostname = input("What's the name for the router?")
if (hostname == ""):
  hostname = "Router"

numberOfSubnets = int(input("How many local subnetworks are connected to the router?"))

# TODO: Make the numberOfSubnets input idiot-proof.
# Find a way to TRY to convert float into int, if not possible, throw an error.

while (numberOfSubnets <= 0):
  numberofSubnets = int(input("Type a correct number of local subnetworks."))
print("Number of subnets is " + str(numberOfSubnets))

# Change list to the dictionary, let the key name be a name of the port
interfacesDictionary = {}
for i in range(numberOfSubnets):
  interfaceIP = input("Type IP address of your " + str(i + 1) + " subnet: ")
  interfaceName = input("Type what interface will the subnet be assigned to: ")
  interfacesDictionary[interfaceName] = interfaceIP
  print("The IP address of your " + str(i + 1) + " subnet is: " + interfaceIP)
  print("The assigned interface: " + interfaceName)

# For future use, the number of end devices might be useful when you decide if your subnet is too small or too big. For now, scrap that up.
'''
for key, value in interfacesDictionary.items():
  numberOfEndDevices = input("How many end devices will be connected to the subnet " + str(value) + "?")
'''
defaultGateway = str(input("Do you want the router to have default ip as .254 in the subnets or you prefer custom ones? Type either 'default' or 'custom'."))
# Fix the logic statement here.
while (defaultGateway != "default" or defaultGateway != "custom"):
  defaultGateway = input("Wrong answer! Type either 'default' or 'custom'!")
print (defaultGateway)

