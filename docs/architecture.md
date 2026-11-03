# Architecture

Abstract is a compiler with optional consumers, not an application backend.

## Compiler flow

`src/cli.rs` parses commands and options. `src/project.rs` discovers a project
and its source/assets. The lexer, AST, schema, instance, logic, validation,
resolution, and version modules implement the language contract. `src/output.rs`
serializes validated documents. Bundling and authenticated encryption are
separate modules; neither changes language semantics.

`src/lib.rs` exposes the compiler library and controls the compiler stack.
The CLI and analysis protocol use that library. Source errors produce
diagnostics with source positions rather than an unchecked output document.

## Editor boundary

The extension owns editor documents, project capture, cancellation, navigation,
and Workspace Trust decisions. The compiler owns semantic analysis and evaluated
results. Tests exercise both unit-level behavior and actual VS Code hosts;
a retained real prior compiler verifies capability negotiation.

## Java boundary

The Maven runtime reads the compiled envelope and model overlays, and opens
supported authenticated bundles. It does not parse Abstract source. CI supplies
a real compiler for cross-language fixtures and checks Java 8 and 21.

## Browser boundary

The browser website lives in the separate Learn Abstract repository. It adapts
the upstream compiler to WebAssembly and runs compilation in a worker. That
integration owns browser memory/time limits, persistence, and web presentation;
those are not guarantees supplied by this native CLI repository.

## Delivery boundary

The compatibility manifest connects source versions to release contracts.
Reusable CI must succeed before release packaging. Native binaries are exercised
before upload; the write-scoped publisher assembles checked assets and hashes.
The release guide describes review, publication, verification, and rollback.
