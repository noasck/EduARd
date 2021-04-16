import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { AdminComponent } from './admin/admin.component';
import { LoginPageComponent } from './admin/login-page/login-page.component';
import { RegistrationComponent } from './admin/registration/registration.component';
import { PupsReadComponent } from './admin/pups/pups-read/pups-read.component';
import { PupsCreateComponent } from './admin/pups/pups-create/pups-create.component';

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
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
