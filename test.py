class Expr:
    def __call__(self, **context):
        raise NotImplementedError("Подклассы должны реализовать метод __call__.")

    def d(self, wrt):
        raise NotImplementedError("Подклассы должны реализовать метод d.")
    
    def __neg__(self):
        return Product(Const(-1), self)

    def __pos__(self):
        return self

    def __add__(self, other):
        return Sum(self, other)

    def __sub__(self, other):
        return Sum(self, -other)

    def __mul__(self, other):
        return Product(self, other)

    def __truediv__(self, other):
        return Fraction(self, other)

class Const(Expr):
    def __init__(self, value):
        self.value = value
    
    def __call__(self, **context):
        return self.value
    
    def d(self, wrt):
        return Const(0)

class Var(Expr):
    def __init__(self, name):
        self.name = name
    
    def __call__(self, **context):
        return context[self.name] 
    
    def d(self, wrt):
        if self.name == wrt.name:
            return Const(1) 
        else:
            return Const(0)
        
class BinOp(Expr):
    def __init__(self, expr1, expr2):
        self.expr1, self.expr2 = expr1, expr2


class Sum(BinOp):
    def __call__(self, **kwargs):
        return self.expr1(**kwargs) + self.expr2(**kwargs)

    def d(self, var):
        return Sum(self.expr1.d(var), self.expr2.d(var))
    
class Product(BinOp):
    def __call__(self, **kwargs):
        return self.expr1(**kwargs) * self.expr2(**kwargs)

    def d(self, var):
        return Sum(Product(self.expr1.d(var), self.expr2), Product(self.expr1, self.expr2.d(var)))

class Fraction(BinOp):
    def __call__(self, **kwargs):
        return self.expr1(**kwargs) / self.expr2(**kwargs)

    def d(self, var):
        numerator = Sum(Product(self.expr1.d(var), self.expr2), 
                        Product(-self.expr1, self.expr2.d(var)))
        denominator = Product(self.expr2, self.expr2)
        return Fraction(numerator, denominator)


def newton_raphson(f, x0, eps=1e-4):
    x = x0
    while True:
        f_x = f(x=x)
        f_prime_x = f.d(Var("x"))(x=x)
        
        if f_prime_x == 0:
            raise ValueError("Производная равна нулю. Метод не может быть применен.")
        
        x_new = x - f_x / f_prime_x
        
        if abs(x_new - x) <= eps:
            return x_new
        
        x = x_new


V = Var
C = Const

print(C(5)(), 5)
print(C(5).d(V("x"))(), 0)
print(V("x")(x=5), 5)
print(V("x").d(V("y"))(x=5), 0)
print(V("x").d(V("x"))(x=5), 1)


print(Sum(V("x"), Fraction(V("x"), V("y")))(x=5, y=2.5), 7.0)
print(Fraction(Sum(C(5), V("y")), Product(V("x"), V("y")))(x=1, y=2), 3.5)
print(Fraction(Sum(C(5), V("y")), Product(V("x"), V("y"))).d(V("x"))(x=1, y=2), -3.5)
print(Fraction(Sum(C(5), V("y")), Product(V("x"), V("y"))).d(V("y"))(x=1, y=2), -1.25)


print((V("x") * V("x") / V("y"))(x=5, y=2.5), 10.0)

x = Var("x")
f = Const(-5) * x * x * x * x * x + Const(3) * x + Const(2)
zero = newton_raphson(f, 0.5, eps=1e-4)
zero, f(x=zero)
print(zero, 1.000000000001132)
print(f(x=zero), -2.490496697760136e-11)