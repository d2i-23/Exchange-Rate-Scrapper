import subprocess

# List of libraries and their versions
libraries = [
    'beautifulsoup4==4.12.3',
    'greenlet==3.0.3',
    'numpy==2.0.0',
    'pandas==2.2.2',
    'playwright==1.45.0',
    'pyee==11.1.0',
    'python-dateutil==2.9.0.post0',
    'pytz==2024.1',
    'six==1.16.0',
    'soupsieve==2.5',
    'typing_extensions==4.12.2',
    'tzdata==2024.1'
]

# Install each library
for library in libraries:
    subprocess.check_call(['pip', 'install', library])

# Initate Playwright 
subprocess.check_call(['playwright', 'install'])
