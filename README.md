# Abstract

A declarative data language for related objects. Define a schema, write instances
and variations, then compile validated JSON, YAML, or RAW for your application.

[Try it in your browser](https://learn-abstract.vercel.app/en/) |
[Language reference](docs/README.md) | [Examples](examples/README.md)

## Build and run

```sh
cargo build --release --locked
cargo run -- init my-project
cargo run -- compile my-project JSON --out my-project.json
```

The current source import is tracked through component-level issues and pull
requests. The compiler and its executable examples are available now; editor,
Java runtime, release automation, and the illustrated tour follow in their own changes.

## Verify

```sh
cargo fmt --all -- --check
cargo clippy --locked --all-targets -- -D warnings
cargo test --locked
```

Source code is available under [MIT](LICENSE).
