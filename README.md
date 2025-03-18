# setup
- create a directory for the game
- create a virtual environment at the top level of the directory
	- `python3 -m venv venv`
		- Virtual environments (venv) in python keep dependncies separate from other projects
- `source venv/bin/activate` activates the virtual environment
- create `requirements.txt` with text `pygame==2.6.1`
- `pip install -r requirements.txt`


Add a scoring system
Implement multiple lives and respawning
Add an explosion effect for the asteroids
Add acceleration to the player movement
Make the objects wrap around the screen instead of disappearing
Add a background image
Create different weapon types
Make the asteroids lumpy instead of perfectly round
Make the ship have a triangular hit box instead of a circular one
Add a shield power-up
Add a speed power-up
Add bombs that can be dropped
