// Usage : node codebase-quality-control/tests/browser/vue-aiod.cjs app/web/targets/app
const path = require('node:path');
const os = require('node:os');
const { createRequire } = require('node:module');
const { pathToFileURL } = require('node:url');
const assert = require('node:assert/strict');
const root = path.resolve(__dirname, '../../..');
const requireApp = createRequire(path.resolve(root, process.argv[2] || 'app/web/targets/app', 'package.json'));
const { chromium } = requireApp('playwright');
(async () => {
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({ viewport: {width:1918,height:924} });
    const errors = [];
    page.on('pageerror', error => errors.push(error.message));
    await page.goto(pathToFileURL(path.join(root,'docs/aiod/vue-d-ensemble-ai-development-engineering.html')).href);
    await page.evaluate(() => document.fonts.ready);
    assert.equal(await page.locator('svg,canvas').count(),0);
    assert.equal(await page.locator('.action').count(),12);
    assert.deepEqual(await page.locator('.consolidation-loop .step-number').allTextContents(),['01','02','03','06','05','04']);
    assert.deepEqual(await page.locator('.consolidation-loop .action strong').allTextContents(),['Interview','Analyse globale','Arbitrage','Livraison','Vérification','Implémentation']);
    assert.equal(await page.locator('.consolidation-loop .action.ai').count(),4);
    assert.deepEqual(await page.locator('.consolidation-loop .action.human').evaluateAll(nodes=>nodes.map(n=>n.dataset.detail)),['conso-arbitrage','conso-verification']);
    assert.equal(await page.locator('.check-ref,.pr-gate').count(),0);
    assert.equal(await page.locator('.check-link').count(),2);
    const link03 = await page.locator('.check-link[data-step="03"] > i').first().boundingBox();
    const step03 = await page.locator('[data-detail="realisation"]').boundingBox();
    assert.ok(Math.abs(link03.x-step03.x-step03.width)<2, 'La liaison 03 part du bord de Implémentation');
    const link06 = await page.locator('.check-link[data-step="06"] > i').first().boundingBox();
    const step06 = await page.locator('[data-detail="finalisation"]').boundingBox();
    assert.ok(Math.abs(link06.y-step06.y-step06.height)<2, 'La liaison 06 part du bas de Livraison');
    const checks = await page.locator('[data-detail="controles"]').boundingBox();
    for (const tip of await page.locator('.control-tip').all()) {
      const arrow = await tip.boundingBox();
      assert.ok(arrow.x>checks.x && arrow.x<checks.x+checks.width && Math.abs(arrow.y+arrow.height-checks.y)<6, 'Les deux liaisons aboutissent aux contrôles');
    }
    assert.equal(await page.locator('[data-detail="controles"]').evaluate(el=>getComputedStyle(el).backgroundColor),'rgb(107, 122, 74)');
    assert.equal(await page.locator('.connections').count(),0);
    assert.match(await page.locator('.checks-use').innerText(), /Exécute les contrôles/);
    assert.match(await page.locator('.checks-enrichment').innerText(), /Enrichit les contrôles/);
    assert.match(await page.locator('.shared-checks').innerText(), /Sans IA · CI\/CD ou à la demande/);
    assert.equal(await page.locator('.cycle-label').count(),2);
    assert.equal(await page.locator('.loop > .cycle-label').count(),0);
    assert.ok(await page.locator('.cycle-label').first().evaluate(el => { const r=el.getBoundingClientRect(); return r.height > r.width; }), 'Cycle IA en vertical sur le retour');
    assert.equal(await page.locator('.iteration-return').count(),2);
    for (const block of ['.coding-block','.consolidation-block']) {
      const title = await page.locator(block+' > h2').boundingBox();
      const header = await page.locator(block+' > .cycle-entry').boundingBox();
      assert.ok(title.y + title.height <= header.y + 1, 'Titre au-dessus de Demandes');
    }
    assert.equal(await page.locator('.consolidation-block > .cycle-entry [data-detail="demandes-consolidation"]').count(),1);
    assert.deepEqual(await page.locator('.consolidation-exit strong').allTextContents(),['PRs de consolidation','Règles et contrôles']);
    assert.equal(await page.locator('.consolidation-loop .boundary').count(),0);
    assert.deepEqual(await page.locator('.coding-loop .step-number').allTextContents(),['01','02','03','06','05','04']);
    assert.equal(await page.locator('.coding-loop .action.ai').count(),5);
    assert.equal(await page.locator('.coding-loop .action.human').count(),1);
    assert.deepEqual(await page.locator('.coding-loop .action strong').allTextContents(), ['Interview','Découpage','Implémentation','Livraison','Reconstitution','Vérification']);
    assert.equal(await page.locator('.coding-loop .action.human').getAttribute('data-detail'),'verification');
    assert.equal(await page.locator('.coding-loop [data-detail="demandes"], .coding-loop [data-detail="pr"]').count(),0);
    assert.equal(await page.locator('.cycle-entry [data-detail="demandes"]').count(),1);
    assert.equal(await page.locator('.cycle-exit [data-detail="pr"]').count(),1);
    assert.equal(await page.locator('.coding-loop [data-detail="interview"]').count(),1);
    await page.screenshot({path:path.join(os.tmpdir(),'aiod-html-desktop.png')});
    assert.equal(await page.locator('.pilot').count(),0);
    const legend = await page.locator('.role-legend').boundingBox();
    assert.ok(legend.x < 100 && legend.y > 800, 'Légende en bas à gauche');
    const before = await page.locator('.workspace').boundingBox();
    assert.match(await page.locator('.signature').innerText(), /AIDE\s*AI Development Engineering/);
    assert.equal(await page.locator('header h1').count(), 0);
    assert.equal(await page.locator('.signature p').count(),1);
    const equalFrameBands = async () => page.evaluate(() => {
      const frame = document.querySelector('.frame').getBoundingClientRect();
      const workspace = document.querySelector('.workspace').getBoundingClientRect();
      return Math.abs((workspace.top - frame.top) - (frame.bottom - workspace.bottom)) < 1;
    });
    assert.ok(await equalFrameBands(), 'Bandes haute et basse de même hauteur');
    const theme = page.locator('[data-detail="couches"]');
    await theme.hover();
    await page.waitForTimeout(250);
    assert.equal(await page.locator('#detail-panel').isVisible(), false, 'Le survol ne doit pas ouvrir le panneau');
    await theme.click();
    await page.locator('#detail-panel:not([hidden])').waitFor();
    assert.match(await page.locator('#detail-list').innerText(),/Branches, worktrees et environnements/);
    assert.deepEqual(await page.locator('.workspace').boundingBox(), before, 'Le panneau doit se superposer sans déplacer le schéma');
    await page.locator('.close').click();
    await page.waitForTimeout(150);
    assert.equal(await page.locator('#detail-panel').isVisible(),false,'Fermer doit rester fermé');
    await theme.click();
    await page.locator('[data-detail="interview"]').hover();
    assert.equal(await page.locator('#detail-title').innerText(),'Couches');
    await page.screenshot({path:path.join(os.tmpdir(),'aiod-html-panel.png')});
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('#detail-panel').isVisible(),false);
    assert.equal(await theme.getAttribute('aria-expanded'),'false');
    await page.locator('[data-detail="documentation"]').focus();
    assert.equal(await page.locator('#detail-panel').isVisible(),false);
    await page.keyboard.press('Enter');
    assert.match(await page.locator('#detail-list').innerText(),/\*\*\/README.md/);
    await page.locator('.close').click();
    assert.equal(await page.locator('[data-detail="documentation"]').evaluate(el => el === document.activeElement),true);
    await page.waitForTimeout(150);
    assert.equal(await page.locator('#detail-panel').isVisible(), false);
    await page.locator('[data-detail="engineering"]').click();
    assert.match(await page.locator('#detail-list').innerText(),/Consignes des agents/);
    await page.keyboard.press('Escape');
    await page.locator('[data-detail="verification"]').click();
    assert.equal(await page.locator('#detail-kind').textContent(),'Humain');
    assert.match(await page.locator('#detail-list').innerText(),/renvoie à la Implémentation/);
    await page.keyboard.press('Escape');
    await page.locator('[data-detail="demande-consolidation"]').click();
    assert.match(await page.locator('#detail-intro').innerText(),/vérification humaine/);
    await page.keyboard.press('Escape');
    await page.locator('[data-detail="regles-controles"]').click();
    assert.match(await page.locator('#detail-list').innerText(),/tests ou vérificateurs déterministes/);
    await page.keyboard.press('Escape');
    await page.locator('[data-detail="process-consolidation"]').click();
    assert.match(await page.locator('#detail-intro').innerText(),/toute la base de code/);
    assert.match(await page.locator('#detail-list').innerText(),/sans IA en CI\/CD ou à la demande/);
    assert.match(await page.locator('#detail-list').innerText(),/écrire les tests ou vérificateurs/);
    await page.keyboard.press('Escape');
    await page.locator('[data-detail="controles"]').click();
    assert.equal(await page.locator('#detail-title').innerText(), 'Codebase Quality Control');
    assert.equal(await page.locator('[data-detail="controles"] strong').innerText(), 'Codebase Quality Control');
    const qualityDetails = await page.locator('#detail-list').innerText();
    for (const text of ['15 domaines', 'Fiabilité des vérifications', 'Chaque convention appartient à un seul domaine', 'informatif', 'sans point de contrôle implémenté', 'sans recopier', 'accepter les cas conformes']) {
      assert.ok(qualityDetails.includes(text), text);
    }
    await page.screenshot({path:path.join(os.tmpdir(),'aide-codebase-quality-control.png')});
    assert.match(await page.locator('#detail-list').innerText(), /La consolidation enrichit/);
    await page.keyboard.press('Escape');
    for (const step of ['interview','decoupage','realisation','verification','reconstitution','finalisation']) {
      await page.locator(`[data-detail="${step}"]`).click();
      assert.match(await page.locator('#detail-list').innerText(), /Sortie attendue/);
      await page.keyboard.press('Escape');
    }
    await page.locator('[data-detail="finalisation"]').click();
    const finalisationHeadings = await page.locator('#detail-list h3').allTextContents();
    assert.ok(finalisationHeadings.indexOf('Faire passer le Codebase Quality Control') < finalisationHeadings.indexOf('Écrire les tests et la documentation'));
    assert.match(await page.locator('#detail-list').innerText(), /Une fois les contrôles réussis/);
    await page.screenshot({path:path.join(os.tmpdir(),'aide-finalisation-details.png')});
    await page.keyboard.press('Escape');
    for (const [key,hook] of [
      ['couches','Paralléliser les agents, limiter les conflits, vérifier plus facilement.'],
      ['consolidation','Corriger toute la base et rendre les bonnes pratiques vérifiables.'],
      ['engineering','Donner aux agents un cadre précis pour agir et savoir s’arrêter.'],
      ['documentation','Rendre le projet compréhensible et chaque décision traçable.']
    ]) {
      await page.locator(`[data-detail="${key}"]`).click();
      assert.equal(await page.locator('#detail-intro').innerText(),hook);
      assert.ok(await page.locator('#detail-description').isVisible());
      assert.ok(await page.locator('#detail-description').innerText());
      assert.equal(await page.locator('#detail-intro').evaluate(el=>getComputedStyle(el).fontWeight),'500');
      if (key==='couches') await page.screenshot({path:path.join(os.tmpdir(),'aide-couches-details.png')});
      await page.keyboard.press('Escape');
    }
    await page.locator('[data-detail="interview"]').click();
    assert.equal(await page.locator('#detail-description').isVisible(),false,'La définition du thème ne reste pas affichée sur une étape');
    await page.keyboard.press('Escape');
    for (const step of ['interview','analyse','arbitrage','implementation','verification','livraison']) {
      await page.locator(`[data-detail="conso-${step}"]`).click();
      assert.match(await page.locator('#detail-list').innerText(), /Sortie attendue/);
      if (step==='analyse') assert.match(await page.locator('#detail-intro').innerText(), /toute la base de code/);
      if (step==='arbitrage') assert.match(await page.locator('#detail-intro').innerText(), /contrôle envisagé détectera les écarts/);
      if (step==='verification') assert.match(await page.locator('#detail-intro').innerText(), /fonctionnement réel des contrôles implémentés/);
      if (step==='livraison') assert.match(await page.locator('#detail-intro').innerText(), /sans IA, en CI\/CD ou à la demande/);
      await page.keyboard.press('Escape');
    }
    const route = await page.locator('.route-start').boundingBox();
    const verification = await page.locator('[data-detail="verification"]').boundingBox();
    assert.ok(Math.abs(route.y - (verification.y + verification.height / 2)) < 2, 'La liaison part de la vérification humaine');
    for (const viewport of [{width:1366,height:768},{width:390,height:844}]) {
      await page.setViewportSize(viewport);
      assert.equal(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth),true);
      assert.ok(await equalFrameBands(), 'Bandes égales sur ordinateur et mobile');
      assert.equal(await page.locator('.explore-hint').count(), 0);
      assert.ok(await page.locator('.workspace').evaluate(el => el.scrollHeight <= el.clientHeight + 1), 'Aucun contenu masqué verticalement');
      assert.equal(await page.locator('.workspace').evaluate(el => getComputedStyle(el).overflowY), 'hidden');
      await page.screenshot({path:path.join(os.tmpdir(),`aiod-html-${viewport.width}.png`)});
    }
    await page.close();
    const mobile = await browser.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true});
    await mobile.goto(pathToFileURL(path.join(root,'docs/aiod/vue-d-ensemble-ai-development-engineering.html')).href);
    await mobile.locator('[data-detail="consolidation"]').tap();
    assert.equal(await mobile.locator('#detail-title').innerText(),'Consolidation');
    assert.match(await mobile.locator('#detail-list').innerText(),/Garde-fous/);
    assert.equal(await mobile.evaluate(() => document.documentElement.scrollWidth <= innerWidth),true);
    await mobile.screenshot({path:path.join(os.tmpdir(),'aiod-html-mobile-panel.png')});
    await mobile.locator('.close').tap();
    assert.equal(await mobile.locator('#detail-panel').isVisible(),false);
    assert.deepEqual(errors,[]);
    console.log('OK : HTML sans SVG, 12 actions, survol sans ouverture, détails au clic/clavier/tactile, fermeture et focus, dimensions ordinateur/mobile, panneau superposé sans déplacement, fermeture persistante.');
  } finally { await browser.close(); }
})().catch(error => { console.error(error); process.exit(1); });
