# Releases and verification

The compiler, language, document protocol, extension, and Java runtime have
separate compatibility values in [`release-manifest.json`](../release-manifest.json).
`python scripts/check-release-manifest.py` checks those values against source.

## Pull requests

The reusable CI workflow checks repository privacy, Rust formatting and Clippy,
compiler tests on Linux/Windows/macOS, Rust 1.85, Java 8/21, extension unit tests,
and actual VS Code 1.92/stable hosts. Host checks build the retained real 1.1.0
compiler to verify capability negotiation. The packaged VSIX is checked too.

`Quality gate` succeeds only when every component check succeeds. A cancelled,
failed, or skipped component does not make the aggregate gate green. Pull
requests should be merged through GitHub after their checks pass.

## Create a release

1. Update the affected component versions and compatibility notes. Keep the
   manifest and source values consistent, and merge the change through a PR.
2. Create a version tag matching `Cargo.toml`, such as `v1.5.0`, on that verified
   commit. `Release` also supports a manual run when a version tag is selected.
   Running it from a branch fails the explicit tag check.
3. The release workflow calls the complete CI workflow first. It then tests and
   builds native Linux x64/arm64, Windows x64, and macOS Intel/Apple-silicon
   executables, and packages the Java library. The VSIX comes from verified CI.
4. Before upload, each native executable must report the expected version,
   compile the automotive fixture, and pass sealed-bundle round-trip and
   tamper-rejection checks using `scripts/verify-release.py`.
5. A write-scoped final job assembles the native binaries, VSIX, JAR, compatibility
   manifest, and `SHA256SUMS.txt` into a draft GitHub release. Review that draft,
   then publish it. All earlier jobs have read-only repository permissions.

Release concurrency is serialized per tag. Re-running a draft can replace its
verified artifacts; a published release is not overwritten by that path.
Third-party Actions are pinned to immutable commit hashes. CI artifacts are
retained for seven days; the GitHub release is the durable distribution.

## Verify a downloaded artifact

The `Verify downloaded release` workflow downloads binaries from a selected
release, checks their checksums and manifest, and exercises the shipped files
on their matching native runners. Select the same release tag under **Use
workflow from** and in the `tag` input.

To verify a compiler manually:

```sh
python scripts/verify-release.py --tag v1.5.0 --asset ./abstract-linux-x64 \
  --checksums ./SHA256SUMS.txt --manifest ./release-manifest.json \
  --automotive ./examples/tutorials/automotive
```

The Java JAR is a regular library, not a fat JAR; its Maven dependencies remain
required. A VSIX can be installed from a local file through VS Code. The current
publisher identifier is `adrienverhaert.abstract-language`; users of an earlier
publisher package must reinstall and update formatter settings explicitly.

## Rollback

Keep a prior verified release available. Reinstall its matching binary or VSIX,
and use its compatibility manifest to check consumer support. Do not silently
move a published tag or mix files from different release checksums. Publish a
new version when replacing a distribution rather than mutating an existing
public release.
