from program import reverse

def test_answer():
  assert reverse('Hello') == 'olleH'
  assert reverse('Happy New Year.') == '.raeY weN yppaH'
