# Python Deepl Translator CLI

## Installation

```bash
pdm install
```

## Usage help and examples

```bash
pdm run python main.py -h
```

Since the API is unofficial, use it at your own risk.

Known issues:

- The API is not stable. While translating very long texts, it may return an error code 429 (Too many requests). In this case, you should wait a few minutes and try again.
- This API is not officially supported by DeepL. It may stop working at any time as the upstream PIP package won't keep up with the changes and is now **archieved**.

Another relavant project: [DeepLX](https://github.com/OwO-Network/DeepLX)
