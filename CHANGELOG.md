# Changelog

## Compiler 1.5.1

- Update `ctutils` to address RUSTSEC-2026-0385, which affects constant-time
  mask generation and `u128` comparisons in earlier dependency versions.
- Audit locked Rust dependencies in the reusable CI and release quality gate.
- Language, document, analysis, and bundle formats are unchanged.

Release history is published on the [GitHub releases page](https://github.com/adrienverhaert/abstract/releases).

Current releases provide the compiler, language reference, Java reader, and VS
Code extension as separate components. Their current values are declared only
in [release-manifest.json](release-manifest.json). Model `versions` in authored
data are independent of those release values.

Recent work includes checked arithmetic, public scalar export, editor analysis,
authenticated optional bundles, and packaging verification. Consult the
[compatibility guide](docs/compatibility.md) before upgrading a consumer or
changing a wire contract.
