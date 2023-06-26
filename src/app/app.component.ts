import { Component, OnInit, OnDestroy } from '@angular/core';
import dados from "./../../Dados.json";
export let exp:any;

exp = 1;
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent {
  part = dados.Particoes
  proc = dados.Processos
  arproc = dados.ArqProcess
  pasta = dados.PastaArq 


  public appPages = [
    { title: 'Pasta', url: '/folder/Nome da Pasta', icon: 'folder-open' },
    { title: 'Arquivo', url: '/folder/Nome do aquivo', icon: 'document' },
    { title: 'Imagem', url: '/folder/imagem', icon: 'image' },
    { title: 'Áudio', url: '/folder/musica', icon: 'musical-note' },
  ];

  public appProcessos= [
    { title: 'Processo Entrada', url: '/folder/processo1', icon: 'arrow-forward' },
    
  ];

  iconPart = 'disc'
  urlPart = '/folder/particao1'

  
  public appParticoes = [
    { title: 'Partição 1', url: '/folder/particao1', icon: 'disc' },
    { title: 'Partição 2', url: '/folder/particao2', icon: 'disc' },
    { title: 'Partição 3', url: '/folder/particao3', icon: 'disc' },
  ];
  
  public labels = [];
  constructor() {
  };
  
  public onClick(f:any){
      
    let exp= f;
    console.log(exp);
    return exp;
  

  }


  
}

// default export (a:object) =>{
//   exp = a
// }
