# Classes allow you to make instances of that class
# Classes are also objects themselves
# L> Type of class is 'type'
# 42 -> int -> type

class A:
  msg: str = "hello"
  score: int = 999

  def reduce_score(self):
    self.score-=1
    print(self.score)

def make_A():
  name = "A"
  bases = ()

  msg: str = "hello"
  score: int = 999

  def reduce_score(self):
    self.score -= 1
    print(self.score)
  
  namespace = {"msg": msg, "score": score, "reduce_score": reduce_score}
  A = type(name, bases, namespace)
  return A

if __name__ == "__main__":
  a0 = A()
  A2 = make_A()
  a1 = A2()

  a0.reduce_score()
  print(a0.msg)

  a1.reduce_score()
  print(a1.msg)