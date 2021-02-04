import { Component } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Router} from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'helloworld';
  name = "";
  email="";
  num:any;
  success:any;
  postData={}

  constructor(private http : HttpClient, public router: Router){}

  click_fun(){
    this.postData = {
      'add' : 'true',
      obj : {
        'name' : this.name,
        'email': this.email,
        'number': this.num 
      }

      
    }
  
    this.http.post("http://127.0.0.1:8000/database/women/", this.postData).subscribe(
      data =>{
        console.log(data);
        this.success = data;
      }
    );

    // this.router.navigate(['/home']);


  }

  // postData = {
  //   add : "ture",
  //   obj : {
  //     'id' : 12345,
  //     'name' : 'shirt',
  //     'color' : 'red',
  //     'size' : 'XL'
  //   }
  // }
  // constructor(private http : HttpClient){
  //     this.http.get("http://127.0.0.1:8000/database/women/").subscribe(data => {
  //       console.log(data);
  //       this.j = data;
  //     })

  //     // this.http.post("http://127.0.0.1:8000/", this.postData).subscribe(
  //     //   data => {
  //     //     console.log(data);
  //     //     this.j = data;
  //     //   }
  //     // )

  // } 
   
}
