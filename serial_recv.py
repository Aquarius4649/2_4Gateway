import serial
import time

# シリアルポートを115200のボーレートで開く
ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)

# UARTからのデータを連続して読み取り、表示する
while True:
    if ser.in_waiting > 0:
        data = ser.readline().decode('utf-8').rstrip()
        print("受信データ:", data)
    time.sleep(0.1)  # CPUを過負荷にしないための軽微な遅延
