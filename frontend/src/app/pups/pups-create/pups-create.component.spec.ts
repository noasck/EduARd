import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PupsCreateComponent } from './pups-create.component';

describe('PupsCreateComponent', () => {
  let component: PupsCreateComponent;
  let fixture: ComponentFixture<PupsCreateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PupsCreateComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PupsCreateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
