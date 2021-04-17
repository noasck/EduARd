import { Injectable, OnInit } from '@angular/core';
import { Observable } from 'rxjs';
import { RepositoryService } from 'src/app/shared/services/repository.service';
export interface Pup {
    join_code: string
    created_at: number
    id: number
    video_filename: string
    name: string
}
@Injectable({
    providedIn: 'root',
})
export class PupService {
    route = 'pups/';
    constructor(public repository: RepositoryService) {

    }

    getPups(): Observable<Pup[]> {
        return this.repository.getData<Pup[]>(this.route);
    }

    getPupsByID(id: number): Observable<Pup> {
        return this.repository.getData<Pup>(this.route + String(id));
    }

    updatePup(id: number, Pup: Pup): Observable<Pup> {
        return this.repository.update<Pup>(this.route + String(id), Pup);
    }

    search(str: string) {
        return this.repository.getData<Pup[]>(this.route + "search/" + str);
    }

    deletePupByID(id: number): Observable<null> {
        return this.repository.delete<null>(this.route + String(id));
    }

    createPup(Pup: Pup): Observable<Pup> {
        return this.repository.create<Pup>(this.route, Pup);
    }
}
