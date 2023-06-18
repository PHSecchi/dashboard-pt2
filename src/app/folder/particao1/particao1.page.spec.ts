import { ComponentFixture, TestBed } from '@angular/core/testing';
import { Particao1Page } from './particao1.page';

describe('Particao1Page', () => {
  let component: Particao1Page;
  let fixture: ComponentFixture<Particao1Page>;

  beforeEach(async(() => {
    fixture = TestBed.createComponent(Particao1Page);
    component = fixture.componentInstance;
    fixture.detectChanges();
  }));

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
