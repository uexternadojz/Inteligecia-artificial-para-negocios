// @ts-check
import { defineConfig } from "astro/config";

import tailwindcss from "@tailwindcss/vite";

// GitHub Pages configuration
// Repository: https://github.com/uexternadojz/Inteligecia-artificial-para-negocios
const site = process.env.SITE_URL || "https://uexternadojz.github.io";
const base = process.env.BASE_PATH || "/Inteligecia-artificial-para-negocios";

// https://astro.build/config
export default defineConfig({
  site,
  base,
  output: "static", // SSG mode for GitHub Pages
  build: {
    assets: "_astro", // Standard Astro assets folder
  },
  vite: {
    plugins: [tailwindcss()],
  },
});
