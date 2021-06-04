import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { ServerService } from 'src/app/shared/services/server.service';

export interface Pup {
    id?: number;
    name: string;
    video_filename?: string;
}

@Injectable({
    providedIn: 'root',
})
export class PupService {
    route = 'pups/';
    constructor(public server: ServerService) {

    }

    getPups(): Observable<Pup[]> {
        return this.server.getData<Pup[]>(this.route);
    }

    getPupsByID(id: number): Observable<Pup> {
        return this.server.getData<Pup>(this.route + String(id));
    }

    updatePup(id: number, Pup: Pup): Observable<Pup> {
        return this.server.update<Pup>(this.route + String(id), Pup);
    }

    search(str: string) {
        return this.server.getData<Pup[]>(this.route + "search/" + str);
    }

    deletePupByID(id: number): Observable<null> {
        return this.server.delete<null>(this.route + String(id));
    }

    createPup(Pup: Pup): Observable<Pup> {
        return this.server.create<Pup>(this.route, Pup);
    }
}
