/**
 * Feminnita — Backend Server
 * Express.js com API de configuração do site
 * Porta: 3456
 *
 * Endpoints:
 *   GET  /api/config          → retorna config.json
 *   POST /api/config          → salva config.json
 *   GET  /api/config/:section → retorna seção específica (loja, hero, nav, etc.)
 */

const express  = require('express');
const fs       = require('fs');
const path     = require('path');
const cors     = require('cors');

const app = express();
const PORT = process.env.PORT || 3456;
const CONFIG_PATH = path.join(__dirname, 'data', 'config.json');

// ── Middleware ────────────────────────────────────────────────────────────────
app.use(cors());
app.use(express.json({ limit: '2mb' }));

// ── Helpers ───────────────────────────────────────────────────────────────────
function readConfig() {
  try {
    return JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8'));
  } catch (e) {
    return {};
  }
}

function writeConfig(data) {
  if (!fs.existsSync(path.join(__dirname, 'data'))) {
    fs.mkdirSync(path.join(__dirname, 'data'), { recursive: true });
  }
  fs.writeFileSync(CONFIG_PATH, JSON.stringify(data, null, 2), 'utf8');
}

// ── GET /api/config ───────────────────────────────────────────────────────────
app.get('/api/config', (req, res) => {
  res.json(readConfig());
});

// ── GET /api/config/:section ──────────────────────────────────────────────────
app.get('/api/config/:section', (req, res) => {
  const cfg = readConfig();
  const sec = cfg[req.params.section];
  if (sec === undefined) return res.status(404).json({ erro: 'Seção não encontrada' });
  res.json(sec);
});

// ── POST /api/config ──────────────────────────────────────────────────────────
// Aceita o objeto completo ou apenas um patch parcial (deep merge por seção)
app.post('/api/config', (req, res) => {
  const atual = readConfig();
  const patch  = req.body;

  // Deep merge: preserva seções não enviadas
  const novo = Object.assign({}, atual);
  for (const key of Object.keys(patch)) {
    if (typeof patch[key] === 'object' && !Array.isArray(patch[key]) && patch[key] !== null) {
      novo[key] = Object.assign({}, atual[key] || {}, patch[key]);
    } else {
      novo[key] = patch[key];
    }
  }

  writeConfig(novo);
  console.log('[config] Salvo em', new Date().toLocaleTimeString('pt-BR'));
  res.json({ ok: true, config: novo });
});

// ── PATCH /api/config/:section ────────────────────────────────────────────────
app.patch('/api/config/:section', (req, res) => {
  const cfg = readConfig();
  const sec = req.params.section;
  if (Array.isArray(req.body)) {
    cfg[sec] = req.body;
  } else {
    cfg[sec] = Object.assign({}, cfg[sec] || {}, req.body);
  }
  writeConfig(cfg);
  res.json({ ok: true, section: sec, data: cfg[sec] });
});

// ── CRUD Produtos ─────────────────────────────────────────────────────────────
const PRODUTOS_PATH = path.join(__dirname, 'data', 'produtos.json');

function readProdutos() {
  try { return JSON.parse(fs.readFileSync(PRODUTOS_PATH, 'utf8')); }
  catch(e) { return []; }
}
function writeProdutos(data) {
  fs.writeFileSync(PRODUTOS_PATH, JSON.stringify(data, null, 2), 'utf8');
}

// GET todos os produtos
app.get('/api/produtos', (req, res) => {
  res.json(readProdutos());
});

// GET produto por id
app.get('/api/produtos/:id', (req, res) => {
  const p = readProdutos().find(x => x.id === req.params.id);
  if (!p) return res.status(404).json({ erro: 'Produto não encontrado' });
  res.json(p);
});

// POST criar novo produto
app.post('/api/produtos', (req, res) => {
  const lista = readProdutos();
  const novo = { ...req.body, id: 'fnt' + Date.now() };
  lista.push(novo);
  writeProdutos(lista);
  res.json({ ok: true, produto: novo });
});

// PUT atualizar produto
app.put('/api/produtos/:id', (req, res) => {
  const lista = readProdutos();
  const idx = lista.findIndex(x => x.id === req.params.id);
  if (idx === -1) return res.status(404).json({ erro: 'Produto não encontrado' });
  lista[idx] = { ...lista[idx], ...req.body, id: req.params.id };
  writeProdutos(lista);
  res.json({ ok: true, produto: lista[idx] });
});

// DELETE produto
app.delete('/api/produtos/:id', (req, res) => {
  let lista = readProdutos();
  const idx = lista.findIndex(x => x.id === req.params.id);
  if (idx === -1) return res.status(404).json({ erro: 'Produto não encontrado' });
  lista.splice(idx, 1);
  writeProdutos(lista);
  res.json({ ok: true });
});

// ── CRUD Pedidos ──────────────────────────────────────────────────────────────
const PEDIDOS_PATH = path.join(__dirname, 'data', 'pedidos.json');

function readPedidos() {
  try { return JSON.parse(fs.readFileSync(PEDIDOS_PATH, 'utf8')); }
  catch(e) { return []; }
}
function writePedidos(data) {
  fs.writeFileSync(PEDIDOS_PATH, JSON.stringify(data, null, 2), 'utf8');
}

app.get('/api/pedidos', (req, res) => res.json(readPedidos()));

app.get('/api/pedidos/:id', (req, res) => {
  const p = readPedidos().find(x => x.id === req.params.id);
  if (!p) return res.status(404).json({ erro: 'Pedido não encontrado' });
  res.json(p);
});

app.post('/api/pedidos', (req, res) => {
  const lista = readPedidos();
  const novo = { ...req.body, id: 'ped' + Date.now(), criadoEm: new Date().toISOString(), status: req.body.status || 'aguard-pag' };
  lista.unshift(novo);
  writePedidos(lista);
  res.json({ ok: true, pedido: novo });
});

app.patch('/api/pedidos/:id', (req, res) => {
  const lista = readPedidos();
  const idx = lista.findIndex(x => x.id === req.params.id);
  if (idx === -1) return res.status(404).json({ erro: 'Pedido não encontrado' });
  lista[idx] = { ...lista[idx], ...req.body };
  writePedidos(lista);
  res.json({ ok: true, pedido: lista[idx] });
});

// ── CRUD Clientes ─────────────────────────────────────────────────────────────
const CLIENTES_PATH = path.join(__dirname, 'data', 'clientes.json');

function readClientes() {
  try { return JSON.parse(fs.readFileSync(CLIENTES_PATH, 'utf8')); }
  catch(e) { return []; }
}
function writeClientes(data) {
  fs.writeFileSync(CLIENTES_PATH, JSON.stringify(data, null, 2), 'utf8');
}

app.get('/api/clientes', (req, res) => res.json(readClientes()));

app.get('/api/clientes/:id', (req, res) => {
  const c = readClientes().find(x => x.id === req.params.id);
  if (!c) return res.status(404).json({ erro: 'Cliente não encontrado' });
  res.json(c);
});

app.post('/api/clientes', (req, res) => {
  const lista = readClientes();
  const existe = lista.find(c => c.email === req.body.email);
  if (existe) return res.status(400).json({ erro: 'E-mail já cadastrado', cliente: existe });
  const novo = { ...req.body, id: 'cli' + Date.now(), criadoEm: new Date().toISOString() };
  lista.unshift(novo);
  writeClientes(lista);
  res.json({ ok: true, cliente: novo });
});

app.put('/api/clientes/:id', (req, res) => {
  const lista = readClientes();
  const idx = lista.findIndex(x => x.id === req.params.id);
  if (idx === -1) return res.status(404).json({ erro: 'Cliente não encontrado' });
  lista[idx] = { ...lista[idx], ...req.body, id: req.params.id };
  writeClientes(lista);
  res.json({ ok: true, cliente: lista[idx] });
});

// ── Páginas do e-commerce (têm prioridade sobre static) ──────────────────────
app.get('/',         (req, res) => res.sendFile(path.join(__dirname, 'feminnita-home.html')));
app.get('/loja',     (req, res) => res.sendFile(path.join(__dirname, 'feminnita-home.html')));
app.get('/admin',    (req, res) => res.sendFile(path.join(__dirname, 'feminnita-admin.html')));
app.get('/produtos', (req, res) => res.sendFile(path.join(__dirname, 'feminnita-plp.html')));
app.get('/carrinho', (req, res) => res.sendFile(path.join(__dirname, 'feminnita-carrinho.html')));
app.get('/checkout', (req, res) => res.sendFile(path.join(__dirname, 'feminnita-checkout.html')));
app.get('/sobre',    (req, res) => res.sendFile(path.join(__dirname, 'feminnita-sobre.html')));
app.get('/login',    (req, res) => res.sendFile(path.join(__dirname, 'feminnita-login.html')));
app.get('/cadastro', (req, res) => res.sendFile(path.join(__dirname, 'feminnita-cadastro.html')));
app.get('/conta',    (req, res) => res.sendFile(path.join(__dirname, 'feminnita-minha-conta.html')));
app.get('/blog',     (req, res) => res.sendFile(path.join(__dirname, '_site', 'index.html')));

// ── Arquivos estáticos (CSS, JS, imagens, etc.) ───────────────────────────────
app.use(express.static(path.join(__dirname), { index: false }));
app.use('/blog', express.static(path.join(__dirname, '_site')));

// ── Start ─────────────────────────────────────────────────────────────────────
app.listen(PORT, () => {
  console.log(`\n  ✦ Feminnita Server rodando em http://localhost:${PORT}`);
  console.log(`  ✦ Admin:  http://localhost:${PORT}/admin`);
  console.log(`  ✦ Config: http://localhost:${PORT}/api/config\n`);
});
