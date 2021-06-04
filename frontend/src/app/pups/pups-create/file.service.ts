import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { EnvironmentUrlService } from 'src/app/shared/services/environment-url.service';
import { ServerService } from 'src/app/shared/services/server.service';

export interface FileResponse {
  id: number;
  filename: string;
}

@Injectable({
  providedIn: 'root'
})
export class FileService {
  ROUTE = 'files/';

  constructor(private server: ServerService, private envUrl: EnvironmentUrlService) { }

  postFile(data): Observable<FileResponse> {
    return this.server.create<FileResponse>(this.ROUTE, data);
  }

  getFiles(): Observable<FileResponse[]> {
    return this.server.getData<FileResponse[]>(this.ROUTE);
  }

  deleteFile(filename): Observable<null> {
    return this.server.delete<null>(this.ROUTE + filename)
  }

  getFileByName(filename): Observable<FormData> {
    return this.server.getData<FormData>(this.ROUTE + filename);
  }

  getLink(filename): string{
    return `${this.envUrl.apiUrl}/${this.ROUTE}/${filename}`
  }
}