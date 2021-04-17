import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';

@Component({
  selector: 'app-pups-create',
  templateUrl: './pups-create.component.html',
  styleUrls: ['./pups-create.component.scss']
})
export class PupsCreateComponent implements OnInit {
  createOption: string = ''
  constructor() { }

  ngOnInit(): void {

      console.log(this.createOption)
  }

}
