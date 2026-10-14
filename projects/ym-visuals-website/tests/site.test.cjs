const test = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');

const siteDir = path.resolve(__dirname, '..');
const htmlPath = path.join(siteDir, 'index.html');
const html = fs.readFileSync(htmlPath, 'utf8');

function allMatches(regex, input = html) {
  return [...input.matchAll(regex)];
}

test('entry page exists and has a complete document skeleton', () => {
  assert.ok(html.length > 10000, 'index.html should contain the complete website');
  assert.match(html, /<!doctype html>/i);
  assert.match(html, /<html\s+lang="en">/i);
  assert.match(html, /<meta\s+charset="utf-8">/i);
  assert.match(html, /<meta\s+name="viewport"/i);
  assert.match(html, /<title>YM Visuals — Visuals That Define You<\/title>/);
  assert.match(html, /<main>/i);
  assert.match(html, /<footer>/i);
});

test('all primary navigation and section anchors resolve', () => {
  const idList = allMatches(/\bid="([^"]+)"/g).map(m => m[1]);
  const ids = new Set(idList);
  const duplicates = [...new Set(idList.filter((id, index) => idList.indexOf(id) !== index))];
  assert.deepEqual(duplicates, [], 'IDs should be unique');
  const hrefs = allMatches(/\bhref="#([^"]+)"/g).map(m => m[1]);
  const missing = [...new Set(hrefs.filter(id => !ids.has(id)))];
  assert.deepEqual(missing, [], 'in-page links should point to existing IDs');
  for (const section of ['home','services','work','approach','about','packages','faq','contact']) {
    assert.ok(ids.has(section), 'missing expected section #' + section);
  }
});

test('interactive controls expose accessible state and labels', () => {
  assert.match(html, /aria-label="Main navigation"/);
  assert.match(html, /class="menu-toggle" aria-expanded="false" aria-controls="nav-links"/);
  assert.ok(allMatches(/class="faq-q" aria-expanded="false"/g).length >= 4, 'FAQ buttons need aria-expanded state');
  assert.match(html, /addEventListener\('click'/);
  assert.match(html, /prefers-reduced-motion:\s*reduce/);
});

test('responsive layout and semantic content are present', () => {
  assert.match(html, /@media\s*\(max-width:\s*650px\)/);
  assert.match(html, /@media\s*\(max-width:\s*900px\)/);
  assert.match(html, /<header\b/);
  assert.match(html, /<nav\b/);
  assert.match(html, /<section\b/);
  assert.match(html, /<h1\b/);
  assert.equal(allMatches(/<h1\b/g).length, 1, 'page should have one primary H1');
});

test('images/links do not silently fabricate external destinations', () => {
  const externalHrefs = allMatches(/\bhref="(https?:[^"]+)"/g).map(m => m[1]);
  assert.deepEqual(externalHrefs, [], 'this prototype should not include unverified external social links');
  assert.match(html, /YOUR-EMAIL-HERE/, 'contact placeholder should remain explicit until official email is known');
  assert.match(html, /Concept sample/);
  assert.match(html, /not client projects or completed commissions/);
});

test('local site assets referenced by the page exist', () => {
  const srcs = allMatches(/\bsrc="([^"]+)"/g).map(m => m[1]).filter(src => !/^(https?:|data:|\/\/)/i.test(src));
  const hrefs = allMatches(/\bhref="([^"]+)"/g).map(m => m[1]).filter(href => !/^(https?:|mailto:|tel:|#|javascript:|\/\/)/i.test(href));
  const missing = [...srcs, ...hrefs].filter(asset => !fs.existsSync(path.resolve(siteDir, asset)));
  assert.deepEqual(missing, [], 'local assets referenced by the page should exist');
});
