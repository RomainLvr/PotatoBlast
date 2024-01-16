## 🥔 **Potato Blast**

This game is a 2D game where you are programming a cannon to blast falling potatoes using ammo shot vertically from the ground. You need to avoid the falling potatoes, because they will destroy your cannon if they fall on it. 

This game has been developped by Samuel LAUNAY, Romain LECOUVREUR and Victorien GONTIER--DURAND during 3rd year of BUT Informatique's Advanced programming courses, while learning Python and good developpement practises like SOLID developpement and Test-Driven development.
	
🎲 **Game rules**
- Deadly potatoes with a shown lifebar fall from the sky and bounce on the ground 
- Your program controls the horizontal movement of your cannon, in order to avoid the falling potatoes and to shoot on them when they are in the shy
- When the lifebar of the potatoes gets empty, the potato disappears and randomly drops temporary powerups for the agent, and the score of your agent increases
- When a potato gets destroyed, you can acquire one of these temporary power-ups : 
	* Freeze : The potatoes stop moving
	* Double bullets : The cannon shoots two bullets instead of one
	* Invincible : Your cannon cannot get destroyed
- If the cannon gets too close too a potato when it hits the ground, you get destroyed and your score and power-ups get reset
- The games never ends, the goal is to get the biggest score possible

⚙ **Admin case**
- To launch an arena with potato blast, simply clone the project from this github link directly: https://github.com/RomainLvr/PotatoBlast .
- To ensure that the game runs smoothly, you'll need to run the PotatoBlast.py program. This program will initialize the arena and activate 2 referees, one for the players and one for the potatoes.

⚙ **Player case**
- More information on README_API.md

📊 **Sequence Diagram**

![Sequence diagram](https://github.com/RomainLvr/PotatoBlast/blob/main/doc/sequence.png)

**Prerequisites**
*Admin*
- To run the project, you need a computer with python installed.
*Player*
- More information on README_API.md

**Installation**
- Clone our project on github.
- Enter your connection variables in an .env folder that you must create in the src/server folder.
- Run PotatoBlast.py to initialize the arene and its parameters

**Tests**
- 

**Roadmap**
- 1. Implementation of several potato profiles (more life, etc.)
- 2. Optimizing potato movement
- 3. Smooth movement type added to make the game more pleasing to the eye.

🖼️ **Maquette**
![Maquette](https://github.com/RomainLvr/PotatoBlast/blob/main/doc/maquette.png)

**Autors**
*PotatoBlast *
- Launay Samuel
- Lecouvreur Romain
- GOntier--DUrand Victorien
*J2L api*
- Julien Arne

**Licence**
Copyright 2024

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.