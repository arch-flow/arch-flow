from setuptools import setup


setup(name='arch-flow',
    version='0.1',
    license='MIT License',
    author='Carlos Vinicius Da Silva',
    long_description="O ArchFlow é uma plataforma de código aberto projetada para simplificar o desenvolvimento de automações. Inspirado no conceito de peças de Lego, o ArchFlow oferece uma variedade de módulos independentes, cada um com funcionalidades específicas. Esses módulos podem ser combinados de forma flexível para atender às necessidades de automação de diferentes projetos. Com uma arquitetura modular e uma ampla gama de funções, o ArchFlow permite aos desenvolvedores criar soluções eficientes e personalizadas, reduzindo o tempo e esforço necessários para o desenvolvimento de software.",
    long_description_content_type="text/markdown",
    author_email='vini989073599@gmail.com',
    keywords='arch flow',
    description=u'O ArchFlow é uma plataforma de código aberto projetada para simplificar o desenvolvimento de automações.',
    packages=['arch_flow', 'arch_flow.exceptions', 'arch_flow.implementations', 'arch_flow.output', 'arch_flow.utils'],
    install_requires=['colorama'],)