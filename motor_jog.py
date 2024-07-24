#!/usr/bin/python3

# SPI interface
from spidev import SpiDev
# delays
import time
# this allows arg parsing
import argparse
# this is for the exit
import sys

###############################
# defaults are hard coded below
###############################
VERSION="1.0.0"
DATE="07-15-2024"

SPEED = 39811
ACCEL = 25119
TIME = 5.0
SPI_MHZ = 300000


################
# Write_Register
################
def Write_Register (command=[]):
    print ("Sending: " + " ".join(hex(x) for x in command))
    msg = command
    spi.xfer (msg)
    #answer = spi.readbytes(5)
    #print ("Recieving: " + " ".join(hex(x) for x in answer))
    #print (" ")


###########
# configure
###########
def configure(motor, reverse, acceleration):

    accel_msb = (int)((acceleration / 0x100) % 0x100)
    accel_lsb = (int)(acceleration % 0x100)
    print ("acceleration msb: " + hex(accel_msb) + " acceleration lsb: " + hex(accel_lsb))

    if reverse:
        # both motors is ie 0x03 (not in logic yet)
        if motor%2 == 1:
            config_01 = [ 0x80, 0x00, 0x00, 0x01, 0x00 ]
        else:
            config_01 = [ 0x80, 0x00, 0x00, 0x02, 0x00 ]

    else:
        config_01 = [ 0x80, 0x00, 0x00, 0x00, 0x00 ]
    config_02 = [ 0x83, 0x00, 0x00, 0x00, 0x00 ]
    config_03 = [ 0x85, 0x00, 0x00, 0x00, 0x00 ]

    config_14 = [ 0x90, 0x00, 0x00, 0x00, 0x00 ]
    config_15 = [ 0x98, 0x00, 0x00, 0x00, 0x00 ]

    if motor%2 == 1:
        config_20 = [ 0xA0, 0x00, 0x00, 0x00, 0x01 ]
    else:
        config_20 = [ 0xA0, 0x00, 0x00, 0x00, 0x00 ]

    config_21 = [ 0xA1, 0x00, 0x00, 0x00, 0x00 ]
    config_23 = [ 0xA3, 0x00, 0x00, 0x00, 0x00 ]
    #config_24 = [ 0xA4, 0x00, 0x00, 0x00, 0x00 ]
    #config_25 = [ 0xA5, 0x00, 0x00, 0x00, 0x00 ]
    config_24 = [ 0xA4, 0x00, 0x00, 0x03, 0xE8 ]
    config_25 = [ 0xA5, 0x00, 0x00, 0x93, 0x50 ]
    config_27 = [ 0xA7, 0x00, 0x00, 0x00, 0x00 ]

    if motor%2 == 1:
        config_26 = [ 0xA6, 0x00, 0x00, accel_msb, accel_lsb ]
        config_28 = [ 0xA8, 0x00, 0x00, accel_msb, accel_lsb ]
    else:
        config_26 = [ 0xA6, 0x00, 0x00, 0x00, 0x00 ]
        config_28 = [ 0xA8, 0x00, 0x00, 0x00, 0x00 ]

    #config_2A = [ 0xAA, 0x00, 0x00, 0x00, 0x00 ]
    #config_2B = [ 0xAB, 0x00, 0x00, 0x00, 0x00 ]
    config_2A = [ 0xAA, 0x00, 0x00, 0x05, 0x78 ]
    config_2B = [ 0xAB, 0x00, 0x00, 0x00, 0x0A ]
    config_2C = [ 0xAC, 0x00, 0x00, 0x00, 0x00 ]
    #config_2D = [ 0xAD, 0x00, 0x00, 0x00, 0x00 ]
    config_2D = [ 0xAD, 0x00, 0x00, 0xC7, 0x96 ]

    config_30 = [ 0xB0, 0x00, 0x07, 0x17, 0x03 ]
    config_31 = [ 0xB1, 0x00, 0x00, 0x00, 0x00 ]
    config_32 = [ 0xB2, 0x00, 0xFF, 0xFF, 0xFF ]
    config_34 = [ 0xB4, 0x00, 0x00, 0x00, 0x00 ]

    if motor%2 == 1:
        config_40 = [ 0xC0, 0x00, 0x00, 0x00, 0x00 ]
    else:
        config_40 = [ 0xC0, 0x00, 0x00, 0x00, 0x01 ]

    config_41 = [ 0xC1, 0x00, 0x00, 0x00, 0x00 ]
    config_43 = [ 0xC3, 0x00, 0x00, 0x00, 0x00 ]
    config_44 = [ 0xC4, 0x00, 0x00, 0x00, 0x00 ]
    config_45 = [ 0xC5, 0x00, 0x00, 0x00, 0x00 ]
    config_47 = [ 0xC7, 0x00, 0x00, 0x00, 0x00 ]
    if motor%2 == 1:
        config_46 = [ 0xC6, 0x00, 0x00, 0x00, 0x00 ]
        config_48 = [ 0xC8, 0x00, 0x00, 0x00, 0x00 ]
    else:
        config_46 = [ 0xC6, 0x00, 0x00, accel_msb, accel_lsb ]
        config_48 = [ 0xC8, 0x00, 0x00, accel_msb, accel_lsb ]

    config_4A = [ 0xCA, 0x00, 0x00, 0x00, 0x00 ]
    config_4B = [ 0xCB, 0x00, 0x00, 0x00, 0x00 ]
    config_4C = [ 0xCC, 0x00, 0x00, 0x00, 0x00 ]
    config_4D = [ 0xCD, 0x00, 0x00, 0x00, 0x00 ]

    config_50 = [ 0xD0, 0x00, 0x07, 0x17, 0x03 ]
    config_51 = [ 0xD1, 0x00, 0x00, 0x00, 0x00 ]
    config_52 = [ 0xD2, 0x00, 0xFF, 0xFF, 0xFF ]
    config_54 = [ 0xD4, 0x00, 0x00, 0x00, 0x00 ]

    config_60 = [0xE0, 0xAA, 0xAA, 0xB5, 0x54 ]
    config_61 = [0xE1, 0x4A, 0x95, 0x54, 0xAA ]
    config_62 = [0xE2, 0x24, 0x49, 0x29, 0x29 ]
    config_63 = [0xE3, 0x10, 0x10, 0x42, 0x22 ]
    config_64 = [0xE4, 0xFB, 0xFF, 0xFF, 0xFF ]
    config_65 = [0xE5, 0xB5, 0xBB, 0x77, 0x7D ]
    config_66 = [0xE6, 0x49, 0x29, 0x55, 0x56 ]
    config_67 = [0xE7, 0x00, 0x40, 0x42, 0x22 ]
    config_68 = [0xE8, 0xFF, 0xFF, 0x80, 0x56 ]
    config_69 = [0xE9, 0x00, 0xF7, 0x00, 0x00 ]
    config_6C = [0xEC, 0x00, 0x01, 0x01, 0xD5 ]
    config_6D = [0xED, 0x00, 0x00, 0x00, 0x00 ]

    config_7C = [0xFC, 0x00, 0x01, 0x01, 0xD5 ]
    config_7D = [0xFD, 0x00, 0x00, 0x00, 0x00 ]

    Write_Register (config_01)
    Write_Register (config_02)
    Write_Register (config_03)

    Write_Register (config_14)
    Write_Register (config_15)

    Write_Register (config_20)
    Write_Register (config_21)
    Write_Register (config_23)
    Write_Register (config_24)
    Write_Register (config_25)
    Write_Register (config_26)
    Write_Register (config_27)
    Write_Register (config_28)
    Write_Register (config_2A)
    Write_Register (config_2B)
    Write_Register (config_2C)
    Write_Register (config_2D)

    Write_Register (config_30)
    Write_Register (config_31)
    Write_Register (config_32)
    Write_Register (config_34)

    Write_Register (config_40)
    Write_Register (config_41)
    Write_Register (config_43)
    Write_Register (config_44)
    Write_Register (config_45)
    Write_Register (config_46)
    Write_Register (config_47)
    Write_Register (config_48)
    Write_Register (config_4A)
    Write_Register (config_4B)
    Write_Register (config_4C)
    Write_Register (config_4D)

    Write_Register (config_50)
    Write_Register (config_51)
    Write_Register (config_52)
    Write_Register (config_54)

    Write_Register (config_60)
    Write_Register (config_61)
    Write_Register (config_62)
    Write_Register (config_63)
    Write_Register (config_64)
    Write_Register (config_65)
    Write_Register (config_66)
    Write_Register (config_67)
    Write_Register (config_68)
    Write_Register (config_69)
    Write_Register (config_6C)
    Write_Register (config_6D)

    Write_Register (config_7C)
    Write_Register (config_7D)


#######################
# how to use the script
#######################
def usage():
    
    parser.print_help (sys.stderr)
    print ("\nExamples:\n")

    print ("motor_jog.py -m 1 -t 10.0")
    print ("  This runs the first motor of the first motor controller chip in the forward direction with default velocity for 10 seconds\n")

    print ("motor_jog.py --motor 4 --reverse --velocity 8000000 --time 8")
    print ("  This runs the second motor of the second motor controller chip in the reverse direction with velocity of 8000000 and default acceleration for 8 seconds\n")

    print ("motor_jog.py -m 3 -r -v 10000 -a 20000")
    print ("  This runs the first motor of the second motor controller chip in the reverse direction with velocity of 10000 and acceleration/deceleration of 20000 for the default number of seconds\n")

    print ("Version: " + VERSION)
    print ("Date: " + DATE)

#######
# start
#######
def start(motor, speed):
    speed_msb = (int)((speed / 0x10000) % 0x100)
    speed_mid_byte = (int)((speed / 0x100) % 0x100)
    speed_lsb = (int)(speed % 0x100)
    print ("speed msb: " + hex(speed_msb) + " speed_mid_byte: " + hex(speed_mid_byte)+ " speed_lsb: " + hex(speed_lsb))

    start_A8 = [ 0xA8, 0x00, 0x00, 0x07, 0xCB ]
    start_A4 = [ 0xA4, 0x00, 0x00, 0x03, 0xE8 ]
    start_A5 = [ 0xA5, 0x00, 0x00, 0x93, 0x50 ]
    # repeat A8
    start_AA = [ 0xAA, 0x00, 0x00, 0x05, 0x78 ]
    start_A3 = [ 0xA3, 0x00, 0x00, 0x00, 0x00 ]
    start_AB = [ 0xAB, 0x00, 0x00, 0x00, 0x0A ]
    start_AC = [ 0xAC, 0x00, 0x00, 0x00, 0x00 ]
    # this is called between A7/A0 below
    start_AD = [ 0xAD, 0x00, 0x00, 0xC7, 0x96 ]

    start_A7 = [ 0xA7, 0x00, 0x03, 0x0D, 0x40 ]
    start_A0 = [ 0xA0, 0x00, 0x00, 0x00, 0x00 ]

    if motor%2 == 1:
        start_A7_C7 = [ 0xA7, 0x00, speed_msb, speed_mid_byte, speed_lsb ]
        start_A0_C0 = [ 0xA0, 0x00, 0x00, 0x00, 0x02 ]
    else:
        start_A7_C7 = [ 0xC7, 0x00, speed_msb, speed_mid_byte, speed_lsb ]
        start_A0_C0 = [ 0xC0, 0x00, 0x00, 0x00, 0x02 ]

    Write_Register (start_A8)
    time.sleep (.001)
    Write_Register (start_A4)
    time.sleep (.001)
    Write_Register (start_A5)
    time.sleep (.001)
    Write_Register (start_A8)
    time.sleep (.001)
    Write_Register (start_AA)
    time.sleep (.001)
    Write_Register (start_A3)
    time.sleep (.001)
    Write_Register (start_AB)
    time.sleep (.001)
    Write_Register (start_AC)
    time.sleep (.001)
    #Write_Register (start_A7_C7)
    #Write_Register (start_A0_C0)
    Write_Register (start_A7)
    Write_Register (start_AD)
    Write_Register (start_A0)


######
# stop
######
def stop(motor):
    if motor%2 == 1:
        start_A7_C7 = [ 0xA7, 0x00, 0x00, 0x00, 0x00 ]
        start_A0_C0 = [ 0xA0, 0x00, 0x00, 0x00, 0x01 ]
    else:
        start_A7_C7 = [ 0xC7, 0x00, 0x00, 0x00, 0x00 ]
        start_A0_C0 = [ 0xC0, 0x00, 0x00, 0x00, 0x01 ]


    Write_Register (start_A7_C7)
    Write_Register (start_A0_C0)


#################################################
# New section to replace the getopt attempt above
#################################################

parser = argparse.ArgumentParser()

# motor argumen to specify which motor number
# below is a required parameter but I want to print out more info for self documentation
# therefore I am not going to pass the "required=True" parameter to the add_argument ()
parser.add_argument ("-m", "--motor", type=int, choices=[1,2,3,4], help="select the motor to drive")

# reverse argument for the motor
parser.add_argument ("-r", "--reverse", action="store_true", help="inverse the direction of the shaft")

# velocity argument to specify the speed of the motor
# can not specify range below because it blows up help messages with every value
#parser.add_argument ("-v", "--velocity", type=int, choices=range(0,8388607), help="Threshold (0-8388607) for the speed of the stepper motor (hint:~40000)")
parser.add_argument ("-v", "--velocity", type=int, default=SPEED, help="Threshold (0-8388607) for the speed of the stepper motor (hint:~40000)")

# acceleration argument to specify max acceleration/deceleration of motor (may not hit this max)
# can not specify range below because it blows up help messages with every value
parser.add_argument ("-a", "--acceleration", type=int, default=ACCEL, help="Threshold (0-65535) for the max acceleration/deceleration of the stepper motor (hint:~25000)")

# time argument the amount of time to run
parser.add_argument ("-t", "--time", type=float, default=TIME, help="seconds to run the motor before slowing down and stopping")


# lets parse
args = parser.parse_args()

# lets do my own checking here and print usage as needed
# also doing my own checks allows me to print examples out when someone violates these checks for them
# to follow for their next attempt
if args.time:
    if args.time < 0.0:
        print(f"The time must be a positive float instead of {args.time}")
        usage ()
        sys.exit ()

if args.velocity:
    if args.velocity < 0 or args.velocity > 8388607:
        print(f"The velocity must be in the range from 0 to 8388607 instead of {args.velocity}")
        usage ()
        sys.exit ()

if args.acceleration:
    if args.acceleration < 0 or args.acceleration > 65535:
        print(f"The acceleration must be in the range from 0 to 65535 instead of {args.acceleration}")
        usage ()
        sys.exit ()

if args.motor:
    if args.motor < 3:
        SPIBUS=4
    else:
        SPIBUS=6
else:
    print ("You should always specify a motor")
    usage ()
    sys.exit ()


###############################
# Setting things up for the bus
###############################

spi = SpiDev ()

spi.open (SPIBUS,0)
spi.max_speed_hz = SPI_MHZ


#################################################
# this runs the code after parameters figured out
#################################################

configure (args.motor, args.reverse, args.acceleration)

# little pause for everything to settle
# TODO: this may not be needed
time.sleep (1)

# start it
start (args.motor, args.velocity)

# wait
#time.sleep (args.time)

# stop it
#stop (args.motor)
