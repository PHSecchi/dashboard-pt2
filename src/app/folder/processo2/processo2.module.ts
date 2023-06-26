import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Processo2PageRoutingModule } from './processo2-routing.module';

import { Processo2Page } from './processo2.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Processo2PageRoutingModule
  ],
  declarations: [Processo2Page]
})
export class Processo2PageModule {}
