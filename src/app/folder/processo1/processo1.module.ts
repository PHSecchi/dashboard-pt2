import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Processo1PageRoutingModule } from './processo1-routing.module';

import { Processo1Page } from './processo1.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Processo1PageRoutingModule
  ],
  declarations: [Processo1Page]
})
export class Processo1PageModule {}
