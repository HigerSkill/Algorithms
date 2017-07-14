//
//  complex.hpp
//

#ifndef complex_hpp
#define complex_hpp

#include <stdio.h>
#include <iostream>

class Complex
{
private:
    double imag;
    double real;
    
public:
    Complex();
    Complex(double, double);
    ~Complex();
    
    Complex operator~() const; 
    
    friend Complex operator+(const Complex & a, const Complex & b);
    friend Complex operator-(const Complex & a, const Complex & b);
    friend Complex operator*(const Complex & a, const Complex & b);
    friend Complex operator*(const double & a, const Complex & c);
    
    friend std::istream & operator>>(std::istream & is, Complex & c);
    friend std::ostream & operator<<(std::ostream & os, const Complex & c);
};

#endif /* complex_hpp */
