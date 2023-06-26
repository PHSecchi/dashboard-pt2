import { Component, OnInit } from '@angular/core';
import dados from "./../../../../Dados.json";

@Component({
  selector: 'app-imagem',
  templateUrl: './imagem.page.html',
  styleUrls: ['./imagem.page.scss'],
})
export class ImagemPage implements OnInit {
  
  pasta = dados.PastaArq

  constructor() { }

  ngOnInit() {
  }

}
