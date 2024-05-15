class Addition:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def perform_addition(self):
        raise NotImplementedError("Subclasses should implement this method.")


class NormalAddition(Addition):
    def perform_addition(self):
        return self.num1 + self.num2


class ComplexAddition(Addition):
    def perform_addition(self):
        real_part = self.num1.real + self.num2.real
        imaginary_part = self.num1.imag + self.num2.imag
        return complex(real_part, imaginary_part)


def main():
    num1 = int(input("Enter the first real number: "))
    num2 = int(input("Enter the second real number: "))
    normal_adder = NormalAddition(num1, num2)
    print("Normal Addition Result:", int(normal_adder.perform_addition()))

    r1 = int(input("Enter the real part of the first complex number: "))
    i1 = int(input("Enter the imaginary part of the first complex number: "))
    co1 = complex(r1, i1)

    r2 = int(input("Enter the real part of the second complex number: "))
    i2 = int(input("Enter the imaginary part of the second complex number: "))
    co2 = complex(r2, i2)

    complex_adder = ComplexAddition(co1, co2)
    print("Complex Addition Result:", complex_adder.perform_addition())


if __name__ == "__main__":
    main()
