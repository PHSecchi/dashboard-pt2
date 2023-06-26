import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { FolderPage } from './folder.page';

const routes: Routes = [
  {
    path: '',
    component: FolderPage
  },
  {
    path: 'imagem',
    loadChildren: () => import('./imagem/imagem.module').then( m => m.ImagemPageModule)
  },
  {
    path: 'particao1',
    loadChildren: () => import('./particao1/particao1.module').then( m => m.Particao1PageModule)
  },
  {
    path: 'processo1',
    loadChildren: () => import('./processo1/processo1.module').then( m => m.Processo1PageModule)
  },
  {
    path: 'processo2',
    loadChildren: () => import('./processo2/processo2.module').then( m => m.Processo2PageModule)
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class FolderPageRoutingModule {}
