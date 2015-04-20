from program import isArmstrong

def test_answer():
  assert isArmstrong(153)
  assert isArmstrong(371)
  assert not isArmstrong(150)
  assert not isArmstrong(1150)
