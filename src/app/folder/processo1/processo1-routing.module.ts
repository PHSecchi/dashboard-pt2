import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Processo1Page } from './processo1.page';

const routes: Routes = [
  {
    path: '',
    component: Processo1Page
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class Processo1PageRoutingModule {}
