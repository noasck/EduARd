import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PupsComponent } from './pups.component';

describe('PupsComponent', () => {
  let component: PupsComponent;
  let fixture: ComponentFixture<PupsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PupsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PupsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
