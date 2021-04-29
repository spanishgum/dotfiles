# dotfiles
My personal configuration dot files. I have left Windows for Ubuntu 16.04 these days and have found it to be extremely rewarding.

I have streamlined this process of loading my full configuration on a brand new instance:

```bash
# clone this repo
git clone http://github.com/spanishgum/dotfiles
cd dotfiles

# Add ppa repositories found in `.apt-repos`
# (some dependencies require non standard repos)
cat .apt-repos | xargs sudo apt-add-repository

# Install packages
cat .aptpacks | xargs sudo apt-get install -y

# use my i3 pre-configured layout
cp -r .config/ ~
# NOTE:
# In my .config/i3/config file, I have paths specific to my directories.
# Go in and change these to avoid errors
```