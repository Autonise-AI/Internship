import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class AnimalService {

  constructor(private http: HttpClient) { }

  getDogs(breed: string){
    return this.http.get('https://dog.ceo/api/breed/' + breed + '/images/random');
  }
}
