import { Component, OnInit } from '@angular/core';

import { Hero } from '../hero';
import { HeroService } from '../hero.service';

@Component({
  selector: 'app-heroes',
  templateUrl: './heroes.component.html',
  styleUrls: ['./heroes.component.css']
})
export class HeroesComponent implements OnInit {

  heroes: Hero[];

  constructor(private heroService: HeroService) {
    // Service injection
    // heroService.getHeroes() should not be called here
    // keep constructor simple with simple initializing 
  }

  getHeroes(): void {
    this.heroService.getHeroes()
      .subscribe(heroes => this.heroes = heroes);
  }

  add(name: string): void {
    name = name.trim();
    if (!name) { return; }
    this.heroService.addHero({ name } as Hero)
      .subscribe(hero => {
        this.heroes.push(hero);
      });
  }

  delete(hero: Hero): void {
    this.heroes = this.heroes.filter(h => h !== hero);
    /*
     * If you neglect to subscribe(), the service will not send the
     * delete request to the server! As a rule, an Observable does
     * nothing until something subscribes!
     * Confirm this for yourself by temporarily removing the subscribe(),
     * clicking "Dashboard", then clicking "Heroes". You'll see the full
     * list of heroes again.
     */
    this.heroService.deleteHero(hero).subscribe();
  }

  ngOnInit() {
    this.getHeroes();
  }

}
