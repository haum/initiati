all: plateau.svg

plateau.svg: svg-doors svg-header svg-footer
	cat svg-header svg-doors svg-footer > plateau.svg

svg-doors: gen-doors.py
	python3 gen-doors.py > svg-doors

svg-header: template.svg
	sed -n -e '/<!-- TEMPLATE CUT -->/,$$!p' template.svg > $@

svg-footer: template.svg
	sed -n -e '1,/<!-- TEMPLATE CUT -->/!p' template.svg > $@

clean:
	rm -f svg-doors svg-header svg-footer plateau.svg
