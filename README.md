# Minroud[^1]
Simple [serverless](https://www.serverless.com) image hosting.

## Deployment

```console
$ serverless deploy
endpoint: https://{identifier}.lambda-url.{region}.on.aws
```

See [this get started guide](https://www.serverless.com/framework/docs/getting-started) for more detailed instructions.

## Usage

### With `curl`
```console
$ curl {endpoint} --header "Content-Type: image/png" --data-binary @image.png
https://{bucket}.s3.{region}.amazonaws.com/{hash}
```

### With [`cml comment`](https://cml.dev/doc/ref/comment)

```console
$ cml comment create --publish --publish-url={endpoint} image.png
https://{bucket}.s3.{region}.amazonaws.com/{hash}
```

[^1]: Named after [Yor's Minroud](https://en.wikipedia.org/wiki/List_of_The_Neverending_Story_characters#Yor) from [The Neverending Story](https://en.wikipedia.org/wiki/The_Neverending_Story).
