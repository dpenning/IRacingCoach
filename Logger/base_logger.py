#!python3
import irsdk, time
import csv, colorsys

ir = irsdk.IRSDK()
ir.startup()

lapID = None
LapDistPct = None
f = None
filename = None

while True:
    if not ir or ir['ReplayPlaySpeed'] == 0:
        continue

    if ir['Lap'] != lapID:
        print( "New Lap ", ir['Lap'])
        if f:
            f.close()
        filename = "LoggedLaps/" + str(int(time.time())) + "_" + str(ir['Lap']) + '.csv'
        f = open(filename, 'w')
        f.write(
            'lapDistPct' + ", " +
            'speed' + ", " +
            'throttle' + ", " +
            'brake' + ", " +
            'gear' + ", " +
            'steeringWheelAngle' + ", " +
            'longAccel' + ", " +
            'latAccel' + ", " +
            'rpm' + ", " +
            'clutch' + "\n"
        )
        lapID = ir['Lap']

    ir.freeze_var_buffer_latest()

    if ir['LapDistPct'] != LapDistPct:
        lapDistPct = ir['LapDistPct']
        speed = ir['Speed']
        throttle = ir['Throttle']
        brake = ir['Brake']
        gear = ir['Gear']
        steeringWheelAngle = ir['SteeringWheelAngle']
        longAccel = ir['LongAccel']
        latAccel = ir['LatAccel']
        rpm = ir['RPM']
        clutch = ir['Clutch']

        f.write(
            str(lapDistPct) + ", " +
            str(speed) + ", " +
            str(throttle) + ", " +
            str(brake) + ", " +
            str(gear) + ", " +
            str(steeringWheelAngle) + ", " +
            str(longAccel) + ", " +
            str(latAccel) + ", " +
            str(rpm) + ", " +
            str(clutch) + "\n"
        )
        LapDistPct = ir['LapDistPct']
