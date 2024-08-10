import os


def generate_rst_for_modules(base_path):
    """Génère des fichiers .rst pour chaque module dans le répertoire donné et ses sous-répertoires."""

    def process_directory(directory, module_prefix):
        """Traite les fichiers Python dans le répertoire donné et ses sous-répertoires."""
        for entry in os.listdir(directory):
            full_path = os.path.join(directory, entry)
            if os.path.isdir(full_path):
                # Si c'est un répertoire, récursivement traiter les
                # sous-répertoires
                process_directory(full_path, f"{module_prefix}.{entry}")
            elif entry.endswith(".py") and entry != "__init__.py":
                # Traite les fichiers Python
                module_name = entry[:-3]  # Enlève '.py'
                rst_file = os.path.join(
                    output_dir, f"{module_prefix}.{module_name}.rst"
                )

                with open(rst_file, "w") as f:
                    f.write(f"{module_prefix}.{module_name}\n")
                    f.write("=" * len(f"{module_prefix}.{module_name}") + "\n\n")
                    f.write(f".. automodule:: {module_prefix}.{module_name}\n")
                    f.write("    :members:\n")
                    f.write("    :undoc-members:\n")
                    f.write("    :show-inheritance:\n")

                print(f"Generated file: {rst_file}")

    # Répertoire de base pour les modules
    modules_dir = os.path.join(base_path, "infrastructure")
    output_dir = os.path.join(base_path, "docs/source")

    # Assurez-vous que le répertoire de sortie existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Générer les fichiers .rst pour les modules Python
    process_directory(modules_dir, "infrastructure")

    # Générer un fichier index.rst avec toutes les références
    index_rst = os.path.join(output_dir, "index.rst")
    with open(index_rst, "w") as f:
        f.write("Documentation\n")
        f.write("=============\n\n")
        f.write(".. toctree::\n")
        f.write("   :maxdepth: 10\n\n")

        for filename in os.listdir(output_dir):
            if filename.endswith(".rst") and filename != "index.rst":
                f.write(f"   {filename[:-4]}\n")

    print(f"Generated index file: {index_rst}")


# Appel de la fonction avec le chemin relatif approprié
generate_rst_for_modules("stockage_service")
