Name:		extra-keyboards
Version:	0.3
Release:	1%{?dist}
Summary:	Extra keyboards for X server

Group:          User Interface/X
License:	Public Domain
Source0:	czdvorak
Source1:	typematrix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	xkeyboard-config
BuildArch:      noarch

%define datadir_xkb_symbols %{_datadir}/X11/xkb/symbols/

%description

This package contains a couple of keyboard modifiers for X server.

This includes modification of Programmer Dvorak (dvp) for users that
do light-weight Czech typing.  Czech letters with diacritics are
accessible through level 3 shift (such as is typically available
through AltGr).

Another extra keyboard is a set of key swaps for type matrix
keyboards.  This is mostly to suit myself.

%prep
:

%build
:

%install
install -d $RPM_BUILD_ROOT%{datadir_xkb_symbols}
for source in %{SOURCE0} %{SOURCE1}; do
    install -m 644 $source $RPM_BUILD_ROOT%{datadir_xkb_symbols}
done

%clean
:

%files
%defattr(-,root,root,-)
%{datadir_xkb_symbols}/*

%changelog
* Sat Oct 29 2011 Petr Machata <pmachata@redhat.com> - 0.3-1
- Add dead_hook to AltGr+/ (mnemonic: the same key as "?")

* Tue Nov 23 2010 Petr Machata <pmachata@redhat.com> - 0.2-1
- Replace ecaron for eacute
- Add the keyswaps keyboard
- Rename the package to extra-keyboards

* Mon Nov 15 2010 Petr Machata <pmachata@redhat.com> - 0.1-1
- Initial release.
