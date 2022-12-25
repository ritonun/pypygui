PyPyGui
=============

PyPyGui is a GUI/HUD library for pygame.

## WIP
current work: refactor class behavior  
	-> Global GUI class  
	-> Label class  
	-> Button class  
	-> create button from label, img, or nothing  
	-> attribute properties to button (outline, color, behavior when clicked or not, ...)  

## v0.3.0
Focus on gui element:  
- [x] slider
- [ ] integration of all gui element in Menu()
- [ ] input
- [ ] checkbox
- [ ] varrying between different option with arrow

## v0.2.0
- [x] Gui global class to handle all gui elements
- [x] label class
- [ ] button class (clickable)
- [ ] button properties (all resizable)
	- [ ] outline
	- [x] image based
	- [x] text
	- [x] rect
- [ ] auto-resize all elements
- [x] No blurry/unclear text -> always scaled up to screen
- [x] fonts selector

## v0.1.0
- [x] Label  
- [x] Button
- [x] Menu (auto-layout)
- [x] Templates color
- [x] menu self mainloop
- [ ] nice defaults templates

## Future function
- [ ] Hud elements (img)
- [ ] auto-doc with sphynx
- [ ] select multiple font (or custom)
- [ ] refactor: change menu element so adding a label deont add a label, but a general element() function customize for label, same for buttons etc...
- [ ] tests/ unittest
- [ ] fix res path import problem
- [ ] include docs in package
