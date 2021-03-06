import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators, NgForm, } from '@angular/forms';
import { NgxFileDropEntry, FileSystemFileEntry, FileSystemDirectoryEntry } from 'ngx-file-drop';
import { Pup, PupService } from '../pups.service';
import { FileService } from './file.service'

@Component({
  selector: 'app-pups-create',
  templateUrl: './pups-create.component.html',
  styleUrls: ['./pups-create.component.scss']
})
export class PupsCreateComponent implements OnInit {
  createOption: string = "";
  currentPup: Pup = { name: "" };
  stage: number = 0;
  public files: NgxFileDropEntry[] = [];
  public videofiles: NgxFileDropEntry[] = [];

  file: File
  fileName: string = ""
  uploadedFile = false

  videofile: File
  uploadedVideo = false
  videofileName: string = ""
  link: string

  form: FormGroup;

  constructor(private pupS: PupService, private fileService: FileService, private formBuilder: FormBuilder) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      avatar: []
    });

  }

  onChangeName(f: NgForm) {
    if (this.currentPup.name != "") {
      this.stage = 1;
      this.pupS.createPup(this.currentPup).subscribe(
        (data) => {
          console.log(data)
        }, (err) => { },
        () => {
          console.log("Completed")
        }
      );
    }
  }

  onChangeMode(f: NgForm) {
  }

  public droppedFile(files: NgxFileDropEntry[]) {
    this.files = files;
    for (const droppedFile of files) {

      // Is it a file?
      if (droppedFile.fileEntry.isFile && (this.createOption == '0')) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {

          // Here you can access the real file
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


  public droppedVideo(files: NgxFileDropEntry[]) {
    this.videofiles = files;
    for (const droppedFile of files) {

      // Is it a file?
      if (droppedFile.fileEntry.isFile && (this.createOption == '1')) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {

          // Here you can access the real file
          this.videofile = file
          this.videofileName = file.name

          this.onSubmitVideo()
        });
      } else {
        // It was a directory (empty directories are added, otherwise only files)
        const fileEntry = droppedFile.fileEntry as FileSystemDirectoryEntry;
        console.log(droppedFile.relativePath, fileEntry);
      }
    }
  }

  public fileOver(event) {
    console.log(event);
  }

  public fileLeave(event) {
    console.log(event);
  }

  onSubmitVideo() {
    let name = ""
    const formData = new FormData()
    formData.append('file', this.videofile)
    console.log(formData.get('file'))
    this.fileService.postFile(formData).subscribe(
      (res) => {
        this.uploadedVideo = true
        name = res.filename
        this.link = this.fileService.getLink(res.filename)
        console.log(res.filename)
      }
    );


    this.videofileName = ""
    this.videofile = null


  }


  onSubmitFile() {
    const formData = new FormData()
    formData.append('file', this.file)
    console.log(formData.get('file'))
    this.fileService.postFile(formData).subscribe(
      (res) => { this.uploadedFile = true }
    );
    this.fileName = ""
    this.file = null
  }

  onFileChange(event): void {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      const formData = new FormData()
      formData.append('file', file)
      console.log(formData.get('file'))
      this.fileService.postFile(formData).subscribe(
        (res) => { this.uploadedFile = true }
      );
    }
  }

}


