py -3 -m pdoc --html --force --output-dir .\docs .\FangCore2
xcopy /s/e .\docs\FangCore2\* .\docs
rmdir /s .\docs\FangCore2

.\docs\index.html