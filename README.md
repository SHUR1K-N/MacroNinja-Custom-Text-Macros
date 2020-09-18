# MacroNinja: Simple Custom Text Macros

## Description
A super simple tool that will send user-defined text from your keyboard whenever a user-defined key combination is pressed. It comes with two editable and user-friendly .CFG files (Soft Macros.cfg and Hard Macros.cfg), holding ten macros each.

This project was created in Python, for personal use with sending semi-automated chat messages while attending online lectures in a state of semi-comatose sleepiness. It has both versions — headless (will run in the background) and windowed (will have a window with a macro-key guide open).

## Default Macros & Usage
- Soft macro modifier key(s): **CTRL**
- Hard macro modifier key(s): **CTRL + ALT**

|   	|While CTRL pressed	|While CTRL + ALT pressed|
|-------|-----------------------|------------------------|
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

<div align="center">
<img src="https://github.com/SHUR1K-N/MacroNinja-Simple-Custom-Text-Macros/blob/master/Images/Example.png" >
<p>Example Execution</p>
</div>


## Optimization
Since the program is designed to indefinitely listen for key strokes until terminated in order to serve its purpose, the consumption of resources (CPU) has also been minimized and optimized; so the program can be left running in the background for as long as required, or even be scheduled to run automatically at every system start (by placing "MacroNinja (Headless).pyw" in the **\Users\USERNAME\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup** directory) without any prominent CPU usage.

## Dependencies to PIP-Install
- **keyboard** (for keyboard control/listening)

------------

My website: http://bit.do/SHUR1KN
