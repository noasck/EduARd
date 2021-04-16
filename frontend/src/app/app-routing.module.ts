import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { AdminComponent } from './admin/admin.component';

import { LoginPageComponent } from './admin/login-page/login-page.component';
import { PupsCreateComponent } from './admin/pups/pups-create/pups-create.component';
import { PupsReadComponent } from './admin/pups/pups-read/pups-read.component';
import { AuthGuard } from './auth.guard';
import { LandingPageComponent } from './landing-page/landing-page.component';

const routes: Routes = [
  {
    path: '', component: LandingPageComponent
  },
  {
    path: 'admin', component: AdminComponent,canActivate: [AuthGuard], children: [
      {path: 'pups', component: PupsReadComponent, children: [
        {path: 'create', component: PupsCreateComponent}
      ]}
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
