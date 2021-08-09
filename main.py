import numpy as np

class Variable():
  def __init__(self, x):
    self.computed_value = x
    self.grad = 0

  def set(self, x):
    self.computed_value = x
    self.grad = 0

  def derivate(self, prop_grad=1):
    self.grad = prop_grad

  def compute(self):
    return self.computed_value

  def __add__(self,other):
    return Plus(self,other)

  def __mul__(self,other):
    return Multiply(self,other)


class Tensor():
  def __init__(self,x):
    try:
      x = np.array(x)
    except:
      print("invalid input type")
    for i in x:
      i = Variable(i)
    self.vals = x

  def shape(self):
    return self.vals.shape


class Function():
  def __init__(self, *args):
    self.children = args
    self.computed_value = None
    self.grad = None

  def calculate_gradient(self):
    self.derivate()


  def __add__(self,other):
    return Plus(self,other)

  def __sub__(self,other):
    return Minus(self,other)

  def __mul__(self,other):
    return Multiply(self,other)



class Plus(Function):
  def compute(self):
    self.computed_value = self.children[0].compute() + self.children[1].compute()
    return self.computed_value

  def derivate(self,prop_grad=1):
    self.grad = prop_grad
    self.children[0].derivate(prop_grad)
    self.children[1].derivate(prop_grad)

class Minus(Function):
  def compute(self):
    self.computed_value = self.children[0].compute() - self.children[1].compute()
    return self.computed_value

  def derivate(self,prop_grad=1):
    self.grad = prop_grad
    self.children[0].derivate(prop_grad)
    self.children[1].derivate(-prop_grad)

class Multiply(Function):
  def compute(self):
    self.computed_value = self.children[0].compute() * self.children[1].compute()
    return self.computed_value

  def derivate(self,prop_grad=1):
    self.grad = prop_grad
    self.children[0].derivate(prop_grad*self.children[1].computed_value)
    self.children[1].derivate(prop_grad*self.children[0].computed_value)






expression = Variable(3)*Variable(8) + Variable(2) + Variable(1)- Variable(4)*Variable(120)

print(expression.compute())


input_tensor = Tensor([[1,2,3],[1,2,3]])
print(input_tensor.shape())

