//
//  complex.cpp
//  

#include <iostream>
#include <istream>
#include "complex.hpp"

Complex::Complex()
{
    imag = real = 0.0;
}

Complex::Complex(double a, double b)
{
    imag = b;
    real = a;
}

Complex::~Complex(){};

Complex operator+(const Complex & a, const Complex & b)
{
    return Complex(a.real + b.real, a.imag + b.imag);
}

Complex operator-(const Complex & a, const Complex & b)
{
    return Complex(a.real - b.real, a.imag - b.imag);
}

Complex operator*(const Complex & a, const Complex & b)
{
    return Complex((a.real * b.real) - (a.imag * b.imag), (a.real * b.imag) + (a.imag * b.real));
}

Complex operator*(const double & a, const Complex & c)
{
    return Complex(c.real * a, c.imag * a);
}

Complex Complex::operator~() const
{
    return Complex(this->real, -(this->imag));
}

std::istream & operator>>(std::istream & is, Complex & c)
{
    std::cout << "Real: ";
    is >> c.real;
    std::cout << "Imaginary: ";
    is >> c.imag;
    
    return is;
}

std::ostream & operator<<(std::ostream & os, const Complex & c)
{
    os << "(" << c.real << ", " << c.imag << "i)" << std::endl;
    
    return os;
}
