import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
//import { ErrorInterceptor } from '../shared/services/http-interceptors/error.interceptor';

@Component({
  selector: 'app-errors',
  templateUrl: './errors.component.html',
  styleUrls: ['./errors.component.scss']
})
export class ErrorsComponent implements OnInit {

  @Input() error: string
  @Output() close = new EventEmitter<void>()

  constructor() { }

  ngOnInit(): void {
  }


}
