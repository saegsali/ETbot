# ETbot

A simple discord bot which can send the lecture links.

### secrets.py
This file contains the secret token and the channel id.
Create this file and add this line:
```
token = "<your_token>"
message_channel_id = <channel_id>
```


### data.json
This file contains all course informations.  
Create this file and add some courses like in this example:
```
{
	
	"courses": [
		{
			"name": "physics lecture",
			"key": "vphysics",
			"link": "https://google.com",
			"day": "monday",
			"time": "08:10",
			"message": "have fun"
		},
		{
			"name": "mathematics lecture",
			"key": "vmath",
			"link": "https://google.com",
			"day": "monday",
			"time": "10:10",
			"message": "have fun"
		}
	]

}
```
