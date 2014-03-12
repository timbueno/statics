PY=python
STATICS=app.py

help:
	@echo 'Makefile for a Statics Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make regenerate                  (re)generate the web site          '
	@echo '   make github                      upload via gh-pages                '
	@echo '                                                                       '

regenerate:
	$(PY) $(STATICS) build

github: regenerate
	ghp-import build
	git push origin gh-pages