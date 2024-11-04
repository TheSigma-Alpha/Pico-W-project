import machine
import time

adcpin = 4
sensor = machine.ADC(adcpin)

greenLed = machine.Pin(0, machine.Pin.OUT)
redLed = machine.Pin(2, machine.Pin.OUT)
blueLed = machine.Pin(3, machine.Pin.OUT)
buzzer = machine.PWM(machine.Pin(6))
potentiometer = machine.ADC(26)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)

convention_factor = 3.3 / (65535)

def ReadTemperature():
    adc_value = sensor.read_u16()
    volt = (3.3/65535) * adc_value
    temperature = 27 - (volt - 0.706)/0.001721
    return round(temperature, 1)


greenLed.value(0)
redLed.value(0)
blueLed.value(0)

maxTemp = 30
MinTemp = 15
toggle_value = False

def SetUpTemprature(): 
    global maxTemp
    global MinTemp
    voltage = potentiometer.read_u16() * convention_factor * 10 + 10
    print("max temp is", maxTemp)
    print("Min temp is", MinTemp)
    print(toggle_value)
    if toggle_value == False:
        maxTemp = voltage
    else:
        MinTemp = voltage

        
def change_value(pin):
    global toggle_value
    # Toggle the value each time the button is pressed
    toggle_value = not toggle_value
    print("Value changed to:", toggle_value)


while True:
    temperature = ReadTemperature()
    SetUpTemprature()
    button.irq(trigger=machine.Pin.IRQ_RISING, handler=change_value)

    if temperature > maxTemp:
        greenLed.value(0)
        redLed.toggle()
        buzzer.freq(500)
        buzzer.duty_u16(1000)
        time.sleep(1)
    else:
        redLed.value(0)
        blueLed.value(0)
        buzzer.duty_u16(0)
        if temperature > MinTemp:
            greenLed.toggle()
            time.sleep(1)


    if temperature < MinTemp:
        greenLed.value(0)
        blueLed.toggle()
        time.sleep(1)
    else:
        blueLed.value(0)
        redLed.value(0)
        buzzer.duty_u16(0)
        if temperature < maxTemp:
            greenLed.toggle()
            time.sleep(1)

    greenLed.value(0)
    redLed.value(0)
    blueLed.value(0)
    

