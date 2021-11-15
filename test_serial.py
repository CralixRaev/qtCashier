import serial

with serial.Serial() as ser:
    ser.baudrate = 19200
    ser.port = 'COM4'
    ser.open()
    ser.read(1000)
