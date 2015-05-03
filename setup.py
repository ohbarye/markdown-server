from setuptools import setup, find_packages

setup(
    name     = 'markdownserver',
    version  = '0.1.0',
    packages = find_packages(),
    include_packages_data = True,
    install_requires = [
        'bottle',
        'Markdown',
        'Pygments',
        'py-gfm',
    ],

    entry_points = """
        [console_scripts]
        markdownserver = markdownserver:main
    """,
)
