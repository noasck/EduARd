import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ServerService } from 'src/app/shared/services/server.service';

export interface Timeline {
  seconds: number;
  model_filename: string;
  id?: number;
  pup_id: number;
}

@Injectable({
  providedIn: 'root'
})

export class TimelineService {
  ROUTE = 'timelines/';

  constructor(private server: ServerService) { }

  postTimeline(data): Observable<Timeline> {
    return this.server.create<Timeline>(this.ROUTE, data);
  }

  getTimeline(): Observable<Timeline[]> {
    return this.server.getData<Timeline[]>(this.ROUTE);
  }

}