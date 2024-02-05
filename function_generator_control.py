
import usbtmc
from time import sleep


CO2FG = usbtmc.Instrument("USB0::0x1AB1::0x0642::DG1ZA232903571::INSTR")
sleep(1)
WaterFG = usbtmc.Instrument("USB0::0x1AB1::0x0642::DG1ZA233304176::INSTR")


while 1:
    print("Ensure Function Generators are currently on")
    print("Choose from the options below")
    print("1: change output status")
    print("2: load output file\n")
    controlchoice = None
    while controlchoice==None:
        controlchoice = int(input())

    if controlchoice==1:
        print("Which FG would you like to change?")
        print("1: CO2")
        print("2: Water\n")
        FGChoice = None
        while FGChoice == None:
            FGChoice = int(input())

        if FGChoice==1:
            print("Which Channel would you like to change?")
            print("1: Pulse Function / Slow scan")
            print("2: Fast scan\n")
            ChannelChoice = None
            while ChannelChoice == None:
                ChannelChoice = int(input())
            print("Turn on or off? (0 or 1)")
            print("0: 0ff")
            print("1: On \n")
            ControlChoice = None
            while ControlChoice == None:
                ControlChoice = int(input())
            CO2FG.write(":OUTP" + str(ChannelChoice) + " " + str(ControlChoice))


        elif FGChoice==2:
            print("Which Channel would you like to change?")
            print("1: Pulse Function / Slow scan")
            print("2: Fast scan\n")
            ChannelChoice = None
            while ChannelChoice == None:
                ChannelChoice = int(input())
            print("Turn on or off? (0 or 1)")
            print("0: 0ff")
            print("1: On \n")
            ControlChoice = None
            while ControlChoice == None:
                ControlChoice = int(input())
            WaterFG.write(":OUTP" + str(ChannelChoice) + " " + str(ControlChoice))

    if controlchoice==2:
        print("Which FG would you like to load a file of?")
        print("1: CO2")
        print("2: Water\n")
        FGChoice = None
        while FGChoice == None:
            FGChoice = int(input())

        if FGChoice == 1:
            CO2FG.write(":OUTP1 0")
            CO2FG.write(":OUTP2 0")
            print("Pick which one you would like to load:")
            print("1: Pulse Function")
            print("2: WMS 1 ")
            print("Possibly add more WMS F's here later")
            filechoice = None
            while filechoice==None:
                filechoice = int(input())
            sleep(1)
            if filechoice == 1:
                CO2FG.write("*RCL USER1")
                sleep(1)
            elif filechoice == 2:
                CO2FG.write("*RCL USER2")
                sleep(1)
            else:
                print("\nTHAT FILE DOES NOT EXIST\n")
                sleep(4)



        elif FGChoice == 2:
            WaterFG.write(":OUTP1 0")
            print("Pick which one you would like to load:")
            print("1: Saved Water Function")
            filechoice = None
            while filechoice==None:
                filechoice = int(input())
            sleep(1)
            if filechoice==1:
                WaterFG.write("*RCL USER1")
                sleep(1)
            else:
                print("\nERROR (Water only has one file dummy\n")
                sleep(4)

