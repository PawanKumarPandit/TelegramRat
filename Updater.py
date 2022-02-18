# Import modules

import os
import time
import shutil
import urllib.request


RAT_Version = urllib.request.urlopen('https://raw.githubusercontent.com/Bainky/Telegram-RAT/master/Version/Version.txt').read().decode('utf8').splitlines()[0]
RAT_Changelogs = urllib.request.urlopen('https://raw.githubusercontent.com/Bainky/Telegram-RAT/master/Version/Changelogs.txt').read().decode('utf8')
RAT_Link = 'https://github.com/Bainky/Telegram-RAT/archive/master.zip'
RAT_Path = 'Telegram-RAT.zip'


# Checking version Telegram-RAT

if RAT_Version == '2.7':
	print('No available updates.')
	input()
else:
	if os.path.exists('Updated Version ' + RAT_Version):
		print('Update is already installed.')
		input()
	else:
		print('Update available. Update now? y/n')
		print('\nChangelogs:\n' + RAT_Changelogs + '\n')
		if input().lower() == 'y'.lower():
			print('\nDownloading update...')
			urllib.request.urlretrieve(RAT_Link, RAT_Path)
			print('Unpacking archive...')
			shutil.unpack_archive(RAT_Path, 'Updated Version ' + RAT_Version)
			os.remove(RAT_Path)
			time.sleep(3)
			print('Update installed.')
			input()
