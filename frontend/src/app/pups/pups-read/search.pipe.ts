import { Pipe, PipeTransform } from '@angular/core';
import { Pup } from '../pups.service';
@Pipe({
  name: 'search'
})
export class SearchPipe implements PipeTransform {
  transform(value: any, str: any): any {
    if (!str) {
      return value
    }
    return value.filter((pup: Pup) =>
      pup.name.toString().toLowerCase().includes(str.toLowerCase()));
  }
}