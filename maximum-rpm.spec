Summary: The "Maximum RPM" book
Name: maximum-rpm
Version: 1.0
Release: 0.1
License: OPL
Group: Documentation
Source: max-rpm.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
"Maximum RPM" is a book about the RPM Package Manager or, as it is known
to its friends, RPM.

The book is divided into two major sections. The first section is for
anyone who needs to use RPM on his/her system. The second section covers
all there is to know about build packages using RPM.

%prep
%setup -q -n max-rpm

%build
./build

%install
rm -rf ${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc html

%changelog
* Thu Apr  5 2001 Jeff Johnson <jbj@redhat.com>
- Create.
