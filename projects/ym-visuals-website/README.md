# YM Visuals — Official Website Prototype

A responsive, no-build static website prototype for YM Visuals. Built with plain HTML, CSS, and JavaScript so it can be hosted using GitHub Pages without installing software.

## Preview the files

Open [index.html](./index.html) in GitHub to inspect the source. To publish this folder as a website, use the steps below.

## Website sections

- Hero and brand message: **Visuals That Define You.**
- Services overview
- Concept portfolio cards
- Four-step design process
- About and brand values
- Quote-based Basic / Standard / Premium package directions
- FAQ accordion
- Contact call to action
- Responsive mobile navigation, semantic landmarks, keyboard-operable controls, SEO metadata, and reduced-motion support

## Before public launch

1. Replace `YOUR-EMAIL-HERE` in the contact `mailto:` link in `index.html` with the official YM Visuals email address.
2. Replace the concept/sample portfolio artwork with approved real work, or keep each concept clearly labeled.
3. Add verified official social links and any confirmed business details.
4. Confirm package scope, revision terms, prices, and turnaround expectations before advertising them.
5. Review the page on a phone and desktop.

The page intentionally does not invent contact details, client results, testimonials, or fixed prices.

## Publish with GitHub Pages (no local installation)

GitHub Pages publishes static HTML/CSS/JavaScript directly from a repository. Because this site is inside the existing AXORA repository, publish from a dedicated branch or move/copy the site files into a dedicated website repository if you want a clean root URL.

### Simplest option: dedicated repository

1. Create a new public repository named `ym-visuals-website` in your GitHub account.
2. Upload the contents of this folder (`index.html`, `.nojekyll`, and this README) to the **root** of that repository using GitHub's **Add file → Upload files** interface.
3. Open **Settings → Pages**.
4. Under **Build and deployment**, choose **Deploy from a branch**.
5. Select branch `main` and folder `/(root)`, then click **Save**.
6. Wait for the Pages deployment to complete, then use **Settings → Pages → Visit site**. The usual project URL is `https://yvan-star.github.io/ym-visuals-website/`.

Publishing is not enabled automatically by this prototype commit. The URL will work only after the repository and Pages configuration exist.

## Brand direction

- Near-black / charcoal and white foundations
- Restrained electric-blue accent
- Sora-style headings with Inter-style body copy and safe fallbacks
- Tagline: **Visuals That Define You.**
- Supporting line: **Simple. Clean. Effective.**

## Technical notes

- No framework, package manager, server, or build step required.
- The Google Fonts connection is optional; system fallbacks are included.
- Contact form is not connected to a backend; the CTA uses a mailto link.
- No analytics, cookies, external form service, or data collection are added.


## Stability checks

The site has a dependency-free regression test suite at `tests/site.test.cjs`. Run it from the repository root with Node.js 20 or newer:

```sh
node --test projects/ym-visuals-website/tests/site.test.cjs
```

A GitHub Actions workflow at `.github/workflows/ym-visuals-site-checks.yml` runs these checks on relevant pushes, pull requests, and manual dispatch. It checks document structure, section anchors/IDs, responsive breakpoints, accessible interaction state, local asset references, and intentional contact/portfolio placeholders.

These are static checks, not a substitute for cross-browser visual testing or a full accessibility audit. The contact CTA is a mailto link (not a backend form), and its placeholder email must be replaced before launch.
