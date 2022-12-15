import time
import lib.Adafruit_CircuitPython_MLX90640.adafruit_mlx90640 as adafruit_mlx90640
import board
import busio
i2c = busio.I2C(scl=board.GP3, sda=board.GP2, frequency=800000)
mlx = adafruit_mlx90640.MLX90640(i2c)
print("MLX addr detected on I2C", [hex(i) for i in mlx.serial_number])
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_4_HZ
frame = [0] * 768
while True:
    try:
        mlx.getFrame(frame)
    except ValueError:
        # these happen, no biggie - retry
        continue
    for h in range(24):
        for w in range(32):
            t = frame[h*32 + w]
            print("%0.1f, " % t, end="")
        print()
    print()