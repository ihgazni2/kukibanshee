pip3 uninstall kukibanshee
git rm -r dist
git rm -r build
git rm -r kukibanshee.egg-info
rm -r dist
rm -r build
rm -r kukibanshee.egg-info
git add .
git commit -m "remove old build"
git push origin master
python3 setup.py install --record install.txt
git add .
git commit -m "$1"
git push origin master

