import { Component, OnInit } from '@angular/core';
import dados from "./../../../../Dados.json";

@Component({
  selector: 'app-processo2',
  templateUrl: './processo2.page.html',
  styleUrls: ['./processo2.page.scss'],
})
export class Processo2Page implements OnInit {

  detProcess = dados.ArqProcess

  constructor() { }

  ngOnInit() {
  }

}
