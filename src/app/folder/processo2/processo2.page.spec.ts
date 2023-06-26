import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Processo2Page } from './processo2.page';

describe('Processo2Page', () => {
  let component: Processo2Page;
  let fixture: ComponentFixture<Processo2Page>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(Processo2Page);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
