import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { Particao1Page } from './particao1.page';

const routes: Routes = [
  {
    path: '',
    component: Particao1Page
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class Particao1PageRoutingModule {}
