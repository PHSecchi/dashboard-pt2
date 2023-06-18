import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Processo1Page } from './processo1.page';

describe('Processo1Page', () => {
  let component: Processo1Page;
  let fixture: ComponentFixture<Processo1Page>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(Processo1Page);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
