> **DEPRACTED**: use [deckagog](https://github.com/notnullgames/deckagog), which has this login stuff, but also a full Gog client.

This is a simple web dialog to login to Gog, for use with [the API](https://gogapidocs.readthedocs.io/).

It just returns the initial auth-code, on stdout. You can use this code to get an auth/refresh token in some other programmming language.

The origiunal purpose was to provide a Gog login for a plugin on steamdeck, or any other script that needs Gog APIs.

## usage

Get the [release](https://github.com/notnullgames/goglogin/releases) for your platform. Run it, and it will open a Gog login dialog. The output on stdout is your initial auth-token. See [example.py](example.py) for an example of using it in another script.

## development

```
cargo run             # try it out
cargo build --release # build for production in target/release/goglogin
```

### dependencies

You will need a few dependencies, depending on your OS. I only tested with Mac & Linux.

#### linux

On Pop!OS 22.04, I had problems with GTK dev-dependencies not being installable. I used docker to work around it.

```
docker run --rm -it --workdir=/app -v ${PWD}:/app rust

apt update && apt install -y libwebkit2gtk-4.0-dev libayatana-appindicator3-dev libappindicator3-dev
cargo build --release
```
