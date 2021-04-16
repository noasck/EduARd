import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PupsReadComponent } from './pups-read.component';

describe('PupsReadComponent', () => {
  let component: PupsReadComponent;
  let fixture: ComponentFixture<PupsReadComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PupsReadComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PupsReadComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
