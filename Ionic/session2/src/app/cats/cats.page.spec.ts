import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { IonicModule } from '@ionic/angular';

import { CatsPage } from './cats.page';

describe('CatsPage', () => {
  let component: CatsPage;
  let fixture: ComponentFixture<CatsPage>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CatsPage ],
      imports: [IonicModule.forRoot()]
    }).compileComponents();

    fixture = TestBed.createComponent(CatsPage);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
