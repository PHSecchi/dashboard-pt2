import { Component, OnInit } from '@angular/core';
import dados from "./../../../../Dados.json";
import {exp} from "./../../app.component";

@Component({
  selector: 'app-particao1',
  templateUrl: './particao1.page.html',
  styleUrls: ['./particao1.page.scss'],
})
export class Particao1Page implements OnInit {

  part = dados.Particoes
  teste = exp
  constructor() { }

  ngOnInit() {
  }
  onClick(){
    console.log("Banana!!!")
    console.log(this.teste)
  }
  
}
