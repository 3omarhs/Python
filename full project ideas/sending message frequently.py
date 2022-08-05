import pyautogui as auto
import emoji

from time import sleep
count = 0

# for i in range(10):
while True:
	auto.write('.')
	auto.press('enter')
	sleep(0.01)
	count += 1
	print("count:", count)

'''
#
'''
# print("\U0001F33A")
# print(emoji.emojize(':hibiscus:', use_aliases=True))