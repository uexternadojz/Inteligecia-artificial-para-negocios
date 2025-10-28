import vinyl01 from "../../assets/vinyls/clase-01/vinilo.webp";
import vinyl02 from "../../assets/vinyls/clase-02/vinilo.webp";
import vinyl03 from "../../assets/vinyls/clase-03/vinilo.webp";

import halo01 from "../../assets/halos/clase-01.webp";
import halo02 from "../../assets/halos/clase-02.webp";
import halo03 from "../../assets/halos/clase-03.webp";

import spine01 from "../../assets/spines/clase-01.png";
import spine02 from "../../assets/spines/clase-02.png";
import spine03 from "../../assets/spines/clase-03.png";

export type ClassStatus = "draft" | "upcoming" | "published";

export interface ClassResource {
  label: string;
  href: string;
  type: "readme" | "slides" | "datasets" | "tools" | "otros";
}

export interface ClassEntry {
  slug: string;
  number: string;
  title: string;
  mood: string;
  synopsis: string;
  status: ClassStatus;
  date: string;
  duration: string;
  modality: string;
  stack: string[];
  metrics: string[];
  resources: ClassResource[];
  vinylImage: ImageMetadata;
  haloImage: ImageMetadata;
  spineImage: ImageMetadata;
}

export const classes: ClassEntry[] = [
  {
    slug: "clase-01-introduccion-ia-corporativa",
    number: "01",
    title: "Introducción IA Corporativa",
    mood: "Penthouse orbital, skyline con haces de datos",
    synopsis:
      "Encendemos la colección con un mapa estratégico de IA corporativa: casos Orbital, marcos de adopción y la mentalidad de impacto.",
    status: "upcoming",
    date: "21 Oct 2025",
    duration: "2h",
    modality: "Presencial / Demo Lab",
    stack: ["Lentes Orbital", "Business Strategy", "Mapa de datos"],
    metrics: ["+12 casos IA Orbital", "Framework adopción 4D", "Checklist IA corporativa"],
    resources: [
      {
        label: "Syllabus general",
        href: "/docs/syllabus",
        type: "readme",
      },
    ],
    vinylImage: vinyl01,
    haloImage: halo01,
    spineImage: spine01,
  },
  {
    slug: "clase-02-vibe-coding",
    number: "02",
    title: "Vibe Coding: IA que Programa",
    mood: "DJ tech mezclando prompts, partículas rojo-cian",
    synopsis:
      "La sesión estelar. Domina Vibe Coding para crear productos funcionales sin escribir código: Lovable, Replit Agent, v0.dev y más.",
    status: "published",
    date: "23 Oct 2025",
    duration: "2h",
    modality: "Práctica 80/20",
    stack: ["Lovable", "Replit Agent", "v0.dev"],
    metrics: ["15+ herramientas", "MVP en 90 minutos", "Casos reales Orbital"],
    resources: [
      {
        label: "Guía completa Clase 02",
        href: "/clases/2025-10-23-clase-02-ia-corporativa/",
        type: "readme",
      },
      {
        label: "Transcripción .vtt",
        href: "/transcripts/clase-02.vtt",
        type: "otros",
      },
    ],
    vinylImage: vinyl02,
    haloImage: halo02,
    spineImage: spine02,
  },
  {
    slug: "clase-03-ia-generativa-visual",
    number: "03",
    title: "IA Generativa Visual",
    mood: "Galería holográfica, mallas visuales flotando",
    synopsis:
      "Diseñamos experiencias visuales con IA: pipelines de Midjourney, Stable Diffusion y loops cinemáticos para campañas.",
    status: "upcoming",
    date: "28 Oct 2025",
    duration: "2h",
    modality: "Demo / Hands-on",
    stack: ["Midjourney", "Imagen 3", "Nano Banana"],
    metrics: ["Guía prompts Orbital", "Workflow entrega creativa", "canvas multimodal"],
    resources: [
      {
        label: "Brief creativo",
        href: "#brief-creativo",
        type: "otros",
      },
    ],
    vinylImage: vinyl03,
    haloImage: halo03,
    spineImage: spine03,
  },
];

export const highlights = [
  {
    title: "Metodología Orbital",
    description: "Laboratorios inmersivos, 80% práctica, retos corporativos reales y feedback en vivo.",
    badge: "Cinemática",
  },
  {
    title: "Stack Inteligente",
    description: "Lovable, Replit, v0.dev, Claude Artifacts y un toolkit curado para prototipar al ritmo del mercado.",
    badge: "Toolset",
  },
  {
    title: "Casos Orbital",
    description: "Strivio, Lighthouse, Jaguar. Narrativas que muestran impacto tangible con dashboards y métricas.",
    badge: "Impacto",
  },
] as const;

export const toolkit = [
  { label: "Lovable", href: "https://lovable.dev" },
  { label: "Replit Agent", href: "https://replit.com/ai" },
  { label: "v0.dev", href: "https://v0.dev" },
  { label: "Claude Artifacts", href: "https://claude.ai" },
  { label: "Cursor IDE", href: "https://cursor.sh" },
  { label: "Gemini Flash", href: "https://ai.google.dev/gemini-api" },
] as const;

export const faqs = [
  {
    question: "¿Necesito saber programar?",
    answer:
      "No. Arrancamos desde cero. La clave es aprender a orquestar prompts, interfaces y decisiones estratégicas para que la IA construya contigo.",
  },
  {
    question: "¿Cómo se entregan los recursos?",
    answer:
      "Cada clase libera README interactivo, transcript y repositorio de assets. Podrás revisarlos desde el micrositio o GitHub.",
  },
  {
    question: "¿Qué necesito llevar?",
    answer:
      "Laptop, cuenta en herramientas IA (puedes usar las versiones free) y mentalidad experimental. Nosotros proveemos datasets y guías.",
  },
] as const;

export const hudMetrics = [
  { label: "Clases activas", value: "03", accent: "red" },
  { label: "Horas en vivo", value: "06h", accent: "cyan" },
  { label: "% práctica", value: "80%", accent: "red" },
  { label: "Herramientas", value: "15+", accent: "cyan" },
] as const;
