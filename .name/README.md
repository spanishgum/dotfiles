## ASCII art name
namefetch.sh will grab print to the screen the contents of art.txt,
which is a soft link to an art file.

playname.sh will loop through all the ascii art name files, but making
sure to only print ones that can fit on the screen.

an art file here is any file with the .art extension.

grab your favorited generated art from [here](http://patorjk.com/software/taag/) and copy it to files in this directory.

getart.py is a python3 script that depends on phantomjs and selenium. It creates an art folder, and downloads every
available ascii art from the website linked above, given the text specified by the -t flag argument.
You can get this working like so:

  - sudo pip3 install selenium
  - npm install phantomjs-prebuilt # note if you try to install with apt-get, you will not have all dependencies
