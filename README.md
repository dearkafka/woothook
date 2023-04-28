# woothook - Chatwoot webhook server using [woot](https://github.com/dearkafka/woot).

Example project can be used as a template for Chatwoot webhook server that performs via Chatwoot API ([woot](https://github.com/dearkafka/woot) package).

It listens for Chatwoot events (specified in Chatwoot >> Integrations >> Webhook >> events) and adds Telegram user name (e.g. @durov) to Contatc Attributes in field "telegram".

However, you are free to use it as an example and template for adding any Chatwoot API related functionality, like connecting Google Spreadsheets, Airtable, etc.

## Install

```
pip install git+https://github.com/dearkafka/woothook
```

## Run

All you need is populate config file with your data (see [example.config](./example.config)) and do this:

```
woothook CONFIG_FILENAME
```

Also it has docker support so you can build it and include into yours docker-compose file.

```
docker build -t woothook .
docker run -it -p 8000:8000 woothook "example.config"
```
One known problem is that Chatwoot requires proper domain name for webhook, so no localhost or ip.
There are several strategies to solve this problem:
* use ngrok or similar service to get public domain name for your local server (however, it is not very reliable/secure as no security is provided by chatwoot or this repo to authenticate and sign requests)
* use nginx/traefik and configure dns on host to point some imagined domain to your local server (this is more reliable and secure, but requires some effort to configure)