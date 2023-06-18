import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular';

import { Particao1PageRoutingModule } from './particao1-routing.module';

import { Particao1Page } from './particao1.page';

@NgModule({
  imports: [
    CommonModule,
    FormsModule,
    IonicModule,
    Particao1PageRoutingModule
  ],
  declarations: [Particao1Page]
})
export class Particao1PageModule {}
