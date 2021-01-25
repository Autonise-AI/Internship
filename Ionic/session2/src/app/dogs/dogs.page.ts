import { Component, OnInit } from '@angular/core';
import { AnimalService } from '../services/animal.service';

@Component({
  selector: 'app-dogs',
  templateUrl: './dogs.page.html',
  styleUrls: ['./dogs.page.scss'],
})
export class DogsPage implements OnInit {

  public dogList = [];
  constructor(private animalservice: AnimalService) { }

  ngOnInit() {
    this.displayDogs('pug');
  }

  displayDogs(breed: string){
    this.dogList = [];
    for (let i = 0; i < 10; i++) {
      this.animalservice.getDogs(breed).subscribe((res: any) => {
        this.dogList.push(res.message);
      }
      );      
    }
  }

}
