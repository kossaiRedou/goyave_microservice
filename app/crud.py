# %%
class calculator:
    def __init__(self, a:int or float, b: int or float):
        
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            self.a = a
            self.b = b
        
        else:
            raise TypeError("type error de variable")
        
        
    def add(self):
        return self.a + self.b
    
    
    def multiply(self):
        return self.a * self.b
# %%
calcul = calculator("a", 2)
print(calcul.add())
print(calcul.multiply())
# %%
