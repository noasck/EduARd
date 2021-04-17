import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, NgForm, Validators } from '@angular/forms';
import { Timestamp } from 'rxjs/internal/operators/timestamp';
import { Pup, PupService } from '../pups.service';

@Component({
  selector: 'app-pups-create',
  templateUrl: './pups-create.component.html',
  styleUrls: ['./pups-create.component.scss']
})
export class PupsCreateComponent implements OnInit {
  createOption: string = "";
  currentPup: Pup = {name: ""};
  stage: number = 0;

  constructor(private formBuilder: FormBuilder, private pupS: PupService) { }

  ngOnInit(): void {
  }

  onChangeName(f: NgForm) {
    if (this.currentPup.name != "") {
      this.stage = 1;
      this.pupS.createPup(this.currentPup).subscribe(
        (data) => {
          console.log(data)
        }, (err) => {},
        () => {
          console.log("Completed")
        }
      );
    }
  }

  onChangeMode(f: NgForm) {
    
  }

}
