# Blog de vacances — une semaine en Provence

Página web estática, em francês, sobre uma semana de férias na Provence, organizada em natureza, cultura e gastronomia. Foi construída com HTML, CSS e JavaScript, sem processo de compilação.

## Executar localmente

A partir da pasta do projeto:

```bash
python3 -m http.server 8000
```

Abre `http://localhost:8000` no browser. Também podes publicar os ficheiros estáticos num alojamento web, respeitando as licenças das imagens e dos recursos externos.

## Estrutura

- `index.html` — conteúdo, navegação e estrutura semântica.
- `css/styles.css` — cores, layout, foco e comportamento responsivo.
- `js/script.js` — animações de entrada, navegação e controlos manuais do carrossel.
- `images/` — imagens locais usadas no artigo.

## Verificações

Não existe uma suite de testes automatizada. Antes de publicar, verifica manualmente a página em desktop e mobile, percorre-a só com teclado, confirma o foco visível e testa os controlos do carrossel. A página usa Google Fonts e Tailwind CDN; estes recursos dependem de terceiros e podem ser bloqueados em algumas redes.

## Direitos dos ativos

Confirma a proveniência, licença e atribuição de cada imagem antes de redistribuir o site. O repositório não concede automaticamente direitos sobre fotografias, marcas ou fontes de terceiros.
