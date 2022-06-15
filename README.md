# Minroud[^1]
Simple [serverless](https://www.serverless.com) image hosting

## Deployment

```console
$ serverless deploy
endpoint: https://{identifier}.lambda-url.{region}.on.aws
```

## Usage

```console
$ curl {endpoint} --header "Content-Type: image/png" --data-binary @image.png
https://{bucket}.s3.{region}.amazonaws.com/{hash}
```

[^1]: Named after [Yor's Minroud](https://en.wikipedia.org/wiki/List_of_The_Neverending_Story_characters#Yor) from [The Neverending Story](https://en.wikipedia.org/wiki/The_Neverending_Story).
