# ETbot

A simple discord bot which can send the lecture links.

### secrets.py
This file contains the secret token.  
Create this file and add this line:
`token = "<your_token>"`

### data.json
This file contains all course informations.
Create this file and add a course like in this example:
```
{
	
	"courses": [
		{
			"name": "physics lecture",
			"key": "vphysics",
			"link": "https://google.com",
			"day": "monday",
			"time": "08:10"
		},
		{
			"name": "mathematics lecture",
			"key": "vmath",
			"link": "https://google.com",
			"day": "monday",
			"time": "10:10"
		}
	]

}
```
