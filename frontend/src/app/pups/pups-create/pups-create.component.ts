import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators, NgForm, } from '@angular/forms';
import { NgxFileDropEntry, FileSystemFileEntry, FileSystemDirectoryEntry } from 'ngx-file-drop';
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
  public files: NgxFileDropEntry[] = [];
  file: File
  fileName: string =""

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

  onChangeMode(f: NgForm) {}

  public dropped(files: NgxFileDropEntry[]) {
    this.files = files;
    for (const droppedFile of files) {

      // Is it a file?
      if (droppedFile.fileEntry.isFile) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {

          // Here you can access the real file
          console.log(droppedFile.relativePath, file);
          this.file = file
          this.fileName = file.name

        });
      } else {
        // It was a directory (empty directories are added, otherwise only files)
        const fileEntry = droppedFile.fileEntry as FileSystemDirectoryEntry;
        console.log(droppedFile.relativePath, fileEntry);
      }
    }
  }

  public fileOver(event){
    console.log(event);
  }

  public fileLeave(event){
    console.log(event);
  }

  onSubmit(){
    const formData = new FormData()
    formData.append('file', this.file)
    /*отправить на сервер */
    console.log(formData.get('file'))
  }
}


