  
import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginPageComponent } from './admin/login-page/login-page.component';
import { PupsCreateComponent } from './pups/pups-create/pups-create.component';
import { PupsReadComponent } from './pups/pups-read/pups-read.component';
import { AuthGuard } from './shared/services/auth.guard';
import { LandingPageComponent } from './landing-page/landing-page.component';
import { PupsComponent } from './pups/pups.component';

const routes: Routes = [
  {
    path: '', component: LandingPageComponent
  },
  {
    path: 'pups', component: PupsComponent, canActivate: [AuthGuard], children: [
      {
        path: '', pathMatch: "full", component: PupsReadComponent
      },
      {
        path: 'create', component: PupsCreateComponent
      },
    ]
  },
  {
    path: 'login', pathMatch: 'full', component: LoginPageComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})

export class AppRoutingModule { }