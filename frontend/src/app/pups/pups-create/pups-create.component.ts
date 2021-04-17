import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-pups-create',
  templateUrl: './pups-create.component.html',
  styleUrls: ['./pups-create.component.scss']
})
export class PupsCreateComponent implements OnInit {
  createOption: string = '1'
  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
  }

  

}
