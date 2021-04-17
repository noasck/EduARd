import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-pups-read',
  templateUrl: './pups-read.component.html',
  styleUrls: ['./pups-read.component.scss']
})
export class PupsReadComponent implements OnInit {
  src: string = ""
  deletePupId = ""
  constructor() { }

  ngOnInit(): void {
  }

}
