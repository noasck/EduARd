import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { BehaviorSubject, Observable } from 'rxjs';
import { map } from 'rxjs/operators';

import { EnvironmentUrlService } from './environment-url.service';
import { stringify } from '@angular/compiler/src/util';

export interface TokenResponse {
  'access_token': string;
  status: string;
}

@Injectable({ providedIn: 'root' })
export class AuthService {
    private currentUserSubject: BehaviorSubject<string>;
    public currentUser: Observable<string>;

    constructor(private http: HttpClient, private env: EnvironmentUrlService) {
        this.currentUserSubject = new BehaviorSubject<string>(JSON.parse(<string>localStorage.getItem('currentUser')));
        this.currentUser = this.currentUserSubject.asObservable();
    }

    public get currentUserValue(): string {
        return this.currentUserSubject.value;
    }

    login(socialToken: string): Observable<string> {
        return this.http.get<TokenResponse>(`${this.env.apiUrl}/users/login/${socialToken}`)
            .pipe(map(tokenResponse => {
                // store user details and jwt token in local storage to keep user logged in between page refreshes
                localStorage.setItem('currentUser', JSON.stringify(tokenResponse.access_token));
                this.currentUserSubject.next(tokenResponse.access_token);
                return tokenResponse.access_token;
            }));
    }

    logout(): void {
        // remove user from local storage to log user out
        localStorage.removeItem('currentUser');
        this.currentUserSubject.next("");
    }
}