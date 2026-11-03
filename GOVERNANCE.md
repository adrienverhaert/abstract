# Governance

Abstract is maintained by [Adrien Verhaert](https://github.com/adrienverhaert).
The maintainer reviews issues, decides compatibility changes, merges verified
pull requests, and publishes releases. Contributions from others are welcome;
no additional maintainers or independent review board are implied.

Discuss changes to language syntax, diagnostics, compiled data, editor protocol,
or supported platforms in an issue. Decisions should cite the relevant
specification section and observable behavior. A maintainer decision should
state the chosen behavior, compatibility effect, and verification.

The published specification defines the language contract. Component versions
and distribution contracts are checked by the release manifest. A release is
cut from a verified commit; tags and published artifact sets should remain
immutable. Security reports follow SECURITY.md, and conduct concerns follow
CODE_OF_CONDUCT.md.

This repository imports an existing implementation into a fresh public history.
Migration issues and PRs document work performed during that import. They do
not represent a reconstruction of review discussions or executions that did
not occur.
