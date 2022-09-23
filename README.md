This is a simple web dialog to login to Gog, for use with [the API](https://gogapidocs.readthedocs.io/).

It just returns the initial auth-code, on stdout. You can use this code to get an auth/refresh token in some other programmming language.

## development

```
cargo run             # try it out
cargo build --release # build for production in target/release/goglogin
```

### dependencies

You will need a few dependencies, dpending on your OS. I only tested with Mac & Linux.

#### linux

On popos 22.04, I had problems with GTK dev-dependencies not being installable. I used docker to work around it.

```
docker run --rm -it --workdir=/app -v ${PWD}:/app rust

apt update && apt install -y libwebkit2gtk-4.0-dev libayatana-appindicator3-dev libappindicator3-dev
cargo build --release
```
