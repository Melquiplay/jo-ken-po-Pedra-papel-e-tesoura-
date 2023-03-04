import random
es = str(input('tu escolhe pedra, papel ou tesoura? ')).lower().strip()
nu = random.randint(1, 3)
if es == 'pedra' and nu == 1:
  print('deu empate, eu joguei pedra')
elif es == 'pedra' and nu == 2:
  print('eu ganhei, eu joguei papel. hehehe')
elif es == 'pedra' and nu == 3:
  print('voce ganhou, eu joguei tesoura!')
elif es == 'papel' and nu == 1:
  print('vc ganhou, eu joguei pedra.')
elif es == 'papel' and nu == 2:
  print('deu empate, eu tambem joguei papel rsrsr!')
elif es == 'papel' and nu == 3:
  print('ganheei eu joguei tesoura 😃!')
elif es == 'tesoura' and nu == 1:
  print('eu ganhei, eu joguei pedra ksksksksk.')
elif es == 'tesoura' and nu == 2:
  print('tu ganhou 🙁 eu joguei papel!')
elif es == 'tesoura' and nu == 3:
  print('deu empate zé. também joguei tesoura, shahshahsha!')
else:
  print('mano cê tem demencia? é só pedra papel e tesoura kkkk, é escreve direito esse bagulho ')
  