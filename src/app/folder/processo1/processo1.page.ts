import { Component, OnInit } from '@angular/core';
import dados from "./../../../../Dados.json";

@Component({
  selector: 'app-processo1',
  templateUrl: './processo1.page.html',
  styleUrls: ['./processo1.page.scss'],
})
export class Processo1Page implements OnInit {

  proc = dados.Processos

  constructor() { }

  ngOnInit() {
  }

}
