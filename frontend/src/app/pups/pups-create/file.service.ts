import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { RepositoryService } from '../../shared/services/repository.service';

export interface FileResponse {
  id: number;
  filename: string;
}

@Injectable({
  providedIn: 'root'
})
export class FileService {
  ROUTE = 'files/';

  constructor(private repo: RepositoryService) { }

  postFile(data): Observable<FileResponse> {
    return this.repo.create<FileResponse>(this.ROUTE, data);
  }

  getFiles(): Observable<FileResponse[]> {
    return this.repo.getData<FileResponse[]>(this.ROUTE);
  }

  deleteFile(filename): Observable<null> {
    return this.repo.delete<null>(this.ROUTE + filename)
  }

  getFileByName(filename): Observable<FormData> {
    return this.repo.getData<FormData>(this.ROUTE + filename);
  }
}