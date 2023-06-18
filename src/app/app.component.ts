import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  public appPages = [
    { title: 'Pasta', url: '/folder/Nome da Pasta', icon: 'folder-open' },
    { title: 'Arquivo', url: '/folder/Nome do aquivo', icon: 'document' },
    { title: 'Imagem', url: '/folder/imagem', icon: 'image' },
    { title: 'Áudio', url: '/folder/musica', icon: 'musical-note' },
  ];

  public appProcessos= [
    { title: 'Processo Entrada', url: '/folder/processo1', icon: 'arrow-forward' },
    { title: 'Processo Saída', url: '/folder/processo2', icon: 'arrow-back' },
  ];

  
  public appParticoes = [
    { title: 'Partição 1', url: '/folder/particao1', icon: 'disc' },
    { title: 'Partição 2', url: '/folder/particao2', icon: 'disc' },
    { title: 'Partição 3', url: '/folder/particao3', icon: 'disc' },
  ];

  public labels = [];
  constructor() {}
}
