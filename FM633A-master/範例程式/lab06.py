from machine import Pin, PWM
import time

buzzer = PWM(Pin(5))
buzzer.duty(512)

buzzer.freq(392)
time.sleep(.5)
buzzer.freq(330)
time.sleep(.5)
buzzer.freq(330)
time.sleep(1.)
buzzer.freq(349)
time.sleep(.5)
buzzer.freq(294)
time.sleep(.5)
buzzer.freq(294)
time.sleep(1.)
buzzer.freq(261)
time.sleep(.5)
buzzer.freq(294)
time.sleep(.5)
buzzer.freq(330)
time.sleep(1.)
buzzer.freq(349)
time.sleep(.5)
buzzer.freq(392)
time.sleep(.5)
buzzer.freq(392)
time.sleep(.5)
buzzer.freq(392)
time.sleep(.5)

buzzer.duty(0) # 關閉蜂鳴器
