// Sidebar of the user guide. Each group lists the pages of one folder under
// src/content/docs/guide/, in the order set by `sidebar.order` in each page.
// Group names in the eight languages of the app.
const group = (dir, en, t) => ({
  label: en,
  translations: t,
  collapsed: dir !== 'start',
  items: [{ autogenerate: { directory: `guide/${dir}` } }],
});

export const sidebar = [
  group('start', 'Getting started', { nl: 'Aan de slag', fr: 'Premiers pas', de: 'Erste Schritte', da: 'Kom i gang', it: 'Per iniziare', es: 'Primeros pasos', pt: 'Primeiros passos' }),
  group('map', 'The map', { nl: 'De kaart', fr: 'La carte', de: 'Die Karte', da: 'Kortet', it: 'La mappa', es: 'El mapa', pt: 'O mapa' }),
  group('spots', 'Spots and agenda', { nl: 'Spots en agenda', fr: 'Spots et agenda', de: 'Spots und Agenda', da: 'Spots og agenda', it: 'Spot e agenda', es: 'Spots y agenda', pt: 'Spots e agenda' }),
  group('field-info', 'Field info', { nl: 'Veldinfo', fr: 'Infos terrain', de: 'Feldinfo', da: 'Feltinfo', it: 'Info sul campo', es: 'Info de campo', pt: 'Info de campo' }),
  group('rules', 'Rules and band plan', { nl: 'Regels en bandplan', fr: 'Règles et plan de bandes', de: 'Regeln und Bandplan', da: 'Regler og båndplan', it: 'Regole e band plan', es: 'Reglas y plan de bandas', pt: 'Regras e plano de bandas' }),
  group('settings', 'Settings', { nl: 'Instellingen', fr: 'Réglages', de: 'Einstellungen', da: 'Indstillinger', it: 'Impostazioni', es: 'Ajustes', pt: 'Definições' }),
  group('travel', 'Travelling', { nl: 'Op reis', fr: 'En voyage', de: 'Auf Reisen', da: 'På rejse', it: 'In viaggio', es: 'De viaje', pt: 'Em viagem' }),
  group('help', 'Problems and questions', { nl: 'Problemen en vragen', fr: 'Problèmes et questions', de: 'Probleme und Fragen', da: 'Problemer og spørgsmål', it: 'Problemi e domande', es: 'Problemas y preguntas', pt: 'Problemas e perguntas' }),
  group('about', 'About Diana', { nl: 'Over Diana', fr: 'À propos de Diana', de: 'Über Diana', da: 'Om Diana', it: 'Su Diana', es: 'Sobre Diana', pt: 'Sobre a Diana' }),
];
