import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService } from 'src/app/shared/services/auth.service';
@Component({
  selector: 'app-login',
  templateUrl: './login-page.component.html',
  styleUrls: ['./login-page.component.scss']
})
export class LoginPageComponent implements OnInit {
  email: FormGroup
  constructor(public auth: AuthService, private router: Router) {
  }

  ngOnInit(): void {
    this.email = new FormGroup({
      email: new FormControl("", [
        Validators.required
      ])
    })
  }

  login(): void {
    setTimeout(() => {
      let token: string = 'juliasupruniuk23@gmail.com';
      this.auth.login(this.email.value.email).subscribe(
        (token) => {
          console.log('Token Request...');
        },
        (err) => { },
        () => this.router.navigate(['/pups/'])
      );
    }, 1000);
  }

}
