import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {NgbModule} from '@ng-bootstrap/ng-bootstrap';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { AdminComponent } from './admin/admin.component';
import { LoginPageComponent } from './admin/login-page/login-page.component';
import { RegistrationComponent } from './admin/registration/registration.component';
import { PupsReadComponent } from './admin/pups/pups-read/pups-read.component';
import { PupsCreateComponent } from './admin/pups/pups-create/pups-create.component';
import { FormsModule } from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent,
    LandingPageComponent,
    AdminComponent,
    LoginPageComponent,
    RegistrationComponent,
    PupsReadComponent,
    PupsCreateComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NgbModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
