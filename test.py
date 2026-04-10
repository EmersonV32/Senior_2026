#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Stop
from pybricks.tools import wait, StopWatch

ev3 = EV3Brick()

left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
motor_a = Motor(Port.A)
motor_d = Motor(Port.D)

#Reset angles
left_motor.reset_angle(0)
right_motor.reset_angle(0)
motor_a.reset_angle(0)
motor_d.reset_angle(0)

wait(50)

# ===== BASIC MOVEMENT FUNCTION =====
def move_motors(left_speed, right_speed, duration_ms=None, rotations=None):
    if duration_ms is not None:
        left_motor.run_time(left_speed, duration_ms, Stop.BRAKE, wait=False)
        right_motor.run_time(right_speed, duration_ms, Stop.BRAKE, wait=True)

    elif rotations is not None:
        angle = 360 * rotations
        left_motor.run_angle(left_speed, angle, Stop.BRAKE, wait=False)
        right_motor.run_angle(right_speed, angle, Stop.BRAKE, wait=True)


# ===== MAIN PROGRAM =====
motor_a.run_angle(-1000, 280)

move_motors(500, -500, duration_ms=1000)
wait(500)

move_motors(-300, 300, rotations=1.21)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)
wait(500)

motor_a.run_angle(600, 250)

motor_d.run(500)
wait(1000)

motor_a.run_angle(-1000, 270)

# Adjust
move_motors(-200, 200, rotations=0.3)
left_motor.stop(Stop.COAST)
right_motor.stop(Stop.COAST)

motor_a.run_angle(200, 50)

motor_d.stop()
wait(50)
motor_d.run_angle(-300, 50)

wait(2000)

move_motors(-100, 100, rotations=0.1)

motor_a.run_angle(600, 250)
wait(1000)

motor_d.run(500)
wait(2000)

# Move forward
move_motors(-400, -400, rotations=0.8)
left_motor.stop(Stop.BRAKE)
right_motor.stop(Stop.BRAKE)

# Turn
move_motors(500, -500, duration_ms=1000)

# Move until line
move_until_reflect_condition(
    left_speed=-400,
    right_speed=400,
    sensor_port=Port.S4,
    threshold=30,
    condition="below"
)

# Small adjust
move_motors(-200, 200, rotations=0.5)
move_motors(500, 500, rotations=0.7)




















# ===== PID LINE FOLLOW =====
pid_line_follower(
    follow_sensor_port=Port.S1,
    stop_sensor_port=Port.S4,
    base_speed=400,
    Kp=2,
    Kd=3,
    target=30,
    stop_mode="c",
    stop_threshold=20,
    side="r"
)

# Adjust
move_motors(-200, 200, rotations=0.2)
move_motors(-500, -500, rotations=0.8)

# ===== FINAL PID LINE FOLLOW =====
pid_line_follower(
    follow_sensor_port=Port.S1,
    stop_sensor_port=Port.S4,
    base_speed=400,
    Kp=2,
    Kd=3,
    target=30,
    stop_mode="c",
    stop_threshold=20,
    side="r"
)