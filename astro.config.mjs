// Diana Fauna & Flora: info site and user guide.
// Published by GitHub Pages at https://diana-faunaflora.github.io/
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { sidebar } from './src/sidebar.mjs';

export default defineConfig({
  site: 'https://diana-faunaflora.github.io',
  base: '/',
  trailingSlash: 'always',
  integrations: [
    starlight({
      title: { en: 'Diana user guide', nl: 'Diana handleiding', de: 'Diana Anleitung', pt: 'Guia de Diana', da: 'Diana brugervejledning', fr: 'Guide d’utilisation Diana', it: 'Guida all’uso di Diana', es: 'Guía de uso de Diana' },
      description: 'Diana Fauna & Flora, the free map app for WWFF activators and hunters.',
      logo: { src: './src/assets/diana-logo.png', alt: 'Diana' },
      favicon: '/icon-192.png',
      defaultLocale: 'root',
      locales: {
        root: { label: 'English', lang: 'en' },
        nl: { label: 'Nederlands', lang: 'nl' },
        fr: { label: 'Français', lang: 'fr' },
        de: { label: 'Deutsch', lang: 'de' },
        da: { label: 'Dansk', lang: 'da' },
        it: { label: 'Italiano', lang: 'it' },
        es: { label: 'Español', lang: 'es' },
        pt: { label: 'Português', lang: 'pt' },
      },
      sidebar,
      customCss: ['./src/styles/fonts.css', './src/styles/diana.css'],
      components: {
        SocialIcons: './src/components/HeaderLinks.astro',
      },
      head: [
        { tag: 'link', attrs: { rel: 'apple-touch-icon', href: '/apple-touch-icon.png' } },
        { tag: 'meta', attrs: { name: 'theme-color', content: '#1b4332' } },
      ],
      tableOfContents: { minHeadingLevel: 2, maxHeadingLevel: 2 },
      lastUpdated: false,
      pagination: true,
    }),
  ],
});
