PyPyGui 
=============

PyPyGui is a GUI library for pygame. It is made to easily handle all gui elements.

## ToDo
### WIP
current work: refactor menu to use new class for label, button, etc...
1. refactor button class with inheritance
2. add properties to button with outline
3. add other properties

### v0.5.0
Focus on gui element:  
- [x] slider
- [ ] integration of all gui element in Menu()
- [ ] input
- [ ] checkbox
- [ ] varrying between different option with arrow

### v0.4.0
- [ ] refactor menu to use new class for label, button, etc...

### v0.3.0
- [ ] refactor Button Class with inheritance
- [ ] add properties to all Gui element
	- [ ] outline
	- [ ] background color
	- [ ] animation
	- [ ] active/unactive state
	- [ ] sound ?
	- [ ] easy to create own properties and add to it
- [ ] ButtonImage -> pos center option

### v0.2.0
- [x] Gui global class to handle all gui elements
- [x] label class
- [x] button class (clickable)
- [x] button properties (all resizable)
	- [x] image based
	- [x] text
	- [x] rect
- [x] auto-resize all elements
- [x] No blurry/unclear text -> always scaled up to screen
- [x] fonts selector

### v0.1.0
- [x] Label  
- [x] Button
- [x] Menu (auto-layout)
- [x] Templates color
- [x] menu self mainloop
- [ ] nice defaults templates

### Future function
- [ ] Hud elements (img)
- [ ] auto-doc with sphynx
- [ ] select multiple font (or custom)
- [ ] refactor: change menu element so adding a label deont add a label, but a general element() function customize for label, same for buttons etc...
- [ ] tests/ unittest
- [ ] fix res path import problem
- [ ] include docs in package
