# Astro Starter Kit: Minimal

```sh
npm create astro@latest -- --template minimal
```

[![Open in StackBlitz](https://developer.stackblitz.com/img/open_in_stackblitz.svg)](https://stackblitz.com/github/withastro/astro/tree/latest/examples/minimal)
[![Open with CodeSandbox](https://assets.codesandbox.io/github/button-edit-lime.svg)](https://codesandbox.io/p/sandbox/github/withastro/astro/tree/latest/examples/minimal)
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/withastro/astro?devcontainer_path=.devcontainer/minimal/devcontainer.json)

> 🧑‍🚀 **Seasoned astronaut?** Delete this file. Have fun!

## 🚀 Project Structure

The project follows the Atomic Design methodology for organizing components, and uses Astro for building fast, content-focused websites.

Here's the structure of the project:
```text
/
├── public/
├── src/
│   ├── components/
│   │   ├── atoms/
│   │   │   ├── Badge.astro
│   │   │   ├── Button.astro
│   │   │   ├── Card.astro
│   │   │   ├── Icon.astro
│   │   │   ├── ImageComponent.astro
│   │   │   ├── InputField.astro
│   │   │   ├── Label.astro
│   │   │   └── Textarea.astro
│   │   ├── molecules/
│   │   │   ├── AccordionItem.astro
│   │   │   ├── FeatureItem.astro
│   │   │   ├── FooterLink.astro
│   │   │   ├── NavbarItem.astro
│   │   │   ├── ServiceCard.astro
│   │   │   ├── TeamMemberCard.astro
│   │   │   └── TestimonialItem.astro
│   │   ├── organisms/
│   │   │   ├── ApproachSection.astro
│   │   │   ├── ContactSection.astro
│   │   │   ├── Footer.astro
│   │   │   ├── Header.astro
│   │   │   ├── HeroSection.astro
│   │   │   ├── Navbar.astro
│   │   │   ├── ServicesSection.astro
│   │   │   └── TestimonialsSection.astro
│   │   └── layouts/
│   │       ├── MainLayout.astro
│   │       └── ServiceLayout.astro
│   ├── pages/
│   │   ├── index.astro
│   │   ├── solutions.astro
│   │   ├── services/
│   │   │   ├── index.astro
│   │   │   ├── creation-de-landing-pages.astro
│   │   │   ├── developpement-front-end-back-end.astro
│   │   │   ├── integration-de-solutions-erp-odoo.astro
│   │   │   ├── developpement-applications-web.astro
│   │   │   ├── seo-referencement-naturel.astro
│   │   │   ├── gestion-de-communaute.astro
│   │   │   └── projets-intelligence-artificielle.astro
│   │   ├── approche-psd.astro
│   │   ├── a-propos-de-nous.astro
│   │   └── contact.astro
│   ├── assets/
│   │   ├── docs/
│   │   ├── icons/
|   |   └── illustration/ 
├── package.json
├── astro.config.mjs
├── tailwind.config.js
├── tsconfig.json
└── README.md
```

Astro looks for `.astro` or `.md` files in the `src/pages/` directory. Each page is exposed as a route based on its file name.

There's nothing special about `src/components/`, but that's where we like to put any Astro/React/Vue/Svelte/Preact components.

Any static assets, like images, can be placed in the `public/` directory.


## 🛠️ Technologie used

Astro: A modern static site builder that delivers lightning-fast performance.
Tailwind CSS: A utility-first CSS framework for rapid UI development.
Docker: For containerizing the application and ensuring consistent environments.
Node.js and npm: For managing dependencies and running the development server.

## 📖 About the Project

The AppInFlow website is designed to showcase our services and solutions, following best practices in web development and design. We have organized our components using the Atomic Design methodology to promote reusability and maintainability.
Sitemap
Accueil
Solutions
Services
Création de Landing Pages
Développement Front-End & Back-End
Intégration de Solutions ERP Odoo
Développement d'Applications Web
SEO (Référencement Naturel)
Gestion de Communauté
Projets d'Intelligence Artificielle
Approche PSD (Process Simplification & Digitalization)
À Propos de Nous
Contact

## 🔧 Getting Started

Prerequisites
Node.js (v14.x or higher)
npm (v6.x or higher)
Docker (optional, if you wish to run the project in a container)

## Installation

1.Clone the repository:
    
```text
git clone git@github.com:chabbanadir/ChabbaDev.git
```
2.Navigate to the project directory:
```text
cd ChabbaDev
```
1.Install dependencies:
```text
npm install
```

## Running the Development Server

To start the local development server:
```text
npm run dev
```

## 🧩 Project Structure Details

Components
The components are organized following the Atomic Design methodology:

Atoms: Basic building blocks (e.g., Button, Icon, InputField).
Molecules: Combinations of atoms (e.g., NavbarItem, ServiceCard).
Organisms: Complex components made up of molecules and atoms (e.g., Header, Footer, HeroSection).
Layouts: Page layouts that structure the overall page (e.g., MainLayout, ServiceLayout).
Pages
The pages are located in the src/pages/ directory and correspond to the routes of the website.

Data
Static data used in the site is stored in the src/data/ directory (e.g., services, team members, testimonials).

Styles
Tailwind CSS is used for styling. The main Tailwind CSS file is src/styles/tailwind.css.
Custom styles and component-specific styles can be added in src/styles/components.css or within the components themselves using <style> blocks.

## 🧞 Commands

All commands are run from the root of the project, from a terminal:

| Command                   | Action                                           |
| :------------------------ | :----------------------------------------------- |
| `npm install`             | Installs dependencies                            |
| `npm run dev`             | Starts local dev server at `localhost:4321`      |
| `npm run build`           | Build your production site to `./dist/`          |
| `npm run preview`         | Preview your build locally, before deploying     |
| `npm run astro ...`       | Run CLI commands like `astro add`, `astro check` |
| `npm run astro -- --help` | Get help using the Astro CLI                     |

## 🐳 Using Docker (Optional)

If you prefer to run the project within a Docker container:

1.Build the Docker image:
```text
npm run dev
```
2.Run the Docker container:
```text
docker run -p 4321:4321 appinflow-website
```
The site will be accessible at http://localhost:4321.

## 👥 Contributing
We welcome contributions! Please open an issue or submit a pull request.

## 📄 License
This project is licensed under the MIT License.

##  📞 Contact
For questions or support, please contact us at moh.chabba@gmail.com.
