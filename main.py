import time
import random

# 最小値、最大値、試行回数を設定するときの関数
def get_number(prompt, minValue=None):
  while True:
    value = input(prompt)
    try:
      value = int(value)
      if minValue is not None and value <= minValue:
        print(f"\n{minValue}よりも大きい値を入力してください\n")
        continue
      return value
    except ValueError:
      print('\n数字が入力されていません\n')

# ゲームの説明文を表示する
print('このゲームは設定した範囲の数字を当てるゲームです。\n'
      '例えば、最小値を1に最大値を3に設定すると1から3までの数字の中でランダムな数字が設定されます。'
      '\n事前に設定した試行回数までにその数字を当てれたらクリアです。\n'
      )

while input('enterを押して条件を設定する\n') != '':
  continue

# ゲームの設定
minNum = get_number('\n最小値を設定してください\n')
maxNum = get_number('\n最大値を設定してください\n', minNum)
tryCount = get_number('\n試行回数を設定してください\n', 0)

# ランダムな数字を生成して1秒待つ
print('\nランダムな数字を設定しています...')
randomNum = random.randint(minNum, maxNum)
time.sleep(1.5)
print('\n\nゲームを開始します\n')
time.sleep(1)

# 試行回数だけ数字を当てさせる
for count in range(tryCount):
  print(f"{str(count + 1)}回目の挑戦です")
  guessNum = input(f"{str(minNum)}から{str(maxNum)}までの数字を当ててください。\n")
  try:
    guessNum = int(guessNum)
    if guessNum < minNum or guessNum > maxNum:
      print('\n範囲外の数字です\n\n')
      continue
  except ValueError:
     print('\n数字が入力されていません\n')
     continue
  else:
    if guessNum == randomNum:
      print('\n正解です！おめでとうございます！')
      break
    else:
      print('\n不正解です\n\n')
      continue
else:
  print('ゲームオーバー！またの挑戦をお待ちしてます！')