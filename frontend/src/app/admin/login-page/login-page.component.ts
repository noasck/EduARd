import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../shared/services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {
  constructor(private auth: AuthService, private router: Router) { }

  ngOnInit(): void {

  }

  clickLogin(): void {
    let token: string = 'jjok730@gmail.com';
    this.auth.login(token).subscribe(
      (token) => {
        console.log('Token Request...');
      },
      (err) => {},
      () => this.router.navigate(['/pups/'])
    );
  }
}