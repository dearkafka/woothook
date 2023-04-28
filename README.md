# woothook - Chatwoot webhook server using woot.

Example project can be used as a template for Chatwoot webhook server that performs via Chatwoot API ([woot](https://github.com/dearkafka/woot) package).

It listens for any telegram messages in Chatwoot and adds Telegram user name (e.g. @durov) to Contatct Attributes field "telegram".

However, you are free to use it as an example and template for adding any Chatwoot API related  functionality, like connecting Google Spreadsheets, Airtable, etc.

Also it has docker support so you can build it and include into yours docker-compose file.
