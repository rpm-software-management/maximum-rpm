AUTOMAKE_OPTIONS = 1.4 foreign

images_gif =	@IMAGES_GIF@
hdir =		html

perl =		@__PERL@
collateindex =	@COLLATEINDEX_PL@
redhat_dsl =	../redhat-html.dsl
jade =		@__JADE@

EXTRA_DIST = \
	ChangeLog \
	fix-index \
	redhat-html.dsl \
	rpm8.sgml \
	rpmbuild8.sgml \
	rpmcache8.sgml \
	rpmdeps8.sgml \
	rpmgraph8.sgml \
	intro-to-rpm.sgml \
	max-rpm.sgml \
	pgp-intro.sgml \
	preface.sgml \
	queryformat-tags.sgml \
	rpm-anywhere.sgml \
	rpm-basics.sgml \
	rpm-b-command.sgml \
	rpm-build.sgml \
	rpm-checksig.sgml \
	rpm-commands.sgml \
	rpm-depend.sgml \
	rpm-erase.sgml \
	rpm-file-format.sgml \
	rpm-inside.sgml \
	rpm-install.sgml \
	rpm-manpage.sgml \
	rpmbuild-manpage.sgml \
	rpmcache-manpage.sgml \
	rpmdeps-manpage.sgml \
	rpmgraph-manpage.sgml \
	rpm-miscellania.sgml \
	rpm-multi.sgml \
	rpm-pgp.sgml \
	rpm-philosophy.sgml \
	rpm-query.sgml \
	rpmrc-file.sgml \
	rpm-reloc.sgml \
	rpm-resources.sgml \
	rpm-rpmlib.sgml \
	rpm-rw-build.sgml \
	rpm-specref.sgml \
	rpm-subpack.sgml \
	rpm-upgrade.sgml \
	rpm-verify.sgml \
	xref.sgml

htmldir = 	/usr/share/doc/@PACKAGE@-@VERSION@
html_DATA =	setup genhtml

noinst_DATA =	setup genhtml ChangeLog # max-rpm.tex

$(hdir):
	rm -rf $(hdir)
	mkdir -p $(hdir)/stylesheet-images
	cp $(images_gif)/*.gif $(hdir)/stylesheet-images
	touch generated-index.sgml

setup: $(hdir)
	touch setup

temp-index.sgml: setup redhat-html.dsl $(EXTRA_DIST)
	( cd $(hdir) ; \
	  $(jade) -d $(redhat_dsl) -t sgml -ihtml -V html-index ../max-rpm.sgml ; \
	  $(perl) $(collateindex) -o ../temp-index.sgml HTML.index ; \
	)

generated-index.sgml: temp-index.sgml fix-index
	( cd $(hdir) ; \
	  cat ../temp-index.sgml | ../fix-index > ../generated-index.sgml ; \
	  $(jade) -d $(redhat_dsl) -t sgml -ihtml ../max-rpm.sgml ; \
	)

genhtml: generated-index.sgml
	touch genhtml

max-rpm.tex: generated-index.sgml
	$(jade) -d @DOCBOOK_PRINT_DSL@  -t tex max-rpm.sgml

max-rpm.pdf: max-rpm.tex
	pdfjadetex --output-format=pdf max-rpm.tex

max-rpm.dvi: max-rpm.tex
	jadetex --output-format=dvi max-rpm.tex

max-rpm.ps: max-rpm.dvi
	dvips -o max-rpm.ps max-rpm.dvi

distclean-htmlPROGRAMS:
	-rm -rf html

install-data-local:
	-rm -f $(DESTDIR)$(htmldir)/setup
	-rm -f $(DESTDIR)$(htmldir)/genhtml
	$(mkinstalldirs) $(DESTDIR)$(htmldir)/$(hdir)
	@list='$(hdir)/*'; for p in $$list; do \
	if test -f $(srcdir)/$$p; then \
	    echo " $(INSTALL_DATA) $(srcdir)/$$p $(DESTDIR)$(htmldir)/$$p"; \
	    $(INSTALL_DATA) $(srcdir)/$$p $(DESTDIR)$(htmldir)/$$p; \
	  else if test -f $$p; then \
	    echo " $(INSTALL_DATA) $$p $(DESTDIR)$(htmldir)/$$p"; \
	    $(INSTALL_DATA) $$p $(DESTDIR)$(htmldir)/$$p; \
	  fi; fi; \
	done

ChangeLog: stamp-h.in
	rcs2log > $@

rpm.texi: redhat-html.dsl rpm8.sgml rpm-manpage.sgml
	docbook2texi -d redhat-html.dsl rpm8.sgml > rpm.texi

rpm.8: redhat-html.dsl rpm8.sgml rpm-manpage.sgml
	docbook2man -d redhat-html.dsl rpm8.sgml

rpmbuild.8: redhat-html.dsl rpmbuild8.sgml rpmbuild-manpage.sgml
	docbook2man -d redhat-html.dsl rpmbuild8.sgml

rpmcache.8: redhat-html.dsl rpmcache8.sgml rpmcache-manpage.sgml
	docbook2man -d redhat-html.dsl rpmcache8.sgml

rpmdeps.8: redhat-html.dsl rpmdeps8.sgml rpmdeps-manpage.sgml
	docbook2man -d redhat-html.dsl rpmdeps8.sgml

rpmgraph.8: redhat-html.dsl rpmgraph8.sgml rpmgraph-manpage.sgml
	docbook2man -d redhat-html.dsl rpmgraph8.sgml
