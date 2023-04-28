# woothook - Chatwoot webhook server using [woot](https://github.com/dearkafka/woot).

Example project can be used as a template for Chatwoot webhook server that performs via Chatwoot API ([woot](https://github.com/dearkafka/woot) package).

It listens for Chatwoot events (specified in Chatwoot >> Integrations >> Webhook >> events) and adds Telegram user name (e.g. @durov) to Contatc Attributes in field "telegram".

However, you are free to use it as an example and template for adding any Chatwoot API related functionality, like connecting Google Spreadsheets, Airtable, etc.


All you need is populate config file with your data (see [example.config](./example.config)) and do this:

```
woothook CONFIG_FILENAME
```

Also it has docker support so you can build it and include into yours docker-compose file.
