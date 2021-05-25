import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators, NgForm, } from '@angular/forms';
import { NgxFileDropEntry, FileSystemFileEntry, FileSystemDirectoryEntry } from 'ngx-file-drop';
import { Pup, PupService } from '../pups.service';
import { FileService } from './file.service'
import { TimelineService } from './timeline.service';

@Component({
  selector: 'app-pups-create',
  templateUrl: './pups-create.component.html',
  styleUrls: ['./pups-create.component.scss']
})
export class PupsCreateComponent implements OnInit {
  createOption: string;
  timelineOption: boolean;
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

  constructor(private pupS: PupService, private fileService: FileService, private formBuilder: FormBuilder, private timelineService: TimelineService) { }

  ngOnInit(): void {
    this.form = this.formBuilder.group({
      seconds: null,
      model_filename: "",
      pup_id: null
    });

  }

  onChangeName(f: NgForm) {
    if (this.currentPup.name != "") {
      this.stage = 1;
    }
  }

  public droppedFile(files: NgxFileDropEntry[]) {
    if (this.createOption == '0') {
      this.files = files;
    }
    else if (this.createOption == '1') {
      this.videofiles = files;
    }
    for (const droppedFile of files) {
      if (droppedFile.fileEntry.isFile) {
        const fileEntry = droppedFile.fileEntry as FileSystemFileEntry;
        fileEntry.file((file: File) => {
          if (this.createOption == '0') {
            this.file = file
            this.fileName = file.name
          }
          else if (this.createOption == '1') {
            this.videofile = file
            this.videofileName = file.name

            this.onSubmitVideo()
          }
        });
      } else {
        const fileEntry = droppedFile.fileEntry as FileSystemDirectoryEntry;
      }
    }
  }


  /*public fileOver(event) {
    console.log(event);
  }

  public fileLeave(event) {
    console.log(event);
  }
*/
  onSubmitVideo() {
    let name = ""
    const formData = new FormData()
    formData.append('file', this.videofile)
    this.fileService.postFile(formData).subscribe(
      (res) => {
        this.uploadedVideo = true
        this.link = this.fileService.getLink(res.filename)
        let pup: Pup = {
          "name": this.currentPup.name,
          "video_filename": res.filename,
        }
        this.pupS.createPup(pup).subscribe(
          (res) => {
            this.form.get('pup_id').setValue(res.id);
            console.log("puuup", res)
          }
        )
      }
    );
    this.videofileName = ""
    this.videofile = null
  }


  onSubmitFile() {
    const formData = new FormData()
    formData.append('file', this.file)
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
      this.fileService.postFile(formData).subscribe(
        (res) => { this.uploadedFile = true }
      );
    }
  }

  onModelChange(event): void {
    if (event.target.files.length > 0) {
      const file = event.target.files[0];
      const formData = new FormData()
      formData.append('file', file)
      this.fileService.postFile(formData).subscribe(
        (res) => {
          this.form.get('model_filename').setValue(res.filename);
          console.log(this.form.value)
        }
      );
    }
  }

  setTimeline() {
    this.timelineService.postTimeline(this.form.value).subscribe(
      res => {
        this.timelineOption = true
      }
    )
    this.form.reset()
    this.currentPup.name = "";
    this.createOption = ""
    this.link = ""
    this.uploadedVideo = false

  }
}


