import { NgModule } from '@angular/core';
import { PreloadAllModules, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '',
    redirectTo: 'folder/Inbox',
    pathMatch: 'full'
  },
  {
    path: 'folder/',
    loadChildren: () => import('./folder/folder.module').then( m => m.FolderPageModule)
  },
  {
    path: 'folder/imagem',
    loadChildren: () => import('./folder/imagem/imagem.module').then( m => m.ImagemPageModule)
  },
  {
    path: 'folder/particao1',
    loadChildren: () => import('./folder/particao1/particao1.module').then( m => m.Particao1PageModule)
  },
  {
    path: 'folder/processo1',
    loadChildren: () => import('./folder/processo1/processo1.module').then( m => m.Processo1PageModule)
  },

];

@NgModule({
  imports: [
    RouterModule.forRoot(routes, { preloadingStrategy: PreloadAllModules })
  ],
  exports: [RouterModule]
})
export class AppRoutingModule {}
