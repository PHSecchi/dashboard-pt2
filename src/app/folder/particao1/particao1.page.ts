import { Component, OnInit } from '@angular/core';
import dados from "./../../../../Dados.json";

@Component({
  selector: 'app-particao1',
  templateUrl: './particao1.page.html',
  styleUrls: ['./particao1.page.scss'],
})
export class Particao1Page implements OnInit {

  part = dados.Particoes

  constructor() { }

  ngOnInit() {
  }

}
