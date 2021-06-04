import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { EnvironmentUrlService } from './environment-url.service';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ServerService {
  public accessToken: string | undefined;

  constructor(private http: HttpClient, private envUrl: EnvironmentUrlService) {
  }

  public getData<T>(route: string): Observable<T> {
    return this.http.get<T>(this.createCompleteRoute(route, this.envUrl.apiUrl), {headers: this.generateHeaders()});
  }

  public create<T>(route: string, body: any): Observable<T> {
    return this.http.post<T>(this.createCompleteRoute(route, this.envUrl.apiUrl), body);
  }

  public update<T>(route: string, body: any): Observable<T> {
    return this.http.put<T>(this.createCompleteRoute(route, this.envUrl.apiUrl), body, {headers: this.generateHeaders()});
  }

  public delete<T>(route: string): Observable<T> {
    return this.http.delete<T>(this.createCompleteRoute(route, this.envUrl.apiUrl), { headers: this.generateHeaders() });
  }
  
  private createCompleteRoute = (route: string, envAddress: string) => {
    return `${envAddress}/${route}`;
  }
  private generateHeaders(): HttpHeaders  {
    return new HttpHeaders({
        'Content-Type': 'application/json'
      });
  }
}