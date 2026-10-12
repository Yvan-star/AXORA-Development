# AXORA AI System Guidelines

## Purpose
Use AI to reduce friction and produce useful outputs, while keeping behavior understandable, reviewable, and appropriately controlled.

## Design
For each AI feature, document:
- User problem and expected benefit
- Model/provider and allowed data inputs
- Output format and intended downstream use
- Known failure modes, evaluation examples, and fallback
- Cost, latency, rate limits, and usage boundaries
- Human oversight needs and prohibited actions

## Security
- Treat prompts, uploaded files, retrieved documents, and model output as untrusted.
- Consider prompt injection, indirect instructions, data exfiltration, and tool misuse.
- Do not place secrets in prompts or expose credentials to model output.
- Enforce tool authorization in application code, not in model instructions alone.
- Give tools the minimum capabilities needed; require explicit approval for consequential external actions.
- Separate trusted system policy from untrusted user/retrieved content.
- Validate structured output against schemas before use.

## Reliability
- Define expected output structure and handle malformed or missing output.
- Use deterministic code for calculations, permissions, and state transitions when possible.
- Add timeouts, retry limits, rate limits, and cost ceilings.
- Log operational metadata only; avoid storing private prompts and responses without a defined purpose and retention policy.
- Evaluate representative success, edge, adversarial, and refusal cases before release.

## Human oversight
Require review where outputs materially affect money, access, privacy, safety, irreversible data changes, or public communications. Do not represent generated results as verified facts without a verification step.

## Release checklist
- [ ] Inputs and downstream actions mapped
- [ ] Prompt-injection and tool-abuse cases considered
- [ ] Output validation implemented
- [ ] Provider data policies reviewed
- [ ] Rate/cost limits configured
- [ ] Evaluation set and failure fallback documented
- [ ] Human approval rules implemented where needed
