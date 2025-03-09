import webview
import subprocess
import os
# import archinstall

# import pathlib
# import json

import tkinter as tk # For Screen Resolution Detection

class Api:
	def test_func(self):
		print("bruh")

root = tk.Tk()

displayWidth = root.winfo_screenwidth()
displayHeight = root.winfo_screenheight()

print('Starting AzuOS Installer...')

# Instantiate Api class
api = Api()

webview.settings = {
	'ALLOW_FILE_URLS': True,
	'ALLOW_DOWNLOADS': True,
	'OPEN_DEVTOOLS_IN_DEBUG': False
}

# webview.create_window('AzuOS Installer', url="index.html", background_color='#000000', js_api=api, fullscreen=True, width=displayWidth, height=displayHeight)

webview.create_window('AzuOS Installer', url="index.html", background_color='#000000', js_api=api, width=1280, height=720)

webview.start(gui='qt', debug=True)
