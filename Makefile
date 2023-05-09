CC = gcc
PYTHON = python3
COMPILER = compiler.py
MAIN = main.c
PROGRAMS = $(wildcard programs/*.s)
DOXYFILE = Doxyfile

all: run

run:
	@echo "Available programs:"
	@for p in $(PROGRAMS); do echo " - $$(basename $${p} _test.s)"; done
	@echo "Enter program name: " && read program && \
	if [[ -z $${program} ]]; then echo "No program entered."; exit 1; fi && \
	if ! (echo $(PROGRAMS) | grep -q "\b$${program}_test.s\b"); then echo "Invalid program name."; exit 1; fi && \
	echo "Do you want the VERBOSE mode? [y/N]" && read verbose && \
	if [[ $${verbose} == "y" ]]; then verbose="VERBOSE"; else verbose=""; fi && \
	echo "Compiling and running $${program}..." && \
	$(PYTHON) $(COMPILER) programs/$${program}_test.s && \
	$(CC) -o main $(MAIN) && \
	if [[ -n $${verbose} ]]; then ./main programs/$${program}_test.bin programs/$${program}_state.txt $${verbose}; else ./main programs/$${program}_test.bin programs/$${program}_state.txt; fi

doc:
	doxygen documentation/$(DOXYFILE)
	@echo "Documentation generated in ./doc folder"

clean:
	@if test -d documentation/html; then rm -rf documentation/html; fi
	@if test -d documentation/latex; then rm -rf documentation/latex; fi
	@for file in ./programs/*.bin; do if test -f $$file; then rm $$file; fi; done
	@if test -f ./*.bin; then rm ./*.bin; fi
	@if test -f main; then rm main; fi
	@echo "Doc and binaries removed"