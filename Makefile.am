AUTOMAKE_OPTIONS = 1.4 foreign

docbook_css =	@DOCBOOK_CSS@
images_gif =	@IMAGES_GIF@
hdir =		html

perl =		@__PERL@
collateindex =	@COLLATEINDEX_PL@
redhat_dsl =	../redhat-html.dsl
jade =		@__JADE@ -d $(redhat_dsl)

EXTRA_DIST = \
	fix-index \
	redhat-html.dsl \
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

noinst_DATA =	setup genhtml

$(hdir):
	rm -rf $(hdir)
	mkdir -p $(hdir)/stylesheet-images
	cp $(docbook_css) $(hdir)
	cp $(images_gif)/*.gif $(hdir)/stylesheet-images
	touch generated-index.sgml

setup: $(hdir)
	touch setup

temp-index.sgml: setup redhat-html.dsl $(EXTRA_DIST)
	( cd $(hdir) ; \
	  $(jade) -t sgml -ihtml -V html-index ../max-rpm.sgml ; \
	  $(perl) $(collateindex) -o ../temp-index.sgml HTML.index ; \
	)

generated-index.sgml: temp-index.sgml fix-index
	( cd $(hdir) ; \
	  cat ../temp-index.sgml | ../fix-index > ../generated-index.sgml ; \
	  $(jade) -t sgml -ihtml ../max-rpm.sgml ; \
	)

genhtml: generated-index.sgml
	touch genhtml

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
