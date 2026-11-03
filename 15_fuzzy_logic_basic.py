# Simple Mamdani-style fuzzy fan controller
# Inputs: temperature and humidity (0 to 10)
temperature = 8
humidity = 7

# Simple membership functions
def low(value):
    return max(0, min(1, (5 - value) / 5))

def high(value):
    return max(0, min(1, (value - 5) / 5))

temp_high = high(temperature)
humidity_high = high(humidity)

# Rules:
# IF temperature is high OR humidity is high THEN fan is fast
fast = max(temp_high, humidity_high)
# IF both are low THEN fan is slow
slow = min(low(temperature), low(humidity))

# Simple weighted average defuzzification
if slow + fast == 0:
    fan_speed = 0
else:
    fan_speed = (slow * 20 + fast * 100) / (slow + fast)

print("Temperature high membership:", temp_high)
print("Humidity high membership:", humidity_high)
print("Fan speed:", round(fan_speed, 2))
