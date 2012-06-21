from setuptools import setup, find_packages

setup(name="tweetBox",
  version=0.1,
  download_url='https://github.com/jayrambhia/tweetBox/tarball/master',
  description="Lite graphical user interface to update twitter status",
  keywords='twitter, tweet, box, gtk, gui,tweepy',
  author='Jay Rambhia',
  author_email='jayrambhia777@gmail.com',
  license='MIT',
  packages = find_packages(),
  requires=['gtk','tweepy'],
  scripts=['tweetBox/scripts/tweetBox']
  )
