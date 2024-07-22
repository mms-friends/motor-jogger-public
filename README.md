## Project-specific setup, run, build, test
Run the python script on pi.  

### Setup
This script will need a motor jogging script and runs a pi connected to it with motors

#### IDE
N/A

### Build, Run, Test
The command is self documenting.
Run it with no parameters to print usage with examples.

These are the current examples as of the last readme update.  

motor_jog.py -m 1 -t 10.0
  This runs the first motor of the first motor controller chip in the forward direction with default velocity for 10 seconds

motor_jog.py --motor 4 --reverse --velocity 8000000 --time 8
  This runs the second motor of the second motor controller chip in the reverse direction with velocity of 8000000 and default acceleration for 8 seconds

motor_jog.py -m 3 -r -v 10000 -a 20000
  This runs the first motor of the second motor controller chip in the reverse direction with velocity of 10000 and acceleration/deceleration of 20000 for the default number of seconds
Examples:

motor_jog.py -m 1 -t 10.0
  This runs the first motor of the first motor controller chip in the forward direction with default velocity for 10 seconds

motor_jog.py --motor 4 --reverse --velocity 8000000 --time 8
  This runs the second motor of the second motor controller chip in the reverse direction with velocity of 8000000 and default acceleration for 8 seconds

motor_jog.py -m 3 -r -v 10000 -a 20000
  This runs the first motor of the second motor controller chip in the reverse direction with velocity of 10000 and acceleration/deceleration of 20000 for the default number of seconds

## More in-house info
https://medmgtserv.atlassian.net/wiki/x/AQBCBg

## Note
The script has a version and last modified date that is printed during the self
documentation or when the help parameter is given.  Please keep these updated
when commits are made.  

## Copyright
 Copyright 2024 Medication Management Services, Inc.
