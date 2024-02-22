from main import *



## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(3)) == 3*3
  assert quadratic_multiply(BinaryNumber(10), BinaryNumber(3)) == 10*3
  assert quadratic_multiply(BinaryNumber(20), BinaryNumber(2)) == 20*2
  
