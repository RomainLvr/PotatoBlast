**Potato Blast**

This game is a 2D game where you are programming a cannon to blast falling potatoes using ammo shot vertically from the ground. You need to avoid the falling potatoes, because they will destroy your cannon if they fall on it. 

This game has been developped by Samuel LAUNAY, Romain LECOUVREUR and Victorien GONTIER--DURAND during 3rd year of BUT Informatique's Advanced programming courses, while learning Python and good developpement practises like SOLID developpement and Test-Driven development.
	
🎲 Game rules: 
- Deadly potatoes with a shown lifebar fall from the sky and bounce on the ground 
- Your program controls the horizontal movement of your cannon, in order to avoid the falling potatoes and to shoot on them when they are in the shy
- When the lifebar of the potatoes gets empty, the potato disappears and randomly drops temporary powerups for the agent, and the score of your agent increases
- When a potato gets destroyed, you can acquire one of these temporary power-ups : 
	* Freeze : The potatoes stop moving
	* Double bullets : The cannon shoots two bullets instead of one
	* Invincible : Your cannon cannot get destroyed
- If the cannon gets too close too a potato when it hits the ground, you get destroyed and your score and power-ups get reset
- The games never ends, the goal is to get the biggest score possible

![Sequence diagram](https://github.com/RomainLvr/PotatoBlast/blob/main/pictures/sequence.png)
