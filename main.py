maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 140)
basic.pause(240)
maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
basic.pause(2800)
maqueen.motor_stop(maqueen.Motors.ALL)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 110)
basic.pause(250)
maqueen.motor_stop(maqueen.Motors.ALL)
basic.pause(1900)
for index in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 120)
    maqueen.servo_run(maqueen.Servos.S2, 30)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 70)
    maqueen.servo_run(maqueen.Servos.S2, 60)
basic.pause(200)
for index2 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 120)
    maqueen.servo_run(maqueen.Servos.S2, 30)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 70)
    maqueen.servo_run(maqueen.Servos.S2, 60)
basic.pause(200)
for index3 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 120)
    maqueen.servo_run(maqueen.Servos.S2, 30)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 70)
    maqueen.servo_run(maqueen.Servos.S2, 60)
basic.pause(200)
for index4 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 120)
    maqueen.servo_run(maqueen.Servos.S2, 30)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 70)
    maqueen.servo_run(maqueen.Servos.S2, 60)
basic.pause(200)
for index5 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 120)
    maqueen.servo_run(maqueen.Servos.S2, 30)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 70)
    maqueen.servo_run(maqueen.Servos.S2, 60)
basic.pause(200)
for index6 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 120)
    maqueen.servo_run(maqueen.Servos.S2, 30)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 80)
    maqueen.servo_run(maqueen.Servos.S2, 60)
maqueen.servo_run(maqueen.Servos.S1, 30)
maqueen.servo_run(maqueen.Servos.S2, 30)
basic.pause(200)
for index7 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 60)
    maqueen.servo_run(maqueen.Servos.S2, 80)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 30)
    maqueen.servo_run(maqueen.Servos.S2, 30)
basic.pause(150)
for index8 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 60)
    maqueen.servo_run(maqueen.Servos.S2, 80)
    basic.pause(100)
    maqueen.servo_run(maqueen.Servos.S1, 30)
    maqueen.servo_run(maqueen.Servos.S2, 30)
basic.pause(150)
for index9 in range(3):
    maqueen.servo_run(maqueen.Servos.S1, 60)
    maqueen.servo_run(maqueen.Servos.S2, 80)
maqueen.servo_run(maqueen.Servos.S1, 120)
maqueen.servo_run(maqueen.Servos.S2, 120)
basic.pause(200)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 241)
basic.pause(1000)
maqueen.motor_stop(maqueen.Motors.ALL)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 60)
basic.pause(200)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 60)
basic.pause(200)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 60)
basic.pause(200)
maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CCW, 60)
basic.pause(200)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 60)
basic.pause(100)
maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CCW, 60)
basic.pause(100)
maqueen.motor_stop(maqueen.Motors.ALL)