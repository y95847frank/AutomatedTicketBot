from setuptools import setup

setup(name='AutoTicketsBot',
      version='0.0.1',
      description='A python package to automatically reserve tickets on a Chinese ticket selling website.',
      url='https://github.com/y95847frank/AutomatedTicketBot',
      author='y95847frank',
      author_email='y95847@gmail.com',
      license='MIT',
      packages=[
          'AutoTicketsBot'
      ],
      install_requires=[
          'splinter',
          'schedule',
          'PyYAML'
      ],
      python_requires='>=3',
      )