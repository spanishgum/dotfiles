## ASCII art name

Ascii art comes from [here](http://patorjk.com/software/taag/).

#### namefetch.sh
print to the screen the contents of art.txt, a soft link to an art file.

#### playname.sh dir
loop through $1/*.art files, printing ones that can fit on the screen, centered.

#### getart.py

`python3 getart.py --verbose --text $USER --dir art`

python3 script that uses phantomjs and selenium. It downloads every ascii art from
the website linked above, using text specified by the -t flag argument.
I got this working on Ubuntu 16.04 like so:
  - sudo pip3 install selenium
  - npm install phantomjs-prebuilt # apt-get method will not have all dependencies
  - export PATH=$PATH:/path/to/node_modules/phantomjs-prebuilt/bin