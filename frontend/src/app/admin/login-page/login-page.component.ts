import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/shared/services/auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {
  constructor(public auth: AuthService, private router: Router) {
  }

  ngOnInit(): void {
  }

  login(): void {
    setTimeout(() => {
      let token: string = 'juliasupruniuk23@gmail.com';
      this.auth.login(token).subscribe(
        (token) => {
          console.log('Token Request...');
        },
        (err) => { },
        () => this.router.navigate(['/pups/'])
      );
    }, 1000);
  }


}