# Minroud[^1]
Simple [serverless](https://www.serverless.com) image hosting.

## Deployment

```console
$ serverless deploy
endpoint: https://{identifier}.lambda-url.{region}.on.aws
```

See [this get started guide](https://www.serverless.com/framework/docs/getting-started) for more detailed instructions.

## Usage

### With [`cml comment`](https://cml.dev/doc/ref/comment)

```console
$ cml comment create --publish --publish-url={endpoint}
```

### With `curl`
```console
$ curl {endpoint} --data-binary @image.png --header "Content-Type: image/png"
https://{bucket}.s3.{region}.amazonaws.com/{hash}
```

#### Overwriting files

Storage is [content-addressable](https://en.wikipedia.org/wiki/Content-addressable_storage) by default, naming objects after their contents' SHA-256 hash. To return a static/unchanging URL (even after overwriting an object's contents) provide a `Content-Seed` header; objects will be named after this header's SHA-256 hash instead.

```console
$ curl {endpoint} --data-binary @file_v1 --header "Content-Seed: $(uuidgen)"
https://{bucket}.s3.{region}.amazonaws.com/8da7...2297
$ curl {endpoint} --data-binary @file_v2 --header "$_"
https://{bucket}.s3.{region}.amazonaws.com/8da7...2297
```

> **Warning**
> _If using `Content-Seed`, use a cryptographically secure value to prevent unauthorized users from reading/overwriting the uploaded files._

[^1]: Named after [Yor's Minroud](https://en.wikipedia.org/wiki/List_of_The_Neverending_Story_characters#Yor) from [The Neverending Story](https://en.wikipedia.org/wiki/The_Neverending_Story).
