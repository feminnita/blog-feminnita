module.exports = function (eleventyConfig) {

  /* ── Arquivos estáticos passados sem processamento ─── */
  eleventyConfig.addPassthroughCopy("style.css");
  eleventyConfig.addPassthroughCopy("script.js");
  eleventyConfig.addPassthroughCopy("admin");
  eleventyConfig.addPassthroughCopy("sobre.html");
  eleventyConfig.addPassthroughCopy("treinamento.html");
  eleventyConfig.addPassthroughCopy("comunidade.html");

  /* ── Ignora arquivos que o Eleventy não deve processar ─ */
  eleventyConfig.ignores.add("node_modules/**");
  eleventyConfig.ignores.add("_site/**");
  eleventyConfig.ignores.add("index.html");       /* substituído por index.njk */
  eleventyConfig.ignores.add("artigo.html");       /* substituído pelo template */
  eleventyConfig.ignores.add("artigo-tecidos.html");
  eleventyConfig.ignores.add("memory/**");
  eleventyConfig.ignores.add(".claude/**");
  eleventyConfig.ignores.add("README.md");

  /* ── Coleção de artigos (mais recentes primeiro) ────── */
  eleventyConfig.addCollection("artigos", function (collectionApi) {
    return collectionApi
      .getFilteredByGlob("artigos/**/*.md")
      .sort((a, b) => b.date - a.date);
  });

  /* ── Filtros de data (pt-BR, sem dependências externas) */
  const MESES = [
    "janeiro","fevereiro","março","abril","maio","junho",
    "julho","agosto","setembro","outubro","novembro","dezembro"
  ];

  eleventyConfig.addFilter("dataFormatada", function (date) {
    const d = new Date(date);
    return `${d.getUTCDate()} de ${MESES[d.getUTCMonth()]} de ${d.getUTCFullYear()}`;
  });

  eleventyConfig.addFilter("dataCurta", function (date) {
    const d = new Date(date);
    const mes = MESES[d.getUTCMonth()].slice(0, 3);
    return `${String(d.getUTCDate()).padStart(2, "0")} ${mes} ${d.getUTCFullYear()}`;
  });

  /* ── Filtros de categoria ───────────────────────────── */
  const CAT_LABEL = {
    "bem-estar":   "Bem-Estar",
    "tecidos":     "Tecidos",
    "treinamento": "Treinamento",
    "comunidade":  "Comunidade",
    "datas":       "Datas Especiais"
  };
  const CAT_ICON = {
    "bem-estar":   "fa-moon",
    "tecidos":     "fa-scissors",
    "treinamento": "fa-chart-line",
    "comunidade":  "fa-heart",
    "datas":       "fa-gift"
  };

  eleventyConfig.addFilter("catLabel", (cat) => CAT_LABEL[cat] || cat);
  eleventyConfig.addFilter("catIcon",  (cat) => CAT_ICON[cat]  || "fa-tag");

  /* ── Configuração geral ─────────────────────────────── */
  return {
    templateFormats: ["njk", "md"],   /* só processa .njk e .md — HTML vai via passthrough */
    markdownTemplateEngine: "njk",
    dir: {
      input:    ".",
      output:   "_site",
      includes: "_includes",
      layouts:  "_layouts"
    }
  };
};
