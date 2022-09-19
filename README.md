This is a simple web dialog to login to Gog, for use with [the API](https://gogapidocs.readthedocs.io/).

It just returns the initial auth-code, on stdout. You can use this code to get an auth/refresh token in some other programmming language.

## development

```
cargo run             # try it out
cargo build --release # build for production in target/release/goglogin
```
