# Dependency and Supply-Chain Policy

## Selection
- Prefer maintained dependencies with a clear purpose and reliable release history.
- Check licenses, platform compatibility, transitive dependencies, maintenance activity, and known security advisories.
- Avoid adding a library for functionality that is trivial and safer to implement directly.

## Updates
- Commit lockfiles for ecosystems that support them.
- Update dependencies deliberately and test behavior after upgrades.
- Remove unused packages.
- Pin actions and high-risk automation dependencies more tightly when feasible; evaluate immutable commit pinning for production workflows.

## Supply-chain safety
- Never run an install script or binary from an unknown source without review.
- Keep registry and publishing tokens out of files and logs.
- Restrict CI permissions and avoid exposing secrets to untrusted pull request code.
- Generate an SBOM or provenance metadata when useful for the project's risk and release process.

## Review record
For significant additions, document purpose, maintenance/license review, security findings, and why existing alternatives were not selected.
