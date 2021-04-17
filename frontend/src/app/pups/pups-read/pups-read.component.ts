import { Component, OnInit } from '@angular/core';
import { Pup, PupService } from '../pups.service';

@Component({
  selector: 'app-pups-read',
  templateUrl: './pups-read.component.html',
  styleUrls: ['./pups-read.component.scss']
})
export class PupsReadComponent implements OnInit {
  src: string = ""
  deletePupId: number = 0
  fetchedPups: Pup[] = []
  errorMessage: string = ""
  pay: boolean = false

  constructor(private pupsService: PupService) { }

  ngOnInit(): void {
    this.pupsService.getPups().subscribe(
      (res) => {
        this.fetchedPups = res
      },
      (error) => {
        this.errorMessage = error;
      },
      () => {
      }
    )
  }

  deletePup(id: number) {
  this.pupsService.deletePupByID(id).subscribe(
      () => {
        this.fetchedPups = this.fetchedPups.filter((pup) => pup.id != id);
      },
      (error) => {
        this.errorMessage = error;
      },
      () => {
        this.deletePupId = 0;
      }
    )
  }

  delegateDelete(id: number | undefined) {
    this.deletePupId = <number>id;
  }
}
