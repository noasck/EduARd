import { environment } from '../../../environments/environment';
import { Injectable } from '@angular/core';

@Injectable({
    providedIn: 'root'
})
export class EnvironmentUrlService {
    public apiUrl: string = environment.apiAddress;
    constructor() { }
}