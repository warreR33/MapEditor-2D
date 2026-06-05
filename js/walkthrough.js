// walkthrough.js — Vista de solo lectura: paso a paso práctico

const Walkthrough = (() => {

  let isActive = false;
  let cwrap = null;
  let panStart = null, panOffStart = null;

  function init() {
    cwrap = document.getElementById('cwrap');
  }

  function onPanDown(e) {
    if (e.button !== 1) return;
    e.preventDefault();
    const s = Editor.getState();
    panStart = { x: e.clientX, y: e.clientY };
    panOffStart = { x: s.offsetX, y: s.offsetY };
    if (cwrap) cwrap.style.cursor = 'grabbing';
  }

  function onPanMove(e) {
    if (!panStart) return;
    Editor.panTo(panOffStart.x + (e.clientX - panStart.x), panOffStart.y + (e.clientY - panStart.y));
  }

  function onPanUp(e) {
    if (e.button !== 1 || !panStart) return;
    panStart = null;
    if (cwrap) cwrap.style.cursor = '';
  }

  function buildPanel() {
    const panel = document.getElementById('pinner-panel');
    if (!panel) return;

    const stepsData = Steps.getData();
    const allSteps = stepsData.steps || [];

    panel.innerHTML = `
      <div class="steps-panel">
        <div class="steps-header">
          <h3>Walkthrough</h3>
        </div>
        <div class="wt-list" id="wt-list"></div>
      </div>`;

    const list = document.getElementById('wt-list');

    allSteps.forEach((step, stepIdx) => {
      const arrows = [...(step.arrows || [])]
        .sort((a, b) => (parseInt(a.number) || 0) - (parseInt(b.number) || 0));

      const section = document.createElement('div');
      section.className = 'wt-step-section';

      const titleRow = document.createElement('div');
      titleRow.className = 'wt-step-title';
      titleRow.innerHTML = `<span class="wt-step-num">${stepIdx + 1}</span><span>${step.name}</span>`;
      section.appendChild(titleRow);

      if (arrows.length === 0) {
        const empty = document.createElement('div');
        empty.className = 'wt-no-arrows';
        empty.textContent = '— Sin flechas —';
        section.appendChild(empty);
      }

      arrows.forEach(arrow => {
        const block = document.createElement('div');
        block.className = 'wt-arrow-block';

        const hdr = document.createElement('div');
        hdr.className = 'wt-arrow-hdr';
        hdr.textContent = `↳ #${arrow.number}`;
        block.appendChild(hdr);

        const wtText = arrow.walkthrough_text || '';
        if (wtText) {
          const p = document.createElement('p');
          p.className = 'wt-arrow-text';
          p.textContent = wtText;
          block.appendChild(p);
        }

        section.appendChild(block);
      });

      list.appendChild(section);
    });
  }

  function activate() {
    isActive = true;
    const panel = document.getElementById('pinner-panel');
    if (panel) panel.classList.remove('hidden');
    if (typeof Pinner !== 'undefined') {
      Pinner.renderPins();
      Pinner.updatePinCount();
    }
    buildPanel();
    if (cwrap) {
      cwrap.addEventListener('mousedown', onPanDown);
      window.addEventListener('mousemove', onPanMove);
      window.addEventListener('mouseup', onPanUp);
    }
    window.dispatchEvent(new Event('resize'));
  }

  function deactivate() {
    isActive = false;
    panStart = null;
    const panel = document.getElementById('pinner-panel');
    if (panel) panel.classList.add('hidden');
    document.querySelectorAll('#map-container .pin').forEach(el => el.remove());
    if (typeof Pinner !== 'undefined' && Pinner.clearPinElements) {
      Pinner.clearPinElements();
    }
    if (cwrap) {
      cwrap.removeEventListener('mousedown', onPanDown);
      window.removeEventListener('mousemove', onPanMove);
      window.removeEventListener('mouseup', onPanUp);
    }
  }

  return { init, activate, deactivate };
})();
