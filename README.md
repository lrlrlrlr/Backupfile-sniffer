## What is backup file?  
Many text editors on Linux (vim, gedit, etc) create backup files whilst you are editing a file. This means that if you are editing ’index.php’, ’index.php ’ will be made. In PHP (and other) configurations this is very dangerous because now everyone can read the file in plaintext.  

It’s a simple but common error often overlooked by system administrators.
	

	
	
## My program structure:
	Class URLHandler:
		a. Handle the url that input by the user;
		b. Test if the url is_reachable by sending a request;
		c. Generate all possible backup file url (text processing)
	Class Files_Hunter:
		a. Sniff if the url is reachable generated in URLHandler;
		b. Present the result.


## My program logic && Practical Use
Please check the doc:   
<https://drive.google.com/open?id=1LgejvQUzPJO2mkwgElzcWCwl13wPKeCi>
