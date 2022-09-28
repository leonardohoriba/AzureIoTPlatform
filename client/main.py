import pigpio
from src.components.Stingray import Stingray
from time import sleep
import threading

from src.helpers.socket_client import SocketClient

raspi = pigpio.pi()
robot = Stingray(raspi)
client = SocketClient()
finished = False

def printSpeed():
    global finished
    while not finished:
        # print(f"Distance: {robot.getSonarDistance()}")
        # robot.triggerSonar()
        client.send({
            "leftWheelSpeed": robot.getLeftWheelSpeed(),
            "rightWheelSpeed": robot.getRightWheelSpeed(),
            "sonarDistance": robot.getSonarDistance()
        })
        sleep(0.001)

robot.triggerSonar()
sleep(0.1)

threadPrintSpeed = threading.Thread(target=printSpeed)
threadPrintSpeed.start()
robot.stop()
sleep(2)
for i in range(500):
    robot.moveToPosition(0)
    sleep(0.01)
for i in range(500):
    robot.moveToPosition(180)
    sleep(0.01)
"""
sleep(5)
robot.moveForward()
sleep(5)
robot.moveRight()
sleep(5)
robot.moveForward()
sleep(5)
robot.stop()
sleep(5)
"""
finished = True
threadPrintSpeed.join()