# serial_interface.py must be in the same directory as example_script.py
import os
print(os.getcwd())

import csv
from serial_interface import arroyo
from time import sleep
from matplotlib import pyplot as plt
from datetime import datetime, timedelta

co2_set_temp=15
co2_set_current=5

w2475_set_temp=15
w2475_set_current=5

w2485_set_temp=15
w2485_set_current=5

timestep=0.001

while 1:
    print("Please choose from below and press enter")
    print("1: Setup Laser Controllers")
    print("2: Bring lasers to preset conditions")
    print("3: Change Laser TEC Settings")
    print("4: Change Laser Current Settings")
    print("5: Shutdown Laser Current Output")
    print("6: Shutdown Laser TECs")
    print("7: Query TEC values")
    print("8: Shutdown TEC MANUALLY (ONLY USE IF SURE)")
    print("9: EMERGENCY CURRENT SHUTDOWN")
    controlchoice = None
    while controlchoice==None:
        controlchoice = int(input())

    if controlchoice==1: #start up lasers
        print("Choose comport with CO2 laser: (serial number 231024156)")
        CO2 = arroyo()
        CO2.set_mode("T")
        CO2.set_heatcool("BOTH")
        initial_co2_temp=CO2.read_temp()
        CO2.set_temp(CO2.read_temp())
        sleep(1)
        if CO2.read_output()!=1:
            CO2.set_output(1)

        print("Choose comport with 2485 laser: (serial number 230723689)")
        W2485 = arroyo()
        W2485.set_mode("T")
        W2485.set_heatcool("BOTH")
        initial_w2485_temp=W2485.read_temp()
        W2485.set_temp(W2485.read_temp())
        sleep(1)
        if W2485.read_output()!=1:
            W2485.set_output(1)

        
        print("Choose comport with 2475 laser: (serial number 230823930)")
        W2475 = arroyo()
        W2475.set_mode("T")
        W2475.set_heatcool("BOTH")
        initial_w2475_temp=W2475.read_temp()
        W2475.set_temp(W2475.read_temp())
        sleep(1)
        if W2475.read_output()!=1:
            W2475.set_output(1)


# 2 - set lasers to presets
    elif controlchoice==2:
        print("The CO2 TEC temp will now set to: ", co2_set_temp)
        if (CO2.read_temp() < co2_set_temp):
            while CO2.read_temp() < co2_set_temp:
                CO2.set_temp(CO2.read_temp() + 0.01)
                #sleep(timestep)

        elif CO2.read_temp() > co2_set_temp:
            while CO2.read_temp() > co2_set_temp:
                CO2.set_temp(CO2.read_temp() - 0.01)
                #sleep(timestep)

        elif (CO2.read_temp() - co2_set_temp) == 0:

            print("ERROR, SET TEMP AND CURRENT TEMP THE SAME")

        print("The W2475 TEC temp will now set to: ", w2475_set_temp)
        if W2475.read_temp() < w2475_set_temp:
            while W2475.read_temp() < w2475_set_temp:
                W2475.set_temp(W2475.read_temp() + 0.01)
                #sleep(timestep)

        elif (W2475.read_temp() > w2475_set_temp):
            while W2475.read_temp() > w2475_set_temp:
                W2475.set_temp(W2475.read_temp() - 0.01)
                #sleep(timestep)

        elif (W2475.read_temp() - w2475_set_temp) == 0:

            print("ERROR, SET TEMP AND CURRENT TEMP THE SAME")

        print("The W2485 TEC temp will now set to: ", w2485_set_temp)
        if (W2485.read_temp() < w2485_set_temp):
            while W2485.read_temp() < w2485_set_temp:
                W2485.set_temp(W2485.read_temp() + 0.01)
                #sleep(timestep)

        elif (W2485.read_temp() > w2485_set_temp):
            while W2485.read_temp() > w2485_set_temp:
                W2485.set_temp(W2485.read_temp() - 0.01)
                #sleep(timestep)

        elif (W2485.read_temp() - w2485_set_temp) == 0:

            print("ERROR, SET TEMP AND CURRENT TEMP THE SAME")
        if CO2.read_laser_state() != 1:
            CO2.set_laser_state(1)

        print("The CO2 Laser Current will now change to ", co2_set_current)
        while CO2.read_laser_current() < co2_set_current:
            CO2.set_laser_current(CO2.read_laser_set_current() + .1)
            if abs(CO2.read_temp() - CO2.read_set_temp()) > 0.02:
                while abs(CO2.read_temp() - CO2.read_set_temp()) > 0.02:
                    #sleep(timestep)
                    continue
            else:
                #sleep(timestep)
                continue

        if W2475.read_laser_state() != 1:
            W2475.set_laser_state(1)
        print("The W2475 Laser Current will now change to ", w2475_set_current)
        while W2475.read_laser_current() < w2475_set_current:
            W2475.set_laser_current(W2475.read_laser_set_current() + .1)
            if abs(W2475.read_temp() - W2475.read_set_temp()) > 0.02:
                while abs(W2475.read_temp() - W2475.read_set_temp()) > 0.02:
                    #sleep(timestep)
                    continue
            else:
                #sleep(timestep)
                continue

        if W2485.read_laser_state() != 1:
            W2485.set_laser_state(1)
        print("The W2485 Laser Current will now change to ", w2485_set_current)
        while W2485.read_laser_current() < w2485_set_current:
            W2485.set_laser_current(W2485.read_laser_set_current() + .1)
            if abs(W2485.read_temp() - W2485.read_set_temp()) > 0.02:
                while abs(W2485.read_temp() - W2485.read_set_temp()) > 0.02:
                    #sleep(timestep)
                    continue
            else:
                #sleep(timestep)
                continue

# 3 - change TEC Temps manually, COMPLETE UNTESTED
    elif controlchoice==3: #NOT FINISHED
        print( "Please choose which laser you'd like to change the temperature of ")
        print("1: CO2")
        print("2: Water (2475)")
        print("3: Water (2485) \n")
        laserchoice = 0
        while laserchoice==0:
            laserchoice = int(input())

        print("Please input new set temp")
        new_set_temp=None
        while new_set_temp==None:
            new_set_temp=float(input())

        if laserchoice==1:
            print("New CO2 temp will move to: ",new_set_temp)
            if (CO2.read_temp() < new_set_temp):
                while CO2.read_temp() < new_set_temp:
                    CO2.set_temp(CO2.read_temp() + 0.01)
                    #sleep(timestep)

            elif (CO2.read_temp() > new_set_temp):
                while CO2.read_temp() > new_set_temp:
                    CO2.set_temp(CO2.read_temp() - 0.01)
                    #sleep(timestep)

            elif (CO2.read_temp() - new_set_temp) == 0:

                print("ERROR, SET TEMP AND CURRENT TEMP THE SAME")
        elif laserchoice==2:
            print("New 2475 temp will move to: ",new_set_temp)
            if (W2475.read_temp() < new_set_temp):
                while W2475.read_temp() < new_set_temp:
                    W2475.set_temp(W2475.read_temp() + 0.01)
                    #sleep(timestep)

            elif (W2475.read_temp() > new_set_temp):
                while W2475.read_temp() > new_set_temp:
                    W2475.set_temp(W2475.read_temp() - 0.01)
                    #sleep(timestep)

            elif (W2475.read_temp() - new_set_temp) == 0:

                print("ERROR, SET TEMP AND CURRENT TEMP THE SAME")
        elif laserchoice==3:
            print("New 2485 temp will move to: ",new_set_temp)
            if (W2485.read_temp()< new_set_temp):
                while W2485.read_temp() < new_set_temp:
                    W2485.set_temp(W2485.read_temp() + 0.01)
                    #sleep(timestep)

            elif (W2485.read_temp() > new_set_temp):
                while W2485.read_temp() > new_set_temp:
                    W2485.set_temp(W2485.read_temp() - 0.01)
                    #sleep(timestep)

            elif (W2485.read_temp() - new_set_temp) == 0:

                print("ERROR, SET TEMP AND CURRENT TEMP THE SAME")

# 4 - change laser currents manually COMPLETE UNTESTED
    elif controlchoice==4: #change laser current
        print("Please choose which laser you'd like to change the current of ")
        print("1: CO2")
        print("2: Water (2475)")
        print("3: Water (2485) \n")
        laserchoice = None
        while laserchoice == None:
            laserchoice = int(input())

        print("Please input new set current")
        new_set_current = 0
        while new_set_current == 0:
            new_set_current = float(input())

        if laserchoice == 1:
            print("New CO2 current will move to: ", new_set_current)
            if CO2.read_laser_set_current()<new_set_current:
                while CO2.read_laser_set_current() < new_set_current:
                    CO2.set_laser_current(CO2.read_laser_set_current() + .1)
                    if abs(CO2.read_temp() - CO2.read_set_temp()) > 0.02:
                        while abs(CO2.read_temp() - CO2.read_set_temp()) > 0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            elif CO2.read_laser_set_current()>new_set_current:
                while CO2.read_laser_set_current() > new_set_current:
                    CO2.set_laser_current(CO2.read_laser_set_current() - .1)
                    if abs(CO2.read_temp() - CO2.read_set_temp()) > 0.02:
                        while abs(CO2.read_temp() - CO2.read_set_temp()) > 0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            elif CO2.read_laser_set_current()==new_set_current:
                print("New CO2 Laser Set current is the same as previous Laser Set Current")



        elif laserchoice == 2:
            print("New 2475 current will move to: ", new_set_current)
            if W2475.read_laser_set_current()<new_set_current:
                while W2475.read_laser_set_current() < new_set_current:
                    W2475.set_laser_current(W2475.read_laser_set_current() + .1)
                    if abs(W2475.read_temp() - W2475.read_set_temp()) > 0.02:
                        while abs(W2475.read_temp() - W2475.read_set_temp()) > 0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            elif W2475.read_laser_set_current()>new_set_current:
                while W2475.read_laser_set_current() > new_set_current:
                    W2475.set_laser_current(W2475.read_laser_set_current() - .1)
                    if abs(W2475.read_temp() - W2475.read_set_temp()) > 0.02:
                        while abs(W2475.read_temp() - W2475.read_set_temp()) > 0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            elif W2475.read_laser_set_current()==new_set_current:
                print("New W2475 Laser Set current is the same as previous Laser Set Current")
        elif laserchoice == 3:
            print("New 2485 current will move to: ", new_set_current)
            if W2485.read_laser_set_current()<new_set_current:
                print("IF 1")
                while W2485.read_laser_set_current() < new_set_current:
                    W2485.set_laser_current(W2485.read_laser_set_current() + .1)
                    if abs(W2485.read_temp() - W2485.read_set_temp()) > 0.02:
                        while abs(W2485.read_temp() - W2485.read_set_temp()) > 0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            elif W2485.read_laser_set_current()>new_set_current:
                print("if 2")
                while W2485.read_laser_set_current() > new_set_current:
                    W2485.set_laser_current(W2485.read_laser_set_current() - .1)
                    if abs(W2485.read_temp() - W2485.read_set_temp()) > 0.02:
                        while abs(W2485.read_temp() - W2485.read_set_temp()) > 0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            elif W2485.read_laser_set_current()==new_set_current:
                print("New W2485 Laser Set current is the same as previous Laser Set Current")


# 5 - Shutdown all 3 laser currents, COMPLETE UNTESTED
    elif controlchoice==5: #shutdown current for all lasers
        #Bring CO2 Current to ZERO

        if CO2.read_laser_set_current()>0:
            while CO2.read_laser_set_current()>0 or CO2.read_laser_current()>0:
                    CO2.set_laser_current(CO2.read_laser_set_current()-0.1)
                    if abs(CO2.read_temp()-CO2.read_set_temp())>0.02:
                        while abs(CO2.read_temp()-CO2.read_set_temp())>0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            print("Laser CO2 Current now at zero, beginning TEC Shutdown")
        else:
            print("Laser C02 Current already at Zero")

        if W2475.read_laser_set_current()>0:
            while W2475.read_laser_set_current()>0 or W2475.read_laser_current()>0:
                    W2475.set_laser_current(W2475.read_laser_set_current()-0.1)
                    if abs(W2475.read_temp()-W2475.read_set_temp())>0.02:
                        while abs(W2475.read_temp()-W2475.read_set_temp())>0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            print("Laser W2475 Current now at zero")
        else:
            print("Laser W2475 Current already at Zero")

        if W2485.read_laser_set_current()>0:
            while W2485.read_laser_set_current()>0 or W2485.read_laser_current()>0:
                    W2485.set_laser_current(W2485.read_laser_set_current()-0.1)
                    if abs(W2485.read_temp()-W2485.read_set_temp())>0.02:
                        while abs(W2485.read_temp()-W2485.read_set_temp())>0.02:
                            #sleep(timestep)
                            continue
                    else:
                        #sleep(timestep)
                        continue
            print("Laser W2485 Current now at zero")
        else:
            print("Laser W2485 Current already at Zero")
        CO2.set_laser_state(0)
        W2485.set_laser_state(0)
        W2475.set_laser_state(0)

# 6 - shutdown all TECs COMPLETE, UNTESTED
    elif controlchoice==6:
        if CO2.read_laser_current()>0 or W2475.read_laser_current()>0 or W2485.read_laser_current()>0:
            print("ERROR!! SHUTDOWN LASER CURRENT BEFORE CHANGING TEC")
        else:
#Bring CO2 TEC Temp until Tek Current=0 and Tek Volts <.02
            print("The CO2 TEC will now shut down")
            if (CO2.read_temp() > initial_co2_temp):
                while (CO2.read_current() > 0 and CO2.read_voltage()>0.02 and (CO2.read_temp() > initial_co2_temp)):
                    CO2.set_temp(float(CO2.read_set_temp())-0.01)
                    #sleep(timestep)

            elif (CO2.read_temp() < initial_co2_temp):
                while (CO2.read_current()>0 and CO2.read_voltage()>0.02 and (CO2.read_temp() < initial_co2_temp)):
                    CO2.set_temp(float(CO2.read_set_temp())+0.01)
                    #sleep(timestep)

            elif (CO2.read_temp() -initial_co2_temp) == 0:
                print("error, CO2 TEC temp should already be at shutdown conditions")
# Shutdown W2485 TEC
            if (W2485.read_temp() > initial_w2485_temp):
                while (W2485.read_current()>0 and W2485.read_voltage()>0.02 and (W2485.read_temp()> initial_w2485_temp)):
                    W2485.set_temp(W2485.read_set_temp()-0.01)
                    #sleep(timestep)

            elif (W2485.read_temp() < initial_w2485_temp):
                while (W2485.read_current()>0 and W2485.read_voltage()>0.02 and (W2485.read_temp() < initial_w2485_temp)):
                    W2485.set_temp(W2485.read_set_temp()+0.01)
                    #sleep(timestep)

            elif (W2485.read_temp() - initial_w2485_temp) == 0:
                print("error, W2485 TEC temp should already be at shutdown conditions")
# Shutdown W2475 TEC
            if (W2475.read_temp() > initial_w2475_temp):
                while (W2475.read_current()>0 and W2475.read_voltage()>0.02 and W2475.read_temp() > initial_w2475_temp):
                    W2475.set_temp(W2475.read_set_temp()-0.01)
                    #sleep(timestep)

            elif (W2475.read_temp() < initial_w2475_temp):
                while (W2475.read_current()>0 and W2475.read_voltage()>0.02 and W2475.read_temp() < initial_w2475_temp):
                    W2475.set_temp(W2475.read_set_temp()+0.01)
                    #sleep(timestep)

            elif W2475.read_temp() - initial_w2475_temp == 0:
                print("error, W2475 TEC temp should already be at shutdown conditions")
        print("All lasers should be at initial conditions, please press 1 if correct to shutdown, or 2 if not")
        print("IF LASERS ARE STILL AT OPERATING TEMPS YOU MAY HAVE RESTARTED THE PROGRAM")
        print("IF YOU HAVE RESTARTED THE PROGRAM, PLEASE SHUTDOWN MANUALLY")
        shutdown_promt=None
        while shutdown_promt==None:
            shutdown_promt=input()
        if shutdown_promt==1:
            print("Laser TECs will now SHUTDOWN")
            W2485.set_output(0)
            W2475.set_output(0)
            CO2.set_output(0)

        else:
            print("Laser TECs will need to be shutdown manually vai GUI or main menu options")
            print("Please use GUI to ensure TEC is at corrent temperature")
            print("You can use the main menu option to change TEC until Shutdown condition is reached")
            sleep(3)

# 7 - Query TEC Values, COMPLETE, UNTESTED
    elif controlchoice==7:
        for i in range(5):
            print("CO2 TEC Values:")
            print("CURRENT: " + str(CO2.read_current()))
            print("VOLTAGE: " + str(CO2.read_voltage()))

            print("\nW285 TEC Values: ")
            print("CURRENT: " + str(W2485.read_current()))
            print("VOLTAGE: " + str(W2485.read_voltage()))

            print("\nW1475 TEC Values: ")
            print("CURRENT: " + str(W2475.read_current()))
            print("VOLTAGE: " + str(W2475.read_voltage()))

# 8 - manual TEC Shutdown, COMPLETE, UNTESTED
    elif controlchoice==8:
        W2485.set_output(0)
        W2475.set_output(0)
        CO2.set_output(0)

# 9 - emergency current shutdown
    elif controlchoice==9:
        CO2.set_laser_current(0)
        W2475.set_laser_current(0)
        W2485.set_laser_current(0)
