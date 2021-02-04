# Django Backend
The demo project is in `mysite`; which contains 2 apps `main` (day 1) and `chat`(day 2) [chat django tutorial](https://channels.readthedocs.io/en/stable/tutorial/index.html). 

`main` django app is where we made API.

```bash 
# run django server 
~/mysite/$ python3 manage.py runserver
```

## API 
* json database
```JSON
 {
"database": {
     "men": [
        {"name": "t-shirt", "price": "999", "size": "M", "color": "black"},
        {"name": "t-shirt", "price": "899", "size": "L", "color": "brown"}
    ],

     "women": []
     }
}
```

* Views and urls
  - "http://127.0.0.1:8000/database/"  >>> views.helloworld()
  - "http://127.0.0.1:8000/database/men/" >>> views.funMen()
  - "http://127.0.0.1:8000/database/women/" >>>  views.funWomen()
  - "http://127.0.0.1:8000/chat/" >>>  Chat app

- **Dont forget to start the redis server to use Chat app**, `$ docker run -p 6379:6379 -d redis:5`




---
## Angular frontend 
* Angular routing example 
```TS
    import {Router} from '@angular/router'; 
    // get the router object in constructor
    constructor(private http : HttpClient, public router: Router) {} 
    click_function() { 
        // redirect to home page if login credentials are correct else again to login like this 
        
        // Call http.post() here to get data from Django backend then with the data we received from backend we can redirect page using below code.
    this.router.navigate(['/home']);   
    // /home is the path for the component we want to redirect.
    }
```

* Post request data format from angular to django 
```JSON
{
      "add" : "true",
      "obj" : {
        "name" : this.name,
        "email": this.email,
        "number": this.num 
      }
}
```

- **If your backend works in postman and it does not work with angular look for CORS error in chrome terminal**, see the day 2 video for CORS error.

* Posting data on API from angular
```TS
this.http.post("http://127.0.0.1:8000/database/women/", this.postData).subscribe(
      data =>{
        console.log(data);
        this.success = data;
      }
    );
``` 
---
### Others
* inside the `other` folder
```
|-- db.json
|-- db.py
|-- req.py
`-- sync.py
```
- db.py file have the read and write function 
- req.py file have the code for requests library
- sycn.py file have the code for async and await use cases in python
---

**NOTE**

Look into slides for any other assistance

---




