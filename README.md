skype-watch
=============

Simple messages watcher for Skype. It can be used to tail (poll) new messages from Skype to external applications, for instance, to trigger some action.

This script simply queries Skype internal DB and operates without any Skype API and permissions from application. 

<b>Usage:</b>

```Usage: ./skype-watch.py <path to skype `main.db` file> <watch interval in seconds>```

<b>Example:</b>

```bash
./skype-watch.py ~/.Skype/solaris.snaut/main.db 1
```
