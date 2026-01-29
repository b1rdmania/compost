import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'Compost',
  description: 'The capital formation layer for Hyperliquid builder markets',

  head: [
    ['link', { rel: 'icon', href: '/logo.svg' }],
    ['meta', { property: 'og:title', content: 'Compost Docs' }],
    ['meta', { property: 'og:description', content: 'The capital formation layer for Hyperliquid builder markets' }],
    ['meta', { name: 'twitter:card', content: 'summary' }],
    ['meta', { name: 'twitter:site', content: '@compostfi' }],
  ],

  themeConfig: {
    logo: '/logo.svg',
    siteTitle: 'Compost',

    nav: [
      { text: 'Home', link: '/' },
      { text: 'Website', link: 'https://compost.fi' },
      { text: 'Twitter', link: 'https://twitter.com/compostfi' }
    ],

    sidebar: [
      {
        text: 'Introduction',
        items: [
          { text: 'Overview', link: '/' }
        ]
      },
      {
        text: 'Context',
        collapsed: false,
        items: [
          { text: 'What is Hyperliquid?', link: '/context/what-is-hyperliquid' },
          { text: 'What is HIP-3?', link: '/context/what-is-hip-3' },
          { text: 'The Barrier', link: '/context/the-barrier' },
          { text: 'The Opportunity', link: '/context/the-opportunity' },
          { text: 'The Problem', link: '/context/the-problem' }
        ]
      },
      {
        text: 'Solution',
        collapsed: false,
        items: [
          { text: 'What is Compost?', link: '/solution/what-is-compost' },
          { text: 'Who It\'s For', link: '/solution/who-its-for' },
          { text: 'cHYPE', link: '/solution/chype' }
        ]
      },
      {
        text: 'Technical',
        collapsed: false,
        items: [
          { text: 'Architecture', link: '/technical/architecture' },
          { text: 'Yield Sources', link: '/technical/yield-sources' },
          { text: 'Yield Flow', link: '/technical/yield-flow' },
          { text: 'Allocation', link: '/technical/allocation' },
          { text: 'Fees', link: '/technical/fees' },
          { text: 'Redemptions', link: '/technical/redemptions' },
          { text: 'Risk', link: '/technical/risk' }
        ]
      },
      {
        text: 'Ecosystem',
        collapsed: false,
        items: [
          { text: 'Integrations', link: '/ecosystem/integrations' },
          { text: 'Institutional', link: '/ecosystem/institutional' }
        ]
      },
      {
        text: 'Appendix',
        collapsed: true,
        items: [
          { text: 'Contracts', link: '/appendix/contracts' },
          { text: 'Audit', link: '/appendix/audit' },
          { text: 'Team', link: '/appendix/team' },
          { text: 'FAQ', link: '/appendix/faq' },
          { text: 'Links', link: '/appendix/links' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'twitter', link: 'https://twitter.com/compostfi' },
      { icon: 'github', link: 'https://github.com/b1rdmania/compost' }
    ],

    footer: {
      message: 'The capital formation layer for Hyperliquid builder markets.',
      copyright: '© 2026 Compost Finance'
    },

    search: {
      provider: 'local'
    }
  }
})
