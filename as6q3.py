class Converter:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def miles(self):
        if self.unit == 'miles':
            return self.value
        elif self.unit == 'km':
            return self.value * 0.621371
        elif self.unit == 'ft':
            return self.value / 5280
        elif self.unit == 'in':
            return self.value / 63360
        elif self.unit == 'cm':
            return self.value / 160934
        elif self.unit == 'm':
            return self.value / 1609.34

    def km(self):
        if self.unit == 'miles':
            return self.value * 1.60934
        elif self.unit == 'km':
            return self.value
        elif self.unit == 'ft':
            return self.value / 3280.84
        elif self.unit == 'in':
            return self.value / 39370.1
        elif self.unit == 'cm':
            return self.value / 100000
        elif self.unit == 'm':
            return self.value / 1000

    def ft(self):
        if self.unit == 'miles':
            return self.value * 5280
        elif self.unit == 'km':
            return self.value * 3280.84
        elif self.unit == 'ft':
            return self.value
        elif self.unit == 'in':
            return self.value / 12
        elif self.unit == 'cm':
            return self.value / 30.48
        elif self.unit == 'm':
            return self.value * 3.28084

    def inch(self):
        if self.unit == 'miles':
            return self.value * 63360
        elif self.unit == 'km':
            return self.value * 39370.1
        elif self.unit == 'ft':
            return self.value * 12
        elif self.unit == 'in':
            return self.value
        elif self.unit == 'cm':
            return self.value / 2.54
        elif self.unit == 'm':
            return self.value * 39.3701

    def cm(self):
        if self.unit == 'miles':
            return self.value * 160934
        elif self.unit == 'km':
            return self.value * 100000
        elif self.unit == 'ft':
            return self.value * 30.48
        elif self.unit == 'in':
            return self.value * 2.54
        elif self.unit == 'cm':
            return self.value
        elif self.unit == 'm':
            return self.value * 100

    def m(self):
        if self.unit == 'miles':
            return self.value * 1609.34
        elif self.unit == 'km':
            return self.value * 1000
        elif self.unit == 'ft':
            return self.value / 3.28084
        elif self.unit == 'in':
            return self.value / 39.3701
        elif self.unit == 'cm':
            return self.value / 100
        elif self.unit == 'm':
            return self.value

def main():
    value = float(input("Enter the value: "))
    unit = input("Enter the unit: ")
    c = Converter(value, unit)
    print(f"Value in miles: {c.miles()}")
    print(f"Value in km: {c.km()}")
    print(f"Value in ft: {c.ft()}")
    print(f"Value in inch: {c.inch()}")
    print(f"Value in cm: {c.cm()}")
    print(f"Value in m: {c.m()}")

main()