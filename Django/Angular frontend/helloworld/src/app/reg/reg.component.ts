import { Component, OnInit } from '@angular/core';
import {Router} from '@angular/router';

@Component({
  selector: 'app-reg',
  templateUrl: './reg.component.html',
  styleUrls: ['./reg.component.css']
})
export class RegComponent implements OnInit {
  title = 'helloworld';
  name = "";
  email="";
  num:any;
  success:any;

  constructor(public router: Router) { }

  ngOnInit(): void {
  }

  click_fun(){
    this.router.navigate(['/home']);
  }

}
