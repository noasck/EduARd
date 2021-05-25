import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RepositoryService } from 'src/app/shared/services/repository.service';

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

  constructor(private repo: RepositoryService) { }

  postTimeline(data): Observable<Timeline> {
    return this.repo.create<Timeline>(this.ROUTE, data);
  }

  getTimeline(): Observable<Timeline[]> {
    return this.repo.getData<Timeline[]>(this.ROUTE);
  }

}