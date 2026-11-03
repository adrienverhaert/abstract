# Security policy

## Supported versions

Security fixes target the current `main` branch and the latest supported
release. The `compat-compiler-1.1.0` snapshot is a test baseline, not a supported
or recommended distribution.

## Report privately

Use [Security → Report a vulnerability](https://github.com/adrienverhaert/abstract/security/advisories/new).
Do not disclose exploit details, credentials, personal information, or customer
data in public issues. Include the affected version/platform, a small synthetic
reproducer, expected/actual behavior, and impact. There is no guaranteed response
deadline or bug bounty.

If private reporting is unavailable, request a private contact channel from the
maintainer without publishing the vulnerability. A report should remain private
until its impact and disclosure plan have been assessed.

## Relevant boundaries

Compiler resource paths, source and output limits, authenticated bundles, the
editor's process execution, Workspace Trust, and untrusted project files are
security-sensitive. The compiler is not a general sandbox for downstream
applications or a complete image decoder. A regular Java JAR still requires its
declared dependencies.

Release artifacts include checksums and a compatibility manifest. The release
pipeline verifies actual native executables, including rejection of tampered
bundles. Follow [release verification](docs/releasing.md) before installing a
binary from a download. Do not run a compiler configured by an untrusted workspace.
