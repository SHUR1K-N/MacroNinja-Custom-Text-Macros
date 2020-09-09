# MacroNinja: Simple Custom Text Macros
## Description
A super simple tool that will send custom user-defined text from your keyboard whenever a user-defined key combination is pressed.

This package contains two editable and user-friendly .CFG files (Soft Macros.cfg and Hard Macros.cfg), holding ten macros each.

## Default Macros & Usage
Soft macro modifier key(s): **Ctrl**

Hard macro modifier key(s): **Ctrl + Alt**

|   	|  While Ctrl pressed	|While Ctrl + Alt pressed|
|-------| 	------------ 	| 	------------	 |
|1.	|Thank you, ma'am!	|Thank you, sir!	 |
|2.	|Yes, ma'am.		|Yes, sir.		 |
|3.	|Okay, ma'am.		|Okay, sir.		 |
|4.	|Understood, ma'am.	|Understood, sir.	 |
|5.	|empty			|empty			 |
|6.	|empty			|empty			 |
|7.	|empty			|empty			 |
|8.	|empty			|empty			 |
|9.	|empty			|empty			 |
|0.	|empty			|empty			 |


## Optimization
Since the program is designed to indefinitely listen for key strokes until terminated in order to serve its purpose, the consumption of resources (CPU) has also been minimized and optimized; so the program can be left running in the background for as long as required, or even be scheduled to run automatically at every system start (by placing MacroNinja (Headless).pyw in the **\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup** directory) without any prominent CPU usage.

This project was created in Python and has both versions — headless (will run in the background) and windowed (will have a window with a macro-key guide open).

## Dependencies you may have to "pip install"

**keyboard** (for keyboard control/listening)

My website: http://bit.do/SHUR1KN