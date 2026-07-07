// Famous Ramous — Pandoc/Typst Template
// Corporate Identity: Gold #C9A14A · Schwarz #000 · Weiß #FFF
// Verwendung: pandoc input.md -o output.pdf --pdf-engine=typst --template=templates/famous-ramous.typ

// === Brand Tokens ===
#let brand-gold = rgb("#C9A14A")
#let brand-gold-dark = rgb("#A6812F")
#let brand-black = rgb("#0A0A0A")
#let brand-grey = rgb("#3A3A3A")
#let brand-grey-light = rgb("#E8E4D9")

// === Pfad zum Logo ===
#let logo-path = "$if(logo)$$logo$$else$Logo/Famous_Ramous_Logo_gold_trans.png$endif$"

// === Page Setup ===
#set page(
  paper: "$if(papersize)$$papersize$$else$a4$endif$",
  margin: (
    top: 2cm,
    bottom: 2.2cm,
    left: 2cm,
    right: 2cm,
  ),
  footer: context {
    let page-num = counter(page).get().first()
    align(center)[
      #line(length: 100%, stroke: 0.6pt + brand-gold)
      #v(2pt)
      #text(size: 8pt, fill: brand-gold-dark, weight: "semibold", tracking: 1pt)[
        EHRLICH. GESUND. STARK.
      ]
      #h(1fr)
      #text(size: 8pt, fill: brand-grey)[
        Seite #page-num
      ]
    ]
  },
)

// === Font Setup ===
#set text(
  font: ("Helvetica Neue", "Helvetica", "Arial"),
  size: 10.5pt,
  fill: brand-black,
  lang: "de",
)

#set par(
  justify: false,
  leading: 0.7em,
  spacing: 0.95em,
)

// === Headings ===
#show heading.where(level: 1): it => {
  v(0.4em)
  block[
    #text(
      size: 22pt,
      weight: "bold",
      fill: brand-black,
      tracking: -0.3pt,
    )[#it.body]
    #v(-2pt)
    #line(length: 60pt, stroke: 2.5pt + brand-gold)
  ]
  v(0.5em)
}

// Variante B: vor "Was MEF ist" einen Seitenumbruch erzwingen,
// damit M/E/F immer auf einer einzelnen Seite zusammenstehen.
#show heading.where(level: 2): it => {
  if it.body == [Was MEF ist] or it.body == [Die ganze Reise im Überblick] {
    pagebreak(weak: false)
  }
  v(0.6em)
  block[
    #text(
      size: 16pt,
      weight: "bold",
      fill: brand-black,
    )[#it.body]
  ]
  v(0.2em)
}

#show heading.where(level: 3): it => {
  v(0.4em)
  block[
    #text(
      size: 12.5pt,
      weight: "bold",
      fill: brand-gold-dark,
      tracking: 0.3pt,
    )[#upper(it.body)]
  ]
}

// === Strong / Emphasis ===
#show strong: it => text(weight: "bold", fill: brand-black)[#it.body]
#show emph: it => text(style: "italic", fill: brand-grey)[#it.body]

// === Lists ===
#set list(
  marker: ([▸], [•]),
  indent: 0.4em,
  body-indent: 0.6em,
  spacing: 0.55em,
)

// === Tables ===
#set table(
  inset: 8pt,
  stroke: (x, y) => (
    bottom: if y == 0 { 1.2pt + brand-gold } else { 0.4pt + brand-grey-light },
    top: none,
    left: none,
    right: none,
  ),
  fill: (x, y) => if y == 0 { brand-black } else { white },
  align: left + horizon,
)

// Force left-align body cells (no justify) — fixes the "Was du erreichst" stretching
#show table.cell.where(y: 0): it => {
  set text(fill: brand-gold, weight: "bold", size: 9.5pt, tracking: 0.5pt)
  upper(it)
}

#show table.cell: it => {
  set par(justify: false, leading: 0.6em)
  set text(size: 10pt)
  it
}

// === Horizontal Rule ===
#let horizontalrule = {
  v(0.5em)
  align(center)[
    #line(length: 30%, stroke: 1pt + brand-gold)
  ]
  v(0.5em)
}

// === Block Quote ===
#show quote: it => block(
  fill: brand-grey-light,
  inset: 12pt,
  stroke: (left: 3pt + brand-gold),
  radius: 2pt,
  width: 100%,
)[#text(style: "italic")[#it.body]]

// === Links ===
#show link: it => text(fill: brand-gold-dark, weight: "medium")[#it.body]

// === Cover Header (Logo) ===
#let cover-block = block[
  #align(center)[
    #image(logo-path, width: 4.5cm)
    #v(0.3em)
    #line(length: 30%, stroke: 0.8pt + brand-gold)
  ]
  #v(0.8em)
]

// === Pandoc Variables Pass-Through ===
$if(highlighting-definitions)$
$highlighting-definitions$
$endif$

// === Document Body ===
#cover-block

$body$
