# AXORA Privacy Principles

Use this guide during discovery, architecture, implementation, and release. It is a practical engineering standard, not legal advice.

## Principles
1. **Purpose limitation:** know why each data element is needed before collecting it.
2. **Minimization:** collect the least data needed for the stated feature.
3. **Transparency:** explain what is collected, why, where it goes, and how long it is kept.
4. **Security:** limit access, protect data in transit and at rest where supported, and avoid sensitive logs.
5. **Retention:** define when records expire and how deletion is handled, including backups and connected providers.
6. **User control:** where applicable, support access, correction, export, and deletion requests.
7. **Accountability:** document the responsible owner, processors, and incident path.

## Design review questions
- What personal or sensitive data is processed?
- Is each data element essential to a named feature?
- Who can access it, including staff, service providers, and AI vendors?
- Is data sent across a network or to another service?
- What are retention, deletion, export, backup, and recovery rules?
- Are minors or other vulnerable users likely to use the product?
- Could analytics or logs identify people unnecessarily?
- What user-facing notices or consent flows may be needed?

## AI and third-party services
Do not submit private user information to an AI or third-party provider until provider terms, retention, training use, access controls, data region, and contractual requirements have been checked for the project's use case.

## Release gate
- [ ] Data inventory and purpose documented
- [ ] Privacy notice reflects actual implementation
- [ ] Retention and deletion behavior defined
- [ ] External processors reviewed
- [ ] Access to production data restricted
- [ ] Logs and telemetry checked for accidental personal data
