import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://baibiandance.netlify.app',
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto'
  },
  prefetch: {
    defaultStrategy: 'viewport'
  }
});