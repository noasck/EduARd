import { Component, OnInit } from '@angular/core';
import { AuthService } from '../shared/services/auth.service';

@Component({
  selector: 'app-pups',
  templateUrl: './pups.component.html',
  styleUrls: ['./pups.component.scss']
})
export class PupsComponent implements OnInit {

  constructor(private auth: AuthService) {

  }
  ngOnInit(): void {
  }

  logout() {
    this.auth.logout()
  }
}