// See https://observablehq.com/framework/config for documentation.
export default {
  title: "Visualização de Dados",

  pages: [
    {
      name: "1 - Introdução",
      open: false,
      pages: [
        {name: "1.1 - Apresentação", path: "/1-Apresentacao"},
      ]
    },
    {
      name: "2 - Desenvolvimento",
      open: false,
      pages: [
        {name: "2.1 - Popularidade Musical", path: "/2-Popularidade_musical"},
        {name: "2.2 - Top 10", path: "/3-Top10"},
        {name: "2.3 - Comparativo", path: "/4-Comparativo"},
      ]
    },
    {
      name: "3 - Fechamento",
      open: false,
      pages: [
        {name: "3.1 - Discussão", path: "/5-Discussao"},
        {name: "3.2 - Conclusão", path: "/6-Conclusao"},
      ]
    }
  ],

  theme: "light",
};
