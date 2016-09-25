from math import pi


def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.num / r.denom, c.imag)


def mul_complex_and_rational(c, r):
    r_magnitute, r_angle = r.num / r.denom, 0
    if r_magnitute < 0:
        r_magnitute, r_angle = -r_magnitute, pi
    return ComplexMA(c.magnitute * r_magnitute, c.angle + r.angle)


def add_rational_and_complex(r, c):
    return add_complex_and_rational(c, r)


def mul_rational_and_complex(r, c):
    return mul_complex_and_rational(c, r)


def rational_to_complex(r):
    return ComplexRI(r.num / r.denom, 0)


class Number(object):
    additers = {("rat", "com"): add_rational_and_complex, ("com", "rat"): add_complex_and_rational}
    multipliers = {("rat", "com"): mul_rational_and_complex, ("com", "rat"): mul_complex_and_rational}

    def __add__(self, other):
        """if self.type_tag==other.type_tag:
            return self.add(other)
        elif (self.type_tag,other.type_tag ) in self.additers:
            return self.cross_play(other,self.additers)"""
        x, y = self.coerce(other)
        return x.add(y)

    def __mul__(self, other):
        """if self.type_tag == other.type_tag:
            return self.mul(other)
        elif (self.type_tag, other.type_tag) in self.multipliers:
            return self.cross_play(other,self.multipliers)"""
        x, y = self.coerce(other)
        return x.mul(y)

    def coerce(self, other):
        if self.type_tag == other.type_tag:
            return (self, other)
        else:
            if (self.type_tag, other.type_tag) in self.coercions:
                coerce_number = self.coerce_to(other)
                return (coerce_number, other)
            if (other.type_tag, self.type_tag) in self.coercions:
                coerce_number = other.coerce_to(self)
                return (self, coerce_number)

    def cross_play(self, other, cross_fns):
        return cross_fns[(self.type_tag, other.type_tag)](self, other)

    def coerce_to(self, other):
        return self.coercions[(self.type_tag, other.type_tag)](self)

    coercions = {("rat", "com"): rational_to_complex}


class Complex(Number):
    type_tag = "com"

    def add(self, other):
        return ComplexRI(self.real + other.real, self.imag + other.imag)

    def mul(self, other):
        return ComplexMA(self.magnitute * other.magnitute, self.angle + other.angle)


from math import atan2


class ComplexRI(Complex):
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    @property
    def magnitute(self):
        return (self.real ** 2 + self.imag * 2)

    @property
    def angle(self):
        return atan2(self.imag, self.real)

    def __repr__(self):
        return 'ComplexRI({0:g},{1:g})'.format(self.real, self.imag)


from math import sin, cos, pi


class ComplexMA(Complex):
    def __init__(self, magnitute, angle):
        self.magnitute = magnitute
        self.angle = angle

    @property
    def real(self):
        return self.magnitute * cos(self.angle)

    @property
    def imag(self):
        return self.magnitute * sin(self.angle)

    def __rerp__(self):
        return 'ComplexMA({0:g},{1:g}*pi'.format(self.magnitute, self.angle / pi)


print(ComplexRI(1, 2) + ComplexMA(2, pi / 2))
from  fractions import gcd


class Rational(Number):
    type_tag = "rat"

    def __init__(self, num, denom):
        g = gcd(num, denom)
        self.num = num / g
        self.denom = denom / g

    def __repr__(self):
        return "Rantional ({0},{1})".format(self.num, self.denom)

    def __add__(self, other):
        nx, ny, dx, dy = self.num, other.num, self.denom, other.denom
        num = nx * dy + ny * dx
        denom = dx ** dy
        return Rational(num, denom)

    def __mul__(self, other):
        num = self.num * other.num
        denom = self.denom * other.denom
        return Rational(num, denom)


print(Rational(3, 5) + Rational(8, 4))
c = ComplexRI(1, 1)
isinstance(c, ComplexRI)


def is_real(c):
    assert isinstance(c, Complex), 'The arguments should be the subtype of Complex'
    if isinstance(c, ComplexRI):
        return c.imag == 0
    if isinstance(c, ComplexMA):
        return c.angle % pi == 0


print(is_real(ComplexMA(2, pi)))
Rational.type_tag = 'rat'
Complex.type_tag = 'com'


def add_complex_and_rational(c, r):
    return ComplexRI(c.real + r.num / r.denom, c.imag)


def mul_complex_and_rational(c, r):
    r_magnitute, r_angle = r.num / r.denom, 0
    if r_magnitute < 0:
        r_magnitute, r_angle = -r_magnitute, pi
    return ComplexMA(c.magnitute * r_magnitute, c.angle + r.angle)


print(ComplexRI(1.5, 0) + Rational(6, 5))
