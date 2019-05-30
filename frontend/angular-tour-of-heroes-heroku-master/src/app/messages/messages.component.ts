import { Component, OnInit } from '@angular/core';

import { MessageService } from '../message.service';

@Component({
  selector: 'app-messages',
  templateUrl: './messages.component.html',
  styleUrls: ['./messages.component.css']
})
export class MessagesComponent implements OnInit {

  messages: string[] = [];

  // public so this service is visible to model binding
  constructor(public messageService: MessageService) { }

  ngOnInit() {
  }

}
