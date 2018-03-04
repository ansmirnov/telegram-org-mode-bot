from setuptools import setup

setup(name='tg_orgmode_bot',
      version='0.1',
      description='Simple bot for using Telegram as "Inbox" in GTD.',
      url='https://github.com/ansmirnov/telegram-org-mode-bot',
      author='Andrey Smirnov',
      author_email='mail@ansmirnov.ru',
      license='MIT',
      packages=['tg_orgmode_bot'],
      install_requires=[
          'python-telegram-bot',
      ],
      entry_points = {
        'console_scripts': ['tg_orgmode_bot=tg_orgmode_bot.bot:run'],
      },
      zip_safe=False)
