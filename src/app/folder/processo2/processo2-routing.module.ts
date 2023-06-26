import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Processo2Page } from './processo2.page';

const routes: Routes = [
  {
    path: '',
    component: Processo2Page
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class Processo2PageRoutingModule {}
