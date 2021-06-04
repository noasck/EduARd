import { Component, OnInit } from '@angular/core';
import { AuthService } from '../shared/services/auth.service';

@Component({
  selector: 'app-landing-page',
  templateUrl: './landing-page.component.html',
  styleUrls: ['./landing-page.component.scss']
})
export class LandingPageComponent implements OnInit {
  authenticated: boolean

  constructor(private auth: AuthService) {

  }
  ngOnInit(): void {
  }

  isActive(): boolean {
    return this.auth.isActive()
  }
}