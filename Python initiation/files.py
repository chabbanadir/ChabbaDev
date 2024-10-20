import os
from pathlib import Path

# Define the base directory (replace with your project root if different)
BASE_DIR = Path(__file__).resolve().parent

# Define the directory and file structure
structure = {
    'components': {
        'atoms': [
            'Button.astro',
            'Icon.astro',
            'InputField.astro',
            'Textarea.astro',
            'Label.astro',
            'Card.astro',
            'ImageComponent.astro',
            'Badge.astro',
        ],
        'molecules': [
            'NavbarItem.astro',
            'FooterLink.astro',
            'AccordionItem.astro',
            'ServiceCard.astro',
            'TestimonialItem.astro',
            'TeamMemberCard.astro',
            'FeatureItem.astro',
        ],
        'organisms': [
            'Header.astro',
            'Navbar.astro',
            'HeroSection.astro',
            'ServicesSection.astro',
            'ApproachSection.astro',
            'TestimonialsSection.astro',
            'ContactSection.astro',
            'Footer.astro',
        ],
        'layouts': [
            'MainLayout.astro',
            'ServiceLayout.astro',
        ],
    },
    'pages': {
        'solutions.astro': None,
        'services': {
            'index.astro': None,
            'creation-de-landing-pages.astro': None,
            'developpement-front-end-back-end.astro': None,
            'integration-de-solutions-erp-odoo.astro': None,
            'developpement-applications-web.astro': None,
            'seo-referencement-naturel.astro': None,
            'gestion-de-communaute.astro': None,
            'projets-intelligence-artificielle.astro': None,
        },
        'approche-psd.astro': None,
        'a-propos-de-nous.astro': None,
        'contact.astro': None,
    },
}

def create_structure(base_path, structure):
    for name, content in structure.items():
        dir_path = base_path / name
        if isinstance(content, dict):
            # Create directory
            dir_path.mkdir(parents=True, exist_ok=True)
            # Recurse into subdirectories
            create_structure(dir_path, content)
        elif isinstance(content, list):
            # Create directory
            dir_path.mkdir(parents=True, exist_ok=True)
            # Create files in the directory
            for filename in content:
                file_path = dir_path / filename
                file_path.touch(exist_ok=True)
        elif content is None:
            # Create file
            file_path = base_path / name
            file_path.touch(exist_ok=True)
        else:
            # If content is not recognized, skip
            pass

if __name__ == '__main__':
    create_structure(BASE_DIR, structure)
    print("Project structure created successfully.")
