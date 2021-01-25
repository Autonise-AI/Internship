import { Component } from '@angular/core';

@Component({
  selector: 'app-tab3',
  templateUrl: 'tab3.page.html',
  styleUrls: ['tab3.page.scss']
})
export class Tab3Page {
  
  public otherList: string[] = ['other1.jpg', 'other2.jpg', 'other3.jpg', 'other4.jpg'];
  constructor() {}
}
